# Is Subsequence

## 🧠 Problem Description

Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise.

A **subsequence** of a string is a new string formed from the original string by deleting some (possibly none) of the characters **without changing the relative order** of the remaining characters.
(https://thita.ai/problems/is-subsequence)

For example:
- `"ace"` is a subsequence of `"abcde"`
- `"aec"` is **not** a subsequence of `"abcde"`

---

## 📌 Examples

### Example 1

**Input:**
s = "abc"
t = "ahbgdc"


**Output:**
true


---

### Example 2

**Input:**
s = "axc"
t = "ahbgdc"


**Output:**
false

---

## 🔒 Constraints

- `0 <= s.length <= 100`
- `0 <= t.length <= 10⁴`
- `s` and `t` consist only of lowercase English letters.

---

## 🔎 Summary

- A subsequence preserves character order but allows deletions.
- The two-pointer approach is optimal for a single query.
- For large-scale repeated queries, preprocess `t` and use binary search for faster lookups.
