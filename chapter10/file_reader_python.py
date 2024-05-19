from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()
# contents = contents.rstrip()
print("Printing the file..")
print(contents)

print("\nLooping through the content ans printing each line..")
for line in contents.splitlines():
    print(line)