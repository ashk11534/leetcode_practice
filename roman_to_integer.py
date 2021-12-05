class Solution:
    def romanToInt(self, s: str) -> int:
        roman_letters = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'A': 0
        }
        s = list(s)
        s.append('A')
        sum = 0
        i = 0
        while i < len(s) - 1:
            if roman_letters[s[i]] < roman_letters[s[i + 1]]:
                sum += abs(roman_letters[s[i]] - roman_letters[s[i + 1]])
                i += 2
                continue
            if roman_letters[s[i]] < roman_letters[s[i - 1]] and roman_letters[s[i]] < roman_letters[s[i + 1]]:
                sum -= roman_letters[s[i]]
            if roman_letters[s[i + 1]] == 0:
                sum += roman_letters[s[i]]
                break
            else:
                sum += roman_letters[s[i]]
            i += 1
        return sum
