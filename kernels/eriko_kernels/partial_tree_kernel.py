#! /usr/bin/python
# -*- coding: utf-8 -*


import sys
import math
import copy
import codecs
from convert import Sm_to_Sk

s1_set=[]
list_len_11=[]
s1_set_new=[]
s2_set=[]
list_len_12=[]
s2_set_new=[]
hukasa=0
hukasa_max=0
delete_set_set=[]
list_jj=[]
#lock = ['a']#-----------------------------------------------------------------------------------
k=0
head=0
alltree=""
yousosuu=0
irekaeset=[]
kekka=[]
irekaeset2=[]
irekaeset3=[]
irekaeset4=[]
kekka1=[]

def partial_tree_kernel(s1,s2,LAMDA):
    global s1_set
    global s1_set_new
    global s2_set
    global s2_set_new
    global delete_set_set
    global list_jj
    global alltree
    global irekaeset
    global irekaeset2
    global list_len_11
    global list_len_12

    taiou = "A_"

    yattaze = []
    yattaze1 = []
    s1 = Sm_to_Sk(s1)
    s2 = Sm_to_Sk(s2)

    s1_array=to_array(s1)#s式から配列の形にする
    #print s1_array
    s2_array=to_array(s2)
    to_subtree_1(s1_array)#配列からサブツリーの集合をつくる


    #書き換え-----------------------------------------------
    head=0
    #print s1_array
    list_len_11.append(s1_array[0])
    #変更すべき点-------------------------------------------------------------
    #対応表つくってS式にしてからぶっ込む
    yousosuu=0
    #print s1_array
    alltree = str(s1_array)
    alltree = alltree.replace('\\','DK')
    #list_len_11.append(s1_array[0])
    list_len_11.sort(cmp=cmp_len,reverse=True)

    #print list_len_11
    #print str(yousosuu)
    for i in list_len_11:
       nazo=[]
       string1 = []
       nazo.append(str(i))
       #print i
       #print str(nazo)[1:-1]
       string1 = str(nazo)[2:-2].replace('\\','DK')
       alltree=alltree.replace(string1,taiou+str(yousosuu),1)
       irekaeset.append([taiou+str(yousosuu)])
       irekaeset2.append(string1)
       yousosuu+=1
    #変更すべき点-----------------------------------------------------------------


    kekka.append(alltree)#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


    #print kekka
    #print irekaeset


    alltree = str(kekka[0])
    alltree = alltree.replace("[","(")
    alltree = alltree.replace("]",")")
    alltree = alltree.replace("\"","")
    alltree = alltree.replace("\'","")
    alltree = alltree.replace(",","")
    #print alltree
    s1_set = kekka


    list_len_11=[]
    s1_set = []

    s1_array=to_array(alltree)
    to_subtree_1666(s1_array)
    list_len_11 = irekaeset


    #書き換え終わり-------------------------------------------
    #print s2_array
    i=0
    #print s1_set
    #list_len_11.append(str("['a'"))
    #list_len_12.append(str("['a'"))
    #list_len_11.append(lock)#------------------------------------------------------------------
    s1_set_new.extend(s1_set)
    #print "s1_set"
    #print s1_set
    #print "--------------------------------"
    #print s1_set
    while i<len(s1_set):
        delete_set=[]
        delete_set_set=[]
        to_subtree_11(s1_set[i],list_len_11,delete_set,0,list_jj)
        list_jj = []
        i+=1
        #print "回数---------------------------------"
    s1_set=s1_set_new#ここですでに枝はつくられるいる・・・・・・・・・・・・・・・・・・・・・・・・
    #to_subtree_11(s1_set[0],list_len_11,0)
    #print "1ok"

    to_subtree_2(s2_array)#配列からサブツリー---------------------------------ああああああ
    #かきかえ

    head=0
    #print s2_array

    yousosuu=0
    alltree = str(s2_array)
    alltree = alltree.replace('\\','DK')
    #list_len_12.append(s1_array[0])
    list_len_12.sort(cmp=cmp_len,reverse=True)


    #print list_len_12
    #print str(yousosuu)
    for i in list_len_12:

       nazo=[]
       string1 = []
       nazo.append(str(i))
       #print i
       #print str(nazo)[1:-1]
       string1 = str(nazo)[2:-2].replace('\\','DK')
       alltree=alltree.replace(string1,taiou+str(yousosuu),1)
       irekaeset3.append([taiou+str(yousosuu)])
       irekaeset4.append(string1)
       #print string1

       #print str(i)
       #print "ここが肝心"


       yousosuu+=1
    kekka1.append(alltree)





    alltree = str(kekka1[0])
    alltree = alltree.replace("[","(")
    alltree = alltree.replace("]",")")
    alltree = alltree.replace("\"","")
    alltree = alltree.replace("\'","")
    alltree = alltree.replace(",","")
    #print alltree
    s2_set = kekka1

    list_len_12=[]
    s2_set = []

    s2_array=to_array(alltree)
    to_subtree_1999(s2_array)
    list_len_12 = irekaeset3

    #かきかえ-------------

    s2_set_new.extend(s2_set)
    i=0
    while i<len(s2_set):
        delete_set=[]
        delete_set_set=[]

        to_subtree_19(s2_set[i],list_len_12,delete_set,0,list_jj)
        list_jj=[]
        i+=1
    s2_set=s2_set_new

    #--------------------------------------------------------もとにもどしてリストに直す
    alltree = str(s1_set)
    yattaze = []
    yattaze1 = []
    j=1
    #for分をぎゃくからやらなくてはならん
    irekaeset3.reverse()
    #ここからはとおさねえ
    for i in s2_set:
        alltree = str(i)
        alltree = alltree.replace("[","(")
        alltree = alltree.replace("]",")")
        alltree = alltree.replace("\"","")
        alltree = alltree.replace("\'","")
        alltree = alltree.replace(",","")

        #print "----------------------------"
        #print irekaeset3
        #print irekaeset4
        #print"----------------------------"
        j=1
        for i in irekaeset3:
            #print str(i)[2:-2]
            #print str(i)[2:-2] in alltree
            if str(i)[2:-2] in alltree:
                alltree=alltree.replace(str(i)[2:-2],str(irekaeset4[-j]))
            j+=1
        yattaze1.append(str(to_array(alltree)))
        #print yattaze1


    #--------------------------------------------------------もとにもどしてリストに直す
    alltree = str(s1_set)

    j=1
    #for分をぎゃくからやらなくてはならん
    irekaeset.reverse()
    #ここからまたs式にしてはいれつにする
    for i in s1_set:
        alltree = str(i)
        alltree = alltree.replace("[","(")
        alltree = alltree.replace("]",")")
        alltree = alltree.replace("\"","")
        alltree = alltree.replace("\'","")
        alltree = alltree.replace(",","")

        j=1
        for i in irekaeset:

            if str(i)[2:-2] in alltree:
                alltree=alltree.replace(str(i)[2:-2],str(irekaeset2[-j]))

            j+=1

        yattaze.append(str(to_array(alltree)))


    kernel_value=subtree_calculation(yattaze,yattaze1,LAMDA)#ここでカーネルの計算してるーーーーーーーーーーーーーーーーーーーーーーーーーーー
    print "kernel_value:  "+str(kernel_value)
    return kernel_value


