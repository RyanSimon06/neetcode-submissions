class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for i, word in enumerate(strs):
            word_ordered = "".join(sorted(word))
            if word_ordered in mydict:
                mydict[word_ordered].append(word)
            else:
                mydict[word_ordered] = [word]
        return list(mydict.values())