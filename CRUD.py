def create(db, colecao, docs, many = False):
    if many:
        return db[colecao].insert_many(docs)
    return db[colecao].insert_one(docs)

def read(db, colecao, filtroConsulta = {}, filtroSaida = {}, many = False):
    if many:
        return [document for document in db[colecao].find(filtroConsulta, filtroSaida)]
    return db[colecao].find_one(filtroConsulta, filtroSaida)

def readLimit(db, colecao, limit, filtroConsulta = {}, filtroSaida = {}):
    return [document for document in db[colecao].find(filtroConsulta, filtroSaida).limit(limit)]

def update(db, colecao, atualizacao, filtro = {}, many = False):
    if many:
        return db[colecao].update_many(filtro, atualizacao)
    return db[colecao].update_one(filtro, atualizacao)

def delete(db, colecao, filtro = {}, many = False):
    if many:
        return db[colecao].delete_many(filtro)
    return db[colecao].delete_one(filtro)
