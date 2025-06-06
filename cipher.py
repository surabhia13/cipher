"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Surabhi Arun, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: sa59594
"""


# TODO: implement this function. You may delete this comment after you are done.
def rail_fence_encode(string, key):
    """
    pre: string is a string of characters and key is a positive
        integer 2 or greater and strictly less than the length
        of string
    post: returns a single string that is encoded with
        rail fence algorithm
    """
    n = len(string)
    if key < 2 or key >= n:
        return string
    rails = [[] for _ in range(key)]
    row, step = 0, 1
    for ch in string:
        rails[row].append(ch)
        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step
    return "".join("".join(r) for r in rails)


# TODO: implement this function. You may delete this comment after you are done.
def rail_fence_decode(string, key):
    """
    pre: string is a string of characters and key is a positive
        integer 2 or greater and strictly less than the length
        of string
    post: function returns a single string that is decoded with
        rail fence algorithm
    """
    n = len(string)
    if key < 2 or key >= n:
        return string

    cycle = 2 * key - 2
    rail_counts = [0] * key
    rail_for_pos = []
    for i in range(n):
        m = i % cycle
        rail = m if m < key else cycle - m
        rail_for_pos.append(rail)
        rail_counts[rail] += 1

    chunks = []
    idx = 0
    for count in rail_counts:
        chunks.append(string[idx : idx + count])
        idx += count

    pointers = [0] * key
    decoded = []
    for rail in rail_for_pos:
        decoded.append(chunks[rail][pointers[rail]])
        pointers[rail] += 1

    return "".join(decoded)


# TODO: implement this function. You may delete this comment after you are done.
def filter_string(string):
    """
    pre: string is a string of characters
    post: function converts all characters to lower case and then
        removes all digits, punctuation marks, and spaces. It
        returns a single string with only lower case characters
    """
    return "".join(ch for ch in string.lower() if 'a' <= ch <= 'z')


# TODO: implement this function. You may delete this comment after you are done.
def encode_character(p, s):
    """
    pre: p is a character in the pass phrase and s is a character
        in the plain text
    post: function returns a single character encoded using the
        Vigenere algorithm. You may not use a 2-D list
    """
    shift = ord(p) - ord('a')
    val = ord(s) - ord('a')
    return chr((val + shift) % 26 + ord('a'))


# TODO: implement this function. You may delete this comment after you are done.
def decode_character(p, s):
    """
    pre: p is a character in the pass phrase and s is a character
        in the encrypted text
    post: function returns a single character decoded using the
        Vigenere algorithm. You may not use a 2-D list
    """
    shift = ord(p) - ord('a')
    val = ord(s) - ord('a')
    return chr((val - shift) % 26 + ord('a'))


# TODO: implement this function. You may delete this comment after you are done.
def vigenere_encode(string, phrase):
    """
    pre: string is a string of characters and phrase is a pass phrase
    post: function returns a single string that is encoded with
        Vigenere algorithm
    """
    text = filter_string(string)
    key = filter_string(phrase)
    if not key:
        return ""
    return "".join(
        encode_character(key[i % len(key)], ch)
        for i, ch in enumerate(text)
    )


# TODO: implement this function. You may delete this comment after you are done.
def vigenere_decode(string, phrase):
    """
    pre: string is a string of characters and phrase is a pass phrase
    post: function returns a single string that is decoded with
        Vigenere algorithm
    """
    text = filter_string(string)
    key = filter_string(phrase)
    if not text or not key:
        return ""
    return "".join(
        decode_character(key[i % len(key)], ch)
        for i, ch in enumerate(text)
    )


# TODO: implement this function. You may delete this comment after you are done.
def main():
    """Main function that reads stdin and runs each cipher"""
    # read the plain text from stdin (terminal/input)
    print("Rail Fence Cipher\n")
    plaintext = input()
    # read the key from stdin (terminal/input)
    key = int(input())
    # encrypt and print the encoded text using rail fence cipher
    encoded_text = rail_fence_encode(plaintext, key)
    print(f"Plain Text: {plaintext}")
    print(f"Key: {key}")
    print(f"Encoded Text: {encoded_text}\n")

    # read encoded text from stdin (terminal/input)
    cipher_in = input()
    # read the key from stdin (terminal/input)
    key2 = int(input())
    # decrypt and print the plain text using rail fence cipher
    decoded_text = rail_fence_decode(cipher_in, key2)
    print(f"Encoded Text: {cipher_in}")
    print(f"Enter Key: {key2}")
    print(f"Decoded Text: {decoded_text}\n")

    # read the plain text from stdin (terminal/input)
    print("Vigenere Cipher\n")
    pt2 = input()
    # read the pass phrase from stdin (terminal/input)
    pass_phrase = input()
    # encrypt and print the encoded text using Vigenere cipher
    enc2 = vigenere_encode(pt2, pass_phrase)
    print(f"Plain Text: {pt2}")
    print(f"Pass Phrase: {pass_phrase}")
    print(f"Encoded Text: {enc2}\n")

    # read the encoded text from stdin (terminal/input)
    cipher2 = input()
    # read the pass phrase from stdin (terminal/input)
    pass2 = input()
    # decrypt and print the plain text using Vigenere cipher
    dec2 = vigenere_decode(cipher2, pass2)
    print(f"Encoded Text: {cipher2}")
    print(f"Pass Phrase: {pass2}")
    print(f"Decoded Text: {dec2}\n")


# Do NOT modify the following code.
if __name__ == "__main__":
    main()
