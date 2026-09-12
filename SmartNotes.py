
sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n",
]

file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
print("Sample file 'class-notes.txt' created.")
print("\nPART 1: Preview with read(40)")
print("\nPART 2: readlines()")
print("\nPART 3: Loop line by line")
print("\nPART 4: Filter with a condition")
print("\nPART 5: Copy selected lines to a new file")
print("\nPART 6: Organized notes")
