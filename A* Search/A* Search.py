# Set No: G3


from math import *
from queue import PriorityQueue

def calculateDistance(x1, y1, x2, y2):
  xDis = (x2 - x1)
  yDis = (y2 - y1)
  finalDis = sqrt((xDis * xDis) + (yDis * yDis))
  return finalDis


src = 12
dist = 5

G = [
     [(2, 615), (5, 622), (7, 636)], # 0
     [(4, 689), (5, 667)], # 1
     [(0, 615), (3, 626), (6, 664), (7, 655), (10, 650)],#2
     [(2, 626), (6, 655), (10, 625), (11, 644), (12, 653)],#3
     [(1, 689), (5, 689), (9, 665), (10, 652)], #4
     [(0, 622), (1, 667), (4, 689)], #5
     [(2, 664), (3, 655), (7, 687), (12, 638)],#6
     [(0, 636), (2, 655), (6, 687)],  #7
     [(9, 659), (10, 643), (11, 635)],  #8
     [(4, 665), (8, 659), (10, 628)], #9
     [(2, 650), (3, 625), (4, 652), (8, 643), (9, 628)], #10
     [(3, 644), (8, 635), (12, 656)],  #11
     [(3, 653), (6, 638), (11, 656)] #12
]


pos = [
       (401, 161), 
       (334, 401.1), 
       (268.5, 168), 
       (142.5, 152.6),
       (273, 279.4),
       (401.1, 291.6),
       (200, 44.2),
       (344.5, 44.2),
       (44.2, 386.1),
       (195.1, 401.1),
       (147.3, 282.4),
       (44.2, 229.2),
       (44.2, 63.5)
]


n = len(G) 
p = [-1] * n



gn = calculateDistance(pos[src][0], pos[src][1], pos[dist][0], pos[dist][1])
fn = gn

pq = PriorityQueue()
pq.put((fn, src, gn, src))

while not pq.empty():
  (fn, n, gn, parent) = pq.get()

  currentNode = n
  if currentNode == dist:
    p[currentNode] = parent
    break
  if p[currentNode] != -1:
    continue
  
  p[currentNode] = parent
  for v in G[currentNode]:
    gv = gn + v[1]
    n = v[0]
    hv = calculateDistance(pos[n][0], pos[n][1], pos[dist][0], pos[dist][1])
    fv = gv + hv
    pq.put((fv, n, gv, currentNode))
    

ans = []

i = dist
ans.append(dist)
while (i != p[i]):
  ans.insert(0, p[i])
  i = p[i]

for i in range(len(ans)):
  if (i == len(ans) - 1):
    print(ans[i])
  else:
    print(ans[i], end=" -> ")
