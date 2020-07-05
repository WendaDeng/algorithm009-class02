class Solution:
	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		if not beginWord or not endWord or not wordList or endWord not in wordList:
			return 0
		L = len(beginWord)

		# 预处理字典中的每个单词，将其变为通用单词，然后以此为key，原始单词为val，存入字典中
		all_comb_dict = defaultdict(list)
		for word in wordList:
			for i in range(L):
				all_comb_dict[word[:i] + '*' + word[i + 1:]].append(word)

		# BFS准备
		queue = [(beginWord, 1)]
		visited = {beginWord: True}

		while queue:
			cur_word, level = queue.pop(0)
			for i in range(L):
				# 将单词变为通用单词，寻找相连的单词
				inter_word = cur_word[:i] + '*' + cur_word[i + 1:]
				for word in all_comb_dict[inter_word]:
					if word == endWord:
						return level + 1
					if word not in visited:
						visited[word] = True
						queue.append((word, level + 1))
		return 0