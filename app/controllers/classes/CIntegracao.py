from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from app.controllers.classes.propriedades.CPropriedadesIntegracao import CPropriedadesIntegracao

class CIntegracao(Resource):
    
    def setPIntegracoes(self, PIntegracoes):
        self.PIntegracoes = PIntegracoes    
    
    def getPIntegracoes(self):
        return self.PIntegracoes  
    
    def __init__(self):             
        objPIntegracoes = CPropriedadesIntegracao(request)        
        objPIntegracoes.setcamposvalidar(self.getcamposvalidar())
        if objPIntegracoes.Validar() == False:
            self.setPIntegracoes(objPIntegracoes)
            return
           
        self.setPIntegracoes(objPIntegracoes)

    def GravarLog(self):
        print('GravarLog PENDENTE')