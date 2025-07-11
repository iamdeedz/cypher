# Letter Substitution String
letter_sub_str = input("Enter the letter substitution: ")
letter_sub_str = letter_sub_str.lstrip("{")
letter_sub_str = letter_sub_str.rstrip("}")

# Convert string to dictionary
letter_sub = {}
letter_sub_str_split = letter_sub_str.split(", ")

for letter_pair in letter_sub_str_split:
    letter_pair_split = letter_pair.split(": ")

    for i, letter in enumerate(letter_pair_split):
        letter_pair_split[i] = letter.strip("'")

    letter_sub[letter_pair_split[0]] = letter_pair_split[1]

letter_sub_reversed = {v: k for k, v in letter_sub.items()}

# Decode the message

encoded_message = input("What's the encoded message? ")
decoded_message = ""

for letter in encoded_message:
    decoded_message += letter_sub_reversed[letter]


print("The decoded message is: " + decoded_message)
