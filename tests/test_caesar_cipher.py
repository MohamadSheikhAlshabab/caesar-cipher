from caesar_cipher.caesar_cipher import encrypt,decrypt
import re

def test_decrypt():
    actual = decrypt("cat is animal ! hsdfo # rr5",500)
    expected = "igz oy gtosgr   nyjlu   xx "
    assert actual == expected

def test_encrypt():
    actual = encrypt("cat is animal ! hsdfo # rr5",500)
    expected = "igz oy gtosgr   nyjlu   xx "
    assert actual == expected


