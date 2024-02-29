from CRUD import *

def createTeste():
    f = open('docs_teste.json', 'r', encoding='utf-8')
    docs = json.loads(f.read())
    print(create('objeto', docs['objeto'], True))
    print(create('interacao', docs['interacao'], True))
    f.close()

def readTeste():
    print(read('objeto', {'obj_Id': {'$gt': 5, '$lt': 50}}, True))

def updateTeste():
    id = read('objeto')['obj_Id']
    print(update('objeto', {'$set': {'obj_Id': id + 20}}).matched_count)
    print(id, read('objeto', {'obj_Id': id + 20}))

def deleteTeste():
    print(delete('objeto', {'obj_Id': {'$gt': 10}}, True).deleted_count)