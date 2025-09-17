def sort_on(items):
  return items["num"]

def calculate_word_count(text):
  return len(text.split())

def calculate_letter_count(text):
  lower_text = text.lower()
  dict = {}
  for letter in lower_text:
    if letter and letter.isalpha():
      if letter in dict:
        dict[letter] += 1
      else:
        dict[letter] = 1
  
  result = []
  for letter in dict:
    result.append({
      "char": letter,
      "num": dict[letter]
    })
  return sorted(result, key=sort_on, reverse=True)
