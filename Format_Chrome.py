''' Request: string(cookies)
    Return : dict'''

def Changecookies(s):
    t=s.split("; ")
    k=[]
    j=[]
    for r in t:
        w=r.split("=")
        k.append(w[0])
        j.append(w[1])
    f=dict(zip(k,j))
    return f
