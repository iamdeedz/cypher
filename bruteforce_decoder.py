import enchant
dictionary = enchant.Dict("en_GB")

from win10toast import ToastNotifier
toast = ToastNotifier()

alphabet_by_frequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

# -------------------------------------- #

def decode_code_word_with_sub(code_word, letter_sub):
    decoded_word = ""
    for letter in code_word:
        decoded_word += letter_sub[letter]
    return decoded_word


def check_letter_sub(code_word, letter_sub):
    print("Checking Sub")
    print(f"letter sub: {letter_sub}")
    decoded_word = decode_code_word_with_sub(code_word, letter_sub)
    print(f"decoded word: {decoded_word}")
    print("----------------------------------------")
    if dictionary.check(decoded_word):
        with open("./decode_output.txt", "a") as file:
            file.write("\n# --------------- WORD FOUND --------------- #")
            file.write(f"\nEncrypted Word: {word_being_decrypted}")
            file.write(f"\nLetter Substitution: {letter_sub}")
            file.write(f"\nDecrypted Word: {decoded_word}")

# -------------------------------------- #

code = input("Enter the encryted message: ")
words_in_code = code.split(" ")

# Number of unique letters in the code
letters_in_code = []
letters_in_code = [letter for letter in [word for word in words_in_code] if letter not in letters_in_code]
print(letters_in_code)

# Find the longest word in the code
longest_word_index = None
longest_word_len = 0
for i, word in enumerate(words_in_code):
    if len(word) > longest_word_len:
        longest_word_len = len(word)
        longest_word_index = i

# Sort the letters in the longest word by occurrence
letters_in_word = [letter for letter in words_in_code[longest_word_index]]
letters_in_word = sorted(letters_in_word, key=letters_in_word.count, reverse=True)
sorted_letters = []
for letter in letters_in_word:
    sorted_letters.append(letter) if letter not in sorted_letters else None

# -------------------------------------- #


def for_loop_block(letters_index, letter, index, prev_letter, prev_index):
    global unused_letters, letter_sub

    if prev_letter:
        unused_letters.insert(prev_index, prev_letter)
    prev_letter = letter
    prev_index = index

    unused_letters.remove(letter)
    letter_sub[sorted_letters[letters_index]] = letter

    return prev_letter, prev_index


letter_sub = {}
word_being_decrypted = words_in_code[longest_word_index]

# Set all the prev variables to None
for letter in alphabet_by_frequency:
    if letter == "a":
        continue

    exec(f"prev_{letter} = None")
    exec(f"prev_index_{letter} = None")

