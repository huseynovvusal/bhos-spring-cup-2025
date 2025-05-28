n = int(input())
weights = list(map(int, input().split()))
 
def recurse_apples(weights, i = 0, sum1 = 0, sum2 = 0):
	if i == n:
		return abs(sum2 - sum1)
 
	return min(
		recurse_apples(weights, i + 1, sum1 + weights[i], sum2),
		recurse_apples(weights, i + 1, sum1, sum2 + weights[i]),
	)
 
print(recurse_apples(weights))