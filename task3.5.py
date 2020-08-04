weight=int(input("Weight(Вес): "))
a=1
print('1 ' + str(round(weight*0.165,2)))
while a<15:
    a+=1
    weight=weight+a
    print(str(a),":",round(weight*0.165,2))