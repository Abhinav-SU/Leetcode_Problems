import collections
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
            
        # We will map child_word -> [parent_words]
        tree = collections.defaultdict(set)
        
        layer = {beginWord}
        found = False
        
        # ==========================================
        # PHASE 1: Forward BFS (Drawing arrows backwards)
        # ==========================================
        while layer and not found:
            # Python C-level optimization: 
            # Instantly remove all words in the current layer from the dictionary
            # so we never walk backwards or horizontally.
            wordSet -= layer 
            
            next_layer = set()
            
            for word in layer:
                # Micro-optimization: slice prefix and suffix ONCE per index
                # instead of inside the 26-letter loop.
                for i in range(len(word)):
                    prefix, suffix = word[:i], word[i+1:]
                    
                    for char in "abcdefghijklmnopqrstuvwxyz":
                        if char == word[i]:
                            continue
                            
                        newWord = prefix + char + suffix
                        
                        if newWord in wordSet:
                            next_layer.add(newWord)
                            # Draw the arrow BACKWARDS (from child to parent)
                            tree[newWord].add(word)
                            
                            if newWord == endWord:
                                found = True
                                
            layer = next_layer
            
        if not found:
            return []
            
        # ==========================================
        # PHASE 2: Backward DFS (Zero dead ends!)
        # ==========================================
        res = []
        
        def dfs(current_word, path):
            if current_word == beginWord:
                # Because we built the path backwards, we must reverse it before saving
                res.append(path[::-1])
                return
                
            # Walk UP the tree from endWord to beginWord
            for parent in tree[current_word]:
                path.append(parent)
                dfs(parent, path)
                path.pop()
                
        # Kick off DFS from the finish line
        dfs(endWord, [endWord])
        
        return res