d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
print("\U0001F917"*36,"WELCOME","\U0001F917"*36)
while(True):
    try:
        str=input("Enter roman number : ").upper()
        sum=0
        i=0
        while(i<len(str)):
            if(i+1<len(str)):
                if(d[str[i]]>=d[str[i+1]]):
                    sum+=d[str[i]]
                    i+=1
                else:
                    sum+=(d[str[i+1]]-d[str[i]])
                    i+=2
            else:
                sum+=d[str[i]]
                i+=1
        print("Integer value =",sum)
        ch=input("Do you want to continue(yes/no):")
        if(ch.lower()=="no"):
            print("\U0001F917"*36,"THANK YOU","\U0001F917"*36)
            break
        elif(ch.lower()=="yes"):
            continue
        else:
            print("Wrong command")
    except:
        print("Invalid Input")
