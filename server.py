# imports das libs que iremos utlizar
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from app.controllers.classes.clientes.CClientes import Clientes
from app.controllers.classes.produtos.CProdutos import Produtos
from app.controllers.classes.pedidos.CPedidos import Pedidos

WsApi = Flask(__name__)
WsApiRotas = Api(WsApi)

WsApiRotas.add_resource(Clientes, '/API/lojavirtual/clientes')
WsApiRotas.add_resource(Produtos, '/API/lojavirtual/produtos')
WsApiRotas.add_resource(Pedidos, '/API/lojavirtual/pedidos')

if __name__ == '__main__':
    WsApi.run(port=5000)