class Solution:
    # 将问题转换成无向连通图中寻找最短路径，采用 BFS 方法解答
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return  0
        # 每个单词的长度
        L =  len(beginWord)
        all_combi_dict =  defaultdict(list)
        for word in wordList:
            for i in range(L):
                # 将每个单词的每一位替换成 ‘*’ mask
                all_combi_dict[word[:i] + '*' + word[i+1:]].append(word)

        # BFS 遍历队列
        queue = [(beginWord, 1)]
        # 保存已经访问过的节点
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                inter_word = current_word[:i] + '*' + current_word[i+1:]
                # 广度优先遍历所有连边
                for word in all_combi_dict[inter_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combi_dict[inter_word] = []
        return 0
