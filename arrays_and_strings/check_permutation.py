from collections import defaultdict

def check_permutation(string1: str, string2: str) -> bool:

    if len(string1) != len(string2):
        return False

    string1_hashtable = defaultdict(int)
    string2_hashtable = defaultdict(int)

    for letter in string1:
        string1_hashtable[letter.lower()] += 1
    for letter in string2:
        string2_hashtable[letter.lower()] += 1

    if string1_hashtable == string2_hashtable:
        return True
    return False

if __name__ == '__main__':
    print( check_permutation('asd', 'das') ) # should be True
    print( check_permutation('test', 'no') ) # should be False