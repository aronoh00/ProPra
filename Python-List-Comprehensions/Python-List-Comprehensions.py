numbers = [42, 87, 13, 29, 65, 98, 7, 54, 33]
uneven_numbers = [num for num in numbers if num % 2 != 0]
print("ungerade Zahlen:", uneven_numbers)

languages = ["Python", "Java", "JavaScript", "C++", "Ruby"]
length = [len(lang) for lang in languages]
print("Wortlängen:", length)

words = ["Hallo", "Hello", "Ciao", "Hola", "Bonjour"]
short_words = [word.upper() for word in words if len(word) < 5]
print("Short words:", short_words)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
collatz = []
for num in numbers:
    if num % 2 == 0:
        collatz.append(num // 2)
    else:
        collatz.append(3 * num + 1)
print(collatz)
