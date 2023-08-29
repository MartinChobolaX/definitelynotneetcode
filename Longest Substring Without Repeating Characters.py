def solution(s):
    l, r = 0, 0
    long_str = ""
    maxLongStr = 0
    
    while r < len(s):
        if s[r] not in long_str:
            long_str += s[r]
            r += 1
            maxLongStr = max(maxLongStr, len(long_str))
        else:
            long_str = long_str[1:]
            l += 1
            
    maxLongStr = max(maxLongStr, len(long_str))
    return maxLongStr




s1 = "abcabcbb"
result1 = solution(s1)
print(True if result1 == 3 else result1)

s2 = "bbbbb"
result2 = solution(s2)
print(True if result2 == 1 else result2)

s3 = "pwwkew"
result3 = solution(s3)
print(True if result3 == 3 else result3)

s4 = ""
result4 = solution(s4)
print(True if result4 == 0 else result4)

s5 = " "
result5 = solution(s5)
print(True if result5 == 1 else result5)