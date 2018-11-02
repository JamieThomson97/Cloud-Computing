import string

str = "Today, is gonna be the day, that they're gonna give it back to you!"
str2 = "ja!!!,,?!\"?mie"

punctuation = set(string.punctuation)
remove_punct = ''.join(x for x in str2 if x not in punctuation)
print(remove_punct)

print(remove_punct.split())