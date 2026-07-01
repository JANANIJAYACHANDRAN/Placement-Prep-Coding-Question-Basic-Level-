print("Character is vowel or not")
character = input("Enter a character:")
if(character.isalpha()):
    if character in "AEIOUaeiou":
        print("Vowel")
else:
    print("Not a vowel.")
