parent = []
set_size = 0


#Union-Find 초기화 함수
def init_set(nSets) :
    global set_size, parent
    set_size = nSets
    for i in range(nSets):
        parent.append(-1)

#Union-Find의 find()함수
def find(id):               #정점 id가 속한 집합의 대표번호 탐색
    while(parent[id]>=0):   #부모가 있는 동안(-1이 아닌 동안)
        id = parent[id]     #id를 부모 id로 갱신 / 트리를 타고 올라감
    return id               #최종 id 반환 / 크리의 맨 위 노드의 id

#Union-Find의 union()함수
def union(s1, s2):
    global set_size
    parent[s1] = s2
    set_size = set_size -1
    