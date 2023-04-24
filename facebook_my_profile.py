import os
import json
import facebook
import requests

def getTokenFromFile(fileName):
  with open(fileName ,encoding='utf-8') as fp:
    return fp.readline()


if __name__=='__main__':

  token=getTokenFromFile("u.txt")
  graph=facebook.GraphAPI(token)
  profile=graph.get_object('me',fields='name,location{location},likes')
  print(json.dumps(profile, indent=4))

