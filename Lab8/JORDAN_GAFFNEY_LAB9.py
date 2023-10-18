def count_words(line):
    words = line.split()
    return len(words)
file_path = "C:\\Users\\Jordan\\OneDrive\\Documents\\Python\\CS1302\\Lab9\\example.txt"

total_words = 0
total_lines = 0
word_counts_per_line = []

with open(file_path, 'r') as file:
    lines = file.readlines()
    
    for line_number, line in enumerate(lines, start=1):
        line_word_count = count_words(line)
        word_counts_per_line.append((line_number, line_word_count))
        
        total_words += line_word_count
        total_lines += 1

with open(file_path, 'w') as output_file:
    output_file.write(f"Total number of lines: {total_lines}\n")
    output_file.write(f"Total number of words: {total_words}\n")
    output_file.write("Word count per line (line_number >> word_count):\n")
    
    for line_number, word_count in word_counts_per_line:
        output_file.write(f"Line {line_number} >> {word_count} words\n")

print("Results have been written to 'output.txt'.")