"""
MCQ Quiz: Python Programming Fundamentals

3 multiple-choice questions covering strings, data structures, and OOP.
Run this file to take the quiz interactively.
"""

# Each question: (question, options, correct_answer_index, explanation)
QUESTIONS = [
    {
        "question": "What is the output of the following code?\n\n    text = 'Hello World'\n    print(text[::-1])",
        "options": [
            "A) 'Hello World'",
            "B) 'dlroW olleH'",
            "C) 'World Hello'",
            "D) Error: invalid syntax"
        ],
        "correct": 1,
        "explanation": "The slice [::-1] reverses a string in Python. It steps through the string backwards, producing 'dlroW olleH'."
    },
    {
        "question": "Which data structure would be MOST efficient for checking if an element exists in a large collection?",
        "options": [
            "A) List",
            "B) Tuple",
            "C) Set",
            "D) String"
        ],
        "correct": 2,
        "explanation": "Sets use hash tables for O(1) average lookup time, making membership checks much faster than lists or tuples which require O(n) linear search."
    },
    {
        "question": "In Object-Oriented Programming, what does the 'self' parameter in a Python class method refer to?",
        "options": [
            "A) The class itself",
            "B) The instance of the class",
            "C) The parent class",
            "D) A global variable"
        ],
        "correct": 1,
        "explanation": "'self' refers to the specific instance of the class on which the method is called. It allows access to that instance's attributes and other methods."
    }
]


def run_quiz():
    """Run the interactive quiz and display results."""
    score = 0
    print("=" * 50)
    print("PYTHON FUNDAMENTALS QUIZ")
    print("=" * 50)
    
    for i, q in enumerate(QUESTIONS, 1):
        print(f"\nQuestion {i}: {q['question']}\n")
        for option in q["options"]:
            print(f"  {option}")
        
        # Get user answer
        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input. Please enter A, B, C, or D.")
        
        # Check answer
        correct_letter = ['A', 'B', 'C', 'D'][q["correct"]]
        if answer == correct_letter:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer is {correct_letter}.")
        
        print(f"💡 Explanation: {q['explanation']}")
    
    print("\n" + "=" * 50)
    print(f"FINAL SCORE: {score}/{len(QUESTIONS)}")
    print("=" * 50)
    
    if score == len(QUESTIONS):
        print("🏆 Excellent! You've mastered these concepts!")
    elif score >= 2:
        print("👍 Good job! Review the explanations for missed questions.")
    else:
        print("📚 Keep practicing! Review the fundamentals.")


if __name__ == "__main__":
    run_quiz()