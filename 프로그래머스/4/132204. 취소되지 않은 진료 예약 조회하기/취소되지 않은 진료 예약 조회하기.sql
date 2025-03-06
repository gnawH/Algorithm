-- 코드를 입력하세요
SELECT APNT_NO, PT_NAME, A.PT_NO, B.MCDP_CD, C.DR_NAME, B.APNT_YMD
    FROM PATIENT A
    JOIN APPOINTMENT B ON A.PT_NO = B.PT_NO
    JOIN DOCTOR C ON B.MDDR_ID = C.DR_ID AND B.MCDP_CD = C.MCDP_CD
        WHERE APNT_CNCL_YN = 'N' AND B.MCDP_CD = 'CS' AND APNT_YMD LIKE '2022-04-13%' 
            ORDER BY B.APNT_YMD

# SELECT APNT_NO, PT_NAME, A.PT_NO, B.MCDP_CD, DR_NAME, APNT_YMD
#     FROM PATIENT A
#     JOIN APPOINTMENT B ON A.PT_NO = B.PT_NO
#     JOIN DOCTOR C ON B.MDDR_ID = C.DR_ID AND B.MCDP_CD = C.MCDP_CD
#         WHERE APNT_CNCL_YMD NOT LIKE '2022-04-13%' AND B.MCDP_CD = 'CS'
#         GROUP BY APNT_NO
#             ORDER BY B.APNT_YMD