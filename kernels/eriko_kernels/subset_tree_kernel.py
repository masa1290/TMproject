#! /usr/local/bin/python3
# -*- coding: utf-8 -*


import sys
import math
import re
import itertools
from copy import deepcopy
from convert import Sm_to_Sk

def subset_tree_kernel(s1,s2,LAMDA):
    #convert matsuoka's S fomula to kanagawa's S fomula
    s1 = Sm_to_Sk(s1)
    s2 = Sm_to_Sk(s2)

    #s式から配列の形にする
    s1_array=to_array(s1)
    s2_array=to_array(s2)


    s1_set = to_subset_tree(s1_array)#配列からサブツリーの集合をつくる
    s2_set = to_subset_tree(s2_array)

    #print(s1_set)
    #print(s2_set)

    kernel_value=subtree_calculation(s1_set,s2_set,LAMDA)
    #print ("subset tree kernel value:  "+str(kernel_value))
    return kernel_value

def to_array(s): #出来たと思う
    count=0
    array_count=0
    s_array=[]


    s=s.replace(' ','')
    x=s.split("(")
    #print(x)
    i=1
    last_array=s_array
    while i<len(x):
        xx=x[i]
        #print(xx)
        #print(s_array)
        if i==1:                    #第一項とその他の場合分け
            if ")" in xx:
                s_array.append(xx.replace(")",""))
                break
            s_array.append(xx)
            last_array=s_array
            array_count+=1

        else:
            new_array=[]
            xx1=xx.replace(')','')
            new_array.append(xx1)   #新しい配列に入れる
            last_array.append(new_array)#今までの配列に結合
            array_count+=1
            #print(last_array)
            #print(array_count)
            flag=")" in xx  #今見ている項に)があるかのflag
            if flag==0:
                last_array=last_array[len(last_array)-1]
                #print(last_array)
            else:
                end_count=xx.count(")")
                up_array=s_array
                jj=array_count-end_count
                #print(s_array)
                #print(up_array)
                #print(array_count)
                #print(end_count)
                #print(jj)
                j=1
                if j<jj:
                    array_count=1
                    while j<jj:
                        up_array=up_array[len(up_array)-1]
                        array_count+=1
                        j+=1
                else:
                    array_count=1
                last_array=up_array
        i+=1

    return s_array

def to_subset_tree(master):
    subset = []
    subtree = to_subtree(master,subset,1,True)
    #print(subtree)
    subset_tree = make_subset_tree(master,subtree)
    leaves = get_leaves(master,[])
    #print(leaves)
    ans = []

    ans.extend(leaves)
    ans.extend(subset_tree)
    ans.append(master)

    return ans

def make_subset_tree(master,subtree):
    groups = []
    subset_tree = []
    if subtree:
        index_max = max([v[0] for v in subtree ])
        for i in range(1,index_max+1):
            a = [v[1] for v in subtree if v[0] == i]
            ###kこのコードがkey=lenでうまくいく自信はない！！
            a.sort(key=len)
            a.reverse()
            d = {}
            d["normal"]= list(a)
            d["inside"]= list()
            groups.append(d)


    groups = make_inside_tree(groups)

    master_subset = make_master_subset(master,groups)

    #add subtree and inside tree
    for d in groups:
        for tree in d["normal"]:
            subset_tree.append(tree)
        for tree in d["inside"]:
            subset_tree.append(tree)


    subset_tree.extend(master_subset)

    return subset_tree



def make_inside_tree(groups):
    for d in groups:
        normal_list = d["normal"]
        for index, tree1 in enumerate(normal_list):
            for tree2 in normal_list[index+1:]:
                d["inside"].append(substract_tree(tree1,tree2))

    return groups

def make_a_substracted_tree(master,groups,comb):
    comb = list(comb)
    #print(comb)
    every_list = []
    one_list = []
    make_combination_list(master,groups,comb,one_list,every_list)
    #print(every_list)
    substracted_tree = []
    for tree_list in every_list:
        tmp = list(master)
        for tree in tree_list:
            tmp = substract_tree(tmp,tree)
        substracted_tree.append(tmp)

    #print(substracted_tree)
    return substracted_tree

