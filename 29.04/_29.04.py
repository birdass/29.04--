prog=[13,15,34,200,106,50,10,25,0,117,177]
chel=["Anton","Adriana","Maksim","Masha","Stas","Artur","Vika","Lera","Igor","Nikita","Tanja"]
def vse(prog,chel):
    print(prog)
    print(chel)
    print("Отсортировать -sort")
    print("Исключить - del")
    print("Лучшие ученики - top")
    print("Добавить ученика - add")
    print("Кто не идет на комиссию - k")
    vqbor=input("Вы выбираете-  ")
    if vqbor=="k":
        kesk_prog=round(keskmine(prog),1)
        print("Среднее кол-во прогулов: ",kesk_prog)
        for i in range (len(prog)):
            if kesk_prog >= prog[i]:
                chel.pop(i)
            prog.remove(prog[i])
            delete(prog, chel)
            print("Не идут на коммиссию: ")
            return chel    # Не понял как убрать кол-во прогулов
            
    elif vqbor=="sort":
        p,i=sorteerimine(prog,chel)
        for i in range(len(chel)):
            print(chel[i]," proguljal-a   ", prog[i], "raz")
    elif vqbor=="del":
        delete(prog, chel)
        print(prog)
    elif vqbor=="add":
        i=adding(prog,chel)
        print(prog,chel)

    elif vqbor=="top":
        p,i=topbogat(prog,chel)
        

def topbogat(palk,inimesed):
    top,nechel=sorteerimine(prog,chel)
    k= int(input("Сколько людей в топе будет? " ))
    prog.reverse()
    chel.reverse()
    prog.reverse()
    chel.reverse()
    for i in range(0,k,1):
        print(prog[i])
        print(chel[i])
    return prog, chel

    

def adding(prog,chel):
    add=input("Имя нового ученика:  ")
    chel.append(add)
    add_zp=int(input("Кол-во прогулов:  "))
    prog.append(add_zp)
    return prog,chel

def delete(prog, chel):
    for i in range (len(prog)):
        if prog[i] >= 100:
            chel.pop(i)
            prog.remove(prog[i])
            delete(prog, chel)
            return i
    return prog,chel   
            
        
def sorteerimine(prog,chel):
    abi_p=0
    abi_i=""
    n=len(chel)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if prog[i]>prog[j]:
                abi_p=prog[i]
                prog[i]=prog[j]
                prog[j]=abi_p
                abi_i=chel[i]
                chel[i]=chel[j]
                chel[j]=abi_i
    return prog,chel

def keskmine(prog):
    summa=0
    n=len(prog)
    for p in prog:
        summa+=p
    summa=summa/n
    return summa


while True:
    vse(prog,chel)
    