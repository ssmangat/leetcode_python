# Solution for problem_347
# Top k frequent elements
def problem_347(nums:list[int],k:int)-> list[int]:
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
            continue
        counter[num] = 1

    sorted_counter = sorted(counter.items(),key=lambda x: x[1], reverse=True)
    result = []
    for i in range(k):
        result.append(sorted_counter[i][0])

    return result
    
