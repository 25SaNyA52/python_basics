sentence = "Hello world of python"
print(sentence[0])
print(sentence[-1])
#print(sentence[50]) #IndexError: string index out of range
print(sentence[0:4+1])
print(sentence[0:12:1])
print(sentence[0:12:2])
print(sentence[::-1]) #revrese string without using a function
print(sentence[-1:-7:-1])
print(sentence[-10:-1:])
print(sentence[::])
print(sentence[0:])
print(sentence[0:50])

text_len = len(sentence)
print(text_len)
print(sentence[0:text_len-1])

print(id(sentence))
sentence = sentence[0] + sentence[1:]
print(sentence)
print(id(sentence))