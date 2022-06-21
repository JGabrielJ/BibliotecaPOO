import PySimpleGUI as sg
from datetime import datetime, timedelta


logins = open('login.txt', 'rt')
listalogins = logins.read().split('\n')

usuarios = {}
for login in listalogins:
    usuarios[login.split('-')[0]] = login.split('-')[1]

listaAlugados = []
informacoesLivro = {}

livroAlugado = None
situacoes = ['Disponível', 'Alugado', 'Inexistente']


class Usuarios:
    def __init__(self, usuario, senha):
        logins = open('login.txt', 'at')
        logins.write(f'\n{usuario}-{senha}')
        logins.close()


class Alugar:
    def __init__(self, nome):
        self.nome = nome
        informacoesLivro['nome'] = self.nome

    def alugado(self):
        self.horario = datetime.now() - timedelta(hours=3)
        self.devolucao = self.horario + timedelta(days=7)
        print(f'Você alugou o livro {self.nome} no dia {self.horario.strftime("%d/%m/%Y")}!\nDia da devolução: {self.devolucao.strftime("%d/%m/%Y")}\n')

        informacoesLivro['horario'] = self.horario
        informacoesLivro['devolucao'] = self.devolucao
        listaAlugados.append(informacoesLivro.copy())
        informacoesLivro.clear()


class Livros:
    def __init__(self, foto='imagens/livro0.png', titulo='', autor='', genero='', codigo='', situacao=situacoes[2]):
        self.foto = foto
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.codigo = codigo
        self.situacao = situacao


livro0 = Livros()
livro1 = Livros(
    foto='imagens/livro1.png',
    titulo='A Cabana',
    autor='William P. Young',
    genero='Romance, Romance Cristão, Suspense, Ficção Religiosa',
    codigo='978-8599296363',
    situacao=situacoes[0]
)
livro2 = Livros(
    foto='imagens/livro2.png',
    titulo='Ed & Lorraine Warren: Demonologistas',
    autor='Gerald Brittle',
    genero='Biografia, Literatura Cristã',
    codigo='978-8594540164',
    situacao=situacoes[0]
)
livro3 = Livros(
    foto='imagens/livro3.png',
    titulo='H. H. Holmes: Maligno - O Psicopata da Cidade Branca',
    autor='Harold Schechter',
    genero='Romance Policial, Mistério, Suspense',
    codigo='978-6555980097',
    situacao=situacoes[0]
)
livro4 = Livros(
    foto='imagens/livro4.png',
    titulo='O Colecionador',
    autor='John Fowles',
    genero='Suspense Psicológico',
    codigo='978-8594541086',
    situacao=situacoes[0]
)
livro5 = Livros(
    foto='imagens/livro5.png',
    titulo='O Mal Nosso de Cada Dia',
    autor='Donald Ray Pollock',
    genero='Crime, Ficção, Suspense, Mistério',
    codigo='978-8594541864',
    situacao=situacoes[0]
)

listaLivros = [livro0, livro1, livro2, livro3, livro4, livro5]


class TelaLogin:
    def __init__(self):
        sg.theme('BrownBlue')

        self.layout = [
            [sg.Text('Digite as informações solicitadas:', key='status')],
            [sg.Text('Usuário:', size=(7, 0)), sg.Input(size=(37, 0), expand_y=True, key='nome')],
            [sg.Text('Senha:', size=(7, 0)), sg.Input(size=(37, 0), expand_y=True, password_char='*', key='senha')],
            [sg.Button('Fazer Login', size=(10, 0)), sg.Button('Cadastrar-se', size=(10, 0))]
        ]

        self.window = sg.Window('Simulador de Biblioteca Virtual', size=(370, 130)).layout(self.layout)


