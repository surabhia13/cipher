"""
Cipher Test Suite
"""

import unittest
from cipher import (
    rail_fence_encode,
    rail_fence_decode,
    filter_string,
    encode_character,
    decode_character,
    vigenere_encode,
    vigenere_decode,
)


class TestRailFenceEncode(unittest.TestCase):
    """Rail Fence Encode Tests"""

    def test_1(self):
        """rail_fence_encode(): Simple case with key 3 and simple string"""
        word = "HELLO"
        key = 3
        actual = rail_fence_encode(word, key)
        expected = "HOELL"
        self.assertEqual(actual, expected)

    def test_2(self):
        """rail_fence_encode(): Case with minimum key 2 and simple string"""
        word = "ABCD"
        key = 2
        actual = rail_fence_encode(word, key)
        expected = "ACBD"
        self.assertEqual(actual, expected)

    def test_3(self):
        """rail_fence_encode(): Case where key equals the length of the string"""
        word = "HELLO"
        key = 5
        actual = rail_fence_encode(word, key)
        expected = "HELLO"
        self.assertEqual(actual, expected)

    def test_4(self):
        """rail_fence_encode(): Odd length string with key 3"""
        word = "SECRET"
        key = 3
        actual = rail_fence_encode(word, key)
        expected = "SEERTC"
        self.assertEqual(actual, expected)

    def test_5(self):
        """rail_fence_encode(): Single word with non-alphabet characters and key 4"""
        word = "HELLO_WORLD"
        key = 4
        actual = rail_fence_encode(word, key)
        expected = "HWE_OLORDLL"
        self.assertEqual(actual, expected)

    def test_6(self):
        """rail_fence_encode(): Empty string input"""
        word = ""
        key = 3
        actual = rail_fence_encode(word, key)
        expected = ""
        self.assertEqual(actual, expected)

    def test_7(self):
        """rail_fence_encode(): String with spaces and key 3"""
        word = "A B C D"
        key = 3
        actual = rail_fence_encode(word, key)
        expected = "AC   BD"
        self.assertEqual(actual, expected)


class TestRailFenceDecode(unittest.TestCase):
    """Rail Fence Decode Tests"""

    def test_1(self):
        """rail_fence_decode(): Simple case with key 3 and simple string"""
        word = "HOELL"
        key = 3
        actual = rail_fence_decode(word, key)
        expected = "HELLO"
        self.assertEqual(actual, expected)

    def test_2(self):
        """rail_fence_decode(): Case with minimum key (key = 2) and simple string"""
        word = "ACBD"
        key = 2
        actual = rail_fence_decode(word, key)
        expected = "ABCD"
        self.assertEqual(actual, expected)

    def test_3(self):
        """rail_fence_decode(): Case where key equals the length of the string"""
        word = "HELLO"
        key = 5
        actual = rail_fence_decode(word, key)
        expected = "HELLO"
        self.assertEqual(actual, expected)

    def test_4(self):
        """rail_fence_decode(): Odd length string with key 3"""
        word = "SEERTC"
        key = 3
        actual = rail_fence_decode(word, key)
        expected = "SECRET"
        self.assertEqual(actual, expected)

    def test_5(self):
        """rail_fence_decode(): Single word with non-alphabet characters and key 4"""
        word = "HWE_OLORDLL"
        key = 4
        actual = rail_fence_decode(word, key)
        expected = "HELLO_WORLD"
        self.assertEqual(actual, expected)

    def test_6(self):
        """rail_fence_decode(): Empty string input"""
        word = ""
        key = 3
        actual = rail_fence_decode(word, key)
        expected = ""
        self.assertEqual(actual, expected)

    def test_7(self):
        """rail_fence_decode(): String with spaces and key 3"""
        word = "AB  CD"
        key = 3
        actual = rail_fence_decode(word, key)
        expected = "A D BC"
        self.assertEqual(actual, expected)


