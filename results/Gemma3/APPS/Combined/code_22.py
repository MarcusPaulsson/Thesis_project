def is_s_palindrome(s):
    """
    Checks if a string is an "s-palindrome".

    Args:
        s: The input string.

    Returns:
        "TAK" if the string is an "s-palindrome", "NIE" otherwise.
    """

    n = len(s)
    mirror = {
        'b': 'd',
        'd': 'b',
        'o': 'o',
        'p': 'q',
        'q': 'p',
        'v': 'v',
        'w': 'w',
        'x': 'x'
    }

    for i in range(n // 2):
        if s[i] not in mirror or mirror[s[i]] != s[n - 1 - i]:
            return "NIE"

    if n % 2 == 1:
        if s[n // 2] not in mirror or mirror[s[n // 2]] != s[n // 2]:
            return "NIE"

    return "TAK"


if __name__ == "__main__":
    s = input()
    print(is_s_palindrome(s))