print("hello welcome to the jungle survive if you can.")

print()

def  choice (health ,damage):
  print ("-----------------------------------------------")
  while health > 0: 
    print ("HP:", health )
    print("Attack:", damage)
    print ("----------------")
    
    direction = input("pick a direction,r, l, u, d ")

    if (direction == "r") :                   
      print("you encountered a wild predator ")
      
    elif (direction == "u"):
      print("you  found a sword")
      
    
    elif (direction == "l"):
      print("you   found money !")
      
      
    elif (direction == "d"):
      print("you  started your journey back home  ")
       
      
    elif (direction == "d"):
      print("you encountered a evil wizard ",damage,"to the wizard")
      print ("the wizard dies")
      
    else:
      print ("please put a valid choice r, l, u, d ")
   

choice(60,50)