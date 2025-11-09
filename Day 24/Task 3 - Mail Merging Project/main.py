# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from docx import Document
PLACEHOLDER = "[name]"

# Open names file with UTF-8 encoding to avoid decoding errors
with open("./Input/Names/invited_names.txt", encoding="utf-8") as names_file:
    names = names_file.readlines()

# Open the letter template as a .docx file using python-docx
doc = Document("./Input/Letters/starting_letter.docx")

# Iterate over each name and create a new letter
for name in names:
    stripped_name = name.strip()

    # Replace placeholder with actual name in the document
    for para in doc.paragraphs:
        if PLACEHOLDER in para.text:
            para.text = para.text.replace(PLACEHOLDER, stripped_name)

    # Save the modified document with the new name
    doc.save(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx")
