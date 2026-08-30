\"\"\"
MCQ Quiz for Data Science Preparation
Topics: Pandas, NumPy, Data Visualization, Linear Regression, Data Cleaning
Difficulty: 2 Easy, 2 Medium, 1 Hard
\"\"\"

import sys

def run_quiz():
    """Run the MCQ quiz and show answers at the end."""
    mcqs = [
        {
            "question": "What does the pandas method `df.fillna(df.mean())` do?",
            "options": [
                "A) Fills missing values with the mean of each column",
                "B) Fills missing values with the mean of the entire DataFrame",
                "C) Drops rows with missing values",
                "D) Replaces all values with the mean"
            ],
            "correct": "A",
            "explanation": "The `df.mean()` returns a Series of column means. When used in `fillna`, it fills missing values in each column with that column's mean."
        },
        {
            "question": "In NumPy, what is the result of `np.array([1, 2, 3]) @ np.array([4, 5, 6])`?",
            "options": [
                "A) Array([4, 10, 18])",
                "B) 32",
                "C) Array([5, 7, 9])",
                "D) Error: dimensions must match"
            ],
            "correct": "B",
            "explanation": "The @ operator performs matrix multiplication (dot product for 1D arrays). 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32."
        },
        {
            "question": "Which seaborn function is most appropriate for visualizing the distribution of a single continuous variable?",
            "options": [
                "A) sns.scatterplot",
                "B) sns.boxplot",
                "C) sns.histplot",
                "D) sns.heatmap"
            ],
            "correct": "C",
            "explanation": "sns.histplot (or sns.distplot in older versions) is used to plot the distribution of a single continuous variable by binning the values and counting observations per bin."
        },
        {
            "question": "When implementing gradient descent for linear regression, what is the effect of a learning rate that is too high?",
            "options": [
                "A) Convergence to the global minimum is guaranteed but slow",
                "B) The algorithm may diverge or oscillate around the minimum",
                "C) The algorithm will converge faster to a better solution",
                "D) No effect; learning rate only affects speed, not accuracy"
            ],
            "correct": "B",
            "explanation": "If the learning rate is too large, the algorithm may overshoot the minimum and diverge, or oscillate around it without converging."
        },
        {
            "question": "Consider a DataFrame with a column 'date' containing strings in the format 'YYYY-MM-DD'. Which code correctly converts it to datetime?",
            "options": [
                "A) df['date'] = pd.to_datetime(df['date'])",
                "B) df['date'] = df['date'].astype('datetime')",
                "C) df['date'] = pd.convert_date(df['date'])",
                "D) df['date'] = df['date'].datetime()"
            ],
            "correct": "A",
            "explanation": "pd.to_datetime() is the pandas function for converting strings or other formats to datetime objects. It understands the 'YYYY-MM-DD' format by default."
        }
    ]
    
    score = 0
    for i, mcq in enumerate(mcqs, 1):
        print(f"Question {i}: {mcq['question']}")
        for opt in mcq['options']:
            print(f"  {opt}")
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        while user_answer not in ['A', 'B', 'C', 'D']:
            user_answer = input("Invalid input. Please enter A, B, C, or D: ").strip().upper()
        
        if user_answer == mcq['correct']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {mcq['correct']}.\n")
    
    print(f"Your final score: {score}/{len(mcqs)}")
    print("\n" + "="*50)
    print("Answer Key with Explanations:")
    print("="*50)
    for i, mcq in enumerate(mcqs, 1):
        print(f"Q{i}: {mcq['question']}")
        print(f"Correct Answer: {mcq['correct']}")
        print(f"Explanation: {mcq['explanation']}\n")

if __name__ == "__main__":
    # If an argument '--answer-key' is provided, only show the answer key
    if len(sys.argv) > 1 and sys.argv[1] == '--answer-key':
        mcqs = [
            {
                "question": "What does the pandas method `df.fillna(df.mean())` do?",
                "options": [
                    "A) Fills missing values with the mean of each column",
                    "B) Fills missing values with the mean of the entire DataFrame",
                    "C) Drops rows with missing values",
                    "D) Replaces all values with the mean"
                ],
                "correct": "A",
                "explanation": "The `df.mean()` returns a Series of column means. When used in `fillna`, it fills missing values in each column with that column's mean."
            },
            {
                "question": "In NumPy, what is the result of `np.array([1, 2, 3]) @ np.array([4, 5, 6])`?",
                "options": [
                    "A) Array([4, 10, 18])",
                    "B) 32",
                    "C) Array([5, 7, 9])",
                    "D) Error: dimensions must match"
                ],
                "correct": "B",
                "explanation": "The @ operator performs matrix multiplication (dot product for 1D arrays). 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32."
            },
            {
                "question": "Which seaborn function is most appropriate for visualizing the distribution of a single continuous variable?",
                "options": [
                    "A) sns.scatterplot",
                    "B) sns.boxplot",
                    "C) sns.histplot",
                    "D) sns.heatmap"
                ],
                "correct": "C",
                "explanation": "sns.histplot (or sns.distplot in older versions) is used to plot the distribution of a single continuous variable by binning the values and counting observations per bin."
            },
            {
                "question": "When implementing gradient descent for linear regression, what is the effect of a learning rate that is too high?",
                "options": [
                    "A) Convergence to the global minimum is guaranteed but slow",
                    "B) The algorithm may diverge or oscillate around the minimum",
                    "C) The algorithm will converge faster to a better solution",
                    "D) No effect; learning rate only affects speed, not accuracy"
                ],
                "correct": "B",
                "explanation": "If the learning rate is too large, the algorithm may overshoot the minimum and diverge, or oscillate around it without converging."
            },
            {
                "question": "Consider a DataFrame with a column 'date' containing strings in the format 'YYYY-MM-DD'. Which code correctly converts it to datetime?",
                "options": [
                    "A) df['date'] = pd.to_datetime(df['date'])",
                    "B) df['date'] = df['date'].astype('datetime')",
                    "C) df['date'] = pd.convert_date(df['date'])",
                    "D) df['date'] = df['date'].datetime()"
                ],
                "correct": "A",
                "explanation": "pd.to_datetime() is the pandas function for converting strings or other formats to datetime objects. It understands the 'YYYY-MM-DD' format by default."
            }
        ]
        print("="*50)
        print("Answer Key with Explanations:")
        print("="*50)
        for i, mcq in enumerate(mcqs, 1):
            print(f"Q{i}: {mcq['question']}")
            print(f"Correct Answer: {mcq['correct']}")
            print(f"Explanation: {mcq['explanation']}\n")
    else:
        run_quiz()