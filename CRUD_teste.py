from CRUD import *

def createTeste():
    f = open('docs_teste.json', 'r', encoding='utf-8')
    docs = json.loads(f.read())
    print(create('objeto', docs['objeto'], True))
    print(create('interacao', docs['interacao'], True))
    f.close()

def createTeste2(colecao):
    print(create(colecao, read(colecao, filtroSaida = {'_id': 0}, many = True), True))
    
def readTeste():
    print(read('objeto', {'obj_Id': {'$gt': 5, '$lt': 50}}, many = True))

def updateTeste():
    id = read('objeto')['obj_Id']
    print(update('objeto', {'$set': {'obj_Id': id + 20}}).matched_count)
    print(id, read('objeto', {'obj_Id': id + 20}))

def deleteTeste():
    print(delete('objeto', {'obj_Id': {'$gt': 10}}, True).deleted_count)

def replicarDocumentos():
    for i in range(0, 3):
        [createTeste2(colecao) for colecao in colecoes]
        [read(colecao, many = True) for colecao in colecoes]
