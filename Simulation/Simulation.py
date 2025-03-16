n, m = map(int, input().split())
print(n, m)

r, c, d = map(int, input().split())
print(r, c, d)

world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

tracking = [[False] * m for _ in range(n)]
print(tracking)

print(world)

dr = [-1, 0, 1, 0]  # 북, 동, 남, 서
dc = [0, 1, 0, -1]

world[r][c] = 2  # c첫번째 좌표를 방문 처리
count = 1
seaNotgo = 0

while True:

    # 방향 결정
    d = (d - 1) % 4
    nr = r + dr[d]
    nc = c + dc[d]

    if 0 <= nr < n and 0 <= nc < m:
        if world[nr][nc] == 0 and tracking[nr][nc] == False:
            tracking[nr][nc] = True  # 방문 처리
            r = nr
            c = nc
            count += 1
            seaNotgo = 0
            continue

    seaNotgo += 1

    if seaNotgo == 4:
        nr = r - dr[d]
        nc = c - dc[d]

        if 0 <= nr < n and 0 <= nc < m:
            if world[nr][nc] == 1:
                break

            else:
                r = nr
                c = nc
                seaNotgo = 0
        else:
            break

print(count)


# print(r ,c, seaNotgo)


# print("deguging >>> 서쪽으로 한 칸 이동? ", d, nr, nc)  # 3 1 2
# print("debug >>>> 이동 후 world 맵의 바다 or 방문 상태" ,world[nr][nc])   # 0

# break
