\"\"\"
Exercise 12: File I/O - Read and Write
Topic: File Handling
Difficulty: Medium

Problem Statement:
Write a program that reads a text file, counts the number of lines, words, and characters, and writes the statistics to another file.

Solution:
\"\"\"
def file_stats(input_path, output_path):
    """
    Read input file, compute line, word, and character counts, write to output file.
    
    Args:
        input_path: Path to input text file
        output_path: Path to output statistics file
    """
    try:
        with open(input_path, 'r') as infile:
            content = infile.read()
        
        lines = content.splitlines()
        num_lines = len(lines)
        num_words = len(content.split())
        num_chars = len(content)
        
        with open(output_path, 'w') as outfile:
            outfile.write(f"Lines: {num_lines}\\n")
            outfile.write(f"Words: {num_words}\\n")
            outfile.write(f"Characters: {num_chars}\\n")
            
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Create a sample input file for demonstration
    sample_content = """Hello world!
This is a test file.
It contains multiple lines.
Python makes file handling easy."""
    
    with open('sample_input.txt', 'w') as f:
        f.write(sample_content)
    
    # Process the file
    file_stats('sample_input.txt', 'stats_output.txt')
    
    # Read and print the output for verification
    try:
        with open('stats_output.txt', 'r') as f:
            print("Statistics written to stats_output.txt:")
            print(f.read())
    except FileNotFoundError:
        print("Output file not found.")

if __name__ == "__main__":
    main()

# Test Cases
if __name__ == "__main__":
    import os
    
    # Clean up test files if they exist
    for fname in ['test_input.txt', 'test_output.txt']:
        if os.path.exists(fname):
            os.remove(fname)
    
    # Test Case 1: Simple content
    with open('test_input.txt', 'w') as f:
        f.write("Hello world\\nThis is a test.")
    
    file_stats('test_input.txt', 'test_output.txt')
    
    with open('test_output.txt', 'r') as f:
        result = f.read()
    
    expected_lines = "Lines: 2\\nWords: 6\\nCharacters: 25\\n"
    assert result == expected_lines, f"Test 1 failed. Expected:\\n{expected_lines}\\nGot:\\n{result}"
    print("Test Case 1 Passed: Simple content")
    
    # Test Case 2: Empty file
    with open('test_input.txt', 'w') as f:
        f.write("")
    
    file_stats('test_input.txt', 'test_output.txt')
    
    with open('test_output.txt', 'r') as f:
        result = f.read()
    
    expected_lines = "Lines: 0\\nWords: 0\\nCharacters: 0\\n"
    assert result == expected_lines, f"Test 2 failed. Expected:\\n{expected_lines}\\nGot:\\n{result}"
    print("Test Case 2 Passed: Empty file")
    
    # Test Case 3: File with only spaces and newlines
    with open('test_input.txt', 'w') as f:
        f.write("   \\n\\n   ")
    
    file_stats('test_input.txt', 'test_output.txt')
    
    with open('test_output.txt', 'r') as f:
        result = f.read()
    
    # split() on whitespace will give empty list for words
    expected_lines = "Lines: 3\\nWords: 0\\nCharacters: 6\\n"
    assert result == expected_lines, f"Test 3 failed. Expected:\\n{expected_lines}\\nGot:\\n{result}"
    print("Test Case 3 Passed: Only whitespace")
    
    # Clean up
    for fname in ['test_input.txt', 'test_output.txt', 'sample_input.txt', 'stats_output.txt']:
        if os.path.exists(fname):
            os.remove(fname)
    
    print("\\nAll tests passed!")