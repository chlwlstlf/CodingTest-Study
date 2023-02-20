-- 45. 루시와 엘라 찾기 Level 2
# . : 문자 하나를 나타낸다.
# * : 앞에 나온 문자의 0개 이상 반복을 나타낸다.
# ^ : 문자열의 처음을 나타낸다.
# $ : 문자열의 끝을 나타낸다.
# [.] : 괄호 안의 문자열 일치를 확인한다.
# {.} : 반복을 나타낸다.
# | : or 를 나타낸다.

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME REGEXP '^(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty)$'
ORDER BY ANIMAL_ID