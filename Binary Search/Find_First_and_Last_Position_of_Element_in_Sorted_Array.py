class Solution:
    def firstOccurence(self, nums, target):
        low = 0
        high = len(nums)-1
        first = -1
        while(low<= high):
            mid = low + (high - low)//2
            if(nums[mid]==target):
                first=mid
                high = mid-1
            elif (nums[mid] < target):
                low = mid + 1
            else:
                high = mid -1
        return first

    def lastOccurence(self, nums,target):
        low = 0
        high = len(nums)-1
        last = -1
        while(low<=high):
            mid = low + (high-low)//2
            if(nums[mid]==target):
                last = mid
                low = mid + 1
            elif (nums[mid] > target):
                high = mid -1
            else:
                low = mid+1
        return last

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firstoccr = self.firstOccurence(nums,target)
        if(firstoccr == -1):
            return [-1,-1]
        lastoccr = self.lastOccurence(nums,target)
        return [firstoccr,lastoccr]

        
