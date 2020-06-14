### 学习笔记

##### 本周学习的算法包括：深度优先搜索和广度优先搜索、贪心算法以及二分查找算法。针对每一种算法，覃超老师都给出了算法模板，目的是让我们将这些固定套路牢记，然后针对具体的问题只需要对这些模板进行调整即可，这样能够提高解决问题的效率，同时也让我们心里有底。

#### 深度优先搜索（DFS）

##### 深度优先搜索使用栈，因此可以使用递归方式实现，也可以自己维护一个栈来实现。二叉树遍历中的前、中、后序遍历都属于深度优先搜索算法。

##### DFS模板（递归写法）

    visited = set() 
    def dfs(node, visited):
        if node in visited: # terminator
            # already visited 
            return 
        visited.add(node) 
        # process current node here. 
        ...
        for next_node in node.children(): 
            if next_node not in visited: 
                dfs(next_node, visited)

这个递归模板跟之前的递归模板的套路是一致的，包含了标准递归套路4个步骤中前3个必要步骤，即：

    1.terminator
    2.process current level logic
    3.drill down
    4.reverse state

有区别的地方在于，为了防止重复遍历某个节点，甚至陷入死循环，这里需要维护一个额外的 `visited` 集合，用于保存已经被访问过的节点。

##### DFS模板（非递归写法）

    def DFS(self, tree): 
        if tree.root is None: 
            return [] 
        visited, stack = [], [tree.root]
        while stack: 
            node = stack.pop() 
            visited.add(node)
            process (node) 
            nodes = generate_related_nodes(node) 
            stack.push(nodes) 
        # other processing work 
        ...

非递归写法需要自己维护一个栈。


#### 广度优先搜索（BFS）

##### 广度优先搜索使用一个队列实现。遍历过程中逐一将节点放入队列中。然后取出节点访问时，将节点的相邻节点加入队列中。BFS在二叉树中就是层次遍历。

    # Python
    def BFS(graph, start, end):
        visited = set()
        queue = [] 
        queue.append([start]) 
        while queue: 
            node = queue.pop() 
            visited.add(node)
            process(node) 
            nodes = generate_related_nodes(node) 
            queue.push(nodes)
        # other processing work 
        ...

#### 贪心算法

##### 贪心算法也是已经没有学明白的一种高级算法，它的优点是能够快速地找到局部最优的答案。而且能想到的话，实现很简单，时间复杂度往往也是较优的。但它的缺点是往往不能达到全局最优。因此，贪心算法通常需要和其他算法结合起来使用，在某些步骤使用贪心算法。在能够适用贪心的场景中，贪心往往是最佳算法。

##### 贪心算法跟动态规划相比，区别在于它不保存中间结果，因而无法回溯，不能保证总是达到最优解。

#### 二分查找
##### 二分查找的思路比较简单，应用也非常广泛。要掌握二分查找，关键就是要处理好各种边界。

##### 使用二分查找的前提
    1.目标函数单调性（单调递增或递减）

    2.存在上下界（bounded）

    3.能够通过索引访问（index accessible）

##### 二分查找模板
    # Python
    left, right = 0, len(array) - 1 
    while left <= right: 
          mid = (left + right) / 2 
          if array[mid] == target: 
                # find the target!! 
                break or return result 
          elif array[mid] < target: 
                left = mid + 1 
          else: 
                right = mid - 1
             
##### 实际用有很多问题是二分查找的变体，乍一看无法用二分查找进行解决，但是如果仔细观察，往往能够发现规律。解决这些问题往往需要对基本的二分查找模板进行改动，比如"旋转数组"问题中就需要修改条件判断。

##### 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

    class Solution:
        def findMin(self, nums: List[int]) -> int:
            if len(nums) == 1:  return nums[0]
            lo, hi = 0, len(nums) - 1
            if nums[hi] > nums[lo]: return nums[lo]
    
            while lo < hi:
                mid = (lo + hi) // 2
                
                # 判断 mid 附近是否是变动点，即最小值所在点
                if nums[mid] > nums[mid + 1]:   
                    return nums[mid + 1]
                if nums[mid - 1] > nums[mid]:
                    return nums[mid]
                    
                if nums[lo] < nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1