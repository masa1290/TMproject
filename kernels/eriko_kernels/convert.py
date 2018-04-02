import networkx as nx

def show(S):
    L = StoL(S) #S fomula to list
    G = LtoG(L) #list to graph
    nx.nx_agraph.view_pygraphviz(G, prog='dot')  # show graph

#list to graph
def Lm_to_G(L):
    G = nx.DiGraph()
    plist = list() # show who is current parent
    pflag = False
    for char in L:
        if char == "(":
            pflag = True
        elif char == ")":
            plfag = False
            plist.pop()
        else:
            G.add_node(char)
            # add edge from current parent to child if parent exists
            if plist:
                G.add_edge(plist[-1],char)
            # register current parent if the flag is true
            if pflag:
                plist.append(char)
                pflag = False
    return G

#S fomula to list
def S_to_L(S):
    dm = list() #dummy
    string = S.split(" ")
    for chunk in string:
        chunk = chunk.split("(")
        chunk = ["(" if x=="" else x for x in chunk]
        dm2 = list() # dummy2
        for subset in chunk:
            subset = subset.split(")")
            subset = [")" if x=="" else x for x in subset]
            dm2.extend(subset)
        dm.extend(dm2)
    return dm

def Sm_to_G(S):
    L = S_to_L(S)
    G = Lm_to_G(L)
    return G

def G_to_Sk(G):
    root = "".join([n[0] for n in list(G.in_degree()) if n[1] == 0])
    S = "(" + root + ")"
    S = append_child(G,root,S)
    #root = [n for n,d in list(G.in_degree()).items() if d==0]
    #print(root)
    return S

def Sm_to_Sk(S):
    G = Sm_to_G(S)
    S = G_to_Sk(G)
    return S

def append_child(G,parent,S):
    t = S.find(parent)
    for child in list(G[parent].keys()):
        S = S[0:t+1] + " (" + child + ")" + S[t+1:]
        S = append_child(G,child,S)
    return S




#----------Main関数-------------------------------------------------
#convert from s_matsuoka to s_kanagawa for kanagawa's kernel program
#S_matsuoka = "(A B C (D E))"
#S_kanagawa = "(A (B) (C) (D (E)))"
if __name__ == '__main__':
    S_matsuoka = "(A (B G) C (D E))"
    print(S_matsuoka)

    #convert from s_matsuoka to s_kanagawa
    S_kanagawa = Sm_to_Sk(S_matsuoka)
    print(S_kanagawa)

    #nx.nx_agraph.view_pygraphviz(G, prog='dot')  # show graph
