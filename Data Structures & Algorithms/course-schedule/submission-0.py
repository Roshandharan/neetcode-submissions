''' 
 Approach - use DFS to detect Cycles and return true or false accordingly 
 1. Create a directed graph given the list of courses 
 2. For each node, i will do a DFS and mark the path as 3 different states(visited, visiting, unvisited)
 3. Along the DFS path if will mark each visiting path as visiting, if we come across the same visiting status more than once, we know there is a cycle 
 and hece we return False
 else we will return True 
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, prereq in (prerequisites):
            graph[prereq].append(course)
        
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited]*numCourses

        def dfs(node):
            state = states[node]

            if state == visited:
                return True
            elif state == visiting:
                return False
            
            states[node] = visiting

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            states[node] = visited
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True