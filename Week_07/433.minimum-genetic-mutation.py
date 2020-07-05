class Solution:
	def minMutation(self, start: str, end: str, bank: List[str]) -> int:
		if not bank or not start or not end or end not in bank:
			return -1
		l = len(start)
		all_comb_dict = defaultdict(list)
		for gene in bank:
			for i in range(l):
				all_comb_dict[gene[:i] + '*' + gene[i + 1:]].append(gene)

		queue = [(start, 0)]
		visited = {start: True}
		while queue:
			cur_gene, level = queue.pop(0)
			for i in range(l):
				inter_gene = cur_gene[:i] + '*' + cur_gene[i + 1:]
				for gene in all_comb_dict[inter_gene]:
					if end == gene:
						return level + 1
					if gene not in visited:
						visited[gene] = True
						queue.append((gene, level + 1))
		return -1