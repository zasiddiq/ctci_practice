from collections import defaultdict

def palindrome_permutation(string: str) -> bool:
    hash_map = defaultdict(int)

    for letter in string:
        if letter != ' ':
            hash_map[letter.lower()] += 1
    
    odd_count = 0
    for val in hash_map.values():
        if val % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return False
    return True

if __name__ == "__main__":
    print( palindrome_permutation('Tact Coa') ) # True
    print( palindrome_permutation('Able was I ere I saw Elba') ) # True
    print( palindrome_permutation('jhsabckuj ahjsbckj') ) # True

    print( palindrome_permutation('Not a Palindrome') ) # False
    print( palindrome_permutation('Random Words') ) # False