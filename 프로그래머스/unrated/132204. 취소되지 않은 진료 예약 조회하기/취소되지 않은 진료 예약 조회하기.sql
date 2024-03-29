-- 62. 취소되지 않은 진료 예약 조회하기 Level 4

SELECT C.APNT_NO, A.PT_NAME, A.PT_NO, C.MCDP_CD, B.DR_NAME, C.APNT_YMD
FROM APPOINTMENT C JOIN PATIENT A ON C.PT_NO = A.PT_NO JOIN DOCTOR B ON C.MDDR_ID = B.DR_ID
WHERE C.APNT_YMD LIKE '2022-04-13%' AND C.APNT_CNCL_YN = 'N'
ORDER BY C.APNT_YMD