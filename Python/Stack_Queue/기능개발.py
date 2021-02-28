# 문제 설명
# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

# def solution(progresses, speeds):
#     answer = []
#     days =[]
#     for i, p in enumerate(progresses):
#         count = 0
#         while p < 100:
#             p +=  speeds[i]
#             count += 1
#         days.append(count)
#     print(days)
    
#     idx = 0 
#     for i, day in enumerate(days):
#         if i == 0:
#             answer.append(1)
#         elif day > days[i-1]:
#             idx += 1
#             answer.append(1)
#         elif day <= days[i-1]:
#             answer[idx] += 1
    
#     return answer

def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0
    while len(progresses)>0:
        # speed로 days 만큼 일한 만큼을 progress에 더한 값이 100을 넘으면 pop하고, 그날 배포할 수 있는 기능 count += 1
        if (progresses[0] + days*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        # 현재 스택 top에 있는 값이 100을 넘지못하는 경우 == 기능이 완성되지 않은 경우 
        else:
            # days에 1을 더해 하루 더 일을 하고 다시 while문을 돌게함
            days += 1
            # 근데 이미 배포할 수 있는 기능이 누적된 상태 인데 현재 기능은 완성되지 않았다면 
            if count > 0 :
                # n번째 날 배포할 수 있는 기능의 개수는 answer에 append하고 count 초기화 
                answer.append(count)
                count = 0
    # 스택이 비게된 시점에 누적된 count 값을 answer에 append   
    answer.append(count)
    return answer

# https://velog.io/@joygoround/test-%EA%B8%B0%EB%8A%A5%EA%B0%9C%EB%B0%9C-python

# test case 1
print(solution([93,30,55], [1,30,5]))

# test case 2
print(solution([95,90,99,99,80,99], [1,1,1,1,1,1]))