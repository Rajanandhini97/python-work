from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

print("\nLooping through the content and printing each line..")
for line in contents.splitlines():
    replace_line = line.replace('Python', 'C')
    print(replace_line)