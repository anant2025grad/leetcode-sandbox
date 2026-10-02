def isPalindrome(x):
    if x < 0:
        return False
    
    original = x
    reversed = 0
    
    while x > 0:
        digit = x % 10
        reversed = (reversed * 10) + digit
        x = x // 10
        
    return original == reversed - x

# test cases       

print(isPalindrome(131))
print(isPalindrome(11))
print(isPalindrome(12))

"""
    return str(x) == str(x)[::-1]
"""