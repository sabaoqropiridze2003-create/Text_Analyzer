import pytest
from analyzer import count_words, count_characters, count_vowels, reverse_text


def test_count_words():
    assert count_words("hello world python") == 3

def test_count_characters():
    assert count_characters("hello") == 5


def test_count_vowels():
    assert count_vowels("hello") == 2


def test_reverse_text():
    assert reverse_text("hello") == "olleh"