class Biblioteca():
    def __init__(self):
        global listaLivros

        self.lista = []
        for livro in listaLivros:
            self.lista.append(livro.titulo)

        sg.theme('BrownBlue')

        self.options = [
            [sg.Text('Selecione um livro:', size=(15, 0)), sg.Combo(self.lista, size=(53, 0), expand_y=True, key='selec'), sg.Button('🔍', size=(3, 0))],
            [sg.Text('Título do Livro:', size=(15, 0)), sg.Text('', size=(60, 0), text_color='#000000', background_color='#a6b2be', key='titulo')],
            [sg.Text('Autor do Livro:', size=(15, 0)), sg.Text('', size=(60, 0), text_color='#000000', background_color='#a6b2be', key='autor')],
            [sg.Text('Gênero do Livro:', size=(15, 0)), sg.Text('', size=(60, 0), text_color='#000000', background_color='#a6b2be', key='genero')],
            [sg.Text('Código do Livro:', size=(15, 0)), sg.Text('', size=(60, 0), text_color='#000000', background_color='#a6b2be', key='codigo')],
            [sg.Button('Alugar Livro'), sg.Button('Devolver Livro'), sg.Button('Verificar Data'), sg.Text('Situação do Livro:'), sg.Text('', key='situacao')]
        ]

        self.layout = [
            [sg.Text('Seja bem-vindo(a) à nossa Biblioteca Virtual!', size=(720, 0), justification='center')],
            [sg.HorizontalSeparator()],
            [sg.Image('imagens/livro0.png', size=(100, 150), key='foto'), sg.Column(self.options)],
            [sg.Output(size=(95, 15), key='saida')]
        ]

        self.window = sg.Window('Simulador de Biblioteca Virtual', size=(720, 480)).layout(self.layout)


semJuros = True
rentBook = True
openLibrary = True

juros = 0
horarioMOD = datetime.now()

tela_login = TelaLogin()
while True:
    tela_login.event, tela_login.values = tela_login.window.Read()

    if (tela_login.event == sg.WIN_CLOSED):
        openLibrary = False
        break

    if (tela_login.values['nome'] in usuarios.keys() and tela_login.values['senha'] == usuarios[tela_login.values['nome']]):
        if (tela_login.event == 'Fazer Login'):
            tela_login.window['status'].update('Login efetuado com sucesso!')
            break
        if (tela_login.event == 'Cadastrar-se'):
            tela_login.window['status'].update('Usuário já está cadastrado! Faça login para prosseguir...')
    if (tela_login.values['nome'] not in usuarios.keys() or tela_login.values['senha'] != usuarios[tela_login.values['nome']]):
        if (tela_login.event == 'Fazer Login'):
            tela_login.window['status'].update('Usuário não encontrado! Cadastre-se para prosseguir...')
        if (tela_login.event == 'Cadastrar-se'):
            novo_usuario = Usuarios(tela_login.values['nome'], tela_login.values['senha'])
            tela_login.window['status'].update('Cadastro efetuado com sucesso!')
            break