def cmp_len(s1, s2):
    return cmp(len(s1),len(s2))

def to_array(s): #出来たと思う
    global list_len_11

    count=0
    array_count=0
    s_array=[]
    array_newnew=[]
    k=0
    s=s.replace(' ','')
    x=s.split("(")

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
            xx1=xx.replace(')','')

            new_array.append(xx1)#新しい配列に入れる



            #print new_array
            #print "----------"
            last_array.append(new_array)#今までの配列に結合
            array_count+=1

            flag=")" in xx  #今見ている項に)があるかのflag

            if flag==0: #)が無い＝配列をもう一段深くする＝次くっつける配列は今のもの
                last_array=last_array[len(last_array)-1]
            else:#)がある

                end_count=xx.count(")")
                up_array=s_array
                jj=array_count-end_count
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
'''
def to_subtree_1(array):#サブセットツリーの集合を作る
    global s1_set
    #print array

    s1_set.append(str(array))
    #print array
    #print s_set
    i=1
    while i<len(array):
        x=array[i]
        if len(x)>1:
            #s_set.append(x)
            to_subtree_1(x)
            #print x
        else:
            list_len_11.append(x)


        i+=1
'''
def to_subtree_1666(array):#サブセットツリー＋αの集合
    global s1_set
    global list_len_11
    #print "array"
    #print array
    x=[]

    s1_set.append(str(array))
    #print "わからんぞ"
    #print array
    #print len(array)
    #print s1_set
    #print list_len_11
    i=1
    while i<len(array):#ここを変えるんじゃん??
        x=copy.deepcopy(array)
        del x[i]

        #print "array"
        #print array

        if len(x)>1:
            pass
            #print "x"
            #print x
            #s1_set.append(str(x))
            #to_subtree_11(x)
            #print
        else:
            #print x
            list_len_11.insert(0,[x])
        i+=1
    i=1
    while i<len(array):#ここを変えるんじゃん??
        x=array[i]
        if len(x)>1:
            #s_set.append(x)
            to_subtree_1666(x)
        else:
            #print"長さ1"
            #print x
            list_len_11.append(x)
        i+=1

