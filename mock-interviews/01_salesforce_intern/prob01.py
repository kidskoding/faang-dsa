# Input: A string, s, a Roman numeral string that we need to convert into a valid integer value
# Output: Output: The integer value, an int, that will be converted frmo the Roman numeral string input
# 
# 1. Create a dictionary/hash map that will contain the appropriate conversions from Roman numeral to numeric value.
# Also let res be resulting that contains the numerical value conversion
# 
# 2. Check if there is a empty string. If so, return 0
# 
# 3. Loop through our input string s
#   4. Check if the current character being visited is in our dictionary
#   5. If so, get the current characer and check if it comes before or after the next character in s
#   6. If it comes before, we are going to subtract the current character from our resulting value
#   7. Otherwise, if after, we are going to add the current character from our resulting value
# 
# 8. Check if i is equal to the index of the last character in the string,
#    add its roman numeral equivalent value to the resulting value
# 9. Return the resulting value
# 
# Time: O(n)
# Space: O(1)

def prob01(s: str) -> int:
    conversions = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if not s:
        return 0

    res = 0
    i = 0
    while i < len(s) - 1:
        if s[i] in conversions:
            if conversions[s[i]] < conversions[s[i + 1]]:
                res -= conversions[s[i]]
            else:
                res += conversions[s[i]]
        else:
            return 0
        
        i += 1

    if i == len(s) - 1:
        res += conversions[s[-1]]

    return res
