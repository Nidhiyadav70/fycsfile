num = int(input("Enter the number:"))

if num <=1:
    print("Nither prime nor composit")
elif num==2:
    print("prime number")
else:
    for i in range(2,num):
        if num %i==0:
            print("composite number")
            break
        else:
            print("prime number")
