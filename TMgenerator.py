#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import copy

def generator(L):
    TL =list()
    for x in L:
        LL = list() #Leaf list : show who is current leaf
        AL = dict() #added list : show who is already added
        AL[x]=0
        S = "(" + x + ")"
        TL.append(S)
        extender([i for i in L if i != x],S,LL,AL,TL)
    TL.append("EOG")
    return TL

#RL : remained list
#S : current S fomula
def extender(RL,S,LL,AL,TL):
    #print(RL,S,LL,AL)
    for x in RL:
        for al_key, al_value in AL.items():
            if al_key not in LL:
                t = h_parser(S,al_value+1)
                y = S[0:t] + " " + x + S[t:]
                #print(y)
                TL.append(y)
                NLL = copy.deepcopy(LL)
                NLL.append(x)
                NAL = copy.deepcopy(AL)
                NAL[x] = al_value+1
                extender([i for i in RL if i != x],y,NLL,NAL,TL)
            else:
                y = S.replace(al_key, "(" + al_key + " " + x + ")")
                #print(y)
                TL.append(y)
                NLL = copy.deepcopy(LL)
                NLL.append(x)
                NLL.remove(al_key)
                NAL = copy.deepcopy(AL)
                NAL[x] = al_value+1
                extender([i for i in RL if i != x],y,NLL,NAL,TL)



#  hierachy_parser tells where new token should be put
def h_parser(S,n):
    t = len(S)
    for i in range(n):
        t = S.rfind(")",0,t)
    return t #t is location of ")"


'''
if __name__ == '__main__':
    TL = generator(["太朗は","花子を","殴った"])
    print(TL)
'''
