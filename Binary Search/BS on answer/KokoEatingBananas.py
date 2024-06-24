import math
def totalhours(nums, rateofeating):
    ans = 0
    for i in range(len(nums)):
        ans += math.ceil(nums[i] / rateofeating)
    return ans

def kokoeatingbananas(nums, maxhours):
    l, r = 1, max(nums)
    while l <= r:
        m = (l + r) // 2

        # time is the divisor here 
        hours = totalhours(nums, m)

        # Current time is less than given tiem thus we move to the left as we have to find the minimum time
        if hours <= maxhours:
            r = m - 1
        
        # Current timw is greater than the required time thus we move to the right to satisy the constraint
        else:
            l = m + 1
    return l


if __name__ == "__main__":
    arr = [ 1, 2, 1, 2, 17, 12, 12, 13, 1 ]
    minhours = 15
    print("Koko will have to eat ", kokoeatingbananas(arr, minhours), "per hour.")