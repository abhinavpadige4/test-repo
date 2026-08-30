\"\"\"
MCQ Quiz for Data Science Preparation
Total Questions: 5
Topics: Data Cleaning, Descriptive Statistics, Linear Regression, Visualization, K-Means Clustering
Each question includes explanation.
\"\"\"

import random

def run_quiz():
    questions = [
        {
            "question": "Which of the following is the correct way to check for NaN values in a list using Python's math module?",
            "options": [
                "A) math.isnan(x) works for any type x",
                "B) math.isnan(x) only works for float values and raises TypeError for others",
                "C) math.isnan(x) returns True for None values",
                "D) math.isnan(x) can be used directly on a list"
            ],
            "correct": "B",
            "explanation": "math.isnan() only accepts float values. Passing None or non-float types raises a TypeError. To check for NaN in a list, you must first ensure the element is a float."
        },
        {
            "question": "In descriptive statistics, if a dataset has no repeating values, what is the mode?",
            "options": [
                "A) The mode is the mean of the dataset",
                "B) The mode is the median of the dataset",
                "C) There is no mode",
                "D) The mode is the smallest value"
            ],
            "correct": "C",
            "explanation": "The mode is the value that appears most frequently. If no value repeats (all frequencies are 1), then there is no mode."
        },
        {
            "question": "What is the primary purpose of using a learning rate in gradient descent for linear regression?",
            "options": [
                "A) To increase the speed of convergence regardless of stability",
                "B) To control the step size during parameter updates to avoid overshooting the minimum",
                "C) To normalize the input features",
                "D) To calculate the mean squared error"
            ],
            "correct": "B",
            "explanation": "The learning rate determines how large a step we take in the direction of the negative gradient. Too large can cause divergence; too small can make convergence slow."
        },
        {
            "question": "When saving a matplotlib figure using fig.savefig('plot.png'), which backend setting is recommended to avoid GUI-related errors in non-interactive environments?",
            "options": [
                "A) matplotlib.use('TkAgg')",
                "B) matplotlib.use('Agg')",
                "C) matplotlib.use('Qt5Agg')",
                "D) No backend setting is needed"
            ],
            "correct": "B",
            "explanation": "The 'Agg' backend is a non-interactive backend that can write files to disk but cannot display plots. It is suitable for scripts and servers where no GUI is available."
        },
        {
            "question": "In K-Means clustering, what does the inertia metric represent?",
            "options": [
                "A) The number of iterations until convergence",
                "B) The sum of squared distances of samples to their closest cluster center",
                "C) The silhouette score of the clustering",
                "D) The number of clusters formed"
            ],
            "correct": "B",
            "explanation": "Inertia, also known as within-cluster sum of squares, measures how internally coherent the clusters are. Lower inertia indicates tighter clusters."
        }
    ]

    score = 0
    random.shuffle(questions)  # Optional: shuffle for variety
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

    print(f"Quiz completed! Your score: {score}/{len(questions)}")
    return score

if __name__ == "__main__":
    run_quiz()