class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # graph = defaultdict(list)
        n = len(rooms)
        visited = [False] * n

        # for room, key in rooms:
        # graph[room].append(key)

        stack = [(0)]
        visited[0] = True

        while stack:
            room = stack.pop()
            for rKey in rooms[room]:
                if not visited[rKey]:
                    visited[rKey] = True
                    stack.append(rKey)
        print ([visit for visit in visited])
        return all(visited)
