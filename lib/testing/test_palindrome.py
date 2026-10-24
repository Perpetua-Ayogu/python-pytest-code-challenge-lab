import pytest

from palindrome import longest_palindromic_substring


@pytest.mark.parametrize(
    "text, expected",
    [
        ("babad", {"bab", "aba"}),
        ("cbbd", {"bb"}),
        ("racecar", {"racecar"}),
        ("a", {"a"}),
        ("", {""}),
        ("ac", {"a", "c"}),
        ("abc", {"a", "b", "c"}),
        ("aaaa", {"aaaa"}),
        ("abccba", {"abccba"}),
        ("xy12321z", {"12321"}),
        ("a" * 1000, {"a" * 1000}),
    ],
)
def test_longest_palindromic_substring(text, expected):
    assert longest_palindromic_substring(text) in expected
