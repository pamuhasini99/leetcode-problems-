class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordset=set(wordList)
        if endWord not in wordset:
            return []
        par={}
        found=False
        level=set([beginWord])
        while level and not found:
            nl=set()
            for word in level:
                if word in wordset:
                    wordset.remove(word)
            for word in level:
                for i in range(len(word)):
                    for ch in 'qwertyuioplkjhgfdsazxcvbnm':
                        nw=word[:i]+ch+word[i+1:]
                        if nw in wordset:
                            if nw not in par:
                                par[nw]=[]
                            par[nw].append(word)
                            nl.add(nw)
                            if nw==endWord:
                                found=True 
            level=nl
        res=[]
        def bt(word,path):
            if word==beginWord:
                res.append(path[::-1])
                return
            if word not in par:
                return
            for p in par[word]:
                bt(p,path+[p])
        if found:
            bt(endWord,[endWord])
        return res
        

        