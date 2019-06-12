def blackjack(a,b,c):
    nums = a, b, c
    for i in nums:
        if i == 11 and sum(nums) > 21:
            if sum(nums) - 10 <= 21:
                return sum(nums) - 10
    if sum(nums) > 21:
            return "BUST"
    else:
        return sum(nums)

print(blackjack(5,6,7))
print(blackjack(1,12,8))
print(blackjack(9,9,11))