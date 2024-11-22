counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

if 'a' not in counters.keys():
    counters['a'] = 0
print(counters)