# 8. Write a function that takes in a list of integers and returns True if it contains `007` in order
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False
