# Define a mapping of English to Nepali digits
english_to_nepali = {
    '0': '०', '1': '१', '2': '२', '3': '३',
    '4': '४', '5': '५', '6': '६', '7': '७',
    '8': '८', '9': '९'
}

def replace_numbers(text):
    for eng, nep in english_to_nepali.items():
        text = text.replace(eng, nep)
    return text

# Open the file, replace numbers, and save it
input_file = r"C:\Users\HP\Desktop\merged_output.txt"
output_file = 'nepalWiki.txt'

with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

new_content = replace_numbers(content)

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(new_content)

print(f"Numbers replaced and saved to {output_file}")
