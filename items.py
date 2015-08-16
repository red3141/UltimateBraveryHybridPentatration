import json

def readItems():
  with open('ItemData.txt') as f:
    itemData = json.loads(f.read())
  return itemData
