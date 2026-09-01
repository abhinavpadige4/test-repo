\"\"\"
Exercise 11: Working with Dates and Times
Topic: datetime module
Difficulty: Medium

Problem Statement:
Write a program that calculates a person's age based on their birthdate and the current date and also tells them how many days until their next birthday.

Requirements:
- Ask the user to enter their birthdate in YYYY-MM-DD format
- Validate the input format and that it's a valid date
- Calculate the person's current age in years
- Calculate the number of days until their next birthday
- Display both results

Example:
Enter your birthdate (YYYY-MM-DD): 1990-05-15
You are 33 years old.
Your next birthday is in 120 days.
\"\"\"

from datetime import datetime, date

def calculate_age(birth_date):
    \"\"\"Calculate age in years based on birth date.\"\"\"
    today = date.today()
    age = today.year - birth_date.year
    # Adjust if birthday hasn't occurred this year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

def days_until_next_birthday(birth_date):
    \"\"\"Calculate days until next birthday.\"\"\"
    today = date.today()
    # Get this year's birthday
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    # If birthday has already passed this year, use next year's
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    delta = next_birthday - today
    return delta.days

def main():
    while True:
        birth_str = input("Enter your birthdate (YYYY-MM-DD): ").strip()
        try:
            birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()
            # Check that birth date is not in the future
            if birth_date > date.today():
                print("Error: Birthdate cannot be in the future.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid date in YYYY-MM-DD format.")
    
    age = calculate_age(birth_date)
    days_left = days_until_next_birthday(birth_date)
    
    print(f"You are {age} years old.")
    if days_left == 0:
        print("Happy birthday! 🎉")
    else:
        print(f"Your next birthday is in {days_left} days.")

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    # We'll test with a fixed date by mocking date.today
    from unittest.mock import patch
    import datetime as dt
    
    # Test case 1: Birthday today
    with patch('datetime.date') as mock_date:
        mock_date.today.return_value = dt.date(2023, 5, 15)
        mock_date.side_effect = lambda *args, **kw: dt.date(*args, **kw)
        
        birth = dt.date(1990, 5, 15)
        age = calculate_age(birth)
        days = days_until_next_birthday(birth)
        assert age == 33
        assert days == 0
        print("Test 1 passed: Birthday today")
    
    # Test case 2: Birthday in future this year
    with patch('datetime.date') as mock_date:
        mock_date.today.return_value = dt.date(2023, 1, 1)
        mock_date.side_effect = lambda *args, **kw: dt.date(*args, **kw)
        
        birth = dt.date(1990, 5, 15)
        age = calculate_age(birth)
        days = days_until_next_birthday(birth)
        assert age == 32
        assert days > 0  # days until May 15
        print("Test 2 passed: Birthday in future")
    
    # Test case 3: Birthday past this year
    with patch('datetime.date') as mock_date:
        mock_date.today.return_value = dt.date(2023, 12, 1)
        mock_date.side_effect = lambda *args, **kw: dt.date(*args, **kw)
        
        birth = dt.date(1990, 5, 15)
        age = calculate_age(birth)
        days = days_until_next_birthday(birth)
        assert age == 33
        assert days > 0  # days until May 15 next year
        print("Test 3 passed: Birthday past")
    
    print("All unit tests passed!")
    
    # Uncomment below to run interactively
    # main()