import time

def n(i):
  print(bin(int(i)))
  
def ka(f):
   print(bin(int(f)))
  
  
def ui(k):
  print(bin(int(k)))
  
print("welcome to number converter")
time.sleep(1)
v = input("In which programming number system you want to convert to..  (O for octal,H for hexadecimal and D for decimal  ")

while v == "O":
  ka(input("number want to convert -  "))
  
while v == "H":
  ui(input("number want to convert -  "))
  
while v == "D": 
  n(input ("number want to convert -  "))
 
  
 
 
