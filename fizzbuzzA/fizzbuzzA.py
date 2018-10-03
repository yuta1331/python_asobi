#!/home/yuta/.pyenv/shims/python

import sys

argv = sys.argv[1:]

# parse
def parse(argv):
  dic = dict()
  for i in range(len(argv) - 1):
    elem_fb = argv[i].split(':')
    if elem_fb[0].isdigit() == False:
      print('Invalid input')
      return 1, {}, 0
    else:
      dic[int(elem_fb[0])] = elem_fb[1]

  if argv[i+1].isdigit() == False:
    print('Invalid input')
    return 1, {}, 0

  return 0, dic, argv[i+1]

# fizzbuzz
def fizzbuzz(dic, dig):
  num_list = list(dic.keys())
  max_num = 0
  for num in num_list:
    if int(dig) % int(num) == 0:
      if num > max_num:
        max_num = num

  if max_num == 0:
    return dig
  else:
    return dic[max_num]

# main
def main(argv):
  dict_fb = dict()
  errflag, dict_fb, digit = parse(argv)

  if errflag == 1:
    return
  print(fizzbuzz(dict_fb, digit))


if __name__ == '__main__':
  main(argv)
