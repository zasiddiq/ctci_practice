def string_compression(s: str) -> str:
    out = ''
    sum = 1
    for index in range(len(s[:-1])):
        if s[index] == s[index+1]:
            sum+=1
        else:
            out = out + s[index] + str(sum)
            sum = 1
    out = out + s[-1] + str(sum)

    return min(s, out)

        
if __name__ == '__main__':
    print( string_compression('aaabccc') ) # should be a3b1c3
    print( string_compression('aabcccccaaa') ) # should be a2b1c5a3
    print( string_compression('a') ) # should return a