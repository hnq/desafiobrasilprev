from app.controllers.classes.erros.CErros import CErros
from flask import jsonify


class CPropriedadesIntegracao(CErros):
    def __init__(self, v_objRequest):
        self.Request = v_objRequest        

    def setRequest(self, Request):
        self.Request = Request    
    
    def getRequest(self):
        return self.Request   
    
    def setValidado(self, Validado):
        self.Validado = Validado    
    
    def getValidado(self):
        return self.Validado       
    
    def setcredor(self, credor):
        self.credor = credor    
    
    def getcredor(self):
        return self.credor
    
    def setcpfcnpj(self, cpfcnpj):
        self.cpfcnpj = cpfcnpj    
    
    def getcpfcnpj(self):
        return self.cpfcnpj   
    
    def setnome(self, nome):
        self.nome = nome    
    
    def getnome(self):
        return self.nome   
    
    def setdatanascimento(self, datanascimento):
        self.datanascimento = datanascimento    
    
    def getdatanascimento(self):
        return self.datanascimento
    
    def setprofissao(self, profissao):
        self.profissao = profissao    
    
    def getprofissao(self):
        return self.profissao  
    
    def setemail(self, email):
        self.email = email    
    
    def getemail(self):
        return self.email  

    def setidcliente(self, idcliente):
        self.idcliente = idcliente    
    
    def getidcliente(self):
        return self.idcliente    
    
    def setidproduto(self, idproduto):
        self.idproduto = idproduto    
    
    def getidproduto(self):
        return self.idproduto 
    
    def setnomeproduto(self, nomeproduto):
        self.nomeproduto = nomeproduto    
    
    def getnomeproduto(self):
        return self.nomeproduto   

    def setquantidade(self, quantidade):
        self.quantidade = quantidade    
    
    def getquantidade(self):
        return self.quantidade 
     
    def setvalor(self, valor):
        self.valor = valor    
    
    def getvalor(self):
        return self.valor  
    
    def setidpedido(self, idpedido):
        self.idpedido = idpedido    
    
    def getidpedido(self):
        return self.idpedido  
    
    def setcamposvalidar(self, camposvalidar):
        self.camposvalidar = camposvalidar    
    
    def getcamposvalidar(self):
        return self.camposvalidar  
    
    def setlistaprodutos(self, listaprodutos):
        self.listaprodutos = listaprodutos    
    
    def getlistaprodutos(self):
        return self.listaprodutos  
    
    def ValidarBasicAuthorization(self):
        blAutorizado = False
        self.setMsgErro('Basic Authorization não foi informado e/ou é inválido')
        try:
            pass
            if self.Request.authorization.password == 'desafioprev' and self.Request.authorization.username == 'desafio':
                blAutorizado = True
                self.setMsgErro('')
        finally:
            pass
            return(blAutorizado)
    
    # @staticmethod
    def Validar(self):
        self.setValidado(False)
        blErroValidacao = False
        objJsonRequest = self.Request.json
        
        if self.ValidarBasicAuthorization() == False:
            return(False)
        
        arrayCampoValidar = self.getcamposvalidar().split(',')
        for CampoAtual in arrayCampoValidar:                        
            if objJsonRequest.get(CampoAtual):
                if objJsonRequest[CampoAtual] == None:
                    blErroValidacao = True                    
            else:
                blErroValidacao = True
            
            if blErroValidacao == True:
                self.setMsgErro('Campo ' + CampoAtual + ' não foi informado')
                return(False)
            
            eval('self.set' + CampoAtual + '(objJsonRequest[CampoAtual])')
              
        self.setValidado(True)
        return(True)
            
    def MontarJsonRetornoCliente(self):
        return jsonify({'codigo':0,
                        'mensagem':'Cliente Cadastrado Sucesso',
                        'idcliente':self.getidcliente() , 
                        'nomecliente':self.getnome()
                        }) 
        
    def MontarJsonRetornoProduto(self):
        return jsonify({'codigo':0,
                        'mensagem':'Produto Cadastrado Sucesso',
                        'idproduto':self.getidproduto() , 
                        'nomeproduto':self.getnomeproduto()
                        }) 
        
    def MontarJsonRetornoPedido(self):
        return jsonify({'codigo':0,
                        'mensagem':'Pedido Cadastrado Sucesso',
                        'idpedido':self.getidpedido() ,
                        'listaprodutos':self.getlistaprodutos(),
                        'valortotal':'R$ 120.00'
                        }) 
