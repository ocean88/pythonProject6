import random   # Импорт библиотеки рандом

"""
Функция кодировки случайного слова в морзу
"""
def morse_encode(word):
  morse_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
  }

  morse_code = ''
  for char in word.lower():
    if char in morse_dict:
      morse_code += morse_dict[char] + ' '
    else:
      morse_code += char

  return morse_code

"""
Функция получения случайного слова из списка.
"""

def get_word(samples):
  random_word = random.choice(samples)
  morse_code = morse_encode(random_word)

  return random_word, morse_code

def print_statistics(answers):

    """
    Формула подсчета результатов содержания листа answers
    """

    right_answers = sum(answers)
    wrong_answers = len(answers) - right_answers

    """
    Вывод результатов
    """
    print("\n")
    print(f"Всего задачек: {len(answers)}")
    print(f"Отвечено верно: {right_answers}")
    print(f"Отвечено неверно: {wrong_answers}")

samples = ['code', 'bit', 'list', 'soul', 'next']

answers = []

counter = 1

print(f"Сегодня мы потренируемся расшифровывать морзянку. \nНажмите Enter и начнем")
input()

"""
Запуск цикла до 5 рандомных слов(вопросов)
"""

while len(answers) < 5:

    word, morse = get_word(samples) # Вызываем функцию вывода случайного слова
    print(f"Слово {counter}", morse)

    answer_input = str(input("Введите ответ")).lower() # Вводим ответ пользователя для дальнейшей сверки

    if answer_input == word:
        print(f"Правильно это {word}")  # Если ответ правильный
        answers.append(True) # Добавить слово True в лист answers
        counter += 1
    else:
        print(f"Неверно, это {word}") # Если ответ неправильный
        answers.append(False) # Добавить слово False в лист answers
        counter += 1


print_statistics(answers)