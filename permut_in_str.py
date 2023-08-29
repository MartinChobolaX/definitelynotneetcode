from collections import Counter

def checkInclusion(s1, s2):
    s1_count = Counter(s1)
    per_len = len(s1)
    for i in range(len(s2)-per_len+1):
        if Counter(s2[i:i+per_len]) == s1_count:
            return True
    return False
    
print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))
print(checkInclusion(s1 = "ab", s2 = "eidboaoo"))
print(checkInclusion(s1 = "adc", s2 = "dcda"))