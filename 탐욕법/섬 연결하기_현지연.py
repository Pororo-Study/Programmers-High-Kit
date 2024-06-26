# 크루스칼 알고리즘
# 최소 신장 트리 알고리즘

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
# 두 원소가 속한 집합을 합치기
def connect(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0  # 다리 건설 최소 비용
    
    # 부모 배열 초기화
    parent = [0] * n
    # 부모를 자기 자신으로 초기화
    for i in range(n):
        parent[i] = i
    
    # 비용 순으로 정렬
    costs.sort(key=lambda x: x[2])
    
    # 다리를 하나씩 확인하며 사이클이 발생하지 않는 경우에만 집합에 포함
    for a, b, c in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            connect(parent, a, b)
            answer += c
    
    return answer