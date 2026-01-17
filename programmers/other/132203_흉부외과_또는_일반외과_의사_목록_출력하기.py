# 흉부외과 또는 일반외과 의사 목록 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132203
# 작성자: 김수임
# 작성일: 2026. 01. 17. 12:43:45

-- 코드를 입력하세요
SELECT
    DR_NAME,
    DR_ID,
    MCDP_CD,
    DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS 'HIRE_YMD'
FROM DOCTOR
WHERE MCDP_CD IN('CS','GS')
ORDER BY HIRE_YMD DESC,DR_NAME