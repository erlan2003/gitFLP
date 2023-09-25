symbol = input("Введите знак для выделения слов: ")
text = input("Введите строку: ")
words = text.split(symbol)
minWord = None

for word in words:
    if minWord is None or len(word) < len(minWord):
        minWord = word
print("Самое короткое слово: ", minWord)
