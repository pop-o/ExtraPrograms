# Function to remove duplicate lines from a file
def remove_duplicate_lines(input_file, output_file):
    # Create a set to track unique lines
    seen_lines = set()

    # Open the input file and output file
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # If the line hasn't been seen before, write it to the output file
            if line not in seen_lines:
                outfile.write(line)
                seen_lines.add(line)

# File paths
input_file = r'C:\Users\HP\nepalWiki.txt'  # Replace with your input file path
output_file = 'nepaliWiki.txt'  # Replace with your desired output file path

# Remove duplicates
remove_duplicate_lines(input_file, output_file)

print(f"Duplicate lines removed. Output saved to {output_file}")
