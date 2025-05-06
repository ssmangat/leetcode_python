# Solution for problem_128
# This problem Longest Consecutive Sequence can be solved in following steps:
#1. Change the list to a set (this removes duplicates)
#2. Create a longest counter
#3. using a for loop find the smallest number of Sequence
#4. using a condition count the longest sequence from the smallest number using a while loop
def problem_128(nums:list[int])->int:
    if not nums:
        return 0
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num-1 not in num_set:
            curr = num
            seq = 1
            while curr+1 in num_set:
                curr += 1
                seq += 1
            longest = max(longest,seq)

    return longest
