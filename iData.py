from pymongo import MongoClient
import json, time, random

def interagir():
    arq = open('interacao.json', "r", encoding='utf-8')
    docs = json.loads(arq.read())
    arq.close()

    timeout = time.time()
    for i in docs:
        timeout += random.randint(0, 15)
        while True:
            if timeout < time.time():
                db['interacao'].insert_one(i)
                print(f'{i} --- {time.ctime(timeout)}')
                break

def limparColecoes(colecoes):
    for i in colecoes:
        db.drop_collection(i)

def popularColecoes(colecoes):
    for i in colecoes:
        arq = open(f'{i}.json', "r", encoding='utf-8')
        docs = json.loads(arq.read())
        db[i].insert_many(docs)
        arq.close()

def buscarAmizadeMaisRelevante():
    docs = db["amizade_pagerank"].find()
    doc = None
    relevancia = 0
    for i in docs:
        maisRelevante = db["amizade_pagerank"].find_one({"rank_Adjacencia.0.1": {"$gt": relevancia}}, {"rank_Adjacencia": 1})
        if maisRelevante:
            for i in maisRelevante['rank_Adjacencia']:
                if i[1] > relevancia:
                    relevancia = i[1]
                    doc = maisRelevante
        else:
            break
    print(f'{relevancia} - {doc}')

cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["iData"]

colecoes = ["objeto", "interacao", "ambiente_ona", "amizade_pagerank", "classe"]