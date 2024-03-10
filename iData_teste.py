from iData import *
import json, time, random

client, db = conectar()

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

def buscarAmizadeMaisRelevante():
    count = db["amizade_pagerank"].count_documents({})
    doc = None
    relevancia = 0
    for i in range(0, count):
        maisRelevante = db["amizade_pagerank"].find_one({"rank_Adjacencia.0.1": {"$gt": relevancia}}, {"rank_Adjacencia": 1})
        if maisRelevante:
            for j in maisRelevante['rank_Adjacencia']:
                if j[1] > relevancia:
                    relevancia = j[1]
                    doc = maisRelevante
        else:
            break
    print(f'{relevancia} - {doc}')
