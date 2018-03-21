import networkx as nx

def show(S):
    L = StoL(S) #S fomula to list
    G = LtoG(L) #list to graph
    nx.nx_agraph.view_pygraphviz(G, prog='dot')  # show graph

#list to graph
def LtoG(L):
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
def StoL(S):
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


#----------Main関数-------------------------------------------------
if __name__ == '__main__':
    S = "(A (B C (D E)))"
    L = StoL(S) #S fomula to list
    print(L)
    G = LtoG(L) #list to graph
    nx.nx_agraph.view_pygraphviz(G, prog='dot')  # show graph
