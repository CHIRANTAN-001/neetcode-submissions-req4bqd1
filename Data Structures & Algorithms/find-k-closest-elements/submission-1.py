class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # left, right = 0, len(arr) - 1

        # if (k == len(arr)):
        #     return arr
        
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if arr[mid] >= x:
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # left = right - 1

        # #  find the starting left
        # while k > 0:
        #     if left < 0:
        #         right += 1
        #     elif right >= len(arr):
        #         left -= 1
        #     elif abs(arr[right] - x) < abs(arr[left] - x):
        #         right += 1
        #     else:
        #         left -= 1
        #     k -= 1
        
        # return arr[left+1:right]
        
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
        
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
      
        return arr[left : left + k]
        