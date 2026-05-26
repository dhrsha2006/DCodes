import os
e=int(input("""1.Make a file
2.Browse a file \n"""))
if(e==1):
 try:
     i=input("Please enter the name of the file you would like to make: ")
     l=input("Please enter the location where you would like to make the file: ")
     if(l=="desktop" or l=="Desktop"):
        full_path = os.path.join('ENTER THE PATH',i)
        os.mkdir(full_path)
     if(l=="pictures" or l=="Pictures" or l=="picture" or l=="Picture" ):
        full_path = os.path.join("ENTER THE PATH",i)
        os.mkdir(full_path)
     if(l=="documents" or l=="Documents" or l=="docs" or l=="Docs"):
        full_path = os.path.join("ENTER THE PATH",i)
        os.mkdir(full_path)
     if(l=="downloads" or l=="Downloads"):
        full_path = os.path.join("ENTER THE PATH",i)
        os.mkdir(full_path)
     if(l=="Music" or l=="music"):
        full_path = os.path.join("ENTER THE PATH",i)
        os.mkdir(full_path)
     if(i=="Video" or i=="video" or i=="videos" or i=="Videos"):
        full_path = os.path.join("ENTER THE PATH",i)
        os.mkdir(full_path)
     try:
         result=10/0
     except ZeroDivisionError:
         print("")
 except Exception as e:
         print(f"An error occurred: {e}")
if(e==2):
    i=input("Where do you want to search?")
    if(i=="Desktop" or i=="desktop"):
      s=os.listdir(path='ENTER THE PATH')
      print(s)
    if(i=="Pictures" or i=="pictures" or i=="Picture" or i=="picture"):
       s=os.listdir(path="ENTER THE PATH")
       print(s)
    if(i=="Music" or i=="music"):
        s=os.listdir(path="ENTER THE PATH")
        print(s)
    if(i=="Video" or i=="video" or i=="videos" or i=="Videos"):
        s=os.listdir(path="ENTER THE PATH")
        print(s)
    if(i=="Documents" or i=="documents" or i=="docs" or i=="Docs"):
        s=os.listdir(path="ENTER THE PATH")
        print(s)
    if(i=="downloads" or i=="Downloads"):
        s=os.listdir(path="ENTER THE PATH")
        print(s)
else:
    print("Invalid input")
