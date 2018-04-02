#! /usr/local/bin/python3
# -*- coding: utf-8 -*


import sys
import math
from convert import Sm_to_Sk

s1_set=[]
s2_set=[]
hukasa=0
hukasa_max=0

def subtree_kernel(s1,s2,LAMDA):
    global s1_set
    global s2_set
    s1_set = []
    s2_set = []
    #print(s1_set)
    #print(s2_set)
    s1 = Sm_to_Sk(s1)
    s2 = Sm_to_Sk(s2)
    s1_array=to_array(s1)#s式から配列の形にする
    s2_array=to_array(s2)
    to_subtree_1(s1_array)#配列からサブツリーの集合をつくる
    to_subtree_2(s2_array)
    kernel_value=subtree_calculation(s1_set,s2_set,LAMDA)
    #print "kernel_value:  "+str(kernel_value)
    return kernel_value


def to_array(s): #出来たと思う
    #print s
    count=0
    array_count=0
    s_array=[]


    s=s.replace(' ','')
    x=s.split("(")
    #print x
    i=1
    last_array=s_array
    while i<len(x):
        #print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        xx=x[i]
        if i==1:                    #第一項とその他の場合分け
            s_array.append(xx)
            last_array=s_array
            array_count+=1
        else:
            new_array=[]
            #print "追加するもの"
            #print xx
            xx1=xx.replace(')','')
            #print xx1
            new_array.append(xx1)   #新しい配列に入れる
            #print "new_array"
            #print new_array[0]
            #print "last_array"
            #print last_array
            last_array.append(new_array)#今までの配列に結合
            #print last_array
            #print "くっつけたよ"
            array_count+=1
            #print "last"
            #print last_array

            flag=")" in xx  #今見ている項に)があるかのflag
            #print "xx"
            #print xx

            if flag==0: #)が無い＝配列をもう一段深くする＝次くっつける配列は今のもの
                last_array=last_array[len(last_array)-1]
                #print ")無いよ"
                #print "くっつけるもの"
                #print last_array
                #array_count+=1
            else:#)がある
                #print "）ある"
                end_count=xx.count(")")
                #print "くっつけるもの"
                #print last_array
                #print ")の数"
                #print end_count
                #print "配列の深さ？"
                #print array_count
                up_array=s_array
                #ループの条件がおかしいと思う
                #print "配列の深さー)の数"
                #print array_count-end_count
                jj=array_count-end_count
                j=1
                if j<jj:
                    array_count=1
                    while j<jj:
                        #print"ループ-----------"
                        #print "j: "+str(j)
                        #print "jj: "+str(jj)
                        #print up_array
                        up_array=up_array[len(up_array)-1]
                        #print up_array
                        array_count+=1
                        #print array_count
                        j+=1
                else:
                    array_count=1
                #これじゃぜったいだめ
                #print "ループ後配列の深さ"

                #print array_count
                last_array=up_array
                #print last_array
                #print"配列かうんと"
                #print array_count
                #print"last"
                #print last_array
            #print s_array
            #last_array=new_array
            #print"---------------------------------------------------"
            # print array_count
            #print"s_array"
            #print s_array

        #print s_array
        i+=1
    return s_array

def to_subtree_1(array):#集合setを使う？
    global s1_set
    #print array

    s1_set.append(array)
    #print array
    #print s_set
    i=1
    while i<len(array):
        x=array[i]
        if len(x)>1:
            #s_set.append(x)
            to_subtree_1(x)
            #print x


        i+=1

    #print s1_set

def to_subtree_2(array):#集合setを使う？
    global s2_set
    #print array

    s2_set.append(array)
    #print array
    #print s_set
    i=1
    while i<len(array):
        x=array[i]
        if len(x)>1:
            #s_set.append(x)
            to_subtree_2(x)
        #print x


        i+=1

    #print s2_set

def subtree_calculation(list_1,list_2,LAMDA):
    global hukasa_max
    i=0
    value=0
    while i<len(list_1):
        st_1=list_1[i]
        j=0
        while j<len(list_2):
            st_2=list_2[j]
            if st_1==st_2:
                #print("一致")
                depth_search(st_1,0)
                #print deep
                #hukasa_max=0
                #print "-------------------"
                deep=hukasa_max-1
                #print deep
                hukasa_max=0
                #print "-------------------"
                #print sys.setrecursionlimit(st_1)
                #print st_1
                #print st_2
                value+=1*(LAMDA**deep)
            j+=1
        i+=1
    return value


def depth_search(array,hukasa):
    global hukasa_max
    hukasa+=1
    #print hukasa

    i=1

    while i<len(array):
        #print array[i]
        new_hukasa=depth_search(array[i],hukasa)
        if hukasa_max<new_hukasa:
            hukasa_max=new_hukasa

        if hukasa_max<hukasa:
            hukasa_max=hukasa
        i+=1
    return hukasa



def start(s1,s2,kk1_txt,pro1_txt,kk2_txt,pro2_txt,LAMDA):
    global s1_set
    global s2_set
    #print s1
    #print s2
    kernel_value=main(s1,s2,LAMDA)
    s1_set=[]
    s2_set=[]
    return kernel_value



if __name__ == '__main__':
    #s1="(ss (c(d)(a)))"
    s1="(A B)"
    s2="(C (A B))"
    #s1="(n (vadt (nに (a (n (v (nで ) ) ) ) ) (nに (nnの (n ) ) ) (nが ) (aadv ) ) (nを (nnの ) ) (nnは ) (nとは (nnの (nの ) ) ) (d ) )"

    #これができない #s式が間違ってる？？
    #s1="(a (b (c (d (e (f (g ) ) ) ) ) (cc (dd (ee ) ) ) (ccc) ) )"


    #s2="(n (vadt (nを ) (jに (nの ) ) (n ) ) (vv (anを (nr ) ) (nは ) (nnに (vncop ) ) ) (vadvnは ) (nnは (v (n (nnに (v ) ) (aか ) (nを ) ) (nが (nて ) (n ) ) (nを (nn (n (nv ) ) ) ) ) ) (nは (v (nnomnに (dはの (nv (jに (aadv (d (nの (v ) ) (nncop ) ) ) ) (nnの ) ) ) ) ) ) (vadt (nに (a (n (v (nで ) ) ) ) ) (nに (nnの (n ) ) ) (nが ) (aadv ) ) (nを (nnの ) ) (nnは ) (nとは (nnの (nの ) ) ) (d ) )"
    #s1="(s (a (aa (cc)))(b (bb (a (aa (cc)))(b (bb )))))"
    #s2="(s (a (aa (cc)))(b (bb )))"
    #s1="(s(a)(b))"
    #s2="(s(a)(b))"
    print(subtree_kernel(s1,s2,1))

    #s1="(s (a )(b ) )"
    #s2="(s (aa )(b ) )"
