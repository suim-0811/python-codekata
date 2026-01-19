# 이름이 없는 동물의 아이디
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59039
# 작성자: 김수임
# 작성일: 2026. 01. 19. 09:03:37

-- 코드를 입력하세요
SELECT
    ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID;