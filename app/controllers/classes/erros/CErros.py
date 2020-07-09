from flask import jsonify

class CErros(object):
    def __init__(self):   
        self.Msg = ''     
        
    def getMsgErro(self):
        # return self.Msg
        return jsonify({'Codigo':99, 'DescricaoErro':self.Msg}) 

    
    def setMsgErro(self, Msg):
        self.Msg = Msg                 