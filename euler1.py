

#  if we list all natural nums below 10 that are multilies of 3 0r 5, we get 3, 5, 6, 9. The sum of all these is 23

# Find the sum of all multiplieras or 3 or 5 below 1000



def multplies_of_three_or_five(multiple1, multiple2, lower_limit, higher_limit):
    sum = 0
    for i in range(lower_limit, higher_limit):
        
        if i %  multiple1 == 0 or i % multiple2 == 0:
            sum += i
        
    return sum


print(multplies_of_three_or_five(3, 5, 1, 1000))
print(multplies_of_three_or_five(5, 7, 100, 500))
            
            
