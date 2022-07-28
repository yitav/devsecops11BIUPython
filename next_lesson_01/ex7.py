
sentence = 'Hello world!'

# first option:
first_index = sentence.find('o')
print(first_index)
second_index = sentence.find('o', first_index+1)
print(second_index)


#second option:
first_index = sentence.index('o')
print(first_index)
second_index = sentence.index('o', first_index+1)
print(second_index)

#second part of question:
print(sentence[:first_index+1])
print(sentence[second_index:])