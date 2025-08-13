'''
Task 1: String Length Frequency
Objective: Write a function that identifies the most frequent string lengths in an array of strings.
Requirements:
Provide multiple test cases.
Use any language you prefer; JavaScript or Python is recommended.
[Optional] Include a unit test function.
Example:
Input: ['a', 'ab', 'abc', 'cd', 'def', 'gh']
Explanation: The string lengths are [1, 2, 3, 2, 3, 2]. The most frequent length is 2, corresponding to ['ab', 'cd', 'gh'].
Output: ['ab', 'cd', 'gh']
Time Allocation: 45 minutes
'''
# What if there is a case where the frequencies were the same for 2 lengths or more?

# Identifies the most frequent string lengths in an array of strings and returns the strings of that length
def return_most_frequent_length_strings(strings_arr):
    if not strings_arr:
        return []
    
    length_map = {}

    for string in strings_arr:
        cur_length = len(string)
        if cur_length in length_map:
            length_map[cur_length].append(string)
        else:
            length_map[cur_length] = [string]
    
    # get the most frequent length and its values, assuming it returns
    # based on order of insertion when 2 or more lengths have the same frequencies
    frequent_length_strings = max(length_map.values(), key = len)
    return frequent_length_strings

# Debugging function used to check if the function return the expected values
def check_equal(test_case, result, expected):
    print(f"TEST {'PASS:' if result == expected else 'FAIL: '}", test_case)
    print("Expected: ", expected)
    print("Current Output: ", result, "\n")

# Unit test function for task 1
def run_unit_tests():
    check_equal("Given Test",
                return_most_frequent_length_strings(['a', 'ab', 'abc', 'cd', 'def', 'gh']), 
                ['ab', 'cd', 'gh'])
    check_equal("Empty Case",
                return_most_frequent_length_strings([]), 
                [])
    check_equal("Same Frequency Case",
                return_most_frequent_length_strings(['a', 'b', "ab", "ba"]), 
                ['a', 'b'])
    check_equal("One String Case",
                return_most_frequent_length_strings(['a']), 
                ['a'])
    check_equal("5 Lengths That Have The Same Frequency Case",
                return_most_frequent_length_strings(["ab", 'a', "ddd", "ccc", "ba",
                                                     "qwe3", "2323", "00000", 'b', "abcde"]), 
                ['ab', 'ba'])
    check_equal("One Length Only Case",
                return_most_frequent_length_strings(["qwe32", "2323/", "00000", 'b][]|', "abcde"]), 
                ["qwe32", "2323/", "00000", 'b][]|', "abcde"])
    check_equal("Empty String Case",
                return_most_frequent_length_strings(["", "", "", 'b][]|', "abcde"]), 
                ["", "", ""])

# Run the unit tests defined in the Unit test function
run_unit_tests()