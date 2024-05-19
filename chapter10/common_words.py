from pathlib import Path


def common_words_count(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        count = contents.lower().count('the')
        print(f"Word 'the' appears approx {count} times.")


path = Path('enchanted_april')
common_words_count(path)