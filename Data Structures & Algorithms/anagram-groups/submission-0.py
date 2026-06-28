class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = [[strs[0]]]
        for i in range(1, len(strs)):
            is_an = False
            for out in output:
                first_anagram = out[0]
                if self.is_anagram(first_anagram, strs[i]):
                    out.append(strs[i])
                    is_an = True
                    break
            if not is_an:
                output.append([strs[i]])
        return output 
    
    def is_anagram(self, first_word, second_word):
        return sorted(first_word) == sorted(second_word)

