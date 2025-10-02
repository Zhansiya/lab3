def reverse_words():
    s = input()
    words = s.split()         
    reversed_words = words[::-1]  
    result = " ".join(reversed_words) 
    return result

print(reverse_words())
