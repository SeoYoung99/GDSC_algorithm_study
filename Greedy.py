n, m, k = map(int, input().split())
# n =여자 m=남자 k=인턴십
team = 0
if n >= 2*m:  # 남자 수에 맞춰서 팀 구성
    team = m
    n = n-2*m
    if n < k:  # 남은 사람으로 인턴십 인원을 채울 수 없으면
        k = k-n
        team = team - (k//3) - 1
else:  # 여자 수 기준
    team = n//2
    m = m - team
    if m < k:  # 남은 사람으로 인턴십 인원을 채울 수 없으면
        k = k-m
        team = team - (k//3) - 1

print(team)
