from collections import defaultdict

def is_unique(string: str) -> bool:
    unique_hashtable = defaultdict(int)
    for letter in string:
        unique_hashtable[letter.lower()] += 1
    
    for occurances in unique_hashtable.values():
        if occurances > 1:
            return False
        return True

if __name__ == '__main__':
    print( is_unique('Test') ) # should be False
    print( is_unique('Uniqe') ) # should be True