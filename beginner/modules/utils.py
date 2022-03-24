def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number 
    return maximum 

# maximum is a built in function name, it's best to use another name
