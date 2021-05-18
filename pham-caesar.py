word = input()
häufigkeit = [0 for i in range(0, 26)]
for char in word:
    häufigkeit[ord(char)-65] += 1
for index, h in enumerate(häufigkeit):
    print(chr(65+index), h)