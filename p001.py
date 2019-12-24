'''
@Author: qink-DN493
@Date: 2019-12-23 10:08:18
@LastEditors  : qink-DN493
@LastEditTime : 2019-12-24 11:31:50
@Description: 
'''
import time
s = time.time()
def twoSum(nums, target):
    # for k,v in enumerate(nums):
    #     nums2 = nums[k+1:]
    #     for i in range(len(nums2)):
    #         if v + nums2[i] == target:
    #             return [k,i+k+1]
    ##################################
    # for k,v in enumerate(nums):
    #     if target-v in nums[k+1:]:
    #         return [k,nums.index(target-v,k+1)]
    ##################################
    dic = {}
    for k,v in enumerate(nums):
        if v in dic:
            return [dic[v], k]
        else:
            dic[target - v] = k


for i in range(100000):
    twoSum([2,7,11,12],9)
    twoSum([3,2,4],6)
e = time.time()
print('time cost: %.5f'%(e-s))


