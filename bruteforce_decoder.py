
# ------------------------------------------ #
# ----- WARNING: DISGUSTING CODE AHEAD ----- #
# ------------------------------------------ #

import enchant
dictionary = enchant.Dict("en_GB")

from win10toast import ToastNotifier
toast = ToastNotifier()

from datetime import datetime, UTC
from random import shuffle
from multiprocessing import Process

alphabet_by_frequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

# -------------------------------------- #

def decode_code_word_with_sub(code_word, letter_sub):
    decoded_word = ""
    for letter in code_word:
        decoded_word += letter_sub[letter]
    return decoded_word


def check_letter_sub(code_word, letter_sub):
    decoded_word = decode_code_word_with_sub(code_word, letter_sub)

    if dictionary.check(decoded_word):
        decoded_code = []
        # That word was decoded successfully, so check the rest of the code
        num_not_correct = 0
        for word in words_in_code:
            decoded_word = decode_code_word_with_sub(word, letter_sub)
            decoded_code.append(decoded_word)
            if not dictionary.check(decoded_word):
                num_not_correct += 1

        with open("./decode_output.txt", "a") as file:
            file.write("\n# --------------- WORD FOUND --------------- #")
            file.write(f"\nLetter Substitution: {letter_sub}")
            file.write(f"\nDecrypted Word: {decoded_word}")
            file.write(f"\nWords In Code Successfully Decrypted: {len(words_in_code) - num_not_correct}")
            file.write(f"\nWords In Code Decryption Fails: {num_not_correct}")
            file.write(f"\nCode Decryption Percentage: {((len(words_in_code) - num_not_correct) / len(words_in_code)) * 100}")
            decoded_code_str = ""
            for word in decoded_code:
                decoded_code_str += word+" "
            file.write(f"\nDecrypted Code: {decoded_code_str}")
            toast.show_toast(
                "Bruteforce Decoder",
                f"A word has been decrypted successfully. Code Decryption Percentage: {((len(words_in_code) - num_not_correct) / len(words_in_code)) * 100}",
                duration=5,
                threaded=True
            )

# -------------------------------------- #

words_in_code = []


def prepare_for_decode(code):
    global words_in_code
    words_in_code = code.split(" ")

    # Sort the letters in the code by occurrence
    letters_in_code = [letter for letter in code if letter in alphabet_by_frequency]
    letters_in_code = sorted(letters_in_code, key=letters_in_code.count, reverse=True)
    sorted_letters_in_code = []
    sorted_letters_in_code = [letter for letter in letters_in_code if letter not in sorted_letters_in_code]
    if len(sorted_letters_in_code) > 20:
        num_over_limit = len(sorted_letters_in_code) - 20
        for letter in sorted_letters_in_code.copy()[-num_over_limit:-1]:
            sorted_letters_in_code.remove(letter)

    num_under_limit = 20 - len(sorted_letters_in_code)
    ignore_chars = ["_" for _ in range(num_under_limit)]
    sorted_letters_in_code_with_ignore_chars = ignore_chars
    [sorted_letters_in_code_with_ignore_chars.append(letter) for letter in sorted_letters_in_code]

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

    word_being_decrypted = words_in_code[longest_word_index]
    return word_being_decrypted, sorted_letters_in_code_with_ignore_chars

# -------------------------------------- #


def for_loop_block(letters_index, letter, index, prev_letter, prev_index, letter_sub, sorted_letters_in_code, unused_letters):
    if len(sorted_letters_in_code) < letters_index + 1:
        return prev_letter, prev_index, letter_sub

    if prev_letter:
        unused_letters.insert(prev_index, prev_letter)
    prev_letter = letter
    prev_index = index

    unused_letters.remove(letter)
    letter_sub[sorted_letters_in_code[letters_index]] = letter

    return prev_letter, prev_index, letter_sub


