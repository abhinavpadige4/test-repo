\"\"\"
Exercise 4: NumPy - Operations and Linear Algebra
Difficulty: Medium
Topic: NumPy

Problem Statement:
Write a Python script using NumPy to:
1. Perform matrix multiplication of two 2D arrays
2. Calculate the determinant and inverse of a square matrix
3. Solve a system of linear equations Ax = b
4. Compute eigenvalues and eigenvectors of a matrix
5. Perform Singular Value Decomposition (SVD) on a matrix

Expected Output:
Matrix A:
[[1 2]
 [3 4]]
Matrix B:
[[5 6]
 [7 8]]
Matrix multiplication (A @ B):
[[19 22]
 [43 50]]
Determinant of A: -2.0
Inverse of A:
[[-2.   1. ]
 [ 1.5 -0.5]]
Solution to Ax = b (where b = [1, 2]): [-2.  1.5]
Eigenvalues of A: [-0.37228132  5.37228132]
Eigenvectors of A:
[[-0.82456484 -0.41597356]
 [ 0.56576746 -0.90937671]]
SVD of A:
Singular values: [5.4649857  0.36596619]
Left singular vectors:
[[-0.40455358 -0.9145143 ]
 [-0.9145143   0.40455358]]
Right singular vectors:
[[-0.57604844 -0.81741556]
 [-0.81741556  0.57604844]]
\"\"\"

import numpy as np

def numpy_linear_algebra():
    """
    Perform various NumPy linear algebra operations.
    Returns:
        dict: Results of operations for testing
    """
    # Define matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    # 1. Matrix multiplication
    AB = A @ B  # or np.dot(A, B)
    
    # 2. Determinant and inverse
    det_A = np.linalg.det(A)
    inv_A = np.linalg.inv(A)
    
    # 3. Solve linear system Ax = b
    b = np.array([1, 2])
    x = np.linalg.solve(A, b)
    
    # 4. Eigenvalues and eigenvectors
    eigenvals, eigenvecs = np.linalg.eig(A)
    
    # 5. Singular Value Decomposition
    U, s, Vh = np.linalg.svd(A)
    
    # Print results
    print(f"Matrix A:\n{A}")
    print(f"Matrix B:\n{B}")
    print(f"Matrix multiplication (A @ B):\n{AB}")
    print(f"Determinant of A: {det_A}")
    print(f"Inverse of A:\n{inv_A}")
    print(f"Solution to Ax = b (where b = {b}): {x}")
    print(f"Eigenvalues of A: {eigenvals}")
    print(f"Eigenvectors of A:\n{eigenvecs}")
    print(f"SVD of A:")
    print(f"Singular values: {s}")
    print(f"Left singular vectors:\n{U}")
    print(f"Right singular vectors:\n{Vh}")
    
    # Return for testing
    return {
        "A": A,
        "B": B,
        "AB": AB,
        "det_A": det_A,
        "inv_A": inv_A,
        "x": x,
        "eigenvals": eigenvals,
        "eigenvecs": eigenvecs,
        "U": U,
        "s": s,
        "Vh": Vh
    }

# Test cases
if __name__ == "__main__":
    result = numpy_linear_algebra()
    
    # Test 1: Matrix multiplication
    expected_AB = np.array([[19, 22], [43, 50]])
    assert np.allclose(result["AB"], expected_AB), "Matrix multiplication failed"
    
    # Test 2: Determinant
    assert abs(result["det_A"] - (-2.0)) < 0.001, "Determinant calculation failed"
    
    # Test 3: Inverse (check A * A_inv = I)
    identity = np.eye(2)
    assert np.allclose(result["A"] @ result["inv_A"], identity), "Inverse calculation failed"
    
    # Test 4: Solve linear system
    expected_x = np.array([-2., 1.5])
    assert np.allclose(result["x"], expected_x), "Linear system solution failed"
    
    # Test 5: Eigenvalues and eigenvectors (A * v = λ * v)
    for i in range(len(result["eigenvals"])):
        lhs = result["A"] @ result["eigenvecs"][:, i]
        rhs = result["eigenvals"][i] * result["eigenvecs"][:, i]
        assert np.allclose(lhs, rhs), f"Eigenvalue/eigenvector {i} verification failed"
    
    # Test 6: SVD (A = U @ diag(s) @ Vh)
    S = np.zeros((2, 2))
    np.fill_diagonal(S, result["s"])
    assert np.allclose(result["A"], result["U"] @ S @ result["Vh"]), "SVD reconstruction failed"
    
    print("\nAll tests passed!")