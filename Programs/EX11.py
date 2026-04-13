grammar = {"S":["NP VP"],"NP":["Det N"],"VP":["V NP"],"Det":["the"],"N":["dog","cat"],"V":["chased"]}

def parse(sym,w):
    if not w: return False,w
    if sym not in grammar: return (w[0]==sym,w[1:])
    for r in grammar[sym]:
        temp=w[:]; ok=True
        for p in r.split():
            ok,temp=parse(p,temp)
            if not ok: break
        if ok: return True,temp
    return False,w

s="the dog chased the cat".split()
res,rem=parse("S",s)

print("Input Sentence: the dog chased the cat")
print("Output:", "Accepted" if res and not rem else "Rejected")
