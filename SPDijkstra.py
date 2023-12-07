#최단 정점 선택 함수
INF = 9999
def choose_vertext(dist, found) :
    min = INF
    minpos = -1
    for i in range(len(dist)) :
        if dist[i]<min and found[i]==False:
            min - dist[i]
            minpos = i
        return minpos           #최소 dist 정점의 인덱스 반환
    

def shortest_path_dijkstra(vtx, adj, start) :
    vsize = len(vtx)
    dist = list(adj[start])         #dist 배열 생성 및 초기화
    path = [start] * vsize          #path 배열 생성 및 초기화
    found= [False] * vsize          #found 배영ㄹ 생성 및 초기화
    found[start] = True             #시작정점 : 이미 찾아짐
    dist[start] = 0

    for i in range(vsize) :
        print("Step%2d; "%(i+1), dist)
        u = choose_vertext(dist,found)
        found[u] = True

        for w in range(vsize):
            if not found[w] :
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u
        return path