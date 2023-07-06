# Created four Functions to calculate the total cost of a holiday 

# This function will calculate the destinations using if, else, elif statements
# created a menu for the user to select from 
def p_cost():
    
    while True:
        print("Choose any one of our 5 luxurious adventure packages:")
        dest = {1:"Paris",
              2:"Ibiza", 
              3:"Milan",
              4:"Dubai", 
              5:"zanzibar"}
        print(dest)  
        
        dest = (input("Enter your destination option( choose from 1-5): \n "))
        if dest == "1":
            cost = 750
            return cost
            break
        
        elif dest == "2":
            cost = 850
            return cost
            break 
        
        elif dest == "3":
            cost = 600
            return cost
            break 
        
        elif dest == "4":
            cost = 550
            return cost
            break
        
        elif dest == "5":
            cost = 450
            return cost 
            break
        
        else:
            print("Incorrect selection please try again")
            continue 
        
# this variable ask the user how many nights he will stay at hotel 
def hotel_cost(nights):
    total = int(nights * 350)
    return total

# asks user how many day he will use rented car 
def car_rental(days):
    rental_cost= int(days * 200)
    return rental_cost
   
nights = int(input("How many nights will you be staying with us ?: \n "))
Days = int(input("How many days will you need a car for?: \n"))
  
# This will return the total holiday cost of the user   
def holiday_cost(nights, days) :
    price1 = p_cost()
    price2= hotel_cost(nights)
    price3= car_rental(days)
    total = price1 + price2 + price3
    print(f"The Total cost of your holiday will be R", total)
    
holiday_cost(nights,Days)