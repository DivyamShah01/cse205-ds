class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            #print(mid)
            left, right = arr[:mid], arr[mid:]
            #print(left)
            #print(right)
            #print("+")
            left, right = merge_sort(left), merge_sort(right)

            #print("++")
            #print(left)
            #print(right)
            result, i, j = [], 0, 0

            #print(arr)

            while i < len(left) and j < len(right):
                #print("*")
                #print(left)
                #print(right)
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            #print(left)
            result.extend(right[j:])
            #print(right)
            return result
        return merge_sort(nums)