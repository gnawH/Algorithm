-- 코드를 작성해주세요
SELECT ID,
    CASE WHEN A.PR >= 0.75 THEN 'CRITICAL'
        WHEN A.PR >= 0.5 THEN 'HIGH'
        WHEN A.PR >= 0.25 THEN 'MEDIUM'
        WHEN A.PR < 0.25 THEN 'LOW' END AS COLONY_NAME
    FROM (SELECT ID, PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY) AS PR
    FROM ECOLI_DATA) A
    ORDER BY ID