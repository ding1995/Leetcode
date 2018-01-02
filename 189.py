def rotate(nums, k):
    for i in range(k):
        nums[:]=[nums[-1]]+nums[:-1]

nums=[1,2]
k=1
rotate(nums, k)