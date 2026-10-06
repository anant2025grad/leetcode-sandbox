#logic --> typically roman numerals are ordered in
#          greatest to least order, however some
#          numbers, such as 4 (IV) have lesser
#          symbols followed by larger ones.

def romanNumerals(s):
    roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
        }

    total = 0

    for i in range(len(s)):
        if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    
    return total
