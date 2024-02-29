from pymongo import MongoClient
import json

def testarConexao():
    try:
        db.command('ping')
        print("You're connected to iData on MongoDB!")
    except Exception as e:
        print(e)

def popularColecoes(colecoes):
    for i in colecoes:
        arq = open(f'{i}.json', "r", encoding='utf-8')
        docs = json.loads(arq.read())
        db[i].insert_many(docs)
        arq.close()

def limparColecoes(colecoes):
    for i in colecoes:
        db.drop_collection(i)

def desconectar():
    client.close()

client = MongoClient("mongodb://localhost:27017/")
db = client["iData"]

colecoes = ["objeto", "interacao", "ambiente_ona", "amizade_pagerank", "classe"]
