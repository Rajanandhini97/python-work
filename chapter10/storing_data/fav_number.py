from pathlib import Path
import json


def fav_num():
    path = Path('fav_number.json')
    if path.exists():
        contents = path.read_text()
        fav_num = json.loads(contents)
        print(f"I know your favourite number! It's {fav_num}")
    else:
        fav_num = input("What is your favourite number? ")
        contents = json.dumps(fav_num)
        path.write_text(contents)


fav_num()




