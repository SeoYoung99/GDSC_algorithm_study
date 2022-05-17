def func():
    props = input()
    lists = []

    DuckIndex = -1
    seq = False
    for i in props:  # 전체문자열에 대해
        if len(lists) == 0:  # 처음이면
            if i == 'q':
                seq = True  # right sequence

                duck = []
                duck.append(i)
                lists.append(duck)
            else:  # 처음인데 q가 아니면 -1 return
                return(-1)
        else:
            if i == 'q':
                # print('q일때', lists)
                seq = True  # q는 항상 right sequence라 가정
                for j in range(len(lists)):
                    if len(lists[j]) % 5 == 0:
                      # 이미 오리가 완벽히 한번 울엇으면 그 index반환
                        DuckIndex = j
                        # print(DuckIndex)
                        break

                if DuckIndex >= 0:  # 완벽히 운 오리가 있다
                    #print('오리있음', lists)
                    lists[DuckIndex].append(i)
                    #print(DuckIndex, lists)
                    DuckIndex = -1  # 초기화

                else:  # 완벽히 운 오리가 없다 -> 새로운 오리 만들자
                    #print('오리없다', lists)

                    a = []
                    a.append(i)
                    lists.append(a)

            elif i == 'u':
                seq = False
                for j in lists:  # q가 저장된 list를 찾아서 append / 없으면 -1
                    if j[-1] == 'q':
                        seq = True
                        j.append(i)
                        break
                if seq == False:
                    return(-1)

            elif i == 'a':
                seq = False
                for j in lists:
                    if j[-1] == 'u':
                        seq = True
                        j.append(i)
                        break

                if seq == False:
                    return(-1)

            elif i == 'c':
                seq = False
                for j in lists:
                    if j[-1] == 'a':
                        seq = True
                        j.append(i)
                        break
                if seq == False:
                    return(-1)

            elif i == 'k':
                seq = False
                for j in lists:
                    if j[-1] == 'c':
                        seq = True
                        j.append(i)
                        break
                if seq == False:
                    return(-1)

            else:
                return(-1)

    # for i in lists:
    #     if len(i) % 5 == 0:
    #         n += 1
    return(len(lists))


print(func())
