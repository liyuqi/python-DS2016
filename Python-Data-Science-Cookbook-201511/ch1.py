# -*- coding: utf-8 -*-

''' 1. python for Data Science p.61'''

''' 1.1 Using dictionary objects'''
''' 1.1 使用 Dict 物件'''

### 1.1-1 Load a var with sentences
sentence = "Peter Piper picked a peck of pickled peppers A peck of pickled" \
           "Peter Piper picked a peck of pickled peppers A peck of pickled" \
           "peppers Wheres the peck of pickled peppers Peter Piper picked"

### 1.1-2 initialize a dict obj
word_dict = {}

### 1.1-C1 perform the word count
# for word in sentence.split():
#     if word not in word_dict:
#         word_dict[word]=1
#     else:
#         word_dict[word]+=1
### 1.1-1.4 print the word_dict
# print(word_dict)
# word_dict_print = {'a': 2, 'A': 2, 'Peter': 2, 'of': 5, 'Piper': 3, 'pickled': 3, 'pickledpeppers': 1, 'pickledPeter': 1, 'picked': 3, 'peppers': 3, 'the': 1, 'peck': 5, 'Wheres': 1}


## 1.1-C2 perform the word count
for word in sentence.split():
    word_dict.setdefault(word,0)
    word_dict[word]+=1

# print(word_dict)
# word_dict_print = {'a': 2, 'A': 2, 'Peter': 2, 'of': 5, 'Piper': 3, 'pickled': 3, 'pickledpeppers': 1, 'pickledPeter': 1, 'picked': 3, 'peppers': 3, 'the': 1, 'peck': 5, 'Wheres': 1}


## 1.1-C3 perform the word count   === python 2.5 ===
# from collections import defaultdict
# word_dict = defaultdict(int)
#
# for word in sentence.split():
#     word_dict[word]+=1
# print(word_dict)
# defaultdict(<type 'int'>, {'a': 2, 'A': 2, 'Peter': 2, 'of': 5, 'Piper': 3, 'pickled': 3, 'pickledpeppers': 1, 'pickledPeter': 1, 'picked': 3, 'peppers': 3, 'the': 1, 'peck': 5, 'Wheres': 1})


## 1.1-C4 perform the word count   === python 2.5 ===
# from collections import Counter
# words = sentence.split()
# word_count = Counter(words)
#
# print(word_count)
# Counter({'of': 5, 'peck': 5, 'Piper': 3, 'pickled': 3, 'picked': 3, 'peppers': 3, 'a': 2, 'A': 2, 'Peter': 2, 'pickledpeppers': 1, 'pickledPeter': 1, 'the': 1, 'Wheres': 1})


## 1.1-5 Ref
# https://docs.python.org/2/reference/datamodel.html
# https://docs.python.org/2/library/collections.html#collections.OrderedDict
# https://docs.python.org/2/tutorial/datastructures.html#dictionaries
# https://docs.python.org/2/library/json.html
# https://docs.python.org/2/library/collections.html#collections.Counter


''' 1.2 Working with a dictionary of dictionaries p.72'''
## 1.2- Ref:
# Mapping words to Properties using Python Dictionaries
# NLTK lib => http://www.nltk.org/book/ch05.html

from collections import defaultdict

user_movie_rating = defaultdict(lambda :defaultdict(int))
## initialize ratings for Alice
user_movie_rating["Alice"]["LOR1"] = 4
user_movie_rating["Alice"]["LOR2"] = 5
user_movie_rating["Alice"]["LOR3"] = 3
user_movie_rating["Alice"]["SW1"] = 5
user_movie_rating["Alice"]["SW2"] = 3
# print'user_movie_rating: '+user_movie_rating




''' 1.3 Working with tuples p.78'''
## ops
# in, not in
# compare, cpmcate, slice, index
# min(), max()

## 1.3-1 ways of creating a tuple
a_tuple = (1,2,'a')
b_tuple = 1,2,'c'

## 1.3-2 accessing elem of a tuple through index
print 'b_tuple[0]: ', b_tuple[0]    # 1
print 'b_tuple[-1]: ',b_tuple[-1]   # c

## 1.3-3 no possible to change the value of tuple item (immutable)
try:
    b_tuple[0] = 20
except:
    print ("tuple immutable")

## 1.3-4 through tuples are immutable, but tuple elem can be mutable obj
c_tuple = (1,2,[10,20,30])
print 'c_tuple: ', c_tuple

c_tuple[2][0]=100
print 'c_tuple: ', c_tuple

## 1.3-5 tuple no extend, but can concate
print 'a_tuple + b_tuple'
print a_tuple+b_tuple

## 1.3-6 tuple slice
a = (1,2,3,4,5,6,7,8,9,10)
print "a[1:]   : ", a[1:]         # (2, 3, 4, 5, 6, 7, 8, 9, 10)
print "a[1:3]  : ", a[1:3]        # (2, 3)
print "a[1:6:2]: ", a[1:6:2]      # (2, 4, 6) from 1 to 6 step 2
print "a[:-1]  : ", a[:-1]        # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print "a[::-1] : ", a[::-1]       #*(10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