class TestFilterString(unittest.TestCase):
    """Filter String Tests"""

    def test_1(self):
        """filter_string(): Simple case with mixed case letters and spaces"""
        word = "Hello World"
        actual = filter_string(word)
        expected = "helloworld"
        self.assertEqual(actual, expected)

    def test_2(self):
        """filter_string(): Case with digits, punctuation, and spaces"""
        word = "H3ll0, W0rld!"
        actual = filter_string(word)
        expected = "hllwrld"
        self.assertEqual(actual, expected)

    def test_3(self):
        """filter_string(): Case with only alphabetic characters"""
        word = "Alphabet"
        actual = filter_string(word)
        expected = "alphabet"
        self.assertEqual(actual, expected)

    def test_4(self):
        """filter_string(): Case with only numbers and punctuation"""
        word = "1234!@#"
        actual = filter_string(word)
        expected = ""
        self.assertEqual(actual, expected)

    def test_5(self):
        """filter_string(): Empty string input"""
        word = ""
        actual = filter_string(word)
        expected = ""
        self.assertEqual(actual, expected)

    def test_6(self):
        """filter_string(): String with mixed case and punctuation marks"""
        word = "The Quick Brown Fox!"
        actual = filter_string(word)
        expected = "thequickbrownfox"
        self.assertEqual(actual, expected)

    def test_7(self):
        """filter_string(): Case with spaces between characters"""
        word = "   s p a c e s   "
        actual = filter_string(word)
        expected = "spaces"
        self.assertEqual(actual, expected)


class TestEncodeCharacter(unittest.TestCase):
    """Encode Characters Tests"""

    def test_1(self):
        """encode_character(): Basic case with 'a' and 'a'"""
        p = "a"
        s = "a"
        actual = encode_character(p, s)
        expected = "a"
        self.assertEqual(actual, expected)

    def test_2(self):
        """encode_character(): Case with 'z' and 'z'"""
        p = "z"
        s = "z"
        actual = encode_character(p, s)
        expected = "y"
        self.assertEqual(actual, expected)

    def test_3(self):
        """encode_character(): Case with 'a' and 'z'"""
        p = "a"
        s = "z"
        actual = encode_character(p, s)
        expected = "z"
        self.assertEqual(actual, expected)

    def test_4(self):
        """encode_character(): Case with 'm' and 'n'"""
        p = "m"
        s = "n"
        actual = encode_character(p, s)
        expected = "z"
        self.assertEqual(actual, expected)

    def test_5(self):
        """encode_character(): Case with 'z' and 'a'"""
        p = "z"
        s = "a"
        actual = encode_character(p, s)
        expected = "z"
        self.assertEqual(actual, expected)

    def test_6(self):
        """encode_character(): Case with 'd' and 'e'"""
        p = "d"
        s = "e"
        actual = encode_character(p, s)
        expected = "h"
        self.assertEqual(actual, expected)

    def test_7(self):
        """encode_character(): Case with 'a' and 'y'"""
        p = "a"
        s = "y"
        actual = encode_character(p, s)
        expected = "y"
        self.assertEqual(actual, expected)


class TestDecodeCharacter(unittest.TestCase):
    """Decode Characters Tests"""

    def test_1(self):
        """decode_character(): Basic case with 'a' and 'b'"""
        p = "a"
        s = "b"
        actual = decode_character(p, s)
        expected = "b"
        self.assertEqual(actual, expected)

    def test_2(self):
        """decode_character(): Case with 'z' and 'y'"""
        p = "z"
        s = "y"
        actual = decode_character(p, s)
        expected = "z"
        self.assertEqual(actual, expected)

    def test_3(self):
        """decode_character(): Case with 'a' and 'z'"""
        p = "a"
        s = "z"
        actual = decode_character(p, s)
        expected = "z"
        self.assertEqual(actual, expected)

    def test_4(self):
        """decode_character(): Case with 'm' and 'z'"""
        p = "m"
        s = "z"
        actual = decode_character(p, s)
        expected = "n"
        self.assertEqual(actual, expected)

    def test_5(self):
        """decode_character(): Case with 'z' and 'a'"""
        p = "z"
        s = "a"
        actual = decode_character(p, s)
        expected = "b"
        self.assertEqual(actual, expected)

    def test_6(self):
        """decode_character(): Case with 'd' and 'h'"""
        p = "d"
        s = "h"
        actual = decode_character(p, s)
        expected = "e"
        self.assertEqual(actual, expected)

    def test_7(self):
        """decode_character(): Case with 'a' and 'y'"""
        p = "a"
        s = "y"
        actual = decode_character(p, s)
        expected = "y"
        self.assertEqual(actual, expected)


