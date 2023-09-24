text = input("Введите строку: ")
key = input("Введите слово которого хотите найти в строке: ")
words = text.split()
temp = 0

for word in words:
    temp = temp + 1
    if word == key:
        print("Слово ", word," находится на ", temp, "порядке")


