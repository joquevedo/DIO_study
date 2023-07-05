"""
Este código faz parte de uma etapa do curso Python Developer da Digital Inovation One.
Especificamente faz parte da unidade que fala sobre integração de Python com frameworks,
e este implementa alguns documentos em um banco de dados não-relacional através usando MongoDB através
do Pymongo.

Procurei me basear tanto nas informações dadas pelo curso quanto na própria documentação do
framework. O código ainda precisa ser refatorado e aprimorado

Trata-se de um exercício com fins educacionais.
"""

import pymongo as pyM
import datetime

# Criando conexão com MongoDB Atlas (password omitido).
mdBank = pyM.MongoClient("mongodb+srv://jmdb:######@cluster0.5ssgnux.mongodb.net/")

# Criando um banco de dados. 
db = mdBank ["MongoDB"]

# Criando uma coleção
coll = db.create_collection("Bank")

# Criando um documento e inserindo na coleção.
post1 = {

    "nome": "john romero",
    "cpf": "666666666",
    "endereco": "DoomSt 666",
    "tags": ["mongodb", "client", "DOOM"],
    "date" : datetime.datetime.utcnow()
}

x = coll.insert_one(post1).inserted_id


# Criando múltiplos documentos e inserindo na coleção
post2 = {

    "nome": "douglas addams",
    "cpf": "4242",
    "endereco": "Universe 42",
    "tags": ["mongodb", "client", "hitchhiker"],
    "date" : datetime.datetime.utcnow()

}

post3 = {

    "nome": "john ronald reuel tolkien",
    "cpf": "789456",
    "endereco": "Northmoor Road 20",
    "tags": ["mongodb", "client", "Middle Earth"],
    "date" : datetime.datetime.utcnow()

}

y = coll.insert_many([post2, post3]).inserted_ids


# Recuperando dados. 
for doc in coll.find({}).sort("date"):
    print(doc)

print("\n")

for doc in coll.find({}).sort("id"):
    print(doc)

print("\n")

for doc in coll.find({}).sort("name"):
    print(doc)