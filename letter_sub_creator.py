from random import choice

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
unused_letters = alphabet.copy()
letter_sub = {" ": " "}
for letter in alphabet:
    random_letter = choice(unused_letters)
    letter_sub[letter] = random_letter
    unused_letters.remove(random_letter)

message_to_encode = "this is encrypted text"
encoded_message = ""
for letter in message_to_encode:
    encoded_message += letter_sub[letter]

print("Encoded Message: " + encoded_message)
wants_letter_sub = True if input("Do you want the letter substitution? y/n: ").lower() == "y" else False
if wants_letter_sub:
    print(letter_sub)