def make_combination_list(master,groups,comb,this_list,every_list):
    #print("this list: " + str(this_list))
    #print("rest: " + str(comb))
    if comb:
        for tree in groups[comb[0]]["normal"]:
            this_list.append(tree)
            make_combination_list(master,groups,comb[1:],this_list,every_list)
            this_list.remove(tree)
    else:
        #print(this_list)
        #this_listは後に変化するので,idの違うオブジェクトを作成しないと,every_listにappendされた値も変化してしまう
        a = list(this_list)
        every_list.append(a)
    return


#今はグループが二つまでだと仮定する、、
def make_master_subset(master,groups):
    master_subset = list()
    s = list(range(1,len(master)))
    #print(master)
    #print(groups)
    num_groups = len(groups)
    for pic_num in range(1,num_groups+1):
        comb_list = list(itertools.combinations(range(num_groups),pic_num))
        #print(comb_list)
        for comb in comb_list:
            master_subset.extend(make_a_substracted_tree(master,groups,comb))


    '''
    if len(groups) == 1:
        for tree2 in groups[0]["normal"]:
            master_subset.append(substract_tree(master,tree2))
    if len(groups) == 2:
        for tree in groups[0]["normal"]:
            master_subset.append(substract_tree(master,tree))
        for tree1 in groups[1]["normal"]:
            tree = substract_tree(master,tree1)
            master_subset.append(tree)
            for tree2 in groups[0]["normal"]:
                master_subset.append(substract_tree(tree,tree2))
    '''

    return master_subset

def substract_tree(t1,t2):
    t1_s = str(t1)
    t2_s = str(t2)

    a = re.findall(r"'[^']*'",t2_s)
    token = re.sub(r"'", "", a[0])
    newtree = t1_s.replace(t2_s, "")
    newtree = re.sub(r", ,", ", [" + token + "],", newtree)
    newtree = re.sub(r", ]", ", [" + token + "],", newtree)
    newtree = re.sub(r", ,", " " + token, newtree)
    newtree = newtree.replace("[", "(")
    newtree = newtree.replace("]", ")")
    newtree = newtree.replace("'", "")
    newtree = newtree.replace(",", "")

    newtree=to_array(newtree)

    return newtree

def get_leaves(array,leaves):

    i = 0
    while i<len(array):
        x=array[i]
        if len(x)>1:
            leaves = get_leaves(x,leaves)
        elif isinstance(x,list) and len(x) == 1:
            leaves.append(x)

        i+=1

    return leaves

#group index is used to make group to substract from master tree
def to_subtree(array,subset,group_index,first_flag):


    choice_flag = False
    if first_flag :
        if len(array) > 1:
            choice_flag = True
            first_flag = False
    i = 1
    while i<len(array):
        x=array[i]
        if len(x)>1:
            if choice_flag:
                group_index = i
            a = list()
            a.append(group_index)
            a.append(x)
            subset.append(a)
            to_subtree(x,subset,group_index,first_flag)



        i+=1

    return subset


def subtree_calculation(list_1,list_2,LAMDA):
    hukasa_max = 0
    value=0
    for i in list_1:
        for j in list_2:
            a = list_to_set(i)
            b = list_to_set(j)
            #compare as a frozenset (don't consider order if they are same as set
            if a==b:

                depth_search(i,0,hukasa_max)

                deep=hukasa_max-1

                hukasa_max=0

                value+=1*(LAMDA**deep)


    return value

def list_to_set(thislist):
    myset = set()
    iter_thislist = iter(thislist)
    #ignore first token and go next
    myset.add(next(iter_thislist))

    for child in iter_thislist:
        if len(child) == 1:
            myset.add(frozenset(child))
        else: myset.add(list_to_set(child))

    return frozenset(myset)

def depth_search(array,hukasa,hukasa_max):
    hukasa+=1
    # hukasa

    i=1

    while i<len(array):
        # array[i]
        new_hukasa=depth_search(array[i],hukasa,hukasa_max)
        if hukasa_max<new_hukasa:
            hukasa_max=new_hukasa

        if hukasa_max<hukasa:
            hukasa_max=hukasa
        i+=1
    return hukasa

if __name__ == '__main__':
    s1 = "(A B (C G) (D F))"
    s2 = "(A B (C G) (D F))"
    subset_tree_kernel(s1,s2,1)
