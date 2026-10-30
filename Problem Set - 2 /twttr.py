def main():
    twt = input("Input: ")
    op = omit_vowel(twt)
    print(f"Output: {op}")

def omit_vowel(text):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    opstring = ""

    for letter in text:
        if letter not in vowels:
            opstring = opstring + letter
        else:
            continue
    return opstring



main()
