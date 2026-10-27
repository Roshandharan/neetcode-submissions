class Solution:
    def minWindow(self, s: str, t: str) -> str:
       if not s or not t: return ''

       t_chars = {}
       w_chars = {}
       
       for key in t:
        if key not in t_chars:
            t_chars[key] = 1
        else:
            t_chars[key] +=1

       min_win = 10**6
       start_index = -1
       have =0
       need = len(t_chars)
       l = 0

       for r in range(len(s)):
        c = s[r]

        if c not in w_chars:
            w_chars[c] = 1
        else:
            w_chars[c] +=1

        if c in t_chars and t_chars[c]==w_chars[c]:
            have +=1

        while have == need:
            w =r-l+1
            if w<min_win:
                min_win = w
                start_index =l

            if s[l] in t_chars and t_chars[s[l]] == w_chars[s[l]]:
                have -=1

            if w_chars[s[l]] == 1:
                del w_chars[s[l]]
            else:
                w_chars[s[l]] -=1
            l+=1


       if min_win<10**6:
            return s[start_index:start_index+min_win]
       else:
            return ''