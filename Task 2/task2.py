'''
Task 2: Sum of Top Two Integers
Objective: Write a function that finds the sum of the two largest integers in an array.
Requirements:
Provide multiple test cases.
Use any language you prefer; JavaScript or Python is recommended.
[Optional] Include a unit test function.
Example:
Input: [1, 4, 2, 3, 5]
Explanation: The two largest integers are 5 and 4. Their sum is 9.
Output: 9
Time Allocation: 30 minutes

'''

# What if there are less than 2 elements in the array? In this case I will return
# 0 for empty and the first element for arrays with length of 1

# Output the sum of the two largest integers in an array
def sum_largest_two_int(int_arr):
    if not int_arr:
        return 0
    
    if len(int_arr) == 1:
        return int_arr[0]
    
    largest = second_largest = float("-inf")
    
    for num in int_arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    
    result = largest + second_largest
    return result
    
# Debugging function used to check if the function return the expected values
def check_equal(test_case, result, expected):
    print(f"TEST {'PASS:' if result == expected else 'FAIL: '}", test_case)
    print("Expected: ", expected)
    print("Current Output: ", result, "\n")

# Unit test function for task 2
def run_unit_tests():
    check_equal("Given Test",
                sum_largest_two_int([1, 4, 2, 3, 5]), 
                9)
    check_equal("Empty Case",
                sum_largest_two_int([]), 
                0)
    check_equal("Same Integers Case",
                sum_largest_two_int([1, 1, 1, 1, 1]), 
                2)
    check_equal("One String Case",
                sum_largest_two_int([1000000]), 
                1000000)
    check_equal("Mixed Order Case",
                sum_largest_two_int([2, 43343, 656, 1000000,
                                     9999, 100, -5, 1]), 
                1043343)
    check_equal("Negative Case",
                sum_largest_two_int([-2, -43343, -656, -1000000,
                                     -9999, -100, -5, -1]), 
                -3)
    check_equal("Mixed Sign Case",
                sum_largest_two_int([-2, 43343, -656, -1000000,
                                     -9999, -100, 5, -1]), 
                43348)
    check_equal("Large Int Case",
                sum_largest_two_int([-2, 999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 
                                     -656, -1000000,
                                     -9999, -100, -5, -1]), 
                999999999999999999999999999999999999999999999999999999999999999999999999999999999998)
    check_equal("Small Int Case",
                sum_largest_two_int([-2, -999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 
                                     -656, -1000000,
                                     -9999, -100, -5, 1]), 
                -1)
    check_equal("Descending Case",
                sum_largest_two_int([5, 4, 3, 2, 1]), 
                9)
    check_equal("Zeros Case + Negative",
                sum_largest_two_int([0, -1, 0, 0, -2]), 
                0)
    check_equal("Large Int Case 2",
                sum_largest_two_int([10**25, 10**25 - 1, 0]), 
                2 * (10**25) - 1)
    check_equal("Highest At Start Case",
                sum_largest_two_int([999, 1, -3, -1]), 
                1000)
    check_equal("Highest At End Case",
                sum_largest_two_int([1, 3 - 1, 999]), 
                1001)

# Run the unit tests defined in the Unit test function
run_unit_tests()
            