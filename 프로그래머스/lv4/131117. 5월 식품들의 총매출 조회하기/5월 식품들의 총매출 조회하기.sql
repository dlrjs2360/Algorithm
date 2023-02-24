-- 코드를 입력하세요
SELECT A.PRODUCT_ID, A.PRODUCT_NAME, (A.PRICE * B.TOTAL_AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT A
JOIN (
    SELECT PRODUCT_ID, PRODUCE_DATE, AMOUNT, SUM(AMOUNT) AS TOTAL_AMOUNT
    FROM FOOD_ORDER
    WHERE DATE_FORMAT(PRODUCE_DATE, '%m') = 5 AND DATE_FORMAT(PRODUCE_DATE,'%Y') = 2022
    GROUP BY PRODUCT_ID
) B
ON A.PRODUCT_ID = B.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID