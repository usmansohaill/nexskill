def arrayCheck(nums):
    for item in nums:
        if nums[item] == 1 and nums[item + 1] == 2 and nums[item + 2] == 3:
            return True
        else:
            return False


def stringBits(str):
    newStr = str[::2]
    return newStr


def end_other(a, b):
    newA = s.lower(a)
    newB = s.lower(b)
    if newA == newB[-len(newA):] or newB == newA[-len(newB)]:
        return True
    else:
        return False


def doubleChar(str):
    for i in str:
        newChars = i + i
        newStr = newStr + newChar
    return newStr


def no_teen_sum(a, b, c):
    newA = fix_teen(a)
    newB = fix_teen(b)
    newC = fix_teen(c)
    abcSum = newA + newB + newC


def fix_teen(n):
    while n != 15 and n != 16 and n > 12 and n < 20:
        n = 0
    return n


def count_evens(nums):
    count = 0
    for i in nums:
        if nums[i] % 2 == 0:
            count = count + 1
    return count
