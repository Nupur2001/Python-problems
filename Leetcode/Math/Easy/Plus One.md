# 🧮 Plus One — LeetCode Problem #66

## 📘 

You are given a **large integer** represented as an integer array `digits`,  
where each `digits[i]` is the i-th digit of the integer.  
The digits are ordered from **most significant to least significant** (left to right).  
The large integer does **not contain any leading 0's**.

Increment the large integer by one and return the resulting array of digits.

---

### 💡 Example 1:
**Input:**  
`digits = [1,2,3]`  

**Output:**  
`[1,2,4]`  

**Explanation:**  
The array represents the integer `123`.  
Incrementing by one gives `123 + 1 = 124`.  
Thus, the result should be `[1,2,4]`.

---

### 💡 Example 2:
**Input:**  
`digits = [4,3,2,1]`  

**Output:**  
`[4,3,2,2]`  

**Explanation:**  
The array represents `4321`.  
Incrementing by one gives `4321 + 1 = 4322`.

---

### 💡 Example 3:
**Input:**  
`digits = [9]`  

**Output:**  
`[1,0]`  

**Explanation:**  
The array represents `9`.  
Incrementing by one gives `9 + 1 = 10`.

---

### ⚙️ Constraints
- `1 <= digits.length <= 100`  
- `0 <= digits[i] <= 9`  
- The input array does **not** contain any leading zeros.  

---

## 🧩 Solution

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and move backward
        for i in range(len(digits) - 1, -1, -1):
            # If current digit is less than 9, just add one and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If it's 9, set it to 0 and continue the carry
            digits[i] = 0
        
        # If all digits were 9 (e.g. [9,9,9] -> [1,0,0,0])
        return [1] + digits
