# 🎯 Two Sum Problem (LeetCode)

## ✅ Problem Description
Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you **may not use the same element twice**.

Return the answer in **any order**.

---

## 📝 Examples

| Input | Output | Explanation |
|------|--------|-------------|
| `nums = [2,7,11,15], target = 9` | `[0,1]` | Because `nums[0] + nums[1] = 9` |
| `nums = [3,2,4], target = 6` | `[1,2]` | `2 + 4 = 6` |
| `nums = [3,3], target = 6` | `[0,1]` | `3 + 3 = 6` |

---

## 🔒 Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only **one valid answer** exists.

---

## ⚡ Follow-Up
Can you solve it in **less than O(n²)** time?

> Yes ✅ (Solution below is **O(n)**)

---

## 💡 Approach (Efficient: O(n))

We use a **hash map** (dictionary) to store numbers we have seen and their indices.

Steps:
1. Traverse the array.
2. For each number, compute `complement = target - num`.
3. Check if the complement already exists in the dictionary.
4. If yes → Return the pair of indices.
5. If not → Store `num` with its index in the dictionary.

This avoids the nested loop of the brute-force method.

---

## 🧠 Code (Do Not Change Precode)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], i]
            lookup[num] = i
            
            
            
            
## ⏱️ Time Complexity Analysis

| Approach | Time Complexity | Space Complexity | Explanation |
|---------|----------------|-----------------|-------------|
| Brute Force | O(n²) | O(1) | Uses two nested loops to check every pair |
| Optimal (Hash Map) ✅ | **O(n)** | **O(n)** | Uses dictionary to store values and find complement in one pass |

---

## 🎉 Final Notes

- The input guarantees **only one valid pair**, so we can safely return as soon as we find the solution.
- The hash map (dictionary) allows **constant-time lookups**, making the solution efficient.
- Order of indices in the return does not matter.
- We are not allowed to reuse the same element twice — which is handled because every number is stored **after** checking its complement.

---