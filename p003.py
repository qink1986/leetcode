'''
@Author: qink-DN493
@Date: 2019-12-23 10:08:18
@LastEditors  : qink-DN493
@LastEditTime : 2019-12-25 08:28:37
@Description: 
'''

import time
def lengthOfLongestSubstring(s: str) -> int:
    dic = {}
    start = longest = 0
    for k,v in enumerate(s):
        # print(k,v,longest,dic)
        if v in dic and dic[v] >= start:
            start = k + 1
        dic[v] = k
        longest = max(longest, k - start + 1)
    return longest


s = time.time()
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("au"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))

e = time.time()
print('time cost: %.5f'%(e-s))


