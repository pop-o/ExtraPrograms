import os

# Folder path where the text files are located
folder_path = r'C:\Users\HP\Desktop\Neali wiki\train\train'

# Output file where all contents will be merged
output_file = 'merged_output.txt'

# Open the output file in write mode with utf-8 encoding
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a text file
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            
            # Open each text file with utf-8 encoding and append its content to the output file
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n')  # Add a newline after each file's content

print(f"All text files merged into {output_file}")
