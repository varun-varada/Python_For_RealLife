import random
a="p1 p2 p3 p4 p5"# use  input function 
#a=input("Enter the person name with space without comma")
a1=a.split(" ")
a2=random.randint(0,len(a1))
for i in range(len(a1)):
    # print(i)
    if(a2==i):
        print(f"{a1[i]} Should pay the bill")