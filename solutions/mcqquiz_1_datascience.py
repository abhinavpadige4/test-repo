\"\"\"
MCQ Quiz: Data Science Fundamentals
Total Questions: 5 (2 Easy, 2 Medium, 1 Hard)
Each question includes explanation.
\"\"\"
import random

# Define the questions
questions = [
    {
        "question": "What is the primary purpose of the pandas library in Python?",
        "options": [
            "A) Building machine learning models",
            "B) Data manipulation and analysis",
            "C) Creating visualizations",
            "D) Web scraping"
        ],
        "answer": "B",
        "explanation": "Pandas is a powerful library for data manipulation and analysis, providing data structures like DataFrame and Series to handle structured data efficiently."
    },
    {
        "question": "In a linear regression model, what does the R-squared value represent?",
        "options": [
            "A) The slope of the regression line",
            "B) The proportion of variance in the dependent variable explained by the independent variables",
            "C) The correlation coefficient",
            "D) The mean squared error"
        ],
        "answer": "B",
        "explanation": "R-squared (coefficient of determination) measures the proportion of the variance in the dependent variable that is predictable from the independent variable(s). It ranges from 0 to 1."
    },
    {
        "question": "When dealing with missing data in a dataset, which technique is most appropriate for preserving the distribution of the data?",
        "options": [
            "A) Deleting rows with missing values",
            "B) Filling missing values with the mean",
            "C) Filling missing values with the median",
            "D) Using multiple imputation"
        ],
        "answer": "D",
        "explanation": "Multiple imputation creates several different plausible imputed datasets and combines results, preserving the distribution and uncertainty better than single imputation methods like mean/median."
    },
    {
        "question": "Which of the following is NOT a valid step in a typical machine learning workflow?",
        "options": [
            "A) Feature engineering",
            "B) Hyperparameter tuning",
            "C) Data leakage inspection",
            "D) Model deployment"
        ],
        "answer": "C",
        "explanation": "While checking for data leakage is important, it is not a formal step in the workflow; it's part of data preparation and validation. The typical steps are: data collection, cleaning, exploration, feature engineering, model training, evaluation, and deployment."
    },
    {
        "question": "In the context of time series analysis, what does the ACF (Autocorrelation Function) measure?",
        "options": [
            "A) The correlation between a time series and a lagged version of itself",
            "B) The correlation between two different time series",
            "C) The partial correlation controlling for intermediate lags",
            "D) The forecast error variance"
        ],
        "answer": "A",
        "explanation": "The autocorrelation function (ACF) measures the linear relationship between a time series' current value and its past values (lags). It helps identify patterns like seasonality and trend."
    }
]

def run_quiz():
    """Run the MCQ quiz and return the score."""
    score = 0
    random.shuffle(questions)  # Optional: shuffle for variety
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for opt in q['options']:
            print(f"  {opt}")
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        while user_answer not in ['A', 'B', 'C', 'D']:
            user_answer = input("Invalid input. Please enter A, B, C, or D: ").strip().upper()
        if user_answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['answer']}.\n")
        print(f"Explanation: {q['explanation']}\n")
        print("-" * 50)
    print(f"Quiz completed! Your score: {score}/{len(questions)}")
    return score

if __name__ == "__main__":
    run_quiz()