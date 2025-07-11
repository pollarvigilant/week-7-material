#Loop Control Statements

#fruits = ["apple", "banana", "citrus", "dates"]

#for fruit in fruits:
   # if fruit == "citrus":
  #      break #Exits the loop if cherry is found
 #   print(fruit)

#print()

#for fruit in fruits:
   # if fruit == "cherry":
  #      continue #skips cherry and moves to the next
 #   print(fruit)
    
#print()

#for fruit in fruits:
 #   if fruit == "cherry":
#       pass #placeholder, no action is needed for cherry
#    print(fruit)

count = 0

while count < 5:
    print(count)
    count += 1
    if count == 3:
        break #exits the loop when the count is reached - 3