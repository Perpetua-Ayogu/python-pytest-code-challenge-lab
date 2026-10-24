def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    longest = ""

    for center in range(len(s)):
        for left, right in ((center, center), (center, center + 1)):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome = s[left:right + 1]
                if len(palindrome) > len(longest):
                    longest = palindrome
                left -= 1
                right += 1

    return longest
