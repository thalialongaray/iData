from iData import *
import json, time

def buscarAmizadeMaisRelevante():
    count = db["amizade_pagerank"].count_documents({})
    
    idObj = None
    idObjAdj = None
    relevancia = 0
    num = 0

    for i in range(0, count):
        maisRelevante = read(db, "amizade_pagerank", {"rank_Adjacencia.0.1": {"$gt": relevancia}})
        
        if maisRelevante:
            idObj = maisRelevante['rank_Objeto']
            idObjAdj = maisRelevante['rank_Adjacencia'][0][0]
            relevancia = maisRelevante['rank_Adjacencia'][0][1]
            num += 1
        else:
            break

    return idObj, idObjAdj, relevancia, num

vColecoes = ["objeto", "amizade_pagerank"]
numeroDeDocs = [10, 50, 100, 1000]

for i in numeroDeDocs:
    arqObjeto = open(f'jsons/{i}objetos.json', "r", encoding='utf-8')
    arqAmizade = open(f'jsons/{i}amizades.json', "r", encoding='utf-8')
    docs = {"objeto": [], "amizade_pagerank": []}
    docs["objeto"] = json.loads(arqObjeto.read())
    docs["amizade_pagerank"] = json.loads(arqAmizade.read()) 
    arqObjeto.close()
    arqAmizade.close()

    client, db = conectar()
    [delete(db, colecao, many = True) for colecao in vColecoes]
    [create(db, colecao, docs[colecao], many = True) for colecao in vColecoes]
    desconectar(client)
    time.sleep(300)

    client, db = conectar()
    idObj, idObjAdj, relevancia, num = buscarAmizadeMaisRelevante()
    obj = read(db, "objeto", {"obj_Id": idObj})
    objAdj = read(db, "objeto", {"obj_Id": idObjAdj})
    print(f'Número de documentos: {i}\nMaior relevancia encontrada: {relevancia}\nNumero de consultas necessarias: {num}\nAmizade mais relevante:\n\tObjeto:\n\t\t{obj}\n\tObjeto Adjacente:\n\t\t{objAdj}\n')
    desconectar(client)
    time.sleep(300)
