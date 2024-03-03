import json

# Read the original JSON file content
with open('words.json', 'r', encoding='utf-8') as file:
    file_content = file.read()

# Fix the structure by adding commas between objects and wrapping them in a list
fixed_content = '[' + file_content.replace('}{', '},{') + ']'

# Parse the fixed content as JSON
data = json.loads(fixed_content)

# Remove the second-to-last item if there are enough items
if len(data) > 1:
    del data[-2]

# Write the fixed and updated data back to the file
with open('words.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
