-- 46. 조건별로 분류하여 주문상태 출력하기 Level 3

SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
IF(OUT_DATE IS NULL, '출고미정', IF(OUT_DATE>'2022-05-01', '출고대기', '출고완료')) AS 출고여부
FROM FOOD_ORDER