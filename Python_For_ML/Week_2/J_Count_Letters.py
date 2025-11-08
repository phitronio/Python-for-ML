
s = input().strip()


freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1


for ch in sorted(freq.keys()):
    print(f"{ch} : {freq[ch]}")
