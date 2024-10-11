class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        char_cnt = Counter(magazine)
        for char in ransomNote:
            char_cnt[char] -= 1
            if char_cnt[char] < 0:
                return False
        return True
        