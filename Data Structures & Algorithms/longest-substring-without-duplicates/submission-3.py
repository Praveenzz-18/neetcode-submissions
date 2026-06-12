class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_longest = 0
        starting_idx = 0
        current_idx = 0
        seen = {}

        while current_idx < len(s):
            if s[current_idx] in seen:
                if seen[s[current_idx]] < starting_idx:
                    seen[s[current_idx]] = current_idx
                else:
                    if current_idx - starting_idx> current_longest:
                        current_longest = current_idx - starting_idx
                    starting_idx = seen[s[current_idx]] + 1
                    seen[s[current_idx]] = current_idx
            else:
                seen[s[current_idx]] = current_idx
            
            current_idx += 1

        if current_idx - starting_idx> current_longest:
            current_longest = current_idx - starting_idx

        return current_longest