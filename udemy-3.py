def spy_game(nums):
    code  = [0,0,7,'x']
    for i in nums:
        if i == code[0]:
            code.pop(0)
    return len(code) == 1


print(spy_game([1,2,4,0,0,7,5]))