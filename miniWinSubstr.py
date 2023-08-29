from collections import Counter
def minWindow(s, t):
    if (len(t) > len(s)) or not set(t).issubset(set(s)) :
            return ""
    else:
        l,r = 0,len(s)-1
        t_set = set(t)
        t_counter = Counter(t)
        while len(s) > len(t):
            s_counter = Counter(s)
            print(s)
            if (s[0] not in t_set) or (set(s[1:]) >= t_set) and (s_counter[s[0]] - 1 >= t_counter[s[0]]):
                s = s[1:]
            elif (s[-1] not in t_set) or (set(s[:-1]) >= t_set) and (s_counter[s[-1]] - 1 >= t_counter[s[-1]]):
                s = s[:-1]
            else: 
                return s   
        return s
        
        
        
print("My output:",minWindow(s = "ADOBECODEBANC", t = "ABC"))
print("Output: BANC")

print("My output:",minWindow(s = "a", t = "a"))
print("Output: a")

print("My output:",minWindow(s = "ab", t = "a"))
print("Output: a")

print("My output:",minWindow(s = "acbbaca", t = "aba"))
print("Output: baca")

print("My output:",minWindow(s = "cabwefgewcwaefgcf", t = "cae"))
print("Output: cwae")