class TestVigenereEncode(unittest.TestCase):
    """Vigenere Encode Tests"""

    def test_1(self):
        """vigenere_encode(): Basic encoding with lowercase letters"""
        word = "hello"
        phrase = "key"
        actual = vigenere_encode(word, phrase)
        expected = "rijvs"
        self.assertEqual(actual, expected)

    def test_2(self):
        """vigenere_encode(): Encoding with string containing spaces"""
        word = "hello world"
        phrase = "hi"
        actual = vigenere_encode(word, phrase)
        expected = "omstvevzsl"
        self.assertEqual(actual, expected)

    def test_3(self):
        """vigenere_encode(): Encoding with string containing digits"""
        word = "password123"
        phrase = "cs"
        actual = vigenere_encode(word, phrase)
        expected = "rsukygtv"
        self.assertEqual(actual, expected)

    def test_4(self):
        """vigenere_encode(): Encoding with mixed case letters"""
        word = "HelloWorld"
        phrase = "one"
        actual = vigenere_encode(word, phrase)
        expected = "vrpzbacepr"
        self.assertEqual(actual, expected)

    def test_5(self):
        """vigenere_encode(): Encoding with non-alphabetic characters"""
        word = "1234!@#$"
        phrase = "passphrase"
        actual = vigenere_encode(word, phrase)
        expected = ""
        self.assertEqual(actual, expected)

    def test_6(self):
        """vigenere_encode(): Encoding with a longer pass phrase"""
        word = "hello"
        phrase = "longphrase"
        actual = vigenere_encode(word, phrase)
        expected = "ssyrd"
        self.assertEqual(actual, expected)

    def test_7(self):
        """vigenere_encode(): Encoding with an empty string"""
        word = ""
        phrase = "key"
        actual = vigenere_encode(word, phrase)
        expected = ""
        self.assertEqual(actual, expected)


class TestVigenereDecode(unittest.TestCase):
    """Vigenere Decode Tests"""

    def test_1(self):
        """vigenere_decode(): Basic decoding with lowercase letters"""
        word = "rijvs"
        phrase = "key"
        actual = vigenere_decode(word, phrase)
        expected = "hello"
        self.assertEqual(actual, expected)

    def test_2(self):
        """vigenere_decode(): Decoding with string containing spaces"""
        word = "omstvevzsl"
        phrase = "hi"
        actual = vigenere_decode(word, phrase)
        expected = "helloworld"
        self.assertEqual(actual, expected)

    def test_3(self):
        """vigenere_decode(): Decoding with string containing digits"""
        word = "rsukygtv"
        phrase = "cs"
        actual = vigenere_decode(word, phrase)
        expected = "password"
        self.assertEqual(actual, expected)

    def test_4(self):
        """vigenere_decode(): Decoding with mixed case letters"""
        word = "vrpzbacepr"
        phrase = "one"
        actual = vigenere_decode(word, phrase)
        expected = "helloworld"
        self.assertEqual(actual, expected)

    def test_5(self):
        """vigenere_decode(): Decoding with non-alphabetic characters"""
        word = "1234!@#$"
        phrase = "passphrase"
        actual = vigenere_decode(word, phrase)
        expected = ""
        self.assertEqual(actual, expected)

    def test_6(self):
        """vigenere_decode(): Decoding with a longer pass phrase"""
        word = "ssyrd"
        phrase = "longphrase"
        actual = vigenere_decode(word, phrase)
        expected = "hello"
        self.assertEqual(actual, expected)

    def test_7(self):
        """vigenere_decode(): Decoding with an empty string"""
        word = ""
        phrase = "key"
        actual = vigenere_decode(word, phrase)
        expected = ""
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
