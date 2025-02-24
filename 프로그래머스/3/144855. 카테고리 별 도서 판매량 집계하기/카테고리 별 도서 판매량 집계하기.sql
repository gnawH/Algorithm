-- 코드를 입력하세요
SELECT A.CATEGORY, SUM(SALES) AS TOTAL_SALES
    FROM BOOK_SALES B
        JOIN BOOK A
            ON A.BOOK_ID = B.BOOK_ID
                WHERE MONTH(B.SALES_DATE) = 1
                    GROUP BY A.CATEGORY
                        ORDER BY A.CATEGORY