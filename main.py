import sys
from stats import calculate_word_count, calculate_letter_count


def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def sort_on(items):
  return items["num"]

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  filepath = sys.argv[1]
  print(filepath)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  book_text = get_book_text(filepath)
  word_count = calculate_word_count(book_text)
  print("============ Word Count ============")
  print(f"Found {word_count} total words")
  print("============ Character Count ============")
  char_count = calculate_letter_count(book_text)
  for letter in char_count:
    print(f"{letter['char']}: {letter['num']}")
  print("============ END ============")
  
main()
