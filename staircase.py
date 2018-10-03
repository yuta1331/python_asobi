#!/home/yuta/.pyenv/shims/python

def NewStair(n):
  stairs = {1: 1, 2: 2, 3: 4} # {step_num, total}
  if n == 1: return 1
  if n == 2: return 2
  if n == 3: return 4
  else:
    for i in range(4, n+1):
      stairs[i] = stairs[i-1] + stairs[i-2] + stairs[i-3]
    return stairs[n]

if __name__== '__main__':
  for i in range(100):
    print(str(NewStair(i+1)))

'''
#n = int(input())

def saiki_step(nokori):
  if nokori <= 1: return 1
  if nokori == 2: return 2
  if nokori == 3: return 4
  return (saiki_step(nokori-1) + saiki_step(nokori-2) + saiki_step(nokori-3))

#print(str(saiki_step(n)))

for i in range(30):
  print(str(saiki_step(i)))
'''
