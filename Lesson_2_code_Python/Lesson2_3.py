symbol = input("Введите знак для выделения слов: ")
text = input("Введите строку: ")
words = text.split(symbol)
minWord = None

for word in words:
    if minWord is None or len(word) < len(minWord):
        minWord = word

for word in words:
    if len(word) == len(minWord):
        print("Самое короткое слово: ", word)
