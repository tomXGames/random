def sub(p, q):
    if p == True and q == True:
        return True
    elif p == True and q == False:
        return False
    elif p == False and q == True:
        return True
    elif p == False and q == False:
        return True

def idkwhatkillme(p,r, q):
    if not (p or r):
        return True

def bisub(p,q):
    return p==q

for q in [True, False]:
    for p in [True, False]:
        for r in [True, False]:
            if( (not (p == (q or r))) and (idkwhatkillme(p,r,q)) and (r and p)):
                print(p, q, r)