-- 코드를 작성해주세요
SELECT ID
    FROM ECOLI_DATA
        WHERE PARENT_ID IN
            (SELECT ID
                FROM ECOLI_DATA
                    WHERE PARENT_ID IN
                        (SELECT ID
                            FROM ECOLI_DATA
                                WHERE PARENT_ID IS NULL AND ID IN
                                    (SELECT PARENT_ID
                                        FROM ECOLI_DATA
                                            WHERE PARENT_ID IS NOT NULL)))
            ORDER BY ID