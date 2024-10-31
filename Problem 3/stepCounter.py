def feet_to_steps(user_feet):
   #write your code here
   
   return int(user_feet / 2.5)

if __name__ == '__main__':
    #take input feet steps here
    user_feet = float(input("Enter the number of feet walked: "))
    #store it into the function
    steps = feet_to_steps(user_feet)
    #print your steps here
    feet_to_steps(5280)
    print(steps)