r = [1, 2, 4, 9, 3, 4, 1]
k = 2
n = 3
maxn = list()
for i in range(len(r)-2):
    x = r[i:i+k]
    maxn.append(max(x))
maxn = sorted(maxn)
res = max(maxn[0:n])
print(res)
# https://leetcode.com/discuss/interview-question/334191