def to_subtree_1999(array):#サブセットツリー＋αの集合
    global s2_set
    global list_len_12
    #print "array"
    #print array
    x=[]

    s2_set.append(str(array))
    #print "わからんぞ"
    #print array
    #print len(array)
    #print s2_set
    #print list_len_12
    i=1
    while i<len(array):#ここを変えるんじゃん??
        x=copy.deepcopy(array)
        del x[i]

        #print "array"
        #print array

        if len(x)>1:
            pass
            #print "x"
            #print x
            #s1_set.append(str(x))
            #to_subtree_11(x)
            #print
        else:
            #print x
            list_len_12.insert(0,[x])
        i+=1
    i=1
    while i<len(array):#ここを変えるんじゃん??
        x=array[i]
        if len(x)>1:
            #s_set.append(x)
            to_subtree_1999(x)
        else:
            #print"長さ1"
            #print x
            list_len_12.append(x)
        i+=1

def to_subtree_1(array):#サブセットツリー＋αの集合
    global s1_set
    global list_len_11
    global head
    x=[]

    s1_set.append(str(array))
   # print "やるやん"
   # print s1_set
    #print list_len_11

    i=1
    x=copy.deepcopy(array)
    if head!=0:
    	list_len_11.insert(0,x[0])
    head+=1
    '''
    while i<len(array):

       # print "-------------------"
       # print x
        #print "これがxや-------------------"
        del x[i]
       # print x
        #print "hennkouのえx--------------------"
        if len(x)>1:
            pass
        else:
            list_len_11.insert(0,x)
            #print "insa-tされた!"
        i+=1
    '''
    i=1
    while i<len(array):
        x=array[i]
        #print "arrayのx"
        #print x
        if len(x)>1:
            to_subtree_1(x)
        else:
            list_len_11.append(x[0])
            #print "appendされた!"
        i+=1

'''
def henkou(array):#サブセットツリー＋αの集合
    global s1_set
    global list_len_11
    global head
    x=[]
    print "もうわからんわ"
    s1_set.append(str(array))
   # print "やるやん"
    print s1_set
    print list_len_11

    i=1
    x=copy.deepcopy(array)
    if head!=0:
    	list_len_11.insert(0,[x[0]])
    head+=1

    i=1
    while i<len(array):
        x=array[i]
        print "arrayのx"
        print x
        if len(x)>1:
            henkou(x)
        else:
            list_len_11.append(x)
            #print "appendされた!"
        i+=1



'''
def to_subtree_11(sss,list_len_11,delete_set,ii,list_j):#この関数をいじって同じ部分木ができた時も出現回数だけs2_setに入れたい160426
    global delete_set_set
    global s1_set
    global s1_set_new
    global k
    yattaze=False
    list_lencopy=[]
    delete_set_new=[]
    list_wai =[]
    j=ii

    while j<len(list_len_11):
        s=str(sss).find(", "+str(list_len_11[j]))
        #print sss
        #print s
        #print j
        #print "ええええええええ"

        if s==-1:
            j+=1
        else:

            x=str(sss)[:s]+str(sss)[s+len(", "+str(list_len_11[j])):]
            listindexyou=delete_set_set[:]

            if x not in s1_set_new:

                if x.count("[")>1:
                    s1_set_new.append(x)
                    k+=1

                if x.count("[")>2:

                    list_lencopy = list_len_11[:]
                    list_wai = list_j[:]
                    #sys.exit()
                    to_subtree_11(x,list_lencopy,delete_set_new,0,list_wai)


            j+=1
    #print "ここまで大丈夫"


