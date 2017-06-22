k = 0
class analise_sintatica():

	#program
	def program(self, token, line_aux):
		global k
		if(token[k].token == 'PROGRAM'):
			k = k+1
			if(token[k].token == 'Id'):
				k = k+1
				if(token[k].token == 'PONTO_VIRGULA'):
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

	#sitype
	def simple_type(self, token, line_aux):
		global k
		virgula = True
		if(token[k].type == 'TYIDEN'):
			return True
		elif(token[k].token == 'ABRE_PARENTESES'):
			k = k+1
			while(virgula):
				if(token[k].token =='Id'):
					k = k+1
					if(token[k].token == 'VIRGULA'):
						k = k+1
					elif(token[k].token == 'FECHA_PARENTESES'):
						return True
					else:
						print('Erro sintático "," ou ")" esperado: ',line_aux[k])
				else:
					print('Erro sintático Identificador esperado: ',line_aux[k])
			pass
		elif(self.const(token,line_aux) == True):
			k = k+1
			if(token[k].token == 'PONTO'):
				k = k+1
				if(token[k].token == 'PONTO'):
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

	# siexpr
	def simple_expression(self, token, line_aux):
		global k
		flag_para_loop = True
		if(token[k].token == 'ADICAO' or token[k].token == 'SUBTRACAO'):
			k = k+1
			while(flag_para_loop):
				# if(term(token, line_aux) == True):
				if(True):
					if(token[k].token == 'ADICAO'):
						k = k+1
					elif(token[k].token == 'SUBTRACAO'):
						k = k+1
					elif(token[k].token == 'OR'):
						k = k+1
					else:
						return True
		else:
			while(flag_para_loop):
				# if(term(token, line_aux) == True):
				if(True):
					if(token[k].token == 'ADICAO'):
						k = k+1
					elif(token[k].token == 'SUBTRACAO'):
						k = k+1
					elif(token[k].token == 'OR'):
						k = k+1
					else:
						return True
	pass

	#expr
	def expression(self, token, line_aux):
		global k
		flag_expression = True
		# if(simple_expression(token,line_aux) == True)
		if(True):
			k = k+1
			if(token[k].token == 'IGUAL'):
				k = k+1
				flag_expression = True
			elif(token[k].token == 'MENOR'):
				k = k+1
				flag_expression = True
			elif(token[k].token == 'MAIOR'):
				k = k+1
				flag_expression = True
			elif(token[k].token == 'DIFERENTE'):
				k = k+1
				flag_expression = True
			elif(token[k].token == 'MAIOR_IGUAL'):
				k = k+1
				flag_expression = True
			elif(token[k].token == 'MENOR_IGUAL'):
				k = k+1
				flag_expression = True
			elif(token[k].token == 'IN'):
				k = k+1
				flag_expression = True
			else:
				print('Erro sintático na linha: ',line_aux[k],' operador inválido')
			if(flag_expression):
				# if(simple_expression(token,line_aux) == True)
				if(True):
					return True
	pass

	#const
	def const(self,token,line_aux):
		global k
		print(k)
		if(token[k].token == 'CADEIA_DE_CARACTERES'):
			return True
		elif(token[k].token == 'ADICAO' or token[k].token == 'SUBTRACAO'):
			k = k+1
			if(token[k].type == 'COIDEN' or token[k].token == 'NUMERO_INTEIRO' or token[k].token == 'NUMERO_REAL'):
				return True
			else:
				print('Erro sintático na linha: ',line_aux[k],'se esperava identificador, inteiro ou real')
				return False
		elif(token[k].type == 'COIDEN' or token[k].token == 'NUMERO_INTEIRO' or token[k].token == 'NUMERO_REAL'):
			return True
		else:
			print('Erro sintático na linha: ',line_aux[k], 'se esperava "+" ou "-"')
			return False
		return True
	pass

	#term
	def term(self, token, line_aux):
		global k
		while(True):
			if (#factor(token,line_aux,) == True
				True):
				if (token[k].token == "MULTIPLICACAO" or
					token[k].token == "DIVISAO"       or
					token[k].token == "DIV"           or
					token[k].token == "MOD"           or
					token[k].token == "AND"          ):
					k=k+1
				else:
					return True
			else:
				print('Erro sintático na linha: ',line_aux[k]);

				return False
	pass

	def index_field_pointer(self,token,line_aux):
		global k
		flag1 = True
		while(flag1):
			if(token[k].token == "ABRE_COLCHETE"):
				k=k+1
				flag2 = True
				while(flag2):
					if(#expression(token,line_aux)
						True):
						if(token[k].token == "VIRGULA"):
							k=k+1
						elif(token[k].token == "FECHA_COLCHETE"):
							k=k+1
							flag2 = False
						else:
							print('Erro sintático na linha: ',line_aux[k], " se esperava ] ou ,");
							return False
					else:
						print('Erro sintático na linha: ',line_aux[k]," se esperava expression");
						return False
			elif(token[k].token == "PONTO"):
				k=k+1
				if(#FIDEN==
					True):
					pass
			#elif(token[k] == "PONTEIRO"): Não implementado porque não temos ponteiro
			else:
				return True

	pass

	#filist
	def filist(self,token,line_aux):
		global k

		while(True):

			if (token[k].token == "IDEN"):
				k=k+1

				if (token[k].token == "VIRGULA" ):
					k=k+1

				elif (token[k].token == "DOIS_PONTOS"):
					k=k+1

					if (self.type(token,line_aux)):
						k=k+1

						if(token[k].token == "PONTO_VIRGULA"):
							k=k+1
						elif(token[k].token == "CASE"): # se for case de novo , não tratar, pois sera tratado no if ultimo if
						else: return True

					else:
						print('Erro sintático na linha: ',line_aux[k], " se esperava um type");
						return False

				else:
					print('Erro sintático na linha: ',line_aux[k], " se esperava , ou :");
					return False

			if (token[k].token == "CASE"):
				k=k+1
				if(token[k].token == "IDEN"):
					k=k+1
					if (token[k].token == "VIRGULA"):
						k=k+1
						if(token[k].token == "TYIDEN"):
							k=k+1
							if(token[k].token == "OF"):
								k=k+1

								while(True):

									if( token[k].token == "CADEIA_DE_CARACTERES" or token[k].token == "COIDEN" or token[k].token == "NUMERO_REAL" or token[k].token == "NUMERO_INTEIRO"):
								   		k=k+1
								   			if (token[k].token == "VIRGULA"):
								   				k=k+1
								   			elif (token[k].token == "DOIS_PONTOS"):
								   				k=k+1
								   				if(token[k].token == "ABRE_PARENTESES"):
								   					k=k+1
								   					if(self.filist(token,line_aux)):
								   						k=k+1
								   						if (token[k].token == "FECHA_PARENTESES"):
								   							k=k+1
								   							if (token[k].token == "PONTO_VIRGULA"):
								   								k=k+1
								   							else return True

								   						else:
															print('Erro sintático na linha: ',line_aux[k], " se esperava ) ");
															return False
								   					else:
														print('Erro sintático na linha: ',line_aux[k], " se esperava FILIST ");
														return False
								   				else:
													print('Erro sintático na linha: ',line_aux[k], " se esperava ( ");
													return False
								   			
								   			else:
												print('Erro sintático na linha: ',line_aux[k], " se esperava , ou : ");
												return False

								   	elif (token[k].token == "ADICAO" or token[k].token == "SUBTRACAO"):
								   		  k=k+1
								   		  if(token[k].token == "COIDEN" or token[k].token == "NUMERO_INTEIRO" or token[k].token == "NUMERO_REAL"):
								   		  	k=k+1
								   		  		if (token[k].token == "VIRGULA"):
								   					k=k+1
								   				elif (token[k].token == "DOIS_PONTOS"):
								   					k=k+1
								   					if(token[k].token == "ABRE_PARENTESES"):
								   						k=k+1
								   						if(self.filist(token,line_aux)):
								   							k=k+1
								   							if (token[k].token == "FECHA_PARENTESES"):
								   								k=k+1
								   								if (token[k].token == "PONTO_VIRGULA"):
								   									k=k+1
								   								else return True

								   							else:
																print('Erro sintático na linha: ',line_aux[k], " se esperava ) ");
																return False
								   						else:
															print('Erro sintático na linha: ',line_aux[k], " se esperava FILIST ");
															return False
								   					else:
														print('Erro sintático na linha: ',line_aux[k], " se esperava ( ");
														return False
								   			
								   				else:
													print('Erro sintático na linha: ',line_aux[k], " se esperava , ou : ");
													return False


								   	elif (token[k].token == "PONTO_VIRGULA"):
								   		k=k+1

								   	else return True

							else:
								print('Erro sintático na linha: ',line_aux[k], " se esperava OF ");
								return False

						else:
							print('Erro sintático na linha: ',line_aux[k], " se esperava TYIDEN ");
							return False

					else:
						print('Erro sintático na linha: ',line_aux[k], " se esperava , ");
						return False

				else:
					print('Erro sintático na linha: ',line_aux[k], " se esperava um IDEN");
					return False




			if (token[k].token == "PONTO_VIRGULA"):
				k=k+1

	pass

	def type(self,token,line_aux):
		global k;
		return True
	pass



	def analisador(self, token, line_aux):
		global k
		k = k+1
		#self.program(token,line_aux,0)
		#print(self.simple_type(token, line_aux))
		#print(self.simple_expression(token, line_aux))
		print(self.const(token, line_aux))
		#print(self.term(token,line_aux))
		# print(self.index_field_pointer(token,line_aux))
