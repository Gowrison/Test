def weareintrouble(a_smiles,b_smiles):
    if a_smiles ==True and b_smiles== True:
        return True
    elif a_smiles == False and b_smiles==False:
        return True
    else:
        return False

def int_sum(a,b):
    if a==b:
        return (2*(a+b))
    else:
        return a+b

def hours(h):
    hours_arr= []
    for i in range(h+1,24,1):
        hours_arr.append(i)
    return hours_arr


def posi(a,b,neg):
    if neg:
        return (a<0) and (b<0)
    else:
        return(a>0 and b<0) or (a<0 and b>0)


def front_back(s):
    if len(s)==1:
        return s
    else:
        mid=s[1:-1]
        l=s[-1]
        f=s[0]
        return (l + mid +f)


def front3Letters(s,a):
    if len(s)<=3:
        return str(s)*a
    else:
        mid=s[0:3]
        return str(mid)*a

def extra_end(s,a):
    if len(s) >= 2:
        new_s = s[-2:]*a
        return new_s

def zero_list(g_list):
    new_list=[]
    g_list_len=len(g_list)
    new_list_len=g_list_len*2
    last_el=g_list[-1]

    for newel in range(new_list_len):
        new_list.append(0)
    new_list[-1]= last_el
    return new_list





def list_count_9(my_list):
    count=0

    for i in my_list:
        if i ==9:
            count=1 + count
        else:
            count=0 + count
    return count

def list_count_9_nw(g_list):
    return g_list.count(9)

f= lambda a: a*a



if __name__ == '__main__':
    val = weareintrouble(True, False)
    print(val)

    val_3= int_sum(3,3)
    print(val_3)


    val_4=hours(5)
    print(val_4)

    val_5 = posi(-1,-5,True)
    print(val_5)

    Val_6=front_back('gowrison')
    print(Val_6)

    Val_7=front3Letters('gowrison',5)
    print(Val_7)

    val_8=extra_end('gowrison',5)
    print(val_8)

    print(zero_list([1,2,6]))

    print(list_count_9([1,9,9]))

    print(list_count_9_nw([2,9,9,9]))

    f = lambda a: a * a
    print(f(12))

    h = lambda x,y: str(x * x + y)+'Old'
    print(h(3,1))

