# 문제 설명
# 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.
# 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
# 주어진 공항 수는 3개 이상 10,000개 이하입니다.
# tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
# 주어진 항공권은 모두 사용해야 합니다.
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
# 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.


def solution(tickets):
    answer = []
    ticket_graph = dict()
    # [출발지] : [도착지 리스트] 로 티켓 정리
    for ticket in tickets:
        if (ticket[0] in ticket_graph):
            ticket_graph[ticket[0]].append(ticket[1])
        else:
            ticket_graph[ticket[0]] = [ticket[1]]
    
    for starting_point in ticket_graph:
        # 역순으로 저장하는 이유: ticket_graph[starting_point]의 value인
        # [destination list]이 reverse 된 상태에서 pop을 해야 알파벳 순으로 도착지 선택 가능 
        # ex) 'SFO' : ['SFO','ATL'] -pop()-> 'SFO' : ['SFO'] , pop 된 값 = 'ATL'
        ticket_graph[starting_point].sort(reverse=True)

    # print(ticket_graph)

    stack = ["ICN"]
    # stack이 빌때까지 반복 
    while stack:
        # stack top 저장 
        top = stack[-1]
        if top not in ticket_graph or len(ticket_graph[top]) == 0:
            # top이 출발지인 티켓이 없거나 top이 출발지인 티겟이 모두 소진된 경우 
            # answer에 stack을top부터 pop해주면서 역순으로 값을 넣음 
            answer.append(stack.pop())
        else:
            # 우선 stack에 값을 넣어주고, 티켓이 모두 소진되면 stack에서 값을 pop하면서 answer에 넣어주는 것!
            # top을 출발지로 하는 도착지 리스트에서 알파벳이 가장 우선되는 도착지를 pop해서 append
            # append된 값이 새로운 stack top이 될 것임
            stack.append(ticket_graph[top].pop())
    
    print(answer)
    answer.reverse()

    return answer

# test case 1
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# ["ICN", "JFK", "HND", "IAD"]

# test case 2
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]