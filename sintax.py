class analise_sintatica():
    
    def program(self, token, line_aux):
    	k = 0
    	if(token[k] == 'PROGRAM'):
    		k = k+1
    		if(token[k] == 'Id'):
    			k = k+1
    			if(token[k] == 'PONTO_VIRGULA'):
    				k = k+1
    			else:
    				print('Erro sintático na linha: ',line_aux[k])
    		else:
    			print('Erro sintático na linha: ',line_aux[k])
    	else:
   			print('Erro sintático na linha: ',line_aux[k])
pass
    def analisador(self, token, line_aux):
    	self.program(token,line_aux)