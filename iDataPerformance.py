from iData import *
import json, time

arq1k = open('jsons/docs1k.json', "r", encoding='utf-8')
docs1k = json.loads(arq1k.read())
arq1k.close()

numeroDeDocs = [10, 50, 100, 1000]
for i in numeroDeDocs:
    client, db = conectar()
    testarConexao(client)
    
    [delete(db, colecao, many = True) for colecao in colecoes]
    time.sleep(30)
    [create(db, colecao, docs1k[colecao][:i], many = True) for colecao in colecoes]
    time.sleep(30)
    [read(db, colecao, many = True) for colecao in colecoes]
    
    desconectar(client)
    time.sleep(300)
