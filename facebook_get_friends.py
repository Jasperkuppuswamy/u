

import os
import json
import facebook
import requests

def getTokenFromFile(fileName):
    with open(fileName, encoding='utf-8') as fp:
        return fp.readline()


if __name__=='__main__':
  #token=os.environ.get('FACEBOOK_TEMP_TOKEN')
  token=getTokenFromFile("u.txt")
  graph=facebook.GraphAPI(token)
  user=graph.get_object("me")
  friends = graph.get_connections(user["id"],"friends")
  print(json.dumps(friends, indent=4))