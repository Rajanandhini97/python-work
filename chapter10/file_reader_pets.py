from pathlib import Path

filenames = ['cat.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
        # print(f"Path {filename} does not exist")
    else:

        print(contents)