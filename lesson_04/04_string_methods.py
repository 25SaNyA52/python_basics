# lower()
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
print("Aleksandr Piskarev". lower())
print(text.lower())
print("AAA".lower() == "aaa".lower())

# upper()
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
print("Aleksandr Piskarev".upper())
print(text.upper())
print("AAA".upper() == "aaa".upper())

# capitalize()
text = "abcde abcde abcde"
print(text.capitalize())

# title()
text = "abcde abcde abcde"
print(text.title())
print(id(text))
print(id(text.title()))
print(text)

# split()
text = "abcde,abcde,abcde"
text_2 = "abcde abcde abcde"
print(text.split(","))
print(text_2.split())
print(type(text.split()))

# find()
text = "Aleksandr"
print("l" in text)
print("z" in text)
print(text.find("e"))
print(text.find("x"))
print(text.find("K"))
print(text.upper().find("K"))
print(text.find("a"))
print(text.lower().find("a"))

# index()
text = "Aleksandr"
print(text.index("e"))
print(text.index("eksa"))
print(text.index("x")) #ValueError: substring not found

# count()
text = "Aleksandr"
print(text.count("e"))
print(text.count("X"))
print(text.count("a"))

# replace()
text = "Aleksandr.....Piskarev"
print(text)
print(text.replace("a","b"))
print(text.replace(".",",",3))

# join()
text = "Hello"
print(",".join(text))

students = "Ivanov Petrov Sidorov"
list_of_students = students.split(" ")
print(list_of_students)
string_with_students = ",".join(list_of_students)
print(string_with_students)
