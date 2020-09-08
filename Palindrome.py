

def cekPalindrome(kata):
    new_string = list(kata)
    new_string_reverse = list(kata[::-1])
    for i,a in enumerate(kata):
        if new_string[i] != new_string_reverse[i]:
            return False
    return True

print(cekPalindrome('racecar'))