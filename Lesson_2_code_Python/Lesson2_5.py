text = input(" Введите предложение: ")
words = text.split()
temp = 0

for word in words:
    temp = temp + 1

print(" Количество слов в предложении: ", temp)
