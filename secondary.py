import schedule
import time
from datetime import date
from datetime import datetime, timedelta


logins = open('loginss.txt')
listalogins = logins.readlines()

class Usuários:
    def __init__(self, nome, senha):
        logins = open('loginss.txt', 'a')
        logins.write('\n{}\n{}'.format(nome, senha))
        print('\nCadastro realizado com sucesso\n')
        logins.close()
##############################
pergunta = input("Deseja cadastrar um novo usuário ou fazer um login?\n")
while pergunta != "login" and pergunta != 'cadastrar':
  pergunta = input('Digite "login" ou "cadastrar"\n')
mr = 1
mr2 = 0

if pergunta == 'login' and listalogins == []:
  print('Cadastre-se Primeiro :)')
  exit()

if pergunta == 'login':
  for x in range(0, len(listalogins)):
    while mr == 1:
      nome = input('Digite seu nome de usuário\n')
      senha = input('Digite sua senha\n')
      if nome in listalogins[x] and senha in listalogins[x+1]:
        print(f'usuário logado com sucesso Bem vindo(a) {nome}')
        mr = 0
      if nome not in listalogins and senha not in listalogins:
        pass
        

if pergunta == 'cadastrar' and listalogins == []:
    nome = input('\nDigite um nome de usuário: ').strip()
    senha = input(f'\nMuito bem {nome} agora digite uma senha de seu agrado: ').strip()
    Usuários(nome, senha)

elif pergunta == 'cadastrar':
  for x in range(0, len(listalogins)):
    while mr2 == 0:
      nome = input('\nDigite um nome de usuário: ')
      if nome not in listalogins[x]:
        senha = input(f'\nMuito bem {nome} agora digite uma senha de seu agrado: ').strip()
        Usuários(nome, senha)
        mr2 = 1
      else:
        print('\nNome de usuário já existente... Digite um nome disponível por favor')
  

horario = 0
devolucao = 0
dnvv = 'SIM'
listaL = []

while dnvv == 'SIM':
  # Lendo o arquivo onde tem os livros
  def lerArquivo(arqName, modRead):
    global arq
    arq = open(arqName, modRead)
    return arq.read()
    arq.close()
  cont = lerArquivo('livros.txt', 'rt')
    

  # classe de alugar os livros
  class Alugar:
    # Pega o nome do livro
    def __init__(self, nome):
      self.nome = nome
      # Salva o livro na lista
      listaL.append(self.nome)

    def alugado(self):
      # realmente salva o horario em que o livro foi alugado
      global devolucao
      global horario
      self.horario = datetime.now() - timedelta(hours=3)
      devolucao = self.horario + timedelta(days=7)
      print('\nVocê alugou o(s) livro(s)', listaL, 'no dia', self.horario.strftime('%d/%m/%Y'' ás %H:%M:%S.'), '\nDia da devolução:', devolucao.strftime('%d/%m/%Y\n'))
  
  x = 0
  quantidade = int(input("Quantos livros você vai alugar? "))
  while x < quantidade:
    x = x + 1
    while True:
      Livro = str(input('Qual nome do livro que você deseja? '))
      if Livro in cont:
        LivrosAL = Alugar(Livro)
        break
      else:
        print("Esse livro não se encontra no sistema! Tente Novamente!")

  LivrosAL.alugado()

  horarioMOD = datetime.now()
  juros = 0
  y = 0
    
  def verificar():
    global juros
    global y
    global horarioMOD
    horarioMOD = horarioMOD + timedelta(days=1)
    print('Dia ' + horarioMOD.strftime('%d') + '...\n')
    if horarioMOD.strftime('%d/%m/%Y') == devolucao.strftime('%d/%m/%Y'):
      print('Prezado Sr(a).'+nome+'! Dia ' + horarioMOD.strftime('%d/%m/%Y') + ' você precisa devolver o(s) livro(s)', listaL)
      dnv = input('Digite |Sim| para devolver o(s) livro(s)!\nDigite |Nao| para permanecer com o(s) livro(s)! (Sujeito a juros!)').strip().upper()
      if dnv == 'SIM':
        print('Obrigado por devolver os livros! Volte Sempre!')
        y = 1
    elif horarioMOD.strftime('%d/%m/%Y') > devolucao.strftime('%d/%m/%Y'):
      juros = juros + 1
      print('Prezado Sr(a).'+nome+'! Já é dia ' + horarioMOD.strftime('%d/%m/%Y') + ' você ainda precisa devolver o(s) livro(s)', listaL, '\nFoi adicionado mais +R$ 1,00 de juros!\n')
      dnv = input('Digite |Sim| para devolver o(s) livro(s)!\nDigite |Nao| para permanecer com o(s) livro(s)! (Sujeito a juros!)').strip().upper()
      if dnv == 'SIM':
        print(f'Obrigado por devolver os livros, seu juros foi de R${juros},00. Volte sempre!')
        y = 1

  schedule.every(1).seconds.do(verificar)
  while y == 0:
    schedule.run_pending()
  dnvv = input('Você deseja alugar mais livros?\n\nDigite |Sim| para alugar mais livros.\nDigite |Não| para sair da biblioteca.').strip().upper()
print('Obrigado por visitar nossa Biblioteca Virtual! Volte sempre!')