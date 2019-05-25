def main():
   count=0
   while(count!=3):
       try:
           name=input("Enter filename")
           f=open(name,"r")
           print(f.read())
           break;
       except:
           count=count+1
           if(count==3):
               print("File not found, 0 more attempts left")
           else:
               pass
main()