import random
n=1
#sender side
def sender():
    print("Which type of fletcher checksum do you want to implement(FLETCHER-16 or                       FLETCHER-32)?\n")
    print("enter 1 for FLETCHER-16\n")
    print("enter 2 for FLETCHER-32\n")
    global n
    n=int(input())
    print('Enter the message to be sent')
    if n==1:
        print("Enter number between 0 and 255")
    else:
        print("Enter number between 0 and 65535")
    ch=input()
    messagei=[]
    messagei.extend(map(int,ch.split()))
    a=messagei
    #r is in binary form
    r=ifelse(messagei)
    list1=[]
    print("The message sent from the sender side is")
    print(r,"\n\n")
    printerror()
    for i in range(0,len(r)):
        list1.append(int(str(r[i]),2))
    #list1 is in decimal form
    print("1:The message is received accurately")
    receiver(list1)
    print()
    print("2:The numbers in the sender list may be swapped")
    eswap(a[0:len(a)-1])
    print()
    print("3:The numbers may be incremented or decremented equally")
    eincdec(a[0:len(a)-1])
    print()
    print("4:The numbers may be totally changed from what is sent")
    erand(a[0:len(a)-1])
    print()
    print("5:Some extra numbers might be added to the list")
    eextra(a[0:len(a)-1])
    print()
    print("6:The list numbers might be received accurately but the checksum is modified")
    eincs(a[0:len(a)-1])
def checksum16(messagei1):
    #msg is a list to store decimal numbers
    #message is a list to store binary numbers
    msg=messagei1
    message=[]
    for num in messagei1:
        message.append(bin(num)[2:].zfill(8))
    r=int(bin(0)[2:])
    l=int(bin(0)[2:])
    for data in message:
        sum1=binsum16(str(r),data)
        r=int(sum1)%int(bin(256)[2:])
        sum2=binsum16(str(l),str(r))
        l=int(sum2)%int(bin(256)[2:])
    checksum=l*int(bin(256)[2:])+r
    message.append(str(checksum).zfill(16))
    intcheck=(int(str(checksum),2))
    msg.append(intcheck)
    return(message)
def binsum16(num1,num2):
   sum = bin(int(num1,2)+int(num2,2))[2:].zfill(8)
   return(sum)
def receiver(message1):
    list1=[]
    print("The message received at the receiver side is")
    global n
    if n==1:
        for i in range(0,len(message1)-1):
            list1.append(bin(message1[i])[2:].zfill(8))
        list1.append(bin(message1[len(message1)-1])[2:].zfill(16))
    else:
         for i in range(0,len(message1)-1):
            list1.append(bin(message1[i])[2:].zfill(16))
         list1.append(bin(message1[len(message1)-1])[2:].zfill(32))
    print(list1)
    #calchecksum stores the checksum from receiver side
    calchecksum=list1[len(list1)-1]
    listr=message1[0:len(message1)-1]
    #calculating checksum of received list
    checklistr=ifelse(listr)
    #reccalchecksum stores the checksum calculated at the reciever side
    reccalchecksum=checklistr[len(checklistr)-1]
    if reccalchecksum==calchecksum:
        print("Message received accurately")
    else:
        print("Message received with error") 
def eswap(m):
      csl=ifelse(m)
      cs=csl[len(csl)-1]
      #swapls is a list containing list elements swapped
      swapls=[]
      list1=[]
      swapls=swapls+csl[1:2]+csl[0:1]+csl[2:]
      print("The message received at the receiver side is")
      print(swapls)
      for i in range(0,len(swapls)-1):
            list1.append(int(str(swapls[i]),2))
      ncsl=checksum16(list1)
      #ncs is new checksum
      ncs=ncsl[len(ncsl)-1]
      if cs==ncs:
        print("Message received accurately")
      else:
        print("Message received with error")
def eincdec(m):
      csl=ifelse(m)
      cs=csl[len(csl)-1]
      #swapls is a list containing any 2 elements equally incremented and decremented 
      swapls=[]
      list1=[]
      r=csl[0]
      r1=int(str(r),2)
      s=csl[1]
      s1=int(str(s),2)
      global n
      if n==1:
          swapls=swapls+[bin(r1+2)[2:].zfill(8)]+[bin(s1-2)[2:].zfill(8)]+csl[2:]
      else:
          swapls=swapls+[bin(r1+2)[2:].zfill(16)]+[bin(s1-2)[2:].zfill(16)]+csl[2:]
      print("The message received at the receiver side is")
      print(swapls)
      for i in range(0,len(swapls)-1):
            list1.append(int(str(swapls[i]),2))
      ncsl=ifelse(list1)
      #ncs is new checksum
      ncs=ncsl[len(ncsl)-1]
      if cs==ncs:
        print("Message received accurately")
      else:
        print("Message received with error")
