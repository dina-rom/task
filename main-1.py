lst = ['43141', '32441', '431', '4154', '43121']
ans = []
import math
for i in lst:
    a = int(math.pow(int(i), 2))
    if a%2 == 0:
        ans.append(a)

ans