if (openLibrary):
    biblioteca = Biblioteca()
    while True:
        biblioteca.event, biblioteca.values = biblioteca.window.Read()

        if (biblioteca.event == sg.WIN_CLOSED):
            break

        if (biblioteca.event == '🔍'):
            if (biblioteca.values['selec'] not in biblioteca.lista or biblioteca.values['selec'] == biblioteca.lista[0]):
                biblioteca.window['foto'].update(livro0.foto)
                biblioteca.window['titulo'].update(livro0.titulo)
                biblioteca.window['autor'].update(livro0.autor)
                biblioteca.window['genero'].update(livro0.genero)
                biblioteca.window['codigo'].update(livro0.codigo)
                biblioteca.window['situacao'].update(livro0.situacao)

            if (biblioteca.values['selec'] == biblioteca.lista[1]):
                biblioteca.window['foto'].update(livro1.foto)
                biblioteca.window['titulo'].update(livro1.titulo)
                biblioteca.window['autor'].update(livro1.autor)
                biblioteca.window['genero'].update(livro1.genero)
                biblioteca.window['codigo'].update(livro1.codigo)
                biblioteca.window['situacao'].update(livro1.situacao)

            if (biblioteca.values['selec'] == biblioteca.lista[2]):
                biblioteca.window['foto'].update(livro2.foto)
                biblioteca.window['titulo'].update(livro2.titulo)
                biblioteca.window['autor'].update(livro2.autor)
                biblioteca.window['genero'].update(livro2.genero)
                biblioteca.window['codigo'].update(livro2.codigo)
                biblioteca.window['situacao'].update(livro2.situacao)

            if (biblioteca.values['selec'] == biblioteca.lista[3]):
                biblioteca.window['foto'].update(livro3.foto)
                biblioteca.window['titulo'].update(livro3.titulo)
                biblioteca.window['autor'].update(livro3.autor)
                biblioteca.window['genero'].update(livro3.genero)
                biblioteca.window['codigo'].update(livro3.codigo)
                biblioteca.window['situacao'].update(livro3.situacao)

            if (biblioteca.values['selec'] == biblioteca.lista[4]):
                biblioteca.window['foto'].update(livro4.foto)
                biblioteca.window['titulo'].update(livro4.titulo)
                biblioteca.window['autor'].update(livro4.autor)
                biblioteca.window['genero'].update(livro4.genero)
                biblioteca.window['codigo'].update(livro4.codigo)
                biblioteca.window['situacao'].update(livro4.situacao)

            if (biblioteca.values['selec'] == biblioteca.lista[5]):
                biblioteca.window['foto'].update(livro5.foto)
                biblioteca.window['titulo'].update(livro5.titulo)
                biblioteca.window['autor'].update(livro5.autor)
                biblioteca.window['genero'].update(livro5.genero)
                biblioteca.window['codigo'].update(livro5.codigo)
                biblioteca.window['situacao'].update(livro5.situacao)

        if (biblioteca.event == 'Alugar Livro'):
            if (biblioteca.values['selec'] not in biblioteca.lista or biblioteca.values['selec'] == biblioteca.lista[0]):
                print(f'O livro {biblioteca.values["selec"]} não existe!\n')

            for livro in listaLivros:
                if (livro.titulo == biblioteca.values["selec"]):
                    if (livro.situacao == situacoes[0]):
                        rentBook = True
                        break
                    if (livro.situacao == situacoes[1]):
                        print(f'O livro {biblioteca.values["selec"]} já foi alugado!\n')
                        rentBook = False
                        break
                    if (livro.situacao == situacoes[2]):
                        rentBook = False
                        break

            if (biblioteca.values['selec'] in biblioteca.lista):
                if (rentBook):
                    livroAlugado = Alugar(biblioteca.values['selec'])
                    livroAlugado.alugado()

                    for livro in listaLivros:
                        if (livro.titulo == biblioteca.values['selec']):
                            livro.situacao = situacoes[1]
                            biblioteca.window['situacao'].update(livro.situacao)
                            break

        if (biblioteca.event == 'Devolver Livro'):
            if (biblioteca.values['selec'] not in biblioteca.lista or biblioteca.values['selec'] == biblioteca.lista[0]):
                print(f'O livro {biblioteca.values["selec"]} não existe!\n')

            for livro in listaLivros:
                if (livro.titulo == biblioteca.values["selec"]):
                    if (livro.situacao == situacoes[0]):
                        print(f'O livro {biblioteca.values["selec"]} não foi alugado ainda!\n')
                        break
                    if (livro.situacao == situacoes[1]):
                        if (semJuros):
                            livro.situacao = situacoes[0]
                            biblioteca.window['situacao'].update(livro.situacao)
                            print('Obrigado por devolver o livro!\n')

                            horarioMOD = datetime.now()
                        else:
                            livro.situacao = situacoes[0]
                            biblioteca.window['situacao'].update(livro.situacao)
                            print(f'Obrigado por devolver o livro! Sua multa é de R${juros},00!\n')

                            juros = 0
                            horarioMOD = datetime.now()

        if (biblioteca.event == 'Verificar Data'):
            if (listaAlugados != []):
                horarioMOD += timedelta(days=1)
                print(f'Você está no dia {horarioMOD.strftime("%d/%m/%Y")}')

                for livroAL in listaAlugados:
                    if (livroAL['nome'] == biblioteca.values['selec']):
                        if (horarioMOD.strftime('%d/%m/%Y') < livroAL['devolucao'].strftime('%d/%m/%Y')):
                            semJuros = True
                            d = livroAL['devolucao'].day - horarioMOD.day
                            print(f'Faltam {d} dias para você devolver o livro {livroAL["nome"]}.\n')
                            break
                        if (horarioMOD.strftime('%d/%m/%Y') == livroAL['devolucao'].strftime('%d/%m/%Y')):
                            semJuros = True
                            print(f'Hoje é o dia de você devolver o livro {livroAL["nome"]}.\n')
                            break
                        if (horarioMOD.strftime('%d/%m/%Y') > livroAL['devolucao'].strftime('%d/%m/%Y')):
                            juros += 1
                            semJuros = False
                            d = horarioMOD.day - livroAL['devolucao'].day
                            print(f'Já se passaram {d} dias e você ainda precisa devolver o livro {livroAL["nome"]}.\nPortanto, foi adicionado mais R$1,00 ao valor total de sua multa!\n')
                            break
