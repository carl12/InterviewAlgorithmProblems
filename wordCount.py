'''
Word Count Engine

Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.


'''
import random
from string import ascii_lowercase
import f_timer
import time

def word_count_engine(document):
  very_start = time.time()
  start = time.time()

  if document is None or len(document) == 0:
    return []
  
  document = document.lower()
  words = {}
  word = []
  for i in range(len(document)):
    curr = document[i]
    if curr >= 'a' and curr <= 'z':
      word.append(curr)
    
    elif curr == ' ':
      if len(word) > 0:
        word_str = ''.join(word)
        if words.get(word_str) is not None:
          words[word_str][0]+=1
        else:
          words[word_str] = [1, -i]
        word = []
    
  
  if len(word) > 0:
      word_str = ''.join(word)
      if words.get(word_str) is not None:
        words[word_str][0]+=1
      else:
        words[word_str] = [1, -len(document)]
      word = []

  print('first pass: ',time.time()-start)
  start = time.time()

  word_list = []
  
  for key in words.keys():
    word_list.append([words[key], key])

  print('Words entered: ', time.time() - start)
  start = time.time()

  word_list.sort(reverse=True)
  print('Sorted: ', time.time() - start)
  start = time.time()
  result = [[entry[1], str(entry[0][0])] for entry in word_list]
  print("Finished: ", time.time() - start)
  print("Total: ", time.time() - very_start)
  return result


def word_count_engine2(document):
  very_start = time.time()
  start = very_start

  if document is None or len(document) == 0:
    return []

  document = document.lower()
  word_list = document.split(' ')
  word_dict = {}
  largest_count = 0

  for i in range(len(word_list)):
    word = word_list[i]

    char_arr = []
    for char in word:
      if char >= 'a' and char <= 'z':
        char_arr.append(char)
    clean_word = ''.join(char_arr)

    if len(clean_word) > 0:
      count = 0
      if word_dict.get(clean_word) is not None:
        count = word_dict[clean_word] + 1
      else:
        count = 1
      if count > largest_count:
        largest_count = count

      word_dict[clean_word] = count

  print('first pass: ', time.time() - start)
  start = time.time()

  bucket_list = [None for _ in range(largest_count+1)]

  for word in word_dict.keys():
    counter = word_dict[word]
    if bucket_list[counter] == None:
      bucket_list[counter] = []
    bucket_list[counter].append(word)

  print('Bucket made: ', time.time()-start)
  start = time.time()

  result = []
  for i in reversed(range(len(bucket_list))):
    length_list = bucket_list[i]
    if length_list:
      for word in length_list:
        result.append([word, str(i)])

  print("Final: ", time.time()-start)
  print("Finish: ", time.time() - very_start)
  return result


def gen_document(max_word, max_doc):
  length = random.randint(max_doc/2, max_doc)
  print('length: ',length)
  i = 0
  output = []
  last = 0
  while i < length:
    if i > last:
      print(i)
      last+= 3000000
    next = [random.choice(ascii_lowercase) for _ in range(random.randint(0,max_word))]
    output.extend(next+[" "])
    i+= len(next)+1

  return [''.join(output[:length])]


print('starting')
# print(f_timer.time_funcs([word_count_engine, word_count_engine2], gen_document, [100,1000000], 100))
a = gen_document(20, 50000000)[0]

print('starting...')
word_count_engine(a)
print('finished')

print('starting...')
word_count_engine2(a)
print('finished')

print('starting...')
word_count_engine(a)
print('finished')

# print(word_count_engine2(document) == word_count_engine(document))


    
        
    
      