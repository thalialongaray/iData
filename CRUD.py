from iData import *

def create(colecao, docs, many = False):
    if many:
        return db[colecao].insert_many(docs)
    return db[colecao].insert_one(docs)

def read(colecao, filtro = {}, many = False):
    if many:
        return [document for document in db[colecao].find(filtro)]
    return db[colecao].find_one(filtro)

def update(colecao, atualizacao, filtro = {}, many = False):
    if many:
        return db[colecao].update_many(filtro, atualizacao)
    return db[colecao].update_one(filtro, atualizacao)

def delete(colecao, filtro = {}, many = False):
    if many:
        return db[colecao].delete_many(filtro)
    return db[colecao].delete_one(filtro)