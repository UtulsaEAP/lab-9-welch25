def swap_values(user_val1, user_val2, user_val3, user_val4):   
    # Swap the first with the second, and the third with the fourth
    return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__':   
    user_input1 = int(input())
    user_input2 = int(input())
    user_input3 = int(input())
    user_input4 = int(input())
    
    # Store output for every input here
    swapped_values = swap_values(user_input1, user_input2, user_input3, user_input4)
    
    # Print the swapped output
    print(*swapped_values)  # The '*' unpacks the tuple for printing