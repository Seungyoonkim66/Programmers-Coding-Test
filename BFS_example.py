def bfs(graph, start_node):
    visit = list()
    # current_node의 인접한 노드를 담을 큐
    queue = list()

    queue.append(start_node)

    # queue가 비게되면 반복문 종료 
    while queue:
        # 큐의 head에 있는 값을 pop해서 current_node에 저장
        current_node = queue.pop(0)
        # current_node가 아직 방문하지 않은 노드라면 
        if current_node not in visit:
            # visit에 current_node 추가 
            visit.append(current_node)
            # current_node를 키로 하는 밸류 리스트 = graph(current_node)를 queue에 extend
            # 즉, current_node의 인접한 노드들을 queue에 삽입 
            queue.extend(graph[current_node])
        
        # current_node가 이미 방문한 노드라서 visit에 있는 경우 if 문을 그냥 지나침
    
    # queue가 빈 상태가 되어 while 문이 끝나면 visit을 반환 
    return visit 


if __name__ == "__main__":

    gragh = {
        'a' : ['b','c'],
        'b' : ['a','d','e'],
        'c' : ['a','f','g'],
        'd' : ['b'],
        'e' : ['b','h'],
        'f' : ['e'],
        'g': ['g'],
        'h': ['e']
    }

    print(bfs(gragh, 'a'))
