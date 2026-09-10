'''
brute force - O(E.V),

My Approach - topological sort

1. building a graph from the given input, and will compute indgree for relevant nodes(courses) along the path. 
2. queue with all the nodes that are of indgree 0. 
3. visit every node which is in the queue and delete the edges(i will reduce the indgree)
4.  return output accordingly 
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque(i for i in range(numCourses) if indegree[i]==0)
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        
        return order if len(order)==numCourses else []
     