import psycopg2
import json

def importFile(f):
    jsonFile = open(f,"r").read()
    return json.loads(jsonFile)

def main():
    jsonObj = importFile("gened.json")
    for item in jsonObj:
        print(item)
