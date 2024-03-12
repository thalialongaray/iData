from pymongo import MongoClient
from CRUD import *
import json

def conectar():
    client = MongoClient(uri)
    db = client["iData"]
    return client, db

def testarConexao(client):
    try:
        client.iData.command('ping')
        print("You're connected to iData on MongoDB!")
    except Exception as e:
        print(e)

def desconectar(client):
    client.close()

def popularColecoes(db, colecoes):
    for i in colecoes:
        arq = open(f'jsons/{i}.json', "r", encoding='utf-8')
        docs = json.loads(arq.read())
        db[i].insert_many(docs)
        arq.close()

def limparColecoes(db, colecoes):
    for i in colecoes:
        db.drop_collection(i)

# uri = "mongodb://localhost:27017/"
uri = input("Informe a URI: ")

colecoes = ["objeto", "interacao", "ambiente_ona", "amizade_pagerank", "classe"]
