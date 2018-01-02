def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    nums1[:] = nums1[:m]
    nums2[:] = nums2[:n]
    i, j = 0, 0
    while (i < m) & (j < n):
        if nums1[i] >= nums2[j]:
            #nums1[:] = nums1[:i] + [nums2[j]] + nums1[i:]
            nums1.insert(i, nums2[j])
            j = j + 1
        else:
            i = i + 1
    if j < n:
        nums1[:] = nums1[:] + nums2[j:]
    print(nums1)

nums1=[2,0]
m=1
n=1
nums2=[1]
merge(nums1, m, nums2, n)