import random
inp=int(input("Please select 1. for Encryption and 2. for Decryption"))
if inp==1:
    i=input("Please enter a string")
    li=list(i)
    if(len(li)>=3):
            s=li[0]
            li.pop(0)
            li.append(s)
            for i in range(0, 4):
                x = random.randint(97, 122)
                char = chr(x)
                li.insert(i,char)
            joined="".join(li)
            print(joined)
    else:
            li.reverse()
            for i in range(0, 4):
                x = random.randint(97, 122)
                char = chr(x)
                li.insert(i,char)
            joined="".join(li)
            print(joined)
if inp==2:
     i=input("Please enter a string")
     li=list(i)
     if(len(li)>=3):
            for i in range(0,4):
                li.remove(li[0])
            s=li[len(li)-1]
            li.pop(len(li)-1)
            li.insert(0,s)
            joined="".join(li)
            print(joined)
     if(len(li)<3):
           try:
            for i in range(0,4):
                li.pop(0)
            li.reverse()
            joined="".join(li)
            print(joined)
           except IndexError:
               print("")
else:
    print("Please enter a valid input")