def to_subtree_2(array):#サブセットツリー＋αの集合
    global s2_set
    global list_len_12
    global head
    x=[]

    s2_set.append(str(array))
   # print "やるやん"
   # print s2_set
    #print list_len_11

    i=1
    x=copy.deepcopy(array)
    if head!=0:
    	list_len_12.insert(0,x[0])
    head+=1
    '''
    while i<len(array):

       # print "-------------------"
       # print x
        #print "これがxや-------------------"
        print x[i]
        del x[i]
       # print x
        #print "hennkouのえx--------------------"
        if len(x)>1:
            pass
        else:
            list_len_12.insert(0,x)
            #print "insa-tされた!"
        i+=1
    '''
    i=1
    while i<len(array):
        x=array[i]
        #print "arrayのx"
        #print x
        if len(x)>1:
            to_subtree_2(x)
        else:
            list_len_12.append(x[0])
            #print "appendされた!"
        i+=1

'''
def to_subtree_2(array):#サブセットツリー＋αの集合
    global s2_set
    global list_len_12
    #print array

    s2_set.append(str(array))
    #print array
    #print s_set
    i=1
    while i<len(array):#ここを変えるんじゃん??
        x=copy.deepcopy(array)
        del x[i]

        #print "array"
        #print array

        if len(x)>1:
            pass
            #print "x"
            #print x
            #s2_set.append(str(x))
        else:
            #print"長さ1"
            #print x
            list_len_12.insert(0,x[0])
        #to_subtree_11(x)
        #print
        i+=1
    i=1
    while i<len(array):#ここを変えるんじゃん??
        x=array[i]
        if len(x)>1:
            #s_set.append(x)
            to_subtree_2(x)
        else:
            #print"長さ1"
            #print x
            list_len_12.append(x[0])
        i+=1
    #print s2_set

'''


def to_subtree_19(sss,list_len_12,delete_set,ii,list_j):#この関数をいじって同じ部分木ができた時も出現回数だけs2_setに入れたい160426
    global delete_set_set
    global s2_set
    global s2_set_new
    global k

    list_newnewnew=[]
    listindex =[]
    listindexyou =[]
    yattaze=False

    dame=0
    list_lencopy=[]
    set=[]
    delete_set_new=[]
    delete_set_new.extend(delete_set)
    list_wai =[]
    list_nai =[]
    j=ii

    while j<len(list_len_12):
        s=str(sss).find(", "+str(list_len_12[j]))

        if j in list_j:
            j+=1
            continue
        if s==-1:
            j+=1
        else:

            x=str(sss)[:s]+str(sss)[s+len(", "+str(list_len_12[j])):]

            delete_set_new.append(j)
            delete_set_new.sort()
            list_j.append(j)
            list_j.sort()


            if x not in s2_set_new   :#or list_j not in delete_set_set
		list_nai.append(s)
                delete_set_set.append(list_j[:])

                if x.count("[")>1:
                    s2_set_new.append(x)
                    k+=1

                if x.count("[")>2:


                    list_lencopy = list_len_12[:]
                    list_wai = list_j[:]
                    to_subtree_19(x,list_lencopy,delete_set_new,0,list_wai)


            j+=1
    #print "ここまで大丈夫"



