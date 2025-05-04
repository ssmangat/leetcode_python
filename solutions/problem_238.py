# Solution for problem_238
# for this problem, we simply iterate over the provided array nums twice and multiply elemens from left and right
def product_except_self(nums:list[int]) -> list[int]:
    arr = [1] * len(nums) #declaring arr
    left,right = 1,1
    for i in range(len(nums)):
        arr[i] *= left #save product of all previous indexs imn current index
        left *= nums[i]
    for i in range(len(nums)-1,-1,-1):
        arr[i] *= right #same as previous loop but in reverse
        right *= nums[i]

    return arr
