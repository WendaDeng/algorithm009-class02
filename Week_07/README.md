### 学习笔记

本周学习的内容包括：Trie字典树、并查集、双向BFS、高级搜索、AVL树以及红黑树。

#### Trie字典树

Trie树的实现模板

    # Python 
    class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True


#### 并查集

并查集实现模板

    # Python 
    class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True


#### 双向BFS


#### 高级搜索


#### AVL树和红黑树
AVL树和红黑树部分只讲解了理论内容，并未有相应的习题。因为这些知识点比较难，相应的代码实现也比较复杂，因此在面试中几乎不会考察代码实现，而是重点考察对于相关理论知识的掌握是否准确。

##### 二叉搜索树
二叉搜索树的查询时间复杂度只跟其子树的高度有关。如果节点加入二叉搜索树的顺序是随机的，那它的子树高度近似于 O(logn)，查询时间复杂度也是 O(logn)。但是如果加入二叉搜索树的节点它本身是有序或近似有序的，那么整个二叉搜索树会退化成一个链表，查询时间复杂度变为 O(n)，这是比较糟糕的。

##### AVL树
为了解决这个问题，计算机科学家们提出了AVL树，又称平衡二叉树。AVL树的定义要求其左右子树高差的绝对值不超过1，如果超过限制，则会进行相应的旋转操作，重新将二叉搜索树恢复到平衡的状态。AVL树根据失衡情况的不同，有四种不同的旋转操作：

1. 左旋转  对应  右右子树（即右子树的右孩子高度太高了）
2. 右旋转  对应  左左子树（即左子树的左孩子高度太高了）
3. 左右旋转（先左旋转再右旋转）  对应  左右子树（即左子树的右孩子高度太高了）
4. 右左旋转（先右旋转再左旋转）  对应  右左子树（即右子树的左孩子高度太高了）

AVL树对于平衡的要求太严格了，因此插入、删除操作较多时可能需要频繁地旋转从而影响整体的性能。为此计算机科学家们提出了一些新的平衡二叉树，放宽了左右子树高度的平衡限制，避免频繁的旋转操作。其中比较经典的就是红黑树。

##### 红黑树
红黑树是一种近似平衡的二叉搜索树，它能确保任何一个节点的左右子树高度差小于两倍。红黑树有以下几个性质：
1. 节点要么是红色，要么时候黑色
2. 根节点是黑色
3. 每个叶节点（NIL节点，空节点）也是黑色
4. 红色节点不能相邻
5. 从任一节点到其叶子节点上的所有路径包含相同数量的黑色节点

##### AVL树vs红黑树
1. AVL树查找效率高于红黑树，因为其平衡限制更加严格
2. 红黑树插入、删除节点时速度更快，而且需要的平衡操作更少，因为其平衡限制更松
3. AVL树需要在树的节点中额外维护左右子树的高度或高差信息，因此每个节点都需要一个整型数据，而红黑树只需要一个bit用了标识颜色就可以
4. 红黑树更多的被用在语言库中，比如C++中的 map, multimap, multiset等；而AVL树更多地被用在数据库中