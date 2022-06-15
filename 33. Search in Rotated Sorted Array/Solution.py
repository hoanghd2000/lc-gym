class Solution:
    def recur_search(self, nums, first, last, target):
        n = last-first
        if n < 0:
            return -1
        if n == 0:
            if target == nums[first]:
                return first
            else:
                return -1
        if n == 1:
            if target == nums[first]:
                return first
            elif target == nums[last]:
                return last
            else:
                return -1
        else:
            mid = (first+last)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if target == nums[first]:
                    return first
                elif target == nums[mid-1]:
                    return mid-1
                elif first == mid - 1:
                    return self.recur_search(nums, mid+1, last, target)
                elif nums[first] < nums[mid-1]:
                    if target > nums[first] and target < nums[mid-1]:
                        return self.recur_search(nums, first, mid-1, target)
                    else:
                        return self.recur_search(nums, mid+1, last, target)
                else:
                    if (target < nums[first] and target < nums[mid-1]) or (target > nums[first] and target > nums[mid-1]):
                        return self.recur_search(nums, first, mid-1, target)
                    else:
                        return self.recur_search(nums, mid+1, last, target)
            else:
                if target == nums[mid+1]:
                    return mid+1
                elif target == nums[last]:
                    return last
                elif mid+1 == last:
                    return self.recur_search(nums, first, mid-1, target)
                elif nums[mid+1] < nums[last]:
                    if target > nums[mid+1] and target < nums[last]:
                        return self.recur_search(nums, mid+1, last, target)
                    else:
                        return self.recur_search(nums, first, mid-1, target)
                else:
                    if (target < nums[mid+1] and target < nums[last]) or (target > nums[mid+1] and target > nums[last]):
                        return self.recur_search(nums, mid+1, last, target)
                    else:
                        return self.recur_search(nums, first, mid-1, target)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.recur_search(nums, 0, len(nums)-1, target)