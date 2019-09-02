def reverse(text):
    text = ''.join(e for e in text if e.isalnum())
    text = text.lower()
    print(text)
    return text[::-1]

def is_palindrome(text):
    text = ''.join(e for e in text if e.isalnum())
    text = text.lower()
    print(text)
    return text == reverse(text)

something = input("Enter word: ")
if is_palindrome(something):
    print(f"This word ({something}) is polindrome!")
else:
    print(f"This word ({something}) is not polindrome!")

