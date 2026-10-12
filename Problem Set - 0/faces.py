text = input('Send some texts with emoticons.(For Eg. "/I am very Happy Today :)/")' )

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


optext = convert(text)

print(optext)