def erand(m):
      len1=len(m)
      csl=ifelse(m)
      cs=csl[len(csl)-1]
      randnum=[]
      randnumbin=[]
      global n
      if n==1:
          for j in range(len1):
              randnum.append(random.randint(0,255))
          for i in range(0,len(randnum)):
              randnumbin.append(bin(randnum[i])[2:].zfill(8))
          randnumbin.append(bin(m[len(m)-1])[2:].zfill(16))
      else:
          for j in range(len1):
              randnum.append(random.randint(0,65535))
          for i in range(0,len(randnum)):
              randnumbin.append(bin(randnum[i])[2:].zfill(16))
          randnumbin.append(bin(m[len(m)-1])[2:].zfill(32))
      print("The message received at the receiver side is")
      print(randnumbin)
      ncsl=ifelse(randnum)
      #ncs is new checksum
      ncs=ncsl[len(ncsl)-1]      
      if cs==ncs:
        print("Message received accurately")
      else:
        print("Message received with error")
def eextra(m):
      len1=len(m)
      csl=ifelse(m)
      cs=csl[len(csl)-1]
      extra=[]
      extrabin=[]
      extra=extra+m[0:len(m)-1]
      extra.append(random.randint(0,255))
      global n
      if n==1:
          for i in range(0,len(extra)):
              extrabin.append(bin(extra[i])[2:].zfill(8))
          extrabin.append(bin(m[len(m)-1])[2:].zfill(16))
      else:
           for i in range(0,len(extra)):
              extrabin.append(bin(extra[i])[2:].zfill(16))
           extrabin.append(bin(m[len(m)-1])[2:].zfill(32))
      print("The message received at the receiver side is")
      print(extrabin)
      ncsl=ifelse(extra)
      #ncs is new checksum
      ncs=ncsl[len(ncsl)-1]
      if cs==ncs:
        print("Message received accurately")
      else:
        print("Message received with error")
def eincs(m):
      csl=ifelse(m)
      #cse is a list that will contain same elements as the sender side but a wrong checksum 
      cse=[]
      cse=cse+m[0:len(m)-1]
      csebin=[]
      global n
      if n==1:
          for i in range(0,len(cse)):
              csebin.append(bin(cse[i])[2:].zfill(8))
      else:
          for i in range(0,len(cse)):
              csebin.append(bin(cse[i])[2:].zfill(16))
      if n==1:
          randcs=(random.randint(0,65536))
          cs=(bin(randcs)[2:].zfill(16))
      else:
          randcs=(random.randint(0,4294967296))
          cs=(bin(randcs)[2:].zfill(32))
      if n==1:
          csebin.append(bin(randcs)[2:].zfill(16))
      else:
          csebin.append(bin(randcs)[2:].zfill(32))
      print("The message received at the receiver side is")
      print(csebin)
      ncsl=ifelse(cse)
      #ncs is new checksum
      ncs=ncsl[len(ncsl)-1]
      if cs==ncs:
        print("Message received accurately")
      else:
        print("Message received with error")
def printfunc():
      print()
      print("********************WELCOME******************\n")
      print("               FLETCHER CHECKSUM             \n")
def printerror():
      print("The message can be received in different forms at the receiver side that is due to addition of noise the message may or may not be received accurately.\n\n")
      print("The different forms are: \n")
      print("1:The message is received accurately\n")
      print("2:The numbers in the sender list may be swapped\n")
      print("3:The numbers may be incremented or decremented equally\n")
      print("4:The numbers may be totally changed from what is sent\n")
      print("5:Some extra numbers might be added to the list\n")
      print("6:The list numbers might be received accurately but the checksum is modified\n")
def checksum32(messagei1):
        #msg is a list to store decimal numbers
        #message is a list to store binary numbers
        msg=messagei1
        message=[]
        for num in messagei1:
            message.append(bin(num)[2:].zfill(16))
        r=int(bin(0)[2:])
        l=int(bin(0)[2:])
        for data in message:
            sum1=binsum32(str(r),data)
            r=int(sum1)%int(bin(65536)[2:])
            sum2=binsum32(str(l),str(r))
            l=int(sum2)%int(bin(65536)[2:])
       checksum=l*int(bin(65536)[2:])+r
        message.append(str(checksum).zfill(32))
        intcheck=(int(str(checksum),2))
        msg.append(intcheck)
        return(message)
def binsum32(num1,num2):
        sum = bin(int(num1,2)+int(num2,2))[2:].zfill(16)
        return(sum)
def ifelse(messagei):
    global n
    if n==1:
        chks=checksum16(messagei)
    else:
        chks=checksum32(messagei)
    return chks
printfunc()
sender()
