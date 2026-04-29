class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        V=[0]*numCourses
        PV=[0]*numCourses
        graph=[[] for i in range(numCourses)]
        for c,d in prerequisites:
            graph[d].append(c)
        res=[]
        def dfs(node):
            V[node]=1
            PV[node]=1
            for nei in graph[node]:
                if V[nei]==0:
                    if dfs(nei):
                        return True
                elif PV[nei]==1:
                    return True
            res.append(node)
            PV[node]=0
            return False
        for i in range(numCourses):
            if V[i]==0:
                if dfs(i):
                    return []
        return res[::-1]