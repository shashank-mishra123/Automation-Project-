# write the program to read a text file and count the number of lines, words and characters in the file.
from pathlib import Path


def main():
    # Resolve sample.txt relative to this script's directory so the script
    # works regardless of the current working directory.
    file_path = Path(__file__).parent / "sample.txt"

    try:
        with file_path.open("r", encoding="utf-8") as fh:
            text = fh.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    # Count lines, words, and characters
    lines = text.splitlines()
    num_lines = len(lines)
    words = text.split()
    num_words = len(words)
    num_chars = len(text)

    print(f"Reading: {file_path}")
    print(f"Lines: {num_lines}")
    print(f"Words: {num_words}")
    print(f"Characters: {num_chars}")


if __name__ == "__main__":
    main()

