def isSubsequence(s, t):

    # Convert s and t to lists of characters
    set_1 = []  # List to store characters of s
    set_2 = []  # List to store characters of t
    duplicate_tracker = []  # Tracks which characters from t have been matched
    index_tracker = []      # Tracks the indices in t where matches occur

    # If s is empty, it's always a subsequence
    if s == "":
        return True
    # If t is empty but s is not, s can't be a subsequence
    elif t == "":
        return False
    else:
        # Fill set_1 and set_2 with characters from s and t
        for char in s:
            set_1.append(char)
        for char in t:
            set_2.append(char)

        n_len = len(s)
        n_len_2 = len(t)

        # For each character in s, look for a match in t
        for i in range(n_len):
            for j in range(n_len_2):
                # If characters match and t[j] hasn't been matched before
                if set_1[i] == set_2[j] and set_2[j] not in duplicate_tracker:
                    index_tracker.append(j)         # Record the index in t
                    duplicate_tracker.append(set_2[j])  # Mark as matched
                else:
                    j += 1  # (This increment is unnecessary in Python, as for-loop handles it)

        n_len_index = len(index_tracker)
        # If only one match found, s is a subsequence (single char)
        if n_len_index == 1:
            return True
        # If no matches, s is not a subsequence
        elif n_len_index == 0:
            return False
        # If the matched characters don't match s, not a subsequence
        elif duplicate_tracker != set_1:
            return False
        else:
            # Check that the indices in t are strictly increasing
            k = 0
            while k < n_len_index - 1:
                if (index_tracker[k+1] - index_tracker[k]) > 0:
                    k += 1
                else:
                    return False
    # If all checks pass, s is a subsequence of t
    return True


# Example usage
s_1 = "axc"  # The string to check as a subsequence
t_1 = "ahbgdc"  # The main string
ans = isSubsequence(s_1, t_1)  # Call the function
print(ans)  # Output the result (should be False for this example)
