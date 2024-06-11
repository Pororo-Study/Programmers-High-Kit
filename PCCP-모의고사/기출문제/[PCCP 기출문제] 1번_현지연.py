def solution(bandage, health, attacks):
    max_health = health     # 최대 체력
    t = 0                   # 현재 시간
    for i in range(len(attacks)):
        # 회복시간 구하고 체력 회복하기
        recovery_t = attacks[i][0] - t - 1  # 공격시간 직전까지가 체력 회복시간
        health += (recovery_t * bandage[1]) + ((recovery_t // bandage[0]) * bandage[2])
        # 최대 체력 초과 불가
        if health > max_health:
            health = max_health
        # 공격 받기
        health -= attacks[i][1]
        if health <= 0:     # 체력이 0 이하가 되면 죽음
            return -1
        t = attacks[i][0]   # 현재 시간 변환
        
    return health           # 남은 체력 반환