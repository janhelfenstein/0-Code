#python exercise: working with strings
#by Jan Helfenstein

print("Giraffe Academy \nis cool.")

phrase = "Elephant Academy"
print(phrase + " is even cooler!")

phrase2 = "Rhino ACADEMY"
print(phrase2.lower())
print(phrase2.upper())
print(phrase2.upper().isupper())

print(len(phrase2))
print(phrase[0])

phrase.replace("E", "Z") #replace is only temporary!
print(phrase)

print(phrase.replace("E", "Z"))
print(phrase.replace("E", "ZaZaZa"))
print(phrase.replace(phrase[0], "HoioHoio"))

print(phrase.index("a"))
print(phrase.index("Acad"))

