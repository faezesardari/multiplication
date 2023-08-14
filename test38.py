print(' multipication ')
a = int(input("enter row num :"))
b = int(input("enter col num "))
for i in range (1 , a+1) :
    print(i ,end = "\t") 
print()
for j in range(1 , b+1) :
    for k in range(1 , b+1) :
        print(j * k , end = "\t")
    print("\n")

