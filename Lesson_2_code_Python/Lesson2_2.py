text = input("Введите строку: ")
words = text.split(";")
maxWord = ""

for word in words:
    if len(word) > len(maxWord):
        maxWord = word

print("Самое длинное слово: ", maxWord)
