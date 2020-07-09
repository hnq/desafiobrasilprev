
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from app.controllers.classes.CIntegracao import CIntegracao
from random import randint

class Pedidos(CIntegracao):    
    def getcamposvalidar(self):
        return 'idcliente,listaprodutos'
    
    def post(self):
        try:
            pass
        
            objPIntegracoes = self.getPIntegracoes()     
            if objPIntegracoes.getValidado() == False:
                return objPIntegracoes.getMsgErro()               
            print(randint(0,9))         
            objPIntegracoes.setidpedido(randint(0,9))            
            return self.PIntegracoes.MontarJsonRetornoPedido()
            
        finally:
            pass
            self.GravarLog()
    
