# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

# def solution(prices):
#     answer = []

#     k = 0
#     for i in prices:
#         diff = 0
#         for j in prices[k+1:len(prices)]:
#             if i > j:
#                 diff += 1
#                 break
#             else:
#                 diff += 1
#         answer.append(diff)
#         k+=1

#     return answer

# https://gurumee92.tistory.com/170
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i-top
        stack.append(i)

    while stack:
        top = stack.pop()
        answer[top] = n-1-top
    
    return answer



# test case 1
prices = [1,2,3,2,3]
# print(solution(prices))
# [4,3,1,1,0]

# test case
prices = [6,5,3,2,5,1,3,6]
print(solution(prices))
# [1,1,1,2,1,2,1,0]
