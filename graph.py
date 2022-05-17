# def HideandSeek(n,k):
# 	if n+1 == k or n-1 == k or 2*n == k:
# 		return
# 	else:
# 		HideandSeek(n+1,k)
# 		HideandSeek(n-1,k)
# 		HideandSeek(2*n,k)

# HideandSeek(5,17)

from collections import deque


def HideandSeek(n, k):
    if n < 0 or n > 100000 or k < 0 or k > 100000:
        return None
    else:
        queue = deque([[0, n]])
        shortcut = 1000000
        result = []
        while queue:  # 큐가 빌 때까지 반복
            v = queue.popleft()  # 원소 하나 뽑기
            if v[0] > shortcut:
                break
            else:
                if v[1] == k:
                    shortcut = v[0]
                    result.append(v)
                else:
                    h = v[0]+1
                    queue.append([h, v[1]+1])
                    queue.append([h, v[1]-1])
                    queue.append([h, 2*v[1]])
        print(result[0][0])
        print(len(result))
        print(result)


n, k = map(int, input().split())
HideandSeek(n, k)