def to_subtree_22(sss,list_len_12,delete_set,ii):#この関数をいじって同じ部分木ができた時も出現回数だけs2_setに入れたい160426
    global delete_set_set
    global s2_set
    global s2_set_new
    set=[]
    delete_set_new=[]
    delete_set_new.extend(delete_set)

    #print "ii:"+str(ii)
    j=ii
    while j<len(list_len_12):
        delete_set_new=[]
        delete_set_new.extend(delete_set)
        #print "-------------------------------"
        #print "j:"+str(j)
        #print "list_len_12["+str(j)+"]:"+str(list_len_12[j])
        s=str(sss).find(", "+str(list_len_12[j]))
        #print s
        if s==-1:
            j+=1
        else:
            x=str(sss)[:s]+str(sss)[s+len(", "+str(list_len_12[j])):]

            #x=str(set_1[i])-str(list_len_1[j])
            #x=str(sss).replace(", "+str(list_len_12[j]),"")
            '''
            print "リスト"
            print s2_set_new
            print "元のもの"
            print sss
            print "長さ1の要素"
            print list_len_12[j]
            print "x"
            print x
            print ""


            #削除されたものを比較するんだ！！！
            print "削除したものリスト"
            print delete_set_set
            print "今まで削除してたもの"
            print delete_set
            print "j:"+str(j)
            '''
            delete_set_new.append(j)
            delete_set_new.sort()
            #print "新しく削除したもの"
            #print delete_set_new
            y=delete_set_new in delete_set_set
            if y==False:
                #delete_set_new.append(j)
                #print "新しく削除したもの"
                #print delete_set_new
                delete_set_set.append(delete_set_new)
                #s2_set_new.append(x)
                if x.count("[")>1:
                    s2_set_new.append(x)

                if x.count("[")>2:
                    #print "削除されたものそのまま再帰だイェイ"
                    #to_subtree_22(x,list_len_12,j+1)
                    to_subtree_22(x,list_len_12,delete_set_new,0)

            #else:
                #print "同じやつじゃない？"


            '''
            y=x in s2_set_new
            if y==False:
                if x.count("[")>1:
                    print "入れる"
                    #print
                    #s2_set.append(x)
                    s2_set_new.append(x)

                    if x.count("[")>2:
                        print "削除されたものそのまま再帰だイェイ"
                        #to_subtree_22(x,list_len_12,j+1)
                        to_subtree_22(x,list_len_12,delete_set_new,0)
            else:
                print "入れないよー"
                #print s2_set
                #print x
                #print
            '''
            #if sss.count("[")>2:#ここをいじる木がする160426
                #print "元のもの持って再帰だイェイ2"
                #to_subtree_22(sss,list_len_12,j+1)

                #print "何がダメなんだーーー"
            j+=1
    #print "ここまで大丈夫"

def subtree_calculation(list_1,list_2,LAMDA):#ここでカーネルを計算しているーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    global hukasa_max
    i=0
    value=0
    print "list"
    print list_1
    print len(list_1)
    print list_2
    print len(list_2)
    #print ""
    while i<len(list_1):
        st_1=str(list_1[i])
        j=0
        while j<len(list_2):
            st_2=str(list_2[j])
            #print "1:"+str(i)
            #print st_1
            #print "2:"+str(j)
            #print st_2
            if st_1==st_2:
                #print("一致")
                #print st_1
                depth_search(st_1,0)
                #print ""
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
            '''
            else:
                print"一致してないよ"
                print st_1
                print st_2
                print ""
            '''
            j+=1
        i+=1
    return value

'''
def depth_search(array,hukasa):
    global hukasa_max
    hukasa+=1
    #print hukasa_max
    #print hukasa
    #print array

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
'''

def depth_search(array,hukasa):
    global hukasa_max
    #hukasa+=1
    #print hukasa_max
    #print hukasa
    #print array
    x=array[0]
    #print x
    if x=="[":
        hukasa+=1
    elif x=="]":
        hukasa-=1
    #print "深さ"+str(hukasa)
    #print "MAX"+str(hukasa_max)
    if hukasa_max<hukasa:
        hukasa_max=hukasa
    if len(array)>1:
        y=array[1:]
        #print y
        #print ""
        depth_search(y,hukasa)
    '''
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
    '''

