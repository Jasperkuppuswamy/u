
import re
import nltk
# two modules regular expression
def process_file(filename):
  with open(filename, encoding='utf-8') as fp:
    text = fp.read()
    text = text.strip()
    text = re.sub(r'[^\w\s]', '', text)
#In Python, sub is a method provided by the re (regular expression)
    # module that is used to perform string substitution based on a regular expression pattern.

    ## tokenize single comment
    tokens = nltk.word_tokenize(text)
    #tokens=nltk.sent_tokenize()
    return tokens

def get_hashtags(text):
    hashtags = re.findall(r'#(\w+)', text)
    print(hashtags)


get_hashtags("###i love jesus")

file1_tokens = process_file("Mytoken.txt")
file2_tokens = process_file("Mytoken.txt")

combined_tokens = file1_tokens + file2_tokens
#print(combined_tokens)
set1 = set(file1_tokens)
set2 = set(file2_tokens)
intersection = set1.intersection(set2)
#print(intersection)

# Concatenate the two lists
concatenated_list = file1_tokens + file2_tokens
#print("Concatenated list:", concatenated_list)

# Find the common elements between the two lists
common_elements = list(set(file1_tokens).intersection(file2_tokens))
#print("Common elements:", common_elements)

# Find all the elements of both lists, without duplicates
all_elements = list(set(file1_tokens).union(file2_tokens))
#print("All elements without duplicates:", all_elements)


import collections

# Assuming tokens is a list of tokens

# Use the Counter class from collections to count the frequency of each token
token_counts = collections.Counter(combined_tokens)

# Convert the token_counts result to a dictionary
token_freq_dict = dict(token_counts)

# Print the resulting dictionary
print(token_freq_dict)



types of for loops
for element in iterable:
    # do something with element
    fruits = ['apple', 'banana', 'orange']

    for fruit in fruits:
        print(fruit)
apple
banana
orange
for i in range(5):
    print(i)
for i, element in enumerate(iterable):
    # do something with i and element
# An enumerate()loop is used to loop a
   # list
    ##while keeping track of the index of the current element.
    #The enumerate() function returns a tuple of the index and the element,
    #and the for loop then unpacks that tuple into separate variables.The basic syntax of an
    def process_file(filename):
        with open(filename, encoding='utf-8') as fp:
            text = fp.read()
file1_tokens = process_file("Mytoken.txt")
file2_tokens = process_file("Mytoken.txt")

combined_tokens = file1_tokens + file2_tokens
    # Read in the text file
    with open('filename.txt', 'r') as file:
        text = file.read()

    # Check if a word is in the text file
    word = 'racecar'  # replace with the word you want to check
    if word in text:
        # Check if the word is a palindrome
        if word == word[::-1]:
            print(f"{word} is a palindrome")
        else:
            print(f"{word} is not a palindrome")
    else:
        print(f"{word} is not in the text file")


my_dict = {'a': 5, 'b': 2, 'c': 3, 'd': 5, 'e': 2, 'f': 1}

K = 3

for key, value in my_dict.items():
    if value > K:
        print(key, ":", value)







def getTokenFromFile(fileName):
  with open(fileName ,encoding='utf-8') as fp:
    return fp.readline()


if __name__=='__main__':

  token=getTokenFromFile("Mytoken.txt")
  graph=facebook.GraphAPI(token)
  profile=graph.get_object('me',fields='name,location{location},likes')
  print(json.dumps(profile, indent=4))




import os
import json
import facebook

def getTokenFromFile(fileName):
    with open(fileName, encoding='utf-8') as fp:
        return fp.readline()


if __name__=='__main__':
  #token=os.environ.get('FACEBOOK_TEMP_TOKEN')
  token=getTokenFromFile("Mytoken.txt")
  graph=facebook.GraphAPI(token)
  user=graph.get_object("me")
  friends = graph.get_connections(user["id"],"friends")
  print(json.dumps(friends, indent=4))

  import os
  import json
  import facebook
  import requests


  def getTokenFromFile(fileName):
    with open(fileName, encoding='utf-8') as fp:
      return fp.readline()


  if __name__ == '__main__':
    token = getTokenFromFile("Mytoken.txt")
    graph = facebook.GraphAPI(token)
    posts = graph.get_connections('me', 'posts')

    while True:  # keep paginating
      try:
        with open('my_posts.jsonl', 'a') as f:
          for post in posts['data']:
            f.write(json.dumps(post) + "\n")
          # get next page
          posts = requests.get(posts['paging']['next']).json()
      except KeyError:
        # no more pages, break the loop
        break

import os
import json
import facebook
import requests
def getTokenFromFile(fileName):
    with open(fileName, encoding='utf-8') as fp:
        return fp.readline()



if __name__ == '__main__':
 token = getTokenFromFile("Mytoken.txt")
 graph = facebook.GraphAPI(token)
 all_fields = [
 'message',
 'created_time',
 'description',
 'caption',
 'link',
 'place',
 'status_type'
 ]
 all_fields = ','.join(all_fields)
 posts = graph.get_connections('me', 'posts', fields=all_fields)
 while True: # keep paginating
  try:
    with open('my_posts.jsonl', 'a') as f:
      for post in posts['data']:
        f.write(json.dumps(post)+"\n")
 # get next page
      posts = requests.get(posts['paging']['next']).json()
  except KeyError:
 # no more pages, break the loop
   break



import json
from argparse import ArgumentParser
import dateutil.parser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def get_parser():
 parser = ArgumentParser()
 parser.add_argument('--file','-f',required=True,help='The.jsonl file with all the posts')
 return parser

if __name__ == '__main__':
 parser = get_parser()
 args = parser.parse_args()

 with open(args.file) as f:
  posts = []
  for line in f:
   post = json.loads(line)
   created_time = dateutil.parser.parse(post['created_time'])
   posts.append(created_time.strftime('%H:%M:%S'))
 ones = np.ones(len(posts))
 idx = pd.DatetimeIndex(posts)

 my_series = pd.Series(ones, index=idx)

 per_hour = my_series.resample('1H').agg('sum').fillna(0)
# Plotting
 fig, ax = plt.subplots()
 ax.grid(True)
 ax.set_title("Post Frequencies")
 width = 0.8

 ind = np.arange(len(per_hour))
 plt.bar(ind, per_hour)
 tick_pos = ind + width / 2
 labels = []
 for i in range(24):
     d = datetime.now().replace(hour=i, minute=0)
 labels.append(d.strftime('%H:%M'))
 #plt.xticks(tick_pos, labels, rotation=90)
 plt.savefig('posts_per_hour.png')

my_list = [1, 2, 3, 1, 4, 2, 5, 6, 3, 7, 8, 2, 1, 5, 9]


def print_elements_with_frequency_greater_than_k(lst, k):
  # create a dictionary to store the frequency of each element in the list
  freq_dict = {}
  for elem in lst:
    freq_dict[elem] = freq_dict.get(elem, 0) + 1

  # print the elements with frequency greater than k
  for elem, freq in freq_dict.items():
    if freq > k:
      print(elem)


print_elements_with_frequency_greater_than_k(my_list, 2)

