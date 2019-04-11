N, M, D = map(int, input().split())
enemies = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[j] == 1:
            enemies.append([i,j])

archers = [(i,j,k) for i in range(M - 2) for j in range(i+1, M-1) for k in range(j+1, M)]
max_kill = 0
for archer in archers:
    temp_enemies = []
    enemy_num = len(enemies)
    killed_enemy = 0
    for enemy in enemies:
        temp_enemies.append(enemy.copy())
    temp_enemies.sort(key=lambda x: x[1], reverse=True)

    for enemy in temp_enemies:
        enemy.extend(list(map(lambda x: N - enemy[0] + abs(x - enemy[1]), archer)))

    sorted_enemy = []
    for k in range(2, 5):
        sorted_enemy.append(sorted([enemy[:2] + [enemy[k]] + [i] for i, enemy in enumerate(temp_enemies)],
                                   key=lambda x:x[2], reverse=True))

    t = 0
    while enemy_num:
        targets = set([])
        for sorted_enemies in sorted_enemy:
            while not temp_enemies[sorted_enemies[-1][-1]]:
                sorted_enemies.pop()
            if sorted_enemies[-1][2] - t <= D:
                target = sorted_enemies.pop()
                targets.add(target[-1])

        killed_enemy += len(targets)
        enemy_num -= len(targets)
        for target in targets:
            temp_enemies[target] = 0

        # 적들 전진
        for i, enemy in enumerate(temp_enemies):
            if enemy:
                enemy[0] += 1
                if enemy[0] == N:
                    temp_enemies[i] = 0
                    enemy_num -= 1

        t += 1

    max_kill = killed_enemy if killed_enemy > max_kill else max_kill
    if killed_enemy > max_kill:
        max_kill = killed_enemy
print(max_kill)