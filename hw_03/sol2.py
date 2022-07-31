

username = input("Please enter username:")
letters_to_check = ['a', 'b', 'c', 'o']
username_converted = ''
for i in range(len(username)):
    if username[i] == " ":
        break
    elif username[i] in letters_to_check:
        username_converted += username[i].upper()
    else:
        username_converted += username[i].lower()

print(username_converted)
