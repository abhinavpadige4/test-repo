\"\"\"
Exercise 9: File Operations
Topic: File I/O
Difficulty: Medium

Problem Statement:
Write a program that reads a text file, counts the frequency of each word, and writes the results to another file.
The program should:
- Ask the user for the input file name
- Read the content of the input file
- Count the frequency of each word (case-insensitive, ignore punctuation)
- Ask the user for the output file name
- Write the word frequencies to the output file, sorted by frequency (descending)
- Handle file not found errors gracefully

Example:
Input file (sample.txt) contains:
Hello world! Hello everyone. This is a test. Test, test, test!

Output file (word_count.txt) should contain:
test: 4
hello: 2
world: 1
everyone: 1
this: 1
is: 1
a: 1
\"\"\"

import string

def count_words(filename):
    \"\"\"Read a file and return a dictionary of word frequencies.\"\"\"
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
    except FileNotFoundError:
        return None
    
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    
    words = text.split()
    word_count = {}
    for word in words:
        if word:  # skip empty strings
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def write_word_count(word_count, output_filename):
    \"\"\"Write word frequencies to a file, sorted by frequency (descending).\"\"\"
    # Sort by frequency (descending) and then alphabetically for ties
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    with open(output_filename, 'w') as file:
        for word, count in sorted_words:
            file.write(f"{word}: {count}\\n")

def main():
    input_file = input("Enter the input file name: ")
    word_count = count_words(input_file)
    
    if word_count is None:
        print(f"Error: File '{input_file}' not found.")
        return
    
    if not word_count:
        print("The file is empty or contains no words.")
        return
    
    output_file = input("Enter the output file name: ")
    write_word_count(word_count, output_file)
    print(f"Word frequencies written to '{output_file}'.")

if __name__ == "__main__":
    # Test cases
    print("Running test cases...")
    
    # Create a test file
    test_content = "Hello world! Hello everyone. This is a test. Test, test, test!"
    with open("test_input.txt", "w") as f:
        f.write(test_content)
    
    # Test count_words function
    word_count = count_words("test_input.txt")
    expected = {
        'hello': 2,
        'world': 1,
        'everyone': 1,
        'this': 1,
        'is': 1,
        'a': 1,
        'test': 4
    }
    
    if word_count == expected:
        print("PASS: Word count matches expected.")
    else:
        print(f"FAIL: Expected {expected}, got {word_count}")
    
    # Test write_word_count function
    write_word_count(word_count, "test_output.txt")
    
    # Read the output file and check
    with open("test_output.txt", "r") as f:
        lines = f.readlines()
    
    expected_lines = [
        "test: 4\n",
        "hello: 2\n",
        "a: 1\n",
        "everyone: 1\n",
        "is: 1\n",
        "this: 1\n",
        "world: 1\n"
    ]
    
    # Note: The order of words with same frequency is alphabetical in our sort.
    if lines == expected_lines:
        print("PASS: Output file matches expected.")
    else:
        print("FAIL: Output file content:")
        for line in lines:
            print(repr(line))
        print("Expected:")
        for line in expected_lines:
            print(repr(line))
    
    # Clean up test files
    import os
    os.remove("test_input.txt")
    os.remove("test_output.txt")
    
    print("File operations tests completed.")
    
    # Uncomment below to run interactively
    # main()