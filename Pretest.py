# -*- coding: utf-8 -*-
"""Pretest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11rfJeFObYBB4d2ZjX0Bbi4UkvmGdKdET

# **均一平台pretest**

第一題
"""

print('第一題')
s = input('Write a sentence : ')
print('1(A):'+s[::-1])
s = s.split(' ')
a = []
for i in range(len(s)):
  ss = s[i]
  a.append(ss[::-1])
ans_1b = " ".join(a)
print('1(B):'+ans_1b)

"""第二題"""

print('第二題')
n = int(input('Write a number : '))
num = []
num_3 = []
num_5 = []
num_35 = []
num_a = []
out = 0
for i in range(n):
  n = i+1
  num.append(str(n))
  n3 = n%3
  n5 = n%5
  if n3 == 0 and n5 == 0:
    num_35.append(str(n))
  elif n3 == 0:
    num_3.append(str(n))
  elif n5 == 0:
    num_5.append(str(n))
  else:
    num_a.append(str(n))
    out = out+1
num = ",".join(num)
num_3 = ",".join(num_3)
num_5 = ",".join(num_5)
num_35 = ",".join(num_35)
num_aa = ",".join(num_a)
print('Input = '+str(n))
print('其中數字:'+num_3+'被剔除;')
print('還有數字:'+num_5+'被剔除;')
print('但是數字:'+num_35+'被保留;')
print('所以剩下來的數字是:'+num_aa+';')
print('因此 Output:'+str(out))

'''
第三題：
1.『鉛筆』、2.『原子筆』、3.『原子筆和鉛筆』
因袋子外面的標示都是錯的
故有兩種組合
1.tag.2、2.tag.3、3.tag.1
1.tag.3、2.tag.1、3.tag.2
只要選tag為3.的袋子就只有可能拿出鉛筆或者原子筆
如果拿出為鉛筆，那tag.鉛筆的袋子就會是原子筆，tag.原子筆的袋子就會是原子筆和鉛筆；
如果拿出為原子筆，那tag.鉛筆的袋子就會是原子筆和鉛筆，tag.原子筆的袋子就會是鉛筆。
如果是選tag為1.或2.的袋子，則會無解。
'''

'''
第四題：
用每個人所付的錢加被暗槓的錢是沒意義的
因為暗槓的錢是老闆的不是這三個人付的
270*3(三人支出) = 750（套餐）＋60（被暗槓） 
'''