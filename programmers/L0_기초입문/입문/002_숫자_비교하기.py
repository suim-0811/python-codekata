# 숫자 비교하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120807
# 알고리즘: 기초
# 작성자: 김수임
# 작성일: 2026. 01. 19. 09:22:31

def solution(num1, num2):
    if num1 == num2:
        return 1
    else :
        return -1

print(solution(2, 3))
print(solution(11, 11))
print(solution(7, 99));