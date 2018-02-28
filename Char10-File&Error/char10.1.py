with open('python_note_example.txt') as file_obj:
    contents = file_obj.read()
    print(contents.rstrip())
print("------------------------------")
with open('python_note_example.txt') as file_obj:
    lines = file_obj.readlines()

for line in lines:
    print(line.rstrip())
print("------------------------------")
