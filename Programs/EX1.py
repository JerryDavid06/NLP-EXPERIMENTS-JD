import re

text = "My email is test123@gmail.com and phone is 9876543210"

email = re.findall(r'\S+@\S+', text)
phone = re.findall(r'\d{10}', text)

search_word = re.search(r'email', text)

print("Email:", email)
print("Phone:", phone)

if search_word:
    print("Word 'email' found")