def worker(code):
    # exec() doesn't work with the multiprocessing and I can't be bothered figuring out an elegant solution so fuck it.
    # The above line pretty much describes the creation process of this goofy program.
    prev_b = None
    prev_index_b = None
    prev_c = None
    prev_index_c = None
    prev_d = None
    prev_index_d = None
    prev_e = None
    prev_index_e = None
    prev_f = None
    prev_index_f = None
    prev_g = None
    prev_index_g = None
    prev_h = None
    prev_index_h = None
    prev_i = None
    prev_index_i = None
    prev_j = None
    prev_index_j = None
    prev_k = None
    prev_index_k = None
    prev_l = None
    prev_index_l = None
    prev_m = None
    prev_index_m = None
    prev_n = None
    prev_index_n = None
    prev_o = None
    prev_index_o = None
    prev_p = None
    prev_index_p = None
    prev_q = None
    prev_index_q = None
    prev_r = None
    prev_index_r = None
    prev_s = None
    prev_index_s = None
    prev_t = None
    prev_index_t = None

    letter_sub = {}
    local_alphabet = alphabet_by_frequency.copy()
    shuffle(local_alphabet)

    word_being_decrypted, sorted_letters_in_code = prepare_for_decode(code)

    # First letter in code
    for a in local_alphabet:
        unused_letters = local_alphabet.copy()
        unused_letters.remove(a)
        letter_sub[sorted_letters_in_code[0]] = a

        # Second letter
        for index_b, b in enumerate(unused_letters):
            if sorted_letters_in_code[1] != "_":
                prev_b, prev_index_b, letter_sub = for_loop_block(1, b, index_b, prev_b, prev_index_b, letter_sub, sorted_letters_in_code, unused_letters)

            # Third
            for index_c, c in enumerate(unused_letters):
                if sorted_letters_in_code[2] != "_":
                    prev_c, prev_index_c, letter_sub = for_loop_block(2, c, index_c, prev_c, prev_index_c, letter_sub, sorted_letters_in_code, unused_letters)

                # Et cetera
                for index_d, d in enumerate(unused_letters):
                    if sorted_letters_in_code[3] != "_":
                        prev_d, prev_index_d, letter_sub = for_loop_block(3, d, index_d, prev_d, prev_index_d, letter_sub, sorted_letters_in_code, unused_letters)

                    for index_e, e in enumerate(unused_letters):
                        if sorted_letters_in_code[4] != "_":
                            prev_e, prev_index_e, letter_sub = for_loop_block(4, e, index_e, prev_e, prev_index_e, letter_sub, sorted_letters_in_code, unused_letters)

                        for index_f, f in enumerate(unused_letters):
                            if sorted_letters_in_code[5] != "_":
                                prev_f, prev_index_f, letter_sub = for_loop_block(5, f, index_f, prev_f, prev_index_f, letter_sub, sorted_letters_in_code, unused_letters)

                            for index_g, g in enumerate(unused_letters):
                                if sorted_letters_in_code[6] != "_":
                                    prev_g, prev_index_g, letter_sub = for_loop_block(6, g, index_g, prev_g, prev_index_g, letter_sub, sorted_letters_in_code, unused_letters)

                                for index_h, h in enumerate(unused_letters):
                                    if sorted_letters_in_code[7] != "_":
                                        prev_h, prev_index_h, letter_sub = for_loop_block(7, h, index_h, prev_h, prev_index_h, letter_sub, sorted_letters_in_code, unused_letters)

                                    for index_i, i in enumerate(unused_letters):
                                        if sorted_letters_in_code[8] != "_":
                                            prev_i, prev_index_i, letter_sub = for_loop_block(8, i, index_i, prev_i, prev_index_i, letter_sub, sorted_letters_in_code, unused_letters)

                                        for index_j, j in enumerate(unused_letters):
                                            if sorted_letters_in_code[9] != "_":
                                                prev_j, prev_index_j, letter_sub = for_loop_block(9, j, index_j, prev_j, prev_index_j, letter_sub, sorted_letters_in_code, unused_letters)

                                            for index_k, k in enumerate(unused_letters):
                                                if sorted_letters_in_code[10] != "_":
                                                    prev_k, prev_index_k, letter_sub = for_loop_block(10, k, index_k, prev_k, prev_index_k, letter_sub, sorted_letters_in_code, unused_letters)

                                                for index_l, l in enumerate(unused_letters):
                                                    if sorted_letters_in_code[11] != "_":
                                                        prev_l, prev_index_l, letter_sub = for_loop_block(11, l, index_l, prev_l, prev_index_l, letter_sub, sorted_letters_in_code, unused_letters)

                                                    for index_m, m in enumerate(unused_letters):
                                                        if sorted_letters_in_code[12] != "_":
                                                            prev_m, prev_index_m, letter_sub = for_loop_block(12, m, index_m, prev_m, prev_index_m, letter_sub, sorted_letters_in_code, unused_letters)

                                                        for index_n, n in enumerate(unused_letters):
                                                            if sorted_letters_in_code[13] != "_":
                                                                prev_n, prev_index_n, letter_sub = for_loop_block(13, n, index_n, prev_n, prev_index_n, letter_sub, sorted_letters_in_code, unused_letters)

                                                            for index_o, o in enumerate(unused_letters):
                                                                if sorted_letters_in_code[14] != "_":
                                                                    prev_o, prev_index_o, letter_sub = for_loop_block(14, o, index_o, prev_o, prev_index_o, letter_sub, sorted_letters_in_code, unused_letters)

                                                                for index_p, p in enumerate(unused_letters):
                                                                    if sorted_letters_in_code[15] != "_":
                                                                        prev_p, prev_index_p, letter_sub = for_loop_block(15, p, index_p, prev_p, prev_index_p, letter_sub, sorted_letters_in_code, unused_letters)

                                                                    for index_q, q in enumerate(unused_letters):
                                                                        if sorted_letters_in_code[16] != "_":
                                                                            prev_q, prev_index_q, letter_sub = for_loop_block(16, q, index_q, prev_q, prev_index_q, letter_sub, sorted_letters_in_code, unused_letters)

                                                                        for index_r, r in enumerate(unused_letters):
                                                                            if sorted_letters_in_code[17] != "_":
                                                                                prev_r, prev_index_r, letter_sub = for_loop_block(17, r, index_r, prev_r, prev_index_r, letter_sub, sorted_letters_in_code, unused_letters)

                                                                            for index_s, s in enumerate(unused_letters):
                                                                                if sorted_letters_in_code[18] != "_":
                                                                                    prev_s, prev_index_s, letter_sub = for_loop_block(18, s, index_s, prev_s, prev_index_s, letter_sub, sorted_letters_in_code, unused_letters)

                                                                                for index_t, t in enumerate(unused_letters):
                                                                                    prev_t, prev_index_t, letter_sub = for_loop_block(19, t, index_t, prev_t, prev_index_t, letter_sub, sorted_letters_in_code, unused_letters)

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


if __name__ == "__main__":
    code = input("Enter the encrypted message: ")
    words_in_code = code.split(" ")

    process_count = input("How many processes do you want decoding it?\n")
    try:
        process_count = int(process_count)
    except ValueError:
        exit("\nProcess count must be a number.")

    # Add a new section to the output file
    with open("./decode_output.txt", "a") as file:
        file.write(f"\n\n---------- DECODER STARTED AT {str(datetime.now(UTC)).split('.')[0]} UTC ----------")
        file.write(f"\nCode being decrypted: {code}\n")

    processes = []
    for _ in range(process_count):
        process = Process(target=worker, args=(code,))
        processes.append(process)
        process.start()

    print(f"The decoding process has begun. {process_count} processes are currently working. For optimisation purposes, nothing will be printed to this console during the process. If a word is successfully decrypted, or if the process finishes, you will receive a notification.")

    for process in processes:
        process.join()

    toast.show_toast(
        "Bruteforce Decoder",
        "The decoder has finished.",
        duration=10
    )
