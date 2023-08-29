from collections import Counter
def solution(s,k):
    l,r = 0,0
    char_freq = custom_counter(s)
    longest_sub = 1
    while r < len(s):
        char_freq[s[r]] += 1
        while (r - l + 1) - max(char_freq.values()) > k:
            char_freq[s[l]] -=1
            l += 1
        r += 1
        longest_sub = max(longest_sub,r-l)
    return longest_sub


def custom_counter(string):
    char_count = Counter(string)
    
    # Include keys with zero counts
    all_chars = set(string)
    for char in all_chars:
        if char in char_count:
            char_count[char] = 0
    
    return char_count

print(

    f"""Example 1:
Output: 4
My output: {solution("ABAB",2)}
"""
)
print(

    f"""
Example 2:
Output: 4
My output: {solution("AABABBA",1)}

"""
)
print(

    f"""
Example 3:
Output: 4
My output: {solution("AAAA",2)}

"""
)
print(

    f"""
Example 4:
Output: 7
My output: {solution("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
,7)}

"""
)