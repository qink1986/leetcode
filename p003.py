'''
@Author: qink-DN493
@Date: 2019-12-23 10:08:18
@LastEditors  : qink-DN493
@LastEditTime : 2019-12-24 16:03:32
@Description: 
'''

import time
def lengthOfLongestSubstring(s: str) -> int:
    l = len(s)
    if l == 0:
        return l
    for i in range(l):
        left = l - i
        for j in range(i+1):
            ret = s[j:left+j+1]
            # print(ret)
            if not isDup(ret):
                return len(ret)
                        
def isDup(s: str) -> bool:
    for k in range(len(s)):
        left = s[:k] + s[k+1:]
        if s[k] in left:
            return True
    return False

        # for r in range(l-i):
        #     left = ret.pop(ret.index(r))
        #     if r in left:
        #         continue
        #     return l-i



s = time.time()
# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring(""))
# print(lengthOfLongestSubstring("au"))
# print(lengthOfLongestSubstring("bbbbb"))
# print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("pwwkew"))

e = time.time()
print('time cost: %.5f'%(e-s))


