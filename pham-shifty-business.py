used = [False]*26
alphabet = [""]*26
word = input()
pointer = ord(input())-65

while sum(used)>0:
    while used[pointer]:
        pointer += 1
        if pointer == 27: pointer = 0
    
    
    