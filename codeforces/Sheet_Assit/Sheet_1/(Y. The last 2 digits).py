A, B, C, D = map(int, input().split())
 
mult = (A * B * C * D) % 100
 
if mult >= 10 :
  print(mult) 
else :
  print ("0%i" %(mult))


    