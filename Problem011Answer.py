def isSubsequence(s, t):
        set_1 = []
        set_2 = []
        duplicate_tracker = []
        index_tracker = []

        if s == "":
            return True
        elif t == "":
            return False
        else:
            for char in s:
                set_1.append(char)
            
            for char in t:
                set_2.append(char)
            
            n_len = len(s)
            n_len_2 = len(t)
            
            for i in range(n_len):
                for j in range(n_len_2):
                    if set_1[i] == set_2[j] and set_2[j] not in duplicate_tracker:
                        index_tracker.append(j)
                        duplicate_tracker.append(set_2[j])
                    else:
                        j += 1
            n_len_index = len(index_tracker)
            if n_len_index == 1:
                return True
            elif n_len_index == 0:
                return False
            elif duplicate_tracker != set_1:
                return False
            else:
                k = 0
                while k <n_len_index - 1:
                    if (index_tracker[k+1] - index_tracker[k]) > 0:
                        k += 1
                    else:
                        return False
        return True          

s_1 = "axc"
t_1 = "ahbgdc"
ans = isSubsequence(s_1, t_1)
print(ans)
