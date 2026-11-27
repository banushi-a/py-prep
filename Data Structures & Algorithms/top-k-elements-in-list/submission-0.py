class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # plan:
        # freq_to_nums = [1,...,n]: => set([num1,...numM])
        # num_to_freq = {n -> freq}
        freq_to_nums = [None] * (len(nums) + 1)
        num_to_freq = {}
        for num in nums:
            if num in num_to_freq:
                old_freq = num_to_freq[num]
                num_to_freq[num] += 1
                freq_to_nums[old_freq].remove(num)
                if freq_to_nums[old_freq+1] is None:
                    freq_to_nums[old_freq+1] = set([num])
                else:
                    freq_to_nums[old_freq+1].add(num)
            else:
                num_to_freq[num] = 1
                if freq_to_nums[1] is None:
                    freq_to_nums[1] = set([num])
                else:
                    freq_to_nums[1].add(num)
            
        out = []
        curr_freq = len(nums)
        while len(out) < k and curr_freq >= 0:
            if freq_to_nums[curr_freq] is None:
                curr_freq -= 1
                continue
            for n in freq_to_nums[curr_freq]:
                out.append(n)
                if len(out) == k:
                    break
            curr_freq -= 1

        return out