# First letter in code
for a in alphabet_by_frequency:
    unused_letters = alphabet_by_frequency.copy()
    unused_letters.remove(a)
    letter_sub[sorted_letters[0]] = a

    # Second letter
    for index_b, b in enumerate(unused_letters):
        prev_b, prev_index_b = for_loop_block(1, b, index_b, prev_b, prev_index_b)

        # Third
        for index_c, c in enumerate(unused_letters):
            prev_c, prev_index_c = for_loop_block(2, c, index_c, prev_c, prev_index_c)

            # Et cetera
            for index_d, d in enumerate(unused_letters):
                prev_d, prev_index_d = for_loop_block(3, d, index_d, prev_d, prev_index_d)

                for index_e, e in enumerate(unused_letters):
                    prev_e, prev_index_e = for_loop_block(4, e, index_e, prev_e, prev_index_e)

                    for index_f, f in enumerate(unused_letters):
                        prev_f, prev_index_f = for_loop_block(5, f, index_f, prev_f, prev_index_f)

                        for index_g, g in enumerate(unused_letters):
                            prev_g, prev_index_g = for_loop_block(6, g, index_g, prev_g, prev_index_g)

                            for index_h, h in enumerate(unused_letters):
                                prev_h, prev_index_h = for_loop_block(7, h, index_h, prev_h, prev_index_h)

                                for index_i, i in enumerate(unused_letters):
                                    prev_i, prev_index_i = for_loop_block(8, i, index_i, prev_i, prev_index_i)

                                    for index_j, j in enumerate(unused_letters):
                                        prev_j, prev_index_j = for_loop_block(9, j, index_j, prev_j, prev_index_j)

                                        for index_k, k in enumerate(unused_letters):
                                            prev_k, prev_index_k = for_loop_block(10, k, index_k, prev_k, prev_index_k)

                                            for index_l, l in enumerate(unused_letters):
                                                prev_l, prev_index_l = for_loop_block(11, l, index_l, prev_l, prev_index_l)

                                                for index_m, m in enumerate(unused_letters):
                                                    prev_m, prev_index_m = for_loop_block(12, m, index_m, prev_m, prev_index_m)

                                                    for index_n, n in enumerate(unused_letters):
                                                        prev_n, prev_index_n = for_loop_block(13, n, index_n, prev_n, prev_index_n)

                                                        for index_o, o in enumerate(unused_letters):
                                                            prev_o, prev_index_o = for_loop_block(14, o, index_o, prev_o, prev_index_o)

                                                            for index_p, p in enumerate(unused_letters):
                                                                prev_p, prev_index_p = for_loop_block(15, p, index_p, prev_p, prev_index_p)

                                                                for index_q, q in enumerate(unused_letters):
                                                                    prev_q, prev_index_q = for_loop_block(16, q, index_q, prev_q, prev_index_q)

                                                                    for index_r, r in enumerate(unused_letters):
                                                                        prev_r, prev_index_r = for_loop_block(17, r, index_r, prev_r, prev_index_r)

                                                                        for index_s, s in enumerate(unused_letters):
                                                                            prev_s, prev_index_s = for_loop_block(18, s, index_s, prev_s, prev_index_s)

                                                                            for index_t, t in enumerate(unused_letters):
                                                                                prev_t, prev_index_t = for_loop_block(19, t, index_t, prev_t, prev_index_t)

                                                                                for index_u, u in enumerate(unused_letters):
                                                                                    prev_u, prev_index_u = for_loop_block(20, u, index_u, prev_u, prev_index_u)

                                                                                    for index_v, v in enumerate(unused_letters):
                                                                                        prev_v, prev_index_v = for_loop_block(21, v, index_v, prev_v, prev_index_v)

                                                                                        for index_w, w in enumerate(unused_letters):
                                                                                            prev_w, prev_index_w = for_loop_block(22, w, index_w, prev_w, prev_index_w)

                                                                                            for index_x, x in enumerate(unused_letters):
                                                                                                prev_x, prev_index_x = for_loop_block(23, x, index_x, prev_x, prev_index_x)

                                                                                                for index_y, y in enumerate(unused_letters):
                                                                                                    prev_y, prev_index_y = for_loop_block(24, y, index_y, prev_y, prev_index_y)

                                                                                                    for index_z, z in enumerate(unused_letters):
                                                                                                        prev_z, prev_index_z = for_loop_block(25, z, index_z, prev_z, prev_index_z)

                                                                                                        check_letter_sub(word_being_decrypted, letter_sub)
                                                                                                    check_letter_sub(word_being_decrypted, letter_sub)
                                                                                                check_letter_sub(word_being_decrypted, letter_sub)
                                                                                            check_letter_sub(word_being_decrypted, letter_sub)
                                                                                        check_letter_sub(word_being_decrypted, letter_sub)
                                                                                    check_letter_sub( word_being_decrypted, letter_sub)
                                                                                check_letter_sub(word_being_decrypted, letter_sub)
                                                                            check_letter_sub(word_being_decrypted, letter_sub)
                                                                        check_letter_sub(word_being_decrypted, letter_sub)
                                                                    check_letter_sub(word_being_decrypted, letter_sub)
                                                                check_letter_sub(word_being_decrypted, letter_sub)
                                                            check_letter_sub(word_being_decrypted, letter_sub)
                                                        check_letter_sub(word_being_decrypted, letter_sub)
                                                    check_letter_sub(word_being_decrypted, letter_sub)
                                                check_letter_sub(word_being_decrypted, letter_sub)
                                            check_letter_sub(word_being_decrypted, letter_sub)
                                        check_letter_sub(word_being_decrypted, letter_sub)
                                    check_letter_sub(word_being_decrypted, letter_sub)
                                check_letter_sub(word_being_decrypted, letter_sub)
                            check_letter_sub(word_being_decrypted, letter_sub)
                        check_letter_sub(word_being_decrypted, letter_sub)
                    check_letter_sub(word_being_decrypted, letter_sub)
                check_letter_sub(word_being_decrypted, letter_sub)
            check_letter_sub(word_being_decrypted, letter_sub)
        check_letter_sub(word_being_decrypted, letter_sub)
    check_letter_sub(word_being_decrypted, letter_sub)


toast.show_toast(
    "Bruteforce Decoder",
    "The decoder has finished.",
    duration=10
)
