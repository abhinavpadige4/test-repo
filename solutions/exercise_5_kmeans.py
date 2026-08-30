\"\"\"
Exercise 5: K-Means Clustering from Scratch (Hard)
Problem Statement:
Implement the K-Means clustering algorithm.
Write a function `kmeans(X, k, max_iters=100)` that:
- Takes a 2D list X (list of lists, each inner list is a point with n features)
- Number of clusters k
- Maximum iterations
- Returns tuple (centroids, labels, inertia) where:
    centroids: list of k centroids (each centroid is a list of n features)
    labels: list of cluster index for each point
    inertia: sum of squared distances of points to their closest centroid (within-cluster sum of squares)

Use Euclidean distance. Initialize centroids by randomly selecting k distinct points from X.

Test Cases:
1. Simple 2D data with 3 clear clusters.
2. Edge case: k=1 (all points in one cluster).
3. Edge case: k equals number of points (each point its own centroid).
\"\"\"
import random
import math

def euclidean_distance(point1, point2):
    """Compute Euclidean distance between two points."""
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))

def kmeans(X, k, max_iters=100):
    """
    Perform K-Means clustering.
    
    Args:
        X (list of list): Dataset where each element is a list of feature values.
        k (int): Number of clusters.
        max_iters (int): Maximum number of iterations.
    
    Returns:
        tuple: (centroids, labels, inertia)
    """
    n = len(X)
    if n == 0 or k <= 0:
        return [], [], 0
    
    # Initialize centroids: randomly choose k distinct points
    centroids = random.sample(X, k)
    
    for _ in range(max_iters):
        # Assign clusters
        labels = []
        for point in X:
            distances = [euclidean_distance(point, centroid) for centroid in centroids]
            cluster_idx = distances.index(min(distances))
            labels.append(cluster_idx)
        
        # Update centroids
        new_centroids = []
        for i in range(k):
            # Get points assigned to cluster i
            cluster_points = [X[j] for j in range(n) if labels[j] == i]
            if cluster_points:
                # Compute mean of each feature
                centroid = [sum(dim) / len(cluster_points) for dim in zip(*cluster_points)]
                new_centroids.append(centroid)
            else:
                # If no points, keep the old centroid (or reinitialize randomly)
                new_centroids.append(centroids[i])
        
        # Check for convergence (if centroids don't change)
        if new_centroids == centroids:
            break
        centroids = new_centroids
    
    # Compute inertia (within-cluster sum of squares)
    inertia = 0
    for idx, point in enumerate(X):
        centroid = centroids[labels[idx]]
        inertia += euclidean_distance(point, centroid) ** 2
    
    return centroids, labels, inertia

if __name__ == "__main__":
    # Test case 1: Simple 2D data with 3 clusters
    random.seed(42)  # For reproducibility
    X1 = [[1, 1], [1, 2], [2, 1], [2, 2],   # Cluster 1
          [8, 8], [8, 9], [9, 8], [9, 9],   # Cluster 2
          [1, 8], [1, 9], [2, 8], [2, 9]]   # Cluster 3
    centroids1, labels1, inertia1 = kmeans(X1, k=3, max_iters=100)
    print("Test 1: Three clusters")
    print(f"  Centroids: {centroids1}")
    print(f"  Inertia: {inertia1:.2f}")
    # Expect low inertia
    assert inertia1 < 5, "Inertia too high for well-separated clusters"
    
    # Test case 2: k=1
    X2 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    centroids2, labels2, inertia2 = kmeans(X2, k=1, max_iters=100)
    print("\nTest 2: k=1")
    print(f"  Centroids: {centroids2}")
    print(f"  Labels all zero? {all(l == 0 for l in labels2)}")
    assert all(l == 0 for l in labels2), "All points should be in cluster 0"
    
    # Test case 3: k equals number of points
    X3 = [[0, 0], [1, 1], [2, 2]]
    centroids3, labels3, inertia3 = kmeans(X3, k=3, max_iters=100)
    print("\nTest 3: k = n")
    print(f"  Centroids: {centroids3}")
    print(f"  Inertia: {inertia3}")
    # Each point should be its own centroid (or close), inertia near 0
    assert inertia3 < 1e-9, "Inertia should be near zero when k=n"
    
    print("\nAll tests passed!")
    
    # Complexity Analysis:
    # Time Complexity: O(max_iters * n * k * d) where n = number of points, k = clusters, d = dimensions.
    # Space Complexity: O(k*d + n) for centroids and labels.
\"\"\"