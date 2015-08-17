import json
import os

SUMMONERS_RIFT = 0
TWISTED_TREELINE = 1
CRYSTAL_SCAR = 2
HOWLING_ABYSS = 3

def readItems():
  with open('ItemData.txt') as f:
    itemData = json.loads(f.read())
  return itemData

def writeItems(gameMap, startingItems, boots, items, consumables):
  filename = os.path.join(
    "C:", "Riot Games", "League of Legends", "Config", "Global", "Recommended", "ultimateBravery.json")
  if not os.path.exists(os.path.dirname(filename)):
    os.makedirs(os.path.dirname(filename))

  itemSet = {
      "title": "Ultimate Bravery",
      "type": "custom",
      "mode": "any",
      "priority": False,
      "sortrank": 0}
  if gameMap == SUMMONERS_RIFT:
    itemSet["map"] = "SR"
  elif gameMap == TWISTED_TREELINE:
    itemSet["map"] = "TT"
  elif gameMap == CRYSTAL_SCAR:
    itemSet["map"] = "CS"
  elif gameMap == HOWLING_ABYSS:
    itemSet["map"] = "HA"
  else:
    itemSet["map"] = "any"

  blocks = []
  if len(startingItems) > 0:
    blocks.append({
      "type": "Starting Items",
      "recMath": False,
      "minSummonerLevel": -1,
      "maxSummonerLevel": -1,
      "showIfSummonerSpell": "",
      "hideIfSummonerSpell": "",
      "items": startingItems
      })

  if len(boots) > 0:
    blocks.append({
      "type": "Boots",
      "recMath": False,
      "minSummonerLevel": -1,
      "maxSummonerLevel": -1,
      "showIfSummonerSpell": "",
      "hideIfSummonerSpell": "",
      "items": [{"id": str(x), "count": 1} for x in boots]
      })

  if len(items) > 0:
    blocks.append({
      "type": "Items",
      "recMath": False,
      "minSummonerLevel": -1,
      "maxSummonerLevel": -1,
      "showIfSummonerSpell": "",
      "hideIfSummonerSpell": "",
      "items": [{"id": str(x), "count": 1} for x in items]
      })

  if len(consumables) > 0:
    blocks.append({
      "type": "Consumables",
      "recMath": False,
      "minSummonerLevel": -1,
      "maxSummonerLevel": -1,
      "showIfSummonerSpell": "",
      "hideIfSummonerSpell": "",
      "items": [{"id": str(x), "count": 1} for x in consumables]
      })

  itemSet["blocks"] = blocks

  with open(filename, "w") as f:
    f.write(json.dumps(itemSet))
    
  

writeItems("SR", [{"id":"1056", "count":1}, {"id":"2003", "count":2}, {"id":"3340", "count":1}], [1300],
  [1300, 3110, 3100, 3800, 3508, 3003], [2003, 2004, 2044, 2043,2137])
raw_input("Press Enter to continue...")
