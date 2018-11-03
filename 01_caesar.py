import string
alp=string.ascii_uppercase+string.ascii_uppercase[0:3:]
print("Type Massage in Uppercase Letters with using Spaces and dots only")
text=input("enter Massage ::> ")
ciper=''
for i in text:
 if(i!=" " and i!="."):
  x=alp.index(i)+3
  y=alp[x]
  ciper=ciper+y
 else:
  if(i==" "):
   ciper=ciper+" "
  elif(i=="."):
   ciper=ciper+"."   
print("Ciper Massage ::> ",ciper)
 

