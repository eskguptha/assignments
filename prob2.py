"""
Problem #2  
Fill in the Blanks 
 
You are given a puzzle like this: 
 
7 __ 10 __ 2
 
Each blank may be filled with a '+' (plus) or '-' (minus), producing a value k. 
For all combinations of plus and minus, find the value of k that is closest to 
0.  
 
In the above case, there are 4 combinations, each producing a different 
value: 
 
7 + 10 + 2 = 19
7 + 10 - 2 = 15
7 - 10 + 2 = -1
7 - 10 - 2 = -5
 
Of all these combinations, the value that is closest to zero is ​ -1​ . So the 
answer is -
1​ . If there are more than one number that is closest, print the 
absolute value. 
 
Sample Input/Output: 
 
Enter digits: 7,10,2
Value close to zero is -1
Enter digits: 1,2,3,4
Value close to zero is 0
"""
INPUT_DIGITS = input("Enter digits: ")
OUTPUT_DIGIT = None
OUTPUT_DIGIT_LIST = []

# Split input string by comma seperated
input_digit_list = INPUT_DIGITS.split(',')

# Input Numbers should be greter than 2
if len(input_digit_list) > 2:
    # Get First Three Numbers
    input_digit_list = input_digit_list[:3]
    try:
        # Convert string to number and remove space if exist
        first_number, second_number, thrid_number = [int(each_num.strip()) for each_num in input_digit_list]
        # Apply four combinations on give three numbers
        combination_result_1 = first_number + second_number + thrid_number
        combination_result_2 = first_number + second_number - thrid_number
        combination_result_3 = first_number - second_number + thrid_number
        combination_result_4 = first_number - second_number - thrid_number
        # Append each combination result into an array
        OUTPUT_DIGIT_LIST.append(combination_result_1)
        OUTPUT_DIGIT_LIST.append(combination_result_2)
        OUTPUT_DIGIT_LIST.append(combination_result_3)
        OUTPUT_DIGIT_LIST.append(combination_result_4)
        # Sort array from small to large
        OUTPUT_DIGIT_LIST.sort()
        # get all <= 0 values from resultset
        sorted_result_set = [each_num for each_num in OUTPUT_DIGIT_LIST if each_num <= 0]
        # if sorted result set is empty than get list minimum value from >= 0 valueset
        if not sorted_result_set:
            sorted_result_set = [each_num for each_num in OUTPUT_DIGIT_LIST if each_num >= 0]
            sorted_result_set.sort(reverse=True)
        # get least element from resultset
        OUTPUT_DIGIT = sorted_result_set.pop()
        print ("Value close to zero is {}".format(OUTPUT_DIGIT))
    except TypeError as e:
        print ("Please Enter Numbers Only. Ex:7,10,2")
        pass
else:
    print ("Please Enter any three numbers by comma sperated Ex:7,10,2")
