class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        arr,res = [], []
        for n, cnt in count.items():
            arr.append([cnt, n])
        arr.sort()
        print(arr)

        while len(res) < k:
            res.append(arr.pop()[1])
        return res