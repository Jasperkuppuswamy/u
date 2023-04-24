
import re
import nltk

def preprocess(text):
# basic cleaning
    text=text.strip() #REMOVE SPACE
    text=re.sub(r'[^\w\s]','',text)
    text=text.lower()
    tokens=nltk.word_tokenize(text)
    return tokens
print(preprocess("i am hiii."
                 " hello ppll"))

def get_hashtags(text):
    hashtags=re.findall(r"#(\w+)",text)
    return hashtags


print(get_hashtags("i am #mms xxx."
                 " hello #ppll"))

def tag_tokens(preprocessed_tokens):
    pos=nltk.pos_tag(preprocessed_tokens)
    return pos

tag_tokens(["hello", "broo","what"])

import nltk
file_content = open("hi.txt").read()
tokens = nltk.word_tokenize(file_content)
print(tokens)

with open ('hi.txt') as dx:
    for line in dx:
        tokens = nltk.word_tokenize(line)
        print(tokens)

f = open("work.txt","w")

f.write("Hello World, \n")
f.write("This data will be written to the file.")

# close file
f.close()
