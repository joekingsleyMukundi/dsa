import math
results = []
def solution (n):
    result = math.isqrt(n)
    sqresult = result * result
    results.append(sqresult)
    if sqresult == n:
        return
    remResult = n-sqresult
    solution(remResult)

res = solution(12)
print(results)