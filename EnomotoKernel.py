import networkx as nx
import StoG

# this kernel consider all of subtree and assume that there is no same node
# a node would be counted as a subtree
def kernel(s1,s2):
    #s1dict's value is flag of subtree(which is 1 or 0) keyd by subtree
    s1dict = make_subtree(s1)
    s2dict = make_subreee(s2)
    s = 0
    elist = list()
    elist.extend(s1dict.keys())
    elist.extend(s2dict.keys())
    for i in elist:
        s += s1dict.get(i, 0) * s2dict.get(i, 0)
    return s

#make subtree
def make_subtree(s):
    #hdict's value is list of subtree keyd by hierarchy depth
    hdict = make_hsubtree(s)

#make subtree of s which is bridge between each floor
def make_hsubtree(s):
    L = StoG.StoL(s)
    G = nx.DiGraph()
    hdict = dict()
    floor = 0 # a->b->c a->b is on the floor1 ,b->c is on the floor2
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
            
            if plist:
                G.add_edge(plist[-1],char)
            # register current parent if the flag is true
            if pflag:
                plist.append(char)
                pflag = False



if __name__ == '__main__':
    make_hsubtree("(A (B C E) D)")
