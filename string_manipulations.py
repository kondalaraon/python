#String manipulation 
first_name = "sai"
last_name = "baba"
full_name = first_name + "" + last_name
print(full_name)

repeated_test = "Hello, " * 3
print(repeated_test)


message = "Python Programing"
first_character = message[0]
print(first_character) # print = P

print(message[:6])

substring1 = message[7:]
print(substring1)

substring2 = message[7:4]
print(substring2)


message_length = len(message)
print(message_length)

upper_case = message.upper()
lower_case = message.lower()
word_list = message.split()

print(upper_case)
print(lower_case)
print(word_list)

