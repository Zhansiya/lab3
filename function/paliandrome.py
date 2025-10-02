def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


print(is_palindrome("madam"))          
print(is_palindrome("Madam"))         
print(is_palindrome("nurses run"))     
print(is_palindrome("hello"))        
