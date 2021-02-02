# 문제 설명
# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.



def solution(n, computers):
    answer = 0
    visited = [0]*n

    def dfs(computers, visited, start):
        # 시작 노드를 stack에 삽입 
        stack = [start]
        while stack:
            # stack top 에 있는 값을 cur로 저장 
            cur = stack.pop()
            # 현재 노드가 아직 방문하지 않았다면 방문 표시 
            if visited[cur] == 0:
                visited[cur] = 1
            # cur 노드와 다른 컴퓨터간의 모든 연결 관계 확인  
            for i in range(n):
                # 방문하지 않은 다른 컴퓨터와의 연결관계 (1) 이라면 stack에 push
                if computers[cur][i] == 1 and visited[i] == 0:
                    stack.append(i)
                    # 연결된 컴퓨터가 있다면 while문 처음으로 돌아가 다시 반복할 것이고, 
                    # 그렇지 않으면 stack이 비어있다는 것을 의미하므로 반복문이 종료 -> DFS 종료 

    # DFS 시작 노드 인덱스 
    i = 0
    # 모든 노드를 방문할 때까지 DFS 반복 
    while 0 in visited:
        # 시작 노드가 아직 방문하지 않았다면 DFS 돌기 
        if visited[i] == 0:
            dfs(computers,visited,i)
            # DFS 가 끝날 때 마다 네트워크 하나 방문이 완료된 것이므로 answer += 1
            answer += 1
        # 다음 인덱스를 시작 노드로 넘기는데 이미 방문된 노드라면 DFS 돌지 않고 다음으로 넘어감 
        i+=1

    return answer
    


# test case 1
print(solution(3, [[1,1,0],[1,1,0],[0,0,1]]))
print()
# test case 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