## 1.3-7 min() max()
print "min(a)  : ", min(a)        # 1
print "max(a)  : ", max(a)        # 10

## 1.3-8 lookup element
if 99 in a:
    print "Element 1 is in tuple a"
else:
    print "Element 99 not in tuple a"

from collections import namedtuple

vector = namedtuple("Dimension",'x y z')
vec1 = vector(1,1,1)
vec2 = vector(1,0,1)

mahattanDistance = abs(vec1.x - vec2.x) + abs(vec1.y - vec2.y) + abs(vec1.z - vec2.z)

print "Manhatatan Distance between vectors = ", mahattanDistance

''' 1.4 Using sets p.87'''
## 1.4-1 init 2 sentences
st1 = "dogs chase cats"
st2 = "dogs hate cats"

## 1.4-2 create set of 2 words from strings
st1_words = set(st1.split())
st2_words = set(st2.split())

## 1.4-3 find unique words in set, vocab size
st1num = len(st1_words)
st2num = len(st2_words)

## 1.4-4 find list of common word between 2 sets
cmn_words = st1_words.intersection(st2_words)
no_cmd_words = len(st1_words.intersection(st2_words))

## 1.4-5 find list of unique word
unq_words = st1_words.union(st2_words)
no_unq_words = len(st1_words.union(st2_words))

## 1.4-6 Jaccard similar
similarity = no_cmd_words / (1.0*no_unq_words)

## 1.4-7 show
print "\nset manipulate"
print "no_cmd_words:\t", no_cmd_words
print "cmn_words:\t", cmn_words
print "no_unq_words:\t", no_unq_words
print "unq_words:\t", unq_words
print "similarity:\t", similarity

## 1.4-8.1
from sklearn.metrics import jaccard_similarity_score

a = [1 if w in st1_words else 0 for w in unq_words]
b = [1 if w in st2_words else 0 for w in unq_words]

print "jaccard: ", jaccard_similarity_score(a,b)
print "a: ",a
print "b: ",b


''' 1.5 Writing a list p.93'''
## 1.5-1
a = range(1,10)
b = ['a','b','c']

print 'a[]:\t',     a[0:]    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print 'a[0]:\t',    a[0]     # 1
print 'a[-1]:\t',   a[-1]    # 9

### 1.5-2 slice, indexing
print 'a[1:3]:\t',  a[1:3]      # [2, 3]
print 'a[1:]:\t',   a[1:]       # [2, 3, 4, 5, 6, 7, 8, 9]
print 'a[-1:]:\t',  a[-1:]      # [9]
print 'a[:-1]:\t',  a[:-1]      # [1, 2, 3, 4, 5, 6, 7, 8]

### 1.5-4 list concatenate
a = [1,2]
b = [3,4]
print 'a+b',a+b                 # [1,2,3,4]

print min(a),max(a)

if 1 in a:
    print "elem 1 is in list a"
else:
    print "elem 1 is in tuple a"

a = range(1,10)
a.append(10)
print a

### 1.5-9 list stack
a_stack=[]
a_stack.append(1)
a_stack.append(2)
a_stack.append(3)

print 'a_stack.pop(): ',a_stack.pop()
print 'a_stack.pop(): ',a_stack.pop()
print 'a_stack.pop(): ',a_stack.pop()

### 1.5-10 list queue
a_queue = []
a_queue.append(1)
a_queue.append(2)
a_queue.append(3)

print 'a_queue.pop(0): ',a_queue.pop(0)
print 'a_queue.pop(0): ',a_queue.pop(0)
print 'a_queue.pop(0): ',a_queue.pop(0)

### 1.5-11 sort, reverse
from random import shuffle
a = range(1,10)
shuffle(a)
print 'shuffle(a): ',a              # [6, 3, 8, 2, 4, 1, 5, 9, 7]
print 'a.sort(): ',a.sort(),a       # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print 'a.reverse(): ',a.reverse(),a # [9, 8, 7, 6, 5, 4, 3, 2, 1]


'''
1.6 Creating a list from another list - list comprehension p.101
1.7 Using iterators p.
1.8 Generating an iterator and a generator p.
1.9 Using iterables p.
1.10 Passing a function as a variable p.
1.11 Embedding functions in another function p.
1.12 Passing a function as a parameter p.
1.13 Returning a function p.
1.14 Altering the function behavior with decorators p.
1.15 Creating anonymous functions with lambda p.
1.16 Using the map function p.
1.17 Working with filters p.
1.18 Using zip and izip p.
1.19 Processing arrays from the tabular data p.
1.20 Preprocessing the columns p.
1.21 Sorting lists p.
1.22 Sorting with a key p.
1.23 Working with itertools p.
'''




















