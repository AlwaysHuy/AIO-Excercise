# -*- coding: utf-8 -*-
"""Week2-homework.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aItkRjA5ZSsYJMEcUuPYxvVOv-waHq9l
"""

def max_kernel(num_list,k):
  result = []
  data = []
  len_list = len(num_list)
  for i in range(len_list - k + 1):
    data = (num_list[i:i+k])
    print(data)
    result.append(max(data))
  return result
assert max_kernel ([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
max_kernel(num_list,3)

#Tạo hàm để thực thi
def character_count(word):
  count = {}
  for char in word:
    if char not in count:
      count[char] = 1
    else:
      count[char] += 1
  return count
assert character_count('Baby') == {'B':1, 'a': 1 , 'b': 1 , 'y': 1 }
print(sorted(character_count('smiles').items()))

# câu 3
!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
file_path = 'P1_data.txt'
with open(file_path , 'r') as f:
  data = f.read()
def data_preprocessing(data):
  data = data.lower()
  data = data.replace('\n',' ')
  words = data.split()
  result = {}
  for word in words:
    if word not in result:
      result[word] = 1
    else:
      result[word] += 1
  return result
word_count = data_preprocessing(data)
def get_word_count(word,word_count):
  if word in word_count:
    return word_count[word]
  else:
    return 0
get_word_count('man',word_count)

# câu 5
def check_the_number(N):
  list_of_numbers=[]
  result = ''
  for i in range(1,5):
    list_of_numbers.append(i)
  if N in list_of_numbers:
    result = 'True'
  else:
    result = 'FALSE'
  return result
N = 7
assert check_the_number(N) == 'FALSE'
N = 2
result = check_the_number(N)
print(result)

# câu 6
def my_function(data , max , min ) :
  result = []
  for i in data:
    if i < min :
      result.append(min)
    elif i > max:
      result.append(max)
    else:
      result.append(i)
  return result
my_list = [5,2,5,0,1]
max = 1
min = 0
assert my_function(my_list,max,min) == [1,1,1,0,1]
my_list = [10,2,5,0,1]
max = 2
min = 1
print(my_function(max = max,min=min,data = my_list))

# câu 7
def b_function(x,y):
  x.extend(y)
  return x
list_num1 = ['a', 2 ,5]
list_num2 = [1,1]
list_num3 = [0,0]
assert b_function(list_num1,b_function(list_num2,list_num3)) == ['a', 2 ,5, 1, 1, 0, 0]

list_num1 = [1 , 2]
list_num2 = [3 , 4]
list_num3 = [0 , 0]
print(b_function(list_num1,b_function(list_num2,list_num3)))

# câu 8
def c_function(n):
  return min(n)

my_list = [1,22,93,-100]
assert c_function(my_list) == -100
my_list = [1,2,3,-1]
print(c_function(my_list))

# câu 9
def d_function(n):
  return max(n)
my_list = [1001,9,100,0]
assert d_function(my_list) == 1001
my_list = [1,9,9,0]
print(d_function(my_list))

# câu 10
def e_function(integers, number = 1 ):
  for i in range(len(integers)) :
    if integers[i] == number:
      return True
    else :
      return False
my_list = [1.3,9,4]
assert e_function(my_list,-1) == False
my_list = [1,9,4]
print(e_function(my_list,2))

# Câu 11
def f_function(list_nums =[0,1,2]):
  var = 0
  for i in list_nums:
    var += i
  return var/len(list_nums)
assert f_function([4,6,8]) == 6
print(f_function())

# Câu 12
def g_function(data):
  var = []
  for i in data:
      if i % 3 == 0:
          var.append(i)
  return var

assert g_function([3 , 9 , 4, 5 , 1]) == [3 , 9 ]
print(g_function([1,2,3,5,6]))

# Câu 13
def h_function(y):
  var = 1
  while (y > 1 ) :
    var *= y
    y -= 1
  return var
assert h_function(8) == 40320
print(h_function(4))

# Câu 14
def j_function(x):
  return x[::-1]
x = 'I can do it'
assert j_function(x) == 'ti od nac I'

x = ' apricot'
print(j_function(x))

# câu 15
def function_helper(x):
  if x > 0:
    return 'T'
  else :
    return 'N'
def k_function(data):
  res = [function_helper(x) for x in data]
  return res
data = [ 10, 0 , -10 , -1]
assert k_function(data) == ['T', 'N', 'N', 'N']

data = [ 2, 3 ,5 ,-1 ]
print(k_function(data))

# Câu 16
def function_helper_2(x, data):
  for i in data :
    if x ==i :
      return 0
  return 1
def l_function(data):
  res = []
  for i in data :
    if function_helper_2(i,res):
      res.append(i)
  return res
lst = [10, 10, 9, 7 ,7]
assert l_function(lst) == [10, 9, 7]

lst = [9,9,8,1,1]
print(l_function(lst))

# Câu 4
def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Xóa
                               dp[i][j - 1] + 1,    # Thêm
                               dp[i - 1][j - 1] + 1) # Thay thế

    return dp[m][n]

assert levenshtein_distance('hi','hello') == 4.0
print(levenshtein_distance('hola','hello'))

