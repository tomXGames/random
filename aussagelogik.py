def sub(p, q):
    if p == q or not q:
        return True
    return False

def bisub(p,q):
    return p==q

for q in [True, False]:
    for p in [True, False]:
        for s in [True, False]:
            for r in [True, False]:
                print(bisub(s,p), sub(s,q), bisub(p, (not q)), bisub((not r), s))

