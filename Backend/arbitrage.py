from binance import *

price_list = getDataFromAPI()

def dijkstrasAlgorithm(price_list,dist,relaxer):
    # Write your code here.
    flag = 0
    visited = set()
    while len(visited)<len(price_list):
        source = getMinDistVertex(dist, visited)
        if dist[source]==float("inf"):
            break
        visited.add(source)
        for dest,weight in price_list[source]:
            if dest in price_list and dest not in visited and dist[dest]>weight+dist[source]:
                flag = 1
                dist[dest] = weight+dist[source]
                relaxer[dest] = source
#     print(dist)
    return flag


def getMinDistVertex(dist,visited):
    minDist = float("inf")
    minDistVertex = -1
    for vertex in dist.keys():
        # print(dist[vertex])
        if vertex not in visited and dist[vertex]<=minDist:
            minDist = dist[vertex]
            minDistVertex = vertex

    return minDistVertex

def getNegativeCycle(price_list,dist,relaxer):
    flag = 0
    visited = set()
    print_cycle = []
    while len(visited)<len(price_list):
        source = getMinDistVertex(dist, visited)
        if dist[source]==float("inf"):
            break
        visited.add(source)

        for dest,weight in price_list[source]:
            if dest in price_list and dest not in visited and dist[dest]>weight+dist[source]:
                flag = 1
                dist[dest] = weight+dist[source]
                print_cycle = [dest, source]
# Start from the source and go backwards until you see the source vertex again or any vertex that already exists in print_cycle array
                while relaxer[source] not in  print_cycle:
                    print_cycle.append(relaxer[source])
                    source = relaxer[source]
                print_cycle.append(relaxer[source])


    return [flag,print_cycle]
#   

def bellmanFord(price_list):
    dist = {}
    for key in price_list.keys():
        dist[key] = float('inf')
    source = 'BTC'    
    flag = 0
    relaxer = {}   
    for index in range(len(price_list)-1):       
        dist[source] = 0
        dijkstrasAlgorithm(price_list,dist,relaxer)
    # print(dist)  
    # print("====================")
    flag,cycle = getNegativeCycle(price_list,dist,relaxer)  
    # print(dist)
    if flag==1:
        print("Arbitrage Detected")
        print("Arbitrage: "+'->'.join(reversed(cycle)))

    else:
        print("No Arbitrage at the moment")

bellmanFord(price_list)    
        