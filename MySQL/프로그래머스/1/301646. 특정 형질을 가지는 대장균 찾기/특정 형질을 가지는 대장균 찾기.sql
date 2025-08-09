# 비트로 형질 존재 여부 확인:
# 1번 = 1 (2⁰)
# 2번 = 2 (2¹)
# 3번 = 4 (2²)
# 4번 = 8 

SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE (GENOTYPE & 2) = 0              -- 2번 형질 없음
  AND ( (GENOTYPE & 1) > 0            -- 1번 형질 있음
    OR (GENOTYPE & 4) > 0 )           -- 3번 형질 있음
;    