'''元々はあったものだけどなくていいので消した
def start(s1,s2,kk1_txt,pro1_txt,kk2_txt,pro2_txt,LAMDA):
    global s1_set
    global s2_set
    #print s1
    #print s2
    kernel_value=main(s1,s2,LAMDA)
    s1_set=[]
    s2_set=[]
    return kernel_value
'''


if __name__ == '__main__':



    #s1="(ss (c(d)(a)))"

    #s2="(s (b )(x)(a (aa)))"
    #s1="(n (vadt (nに (a (n (v (nで ) ) ) ) ) (nに (nnの (n ) ) ) (nが ) (aadv ) ) (nを (nnの ) ) (nnは ) (nとは (nnの (nの ) ) ) (d ) )"

    #これができない #s式が間違ってる？？
    s1="(a (b (c (d (e (f (g ) ) ) ) ) (cc (dd (ee ) ) ) (ccc) ) )"


    #s2="(n (vadt (nを ) (jに (nの ) ) (n ) ) (vv (anを (nr ) ) (nは ) (nnに (vncop ) ) ) (vadvnは ) (nnは (v (n (nnに (v ) ) (aか ) (nを ) ) (nが (nて ) (n ) ) (nを (nn (n (nv ) ) ) ) ) ) (nは (v (nnomnに (dはの (nv (jに (aadv (d (nの (v ) ) (nncop ) ) ) ) (nnの ) ) ) ) ) ) (vadt (nに (a (n (v (nで ) ) ) ) ) (nに (nnの (n ) ) ) (nが ) (aadv ) ) (nを (nnの ) ) (nnは ) (nとは (nnの (nの ) ) ) (d ) )"
    s1="(s (a (aa (cc候)))(bあ (bb (a (aa (ccふぁ)))(b (bb )))))"
    #s2="(s (a (aa (cc)))(b (bb )))"

    #s1="(a(b(bb))(c))"     #
    #s2="(a(b)(c))"

    #s1="(a(a)(a))"  #2#同じ部分木ができた時、２つ数えられないよどーしよ
    #s1="(a(a))"

    #s1="(a(a))"
    #s2="(a(a(a))(a(a)))"  #同じ部分木ができた時、２つ数えられないよどーしよ



    #s2="(a(aさ(aaあいう))(a(aa紙)))"  #同じ部分木ができた時、２つ数えられないよどーしよ
    #s1="(a(aさ(aaあいう))(a(aaあいう)))"
    #s1="(a(a(a)(a))(a(a)))"

    #s2="(a(a(aa)))"  #同じ部分木ができた時、２つ数えられないよどーしよ
   # s1="(a(a))"

    #PTsで確認済みのS式
    #s1="(a(b(c))(d(eですが)))" #10
    #s2="(a(b(c))(d(e)))"
    #s1="(a(b)(d))"     #3
    #s2="(a(b)(d))"
    #s1="(s (a (aa))(b )(x))" #12
    #s2="(s (a (aa))(b )(x))"
    #s1="(a(b(c(d))))" #6
    #s2="(a(b(c(d))))"
    #s1="(nで(v(nものいおり)(nを)))" #2
    #s2="(nで(v(nものいおり)(nを)))" #2
    #s1="(a(a)(a))"
    #s1="(ncop (vndncop (nは ) (nで (v (nも ) (nを ) ))) (jnomには (nか (a (nx ) ) ) (nの (nの ) ) ) (vd (d ) (nに ) ) )"
    #s2="(ncop (vndncop (nは ) (nで (v (nも ) (nを ) ))) (jnomには (nか (a (nx ) ) ) (nの (nの ) ) ) (vd (d ) (nに ) ) )"
    #s1="(v (nには (nの ) ) (nnが (nの (nnの ) ) ) (nには (nの ) ) (nが (nの (nnの ) ) ) (c (nて (さ ) ) ) (nには (nの ) ) (nが (nと (nnの ) ) (nの (nv ) ) ) (vも ) (nn (nにな ) ) (d ) )"
    partial_tree_kernel(s1,s2,1)

    #s1="(s (a )(b ) )"
    #s2="(s (aa )(b ) )"
