message = input("> ")
words = message.split(' ') # returns a list of words seperated
# by ' ' parameter
emojis = {
    ":)": "😊",
    ":(": "😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

