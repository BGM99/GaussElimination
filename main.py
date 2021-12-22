import numpy as np

#    x1 x2 x3 x4 = c
m = np.array(
      [[0.2, 0.5, 0.6, 25], 
      [0.4, 0.5, 0.2, 40],
      [0.4, 0, 0.2, 35]])

m = m.astype('float64')

#get zero fields / build triangular shape
d = m.shape[0] - 1
e = 1
zf = []

for x in range(m.shape[0] - 1):
  for y in range(d):
    zf.append([y + e, x])
  d -= 1
  e += 1

print("--Begin--")

for i in range(len(zf)):
  br = zf[i][1] #base row
  n1 = m[zf[i][0], br]
  n2 = m[br, br]

  tmp = np.array(m[br])
  tmp = tmp.astype('float64')

  factor = n1 / n2

  for x in range(tmp.size):
    tmp[x] = tmp[x] * factor

  m[zf[i][0]] = m[zf[i][0]] - tmp
  
  print(m)
  print("Step ", i + 1)