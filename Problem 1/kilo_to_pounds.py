def kilo_to_pounds(kilos):
    # Correctly return the conversion result
    return kilos * 2.20462  # Return only the conversion result

# Main part of the program starts here. Do not remove the line below.
if __name__ == '__main__':
    kilos = float(input())
    
    pounds = kilo_to_pounds(kilos)
    print(f'{pounds:.3f} lbs')  # Format the output to 3 decimal places