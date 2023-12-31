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


def MSTKruskal(vertex, adj): #매개변수 : 정점리스트, 인접행렬
    vsize = len(vertex)      #정점의 개수
    init_set(vsize)          #정점 집합 초기화
    eList = []               #간선 리스트

    for i in range(vsize-1) :         
        for j in range(i+1, vsize) :
            if adj[i][j] != None :
                eList.append((i,j,adj[i][j]))

    #간선 리스트를 가중치의 내림차순으로 정렬:람다 함수 사용
    eList.sort(key = lambda e : e[2], reverse=True)

    edgeAccepted = 0
    while(edgeAccepted < vsize - 1):
        e = eList.pop()
        uset = find(e[0])
        vset = find(e[1])

        if uset != vset :
            print("간선 추가 : (%s,%s,%d)" %
                  (vertex[e[0]],vertex[e[1]],e[2]))
            union(uset,vset)
            edgeAccepted += 1