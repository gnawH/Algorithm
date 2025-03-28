-- 코드를 입력하세요
# SELECT *
#     FROM FIRST_HALF A
#     JOIN JULY B ON A.FLAVOR = B.FLAVOR


SELECT A.FLAVOR
    FROM 
        (SELECT FLAVOR, TOTAL_ORDER
            FROM FIRST_HALF
                GROUP BY FLAVOR) A
    JOIN
        (SELECT FLAVOR, TOTAL_ORDER
            FROM JULY
                GROUP BY SHIPMENT_ID) B ON A.FLAVOR = B.FLAVOR
        GROUP BY A.FLAVOR
            ORDER BY (SUM(A.TOTAL_ORDER) + SUM(B.TOTAL_ORDER)) DESC LIMIT 3;