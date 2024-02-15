def spy_game(nums):
    spy0 = False
    spy00 = False
    spy007 = False
    for num in nums:
        if num == 0:
            if not spy0:
                spy0 = True
            elif not spy00:
                spy00 = True
            elif spy007:
                return True
        elif num == 7:
            if spy00:
                return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0])) 
