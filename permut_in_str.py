from collections import Counter

def checkInclusion(self, s1, s2):
    s1_count = Counter(s1)
    s2_count = Counter(s2)

    l,r = 0,0
    