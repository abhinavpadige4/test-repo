\"\"\"
MCQ Quiz: Data Science Fundamentals
Total Questions: 5
Organized by difficulty: 2 Easy, 2 Medium, 1 Hard
Each question includes explanation.
\"\"\"

import sys

def run_quiz():
    questions = [
        {
            "question": "What is the primary purpose of the pandas library in Python?",
            "options": [
                "A) Data visualization",
                "B) Statistical modeling",
                "C) Data manipulation and analysis",
                "D) Machine learning algorithms"
            ],
            "correct": "C",
            "explanation": "Pandas is a powerful library for data manipulation and analysis. It provides data structures like DataFrame and Series that make it easy to clean, transform, and analyze structured data. While it can be used in conjunction with visualization and modeling libraries, its core strength is data handling."
        },
        {
            "question": "In a linear regression model, what does the R-squared value represent?",
            "options": [
                "A) The slope of the regression line",
                "B) The proportion of variance in the dependent variable explained by the independent variables",
                "C) The correlation coefficient between variables",
                "D) The root mean square error"
            ],
            "correct": "B",
            "explanation": "R-squared (coefficient of determination) measures the proportion of the variance in the dependent variable that is predictable from the independent variables. It ranges from 0 to 1, where higher values indicate better fit. It does not represent slope, correlation, or error directly."
        },
        {
            "question": "Which of the following is NOT a common technique for handling missing data?",
            "options": [
                "A) Deletion of rows with missing values",
                "B) Imputation with mean/median/mode",
                "C) Using models that support missing values",
                "D) Ignoring the missing values and proceeding with analysis"
            ],
            "correct": "D",
            "explanation": "Ignoring missing values without any treatment can lead to biased results and incorrect conclusions. Proper handling includes deletion (if appropriate), imputation, or using algorithms that can handle missingness. Simply proceeding as if data is complete is not a valid technique."
        },
        {
            "question": "What is the main difference between supervised and unsupervised learning?",
            "options": [
                "A) Supervised learning uses labeled data, while unsupervised learning uses unlabeled data",
                "B) Supervised learning is for classification, unsupervised for clustering",
                "C) Supervised learning requires more data than unsupervised learning",
                "D) There is no difference; the terms are interchangeable"
            ],
            "correct": "A",
            "explanation": "The key distinction is that supervised learning algorithms learn from labeled training data (input-output pairs), while unsupervised learning algorithms find patterns in unlabeled data. While supervised learning is often used for classification/regression and unsupervised for clustering/dimensionality reduction, the fundamental difference lies in the presence of labels."
        },
        {
            "question": "In the context of K-Means clustering, what does the 'inertia' measure?",
            "options": [
                "A) The number of clusters formed",
                "B) The sum of squared distances of samples to their closest cluster center",
                "C) The silhouette score of the clustering",
                "D) The computational time required for clustering"
            ],
            "correct": "B",
            "explanation": "Inertia (also called within-cluster sum of squares) measures how well the data points were clustered: it is the sum of squared distances between each point and its assigned cluster centroid. Lower inertia indicates denser clusters. It is used in the elbow method to help choose the number of clusters."
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for opt in q['options']:
            print(f"  {opt}")
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        while user_answer not in ['A', 'B', 'C', 'D']:
            user_answer = input("Invalid input. Please enter A, B, C, or D: ").strip().upper()
        
        if user_answer == q['correct']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['correct']}.\n")
        
        print(f"Explanation: {q['explanation']}\n")
        print("-" * 50)
    
    print(f"Quiz complete! Your score: {score}/{len(questions)}")
    return score

if __name__ == "__main__":
    # If run directly, play the quiz
    run_quiz()
else:
    # If imported, provide the questions for testing
    pass