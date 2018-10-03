#!/home/yuta/.pyenv/shims/python
#-*- coding: utf-8 -*-

# http://python.rdy.jp/wiki.cgi?page=%CC%E4%C2%EA%BD%B8#p2

print("Input question")
question = input()

if question == "FtoC":
  print("Input temperature")
  temper = input()
  if temper[-1] == "F":
    trans_temper = (float(temper[0:-1]) - 32) / 1.8
    trans_temper = str(trans_temper) + "C"
  elif temper[-1] == "C":
    trans_temper = float(temper[0:-1]) * 1.8 + 32
    trans_temper = str(trans_temper) + "F"

  print(trans_temper)

elif question == "16dump":
  print("Input string")
  string = input()
  print(''.join('%02x '%ord(s) for s in string))

elif question == "PnText":
  print(open('text.txt').read().count('Python'))

elif question == "PSWD":
  from random import choice
  print("Input the length of password?")
  lenOfPasswd = int(input())
  chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/!%$&'()=~|@`[]{}*<>?_;:,."
  password = ''.join(choice(chars) for c in range(lenOfPasswd))
  print(password)

elif question == "pythond":
  def perms(in_str, out_num, now_list=[]):
    if out_num < 1:
      yield now_list
      return
    for i, s in enumerate(in_str):
      yield from perms(in_str[:i] + in_str[i+1:], out_num-1, now_list + [in_str[i]])

  print("Input string")
  in_str = input()
  print("Input number")
  out_str_num = int(input())
  if len(in_str) < out_str_num:
    print("invalid number: n is more than len of s")

  out_str_list = list()
  for i in perms(in_str, out_str_num):
    out_str_list.append(''.join(s for s in i))

  print(out_str_list)

elif question == "python":
  def perms(in_str, out_num, now_list=[]):
    if out_num < 1:
      yield now_list
      return
    for i, s in enumerate(in_str):
      yield from perms(in_str, out_num-1, now_list + [in_str[i]])

  print("Input string")
  in_str = input()
  print("Input number")
  out_str_num = int(input())
  if len(in_str) < out_str_num:
    print("invalid number: n is more than len of s")

  out_str_list = list()
  for i in perms(in_str, out_str_num):
    out_str_list.append(''.join(s for s in i))

  print(out_str_list)
