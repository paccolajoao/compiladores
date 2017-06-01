k = 0
class analise_sintatica():
	def program(self, token, line_aux):
		global k
		if(token[k] == 'PROGRAM'):
			k = k+1
			if(token[k] == 'Id'):
				k = k+1
				if(token[k] == 'PONTO_VIRGULA'):
					k = k+1
				else:
					print('Erro sintático na linha: ',line_aux[k])
					return False
			else:
				print('Erro sintático na linha: ',line_aux[k])
				return False
		else:
			print('Erro sintático na linha: ',line_aux[k])
			return False

		return True
	def simple_type(self, token, line_aux):
		global k
		virgula = True
		if(token[k] == 'INTEGER' or token[k] == 'REAL' or token[k] == 'CHAR'):
			return True
		elif(token[k] == 'ABRE_PARENTESES'):
			k = k+1
			while(virgula):
				if(token[k] =='Id'):
					k = k+1
					if(token[k] == 'VIRGULA'):
						k = k+1
					elif(token[k] == 'FECHA_PARENTESES'):
						return True
					else:
						print('Erro sintático "," ou ")" esperado: ',line_aux[k])
				else:
					print('Erro sintático Identificador esperado: ',line_aux[k])
			pass
		elif(self.const(token,line_aux) == True):
			k = k+1
			if(token[k] == 'PONTO'):
				k = k+1
				if(token[k] == 'PONTO'):
					k = k+1
					if(self.const(token,line_aux) == True):
						print(k)
						return True
					else:
						print('Erro sintático constante esperada: ',line_aux[k])
				else:
					print('Erro sintático "." esperado: ',line_aux[k])
			else:
				print('Erro sintático "." esperado: ',line_aux[k])
		else:
			print('Erro sintático, nem Identificador, nem "(" e nem const achado: ',line_aux[k])
		print(k)
		return True
	pass
	def simple_expression(self, token, line_aux):
		global k
		flag_para_loop = True
		if(token[k] == 'ADICAO' or token[k] == 'SUBTRACAO'):
			k = k+1
			while(flag_para_loop):
				# if(term(token, line_aux) == True):
				if(True):
					if(token[k] == 'ADICAO'):
						k = k+1
					elif(token[k] == 'SUBTRACAO'):
						k = k+1
					elif(token[k] == 'OR'):
						k = k+1
					else:
						return True
		else:
			while(flag_para_loop):
				# if(term(token, line_aux) == True):
				if(True):
					if(token[k] == 'ADICAO'):
						k = k+1
					elif(token[k] == 'SUBTRACAO'):
						k = k+1
					elif(token[k] == 'OR'):
						k = k+1
					else:
						return True
	pass

	def expression(self, token, line_aux):
		global k
		flag_expression = False
		flag_expression = True
		# if(simple_expression(token,line_aux) == True)
		if(True):
			k = k+1
			if(token[k] == 'IGUAL'):
				k = k+1
				flag_expression = True
			elif(token[k] == 'MENOR'):
				k = k+1
				flag_expression = True
			elif(token[k] == 'MAIOR'):
				k = k+1
				flag_expression = True
			elif(token[k] == 'DIFERENTE'):
				k = k+1
				flag_expression = True
			elif(token[k] == 'MAIOR_IGUAL'):
				k = k+1
				flag_expression = True
			elif(token[k] == 'MENOR_IGUAL'):
				k = k+1
				flag_expression = True
			elif(token[k] == 'IN'):
				k = k+1
				flag_expression = True
			else:
				print('Erro sintático na linha: ',line_aux[k],' operador inválido')
			if(flag_expression):
				# if(simple_expression(token,line_aux) == True)
				if(True):
					return True
	pass
	def const(self,token,line_aux):
		global k
		if(token[k] == 'CADEIA_DE_CARACTERES'):
			return True
		elif(token[k] == 'ADICAO' or token[k] == 'SUBTRACAO'):
			k = k+1
			if(token[k] == 'Id' or token[k] == 'NUMERO_INTEIRO' or token[k] == 'NUMERO_REAL'):
				return True
			else:
				print('Erro sintático na linha: ',line_aux[k],'se esperava identificador, inteiro ou real')
				return False
		elif(token[k] == 'Id' or token[k] == 'NUMERO_INTEIRO' or token[k] == 'NUMERO_REAL'):
			return True
		else:
			print('Erro sintático na linha: ',line_aux[k], 'se esperava "+" ou "-"')
			return False
		return True
	pass
	def analisador(self, token, line_aux):
		#self.program(token,line_aux,0)
		# print(self.simple_type(token, line_aux))
		print(self.simple_expression(token, line_aux))
