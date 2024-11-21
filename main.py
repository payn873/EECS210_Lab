'''
Author: Wyatt Payne
Name: main.py
Lab: Lab11
Purpose: Finds the shortest path between two vertices in a given graph using Dijkstra's Algorithm.
'''

def main():
    #Input matrix
    m = input("Enter the elements of the matrix{-1 is infinity}([1,2,3][4,5,6][7,8,9]): ")
    #Turn input into a usable matrix
    m = m.split("[")
    m.pop(0)
    #Turns each element in the matrix into a usable integer
    for i in range(len(m)):
        m[i] = m[i].split(',')
        if len(m[i]) > len(m):
            m[i].pop()
        m[i][len(m)-1] = m[i][len(m)-1][0]
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    vertex = list("abcdefghijklmnopqrstuvwxyz")
    print(tracker(len(m),vertex.index("b")))

def tracker(length, node):
    m = []
    for i in range(length):
        m.append([])
        m[i].append(-1)
        m[i].append('-')
    m[node][0] = 0
    return m

def shortestP(m, vertex, start, end):
    t = tracker(len(m), start)
    s = []
    u = []
    for i in range(len(m)):
        u.append(vertex[i])
    s.append(vertex[t.index([0,'-'])])
    while not(vertex[end] in s):
        u = [-1,'-']
        for i in range(len(t)):
            if t[i][0] > 0:
                if vertex[i] not in s:
                    if u[0] < 0 or t[i] < u[0]:
                        u = [t[i][0],vertex[i]]
        
        
main()
