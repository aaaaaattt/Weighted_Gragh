#dist가 최소인 정점 탐색 함수

INF = 999 #가장 큰 가중치
def getMinVertext(dist,selected) :
    minv = 0
    mindist = INF
    for v in range(len(dist)) :
        if not selected[v] and dist[v]<mindist :
            mindist = dist[v]
            minv = v
    return minv

def MSTPrim(vertex,adj) :
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0

    for i in range(vsize) :
        u = getMinVertext(dist, selected)
        selected[u] = True
        print(vertex[u], end=' ')


        for v in range(vsize) :
            if(adj[u][v] != None):
                if selected[v] == False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]
        print()