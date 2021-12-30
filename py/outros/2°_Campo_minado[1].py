# importações 
from random import randint
from time import sleep

def criar_matrix(* val, tam, list = True ):
	"""Val recebe os valores ou valor da Matrix, tam define os lados é com a list você diz só quer colocar
	 um ou mais valor ele já está definida por padrão como lista True, é no final retorna uma lista"""
	num = []
	nu = []
	cont = 0
	for x in range(0, tam):
		for y in range(0, tam):
			if list == True:
				nu.append(0)
				if (len(val) -1) >= cont:
					nu[y] = val[cont]
				cont += 1
			else:
				nu.append(val[0])
		num.append(0)
		num[x] = nu[:]
		nu.clear()
	return(num)

def mostra_matrix(matrix, tam, detalhe = 1, espa = 0, cor = "\033[m", cor2 = "\033[m", cor3 = "\033[m", tempo = 0):
	"""você coloca uma lista em Matrix é o tamanho dos lados obrigatoriamente, você pode controlar o tamanho das linhas
	 em detalhes casso diferente de 1, é os espaços na casa espa, a última opção cor é o código \033[m a cor 1 é do ''_'' e a 2 e do ''|' e a 3 o "★''. """
	
	if detalhe == 1:
		det = (tam * 5) + 5
	else:
		det = detalhe

	for x in range(0, tam):
		print(f"{cor}_"*det)
		print(" "*espa, end=(""))
		print(f" {x + 1} »", end=(""))
		for y in range(0, tam):
			sleep(tempo)
			print(f"{cor2} | {cor3}{matrix[x][y]} ", end=(""), flush = True)
		print(f"{cor2}|")
	print(f"{cor}_"*det)
	if x == (tam - 1):
		for n in range(0, tam):
			if n == 0:
				print(f"{cor2} Y » |", end=(""))
			print(f"{cor2} {n+1} | \033[m", end=(""))
	print("")

def pos_test(X, Y, tam):
	"""Válida uma posição de x e y em um tabuleiro tam*tam"""
	if X >= 0 and Y >= 0 and X < tam and Y < tam:
		return True
	else:
		return False

def lados(x, y, tam):
	"""Essa função verificar o que tem nas posições adjacentes as cordenas x e y
	 eliminados as que pasem do limite tam, retornando uma lista [x, y]"""
	posib = []
	x = int(x)
	y = int(y)
	for X in range(x-1, x+2):
		for Y in range(y-1, y+2):
			pos = [X, Y]
			
			if pos_test(X, Y, tam):
				posib.append(pos)
	return posib

def bombas(b, t):
	"""recebe o número de bombas é o tamanho do tabuleiro
	 é retorna uma lista de posição é as coloca em valores[]"""
	
	bombas = []
	bobs = []
	global valores
	while len(bombas) < b:
		x = randint(0, t-1)
		y = randint(0, t-1)
		bobs = [x, y]
		if bobs not in bombas:
			bombas.append(bobs[:])
			bobs.clear()
			valores[x][y] = "b"
	return bombas

#progama principal

#vc tá com paciência para testar tudo?
saco = 1

#perguntas/configuração
if saco == 0:
	t = 10
	b = 6
else:
	t = int(input("tamanho: "))
	b = int(input("numero de bombas: "))

#criando matrixs
valores = criar_matrix(0, tam = t, list = False)

digit = "*"
visão = criar_matrix(digit, tam = t, list = False)
mostra_matrix(visão, t)

#arrumando posição para as bombas

bombas(b, t)

#aumentando os valores ao redor de bombas

for x in range(0, t):
	for y in range(0, t):
		if valores[x][y] != "b":
			lado = lados(x, y, t)
			for z in range(0, len(lado)):
				if valores[lado[z][0]][lado[z][1]] == "b":
					valores[x][y] += 1

#jogando...
while True:
	#jogada e validação de jogada
	if saco == 0:
		jx = randint(0, t-1)
		jy = randint(0, t-1)
		print(f"x e {jx+1}, y e {jy+1}")
	else:
		teste = 0
		while teste == 0:
			print("")
			jx = int(input("↓X = "))
			jy = int(input("→Y = "))
			jx -= 1
			jy -= 1
			if pos_test(jx, jy, t):
				teste = 1

	# onde foi apertado

	if valores[jx][jy] != "b":
		if valores[jx][jy] == 0:
			ared = lados(jx, jy, t)
			for v in ared:
				x = v[0]
				y = v[1]
				beta = lados(x, y, t)
				for c in beta:
					xx = c[0]
					yy = c[1]
					if visão[xx][yy] == digit:
						if valores[xx][yy] == 0:
							visão[xx][yy] = valores[xx][yy]
							ared.append(c)
						elif valores[xx][yy] != "b":
							visão[xx][yy] = valores[xx][yy]
		elif valores[jx][jy] > 0:
			visão[jx][jy] = valores[jx][jy]
			
		mostra_matrix(visão, t)

	else:
		#Derota, apertou em uma bomba
		res = "♦DERROTA♦"
		print("")
		print(f"\033[1;31m   {res} \033[m")
		mostra_matrix(valores, t, tempo = 0.2)
		break
	#verificador de vitória
	casa = 0
	for x in range(0, t):
		for y in range(0, t):
			if visão[x][y] != digit:
				casa += 1

	if casa == (t*t) - b:
		#Vitoria
		res = "♥VITÓRIA♥"
		print("")
		print(f"    {res}")
		mostra_matrix(valores, t)
		break
