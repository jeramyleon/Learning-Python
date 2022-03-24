def emoji_converter(message):
    words = message.split(' ') # returns a list of words seperated
    # by ' ' parameter
    emojis = {
    ":)": "😊",
    ":(": "😒"
}
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))

# functions usually should not worry about receiving input
# or printing them
