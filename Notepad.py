import os

notes_folder = "notes"

if not os.path.exists(notes_folder):
    os.makedirs(notes_folder)

while True:
    note_title = input("Enter a title for your note: ")
    if not note_title:
        break

    note_text = input("Enter the text for your note: ")

    note_file = open(os.path.join(notes_folder, note_title + ".txt"), "w")
    note_file.write(note_text)
    note_file.close()

    print("Note saved successfully!")
