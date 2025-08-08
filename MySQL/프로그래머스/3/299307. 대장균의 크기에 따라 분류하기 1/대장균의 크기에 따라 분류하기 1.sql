SELECT ID, CASE  -- CASE 문에는 ()를 작성하지 않음
                WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
                WHEN (SIZE_OF_COLONY > 100 AND SIZE_OF_COLONY <= 1000) THEN 'MEDIUM'
                ELSE 'HIGH'
            END AS SIZE
FROM ECOLI_DATA
;