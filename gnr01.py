import tkinter as tk
import tkinter.simpledialog
from random import randint
import time
import pdb;

# Variáveis Globais
janela = tk.Tk()
geracaoEmAndamento = False
numerosGerados = []
listaRotulos = []

#----- PAGINAS -----

# Funções para Páginas
def mostrarPagina(pagina):
    for p in [pagina01, pagina02, pagina03]:
        p.pack_forget()
    pagina.pack()

def fecharPagina():
    janela.destroy()

# Funções para Página 01
def mostrarPagina02():
    mostrarPagina(pagina02)

def mostrarPagina03():
    mostrarPagina(pagina03)


#----- DEFINICOES DA JANELA -----

# Definições da Janela
janela.title("Gerador De Numero Real")
janela.geometry("360x540")

#----- PAGINAS COMO WIDGETS FREME -----

pagina01 = tk.Frame(janela)
pagina02 = tk.Frame(janela)
pagina03 = tk.Frame(janela)

#----- FIM PAGINAS COMO WIDGETS FREME -----

#----- INICIO DA JANELA 01 -----

# Adiciona um rótulo à pagina01
rotulo01 = tk.Label(pagina01, text="Gerador De Numero Real 1.1")
rotulo01.pack(pady=10)

# Criar botão para iniciar - ir para outra pagina.
botaoIniciar = tk.Button(pagina01, text="Iniciar", command=mostrarPagina02)
botaoIniciar.pack(pady=10)

# Criar botão para creditos - ir para outra pagina.
botaoCreditos = tk.Button(pagina01, text="Creditos", command=mostrarPagina03)
botaoCreditos.pack(pady=10)

# Cria um botão para fechar a pagina01
botaoFechar = tk.Button(pagina01, text="Fechar", command=fecharPagina)
botaoFechar.pack(pady=10)

# Inicialmente, mostra a primeira página
mostrarPagina(pagina01)

#----- FINAL DA JANELA 01 -----

#----- INICIO DA JANELA 02 -----

# Variável global para armazenar o rótulo de números
rotuloNumeros = None

# Variáveis globais
geracaoEmAndamento = False
numerosGerados = []
i = None

# Adiciona um rótulo à pagina02
rotulo02 = tk.Label(pagina02, text="Gerar Números")
rotulo02.grid(row=0, column=0, padx=10, pady=5)

def reativarBotaoGerar():
    # Reativa o botão A após 3+1 segundos
    botaoGerar.config(state=tk.NORMAL)
    

def iniciarCronometro():

    # Inicializa o tempo restante (em segundos)
    tempoRestante = 4

    def atualizarCronometro():
        nonlocal tempoRestante
        if tempoRestante > 0:
            tempoRestante -= 1
            rotuloCronometro.config(text=f"Tempo restante: {tempoRestante} segundos")
            # Atualiza o cronômetro a cada segundo
            janela.after(1000, atualizarCronometro)
        
        else:
            rotuloCronometro.config(text="Gerador Liberado!")
            # Quando o tempo acabar, reativa o botão A
            reativarBotaoGerar()

    # Inicia o cronômetro
    atualizarCronometro()

# Rótulo para exibir o cronômetro
rotuloCronometro = tk.Label(pagina02, text="Gerador Liberado!")
rotuloCronometro.grid(row=1, column=0, pady=(10, 0))
#rotuloCronometro.pack(pady=(10, 0))

# Função para gerar 2 números aleatórios
def gerarA():
    return ''.join(str(randint(0, 9)) for _ in range(2))

# Função para gerar 8 números aleatórios
def gerarB():
    return ''.join(str(randint(0, 9)) for _ in range(8))

# Adiciona um rótulo em branco antes de mostrar os números gerados
rotuloEspaco = tk.Label(pagina02, text="\n".join([""] * 10))
rotuloEspaco.grid(row=3, column=0, pady=1)

# Adiciona um rótulo para exibir os números gerados
aler = tk.Label(pagina02, text="Nenhum número gerado!")
aler.grid(row=3, column=0, pady=(15, 5))

def copiarNumero(numero):
    janela.clipboard_clear()
    janela.clipboard_append(numero)
    janela.update()

# Função para gerar 10 números usando a lógica fornecida
def gerarNumeros():
    global geracaoEmAndamento, numerosGerados, listaRotulos

    botaoGerar.config(state=tk.DISABLED)
    iniciarCronometro()
    janela.after(5000, reativarBotaoGerar)

    if not geracaoEmAndamento:
        geracaoEmAndamento = True
        wtsBr = "wa.me/55"
        digBr = "9"
        numerosGerados = [wtsBr + gerarA() + digBr + gerarB() for _ in range(10)]
        listaRotulos = []

        rotuloEspaco.config(text="")
        aler.config(text="")

        for i, numero in enumerate(numerosGerados):
            nomeRotulo = f"rotuloNumeros{i + 1}"
            rowPosition = 3 + i
            rotuloNumeros = tk.Label(pagina02, text=numero, name=nomeRotulo)
            rotuloNumeros.grid(row=rowPosition, column=0, pady=2)
            
            # Adiciona o rótulo à lista
            listaRotulos.append(rotuloNumeros)

            botaoCopiarTodos.grid(row=i + 4, column=0, pady=10)
            botaoLimpar.grid(row=i + 5, column=0, pady=10)
            botaoInicio02.grid(row=i + 6, column=0, padx=10, pady=10)
            botaoFechar02.grid(row=i + 7, column=0, padx=10, pady=10)


            # Adiciona evento de clique para cada rótulo
            rotuloNumeros.bind("<Button-1>", lambda event, num=numero: copiarNumero(num))

        if numerosGerados:
            botaoCopiarTodos.config(state=tk.NORMAL)
            botaoLimpar.config(state=tk.NORMAL)
        else:
            rotuloNumeros.config(text="Nenhum número gerado!")
            botaoLimpar.config(state=tk.DISABLED)
            botaoCopiarTodos.config(state=tk.DISABLED)


    geracaoEmAndamento = False


# Criar botão para Nmr Brasil - ir para outra pagina.
botaoGerar = tk.Button(pagina02, text="Gerar", command=gerarNumeros)
botaoGerar.grid(row=2, column=0, padx=10, pady=5)
#botaoGerar.pack(pady=(0, 20))

def voltarEstado():
    botaoCopiarTodos.config(state=tk.NORMAL, text="Copiar Todos")

def copiarTodosNumeros():
    numeros_concatenados = "\n".join(numerosGerados)
    janela.clipboard_clear()
    janela.clipboard_append(numeros_concatenados)
    janela.update()
    botaoCopiarTodos.config(text="Texto Copiado", state=tk.DISABLED)
    janela.after(3000, lambda: voltarEstado())


# Criar botão para copiar todos os numeros.
botaoCopiarTodos = tk.Button(pagina02, text="Copiar Todos", command=copiarTodosNumeros, state=tk.DISABLED)
botaoCopiarTodos.grid(row=4, column=0, pady=10)


# Função para limpar os números gerados
def limparNumeros():
    global numerosGerados, geracaoEmAndamento

    numerosGerados = []
    geracaoEmAndamento = False

    # Limpar rótulos de números e adicionar espaço em branco
    for rotulo in listaRotulos:
        rotulo.destroy()

    # Adiciona um rótulo para indicar que nenhum número foi gerado
    rotuloEspaco.config(text="\n".join([""] * 10))
    aler.config(text="Nenhum Numero Gerado!")
    
    # Corrigindo a adição dos widgets à lista
    listaRotulos.extend([aler, rotuloEspaco])

    # Desabilitar o botão "Copiar" e "Limpar"
    botaoLimpar.config(state=tk.DISABLED)
    botaoCopiarTodos.config(state=tk.DISABLED)


# Adiciona um botão "Limpar"
botaoLimpar = tk.Button(pagina02, text="Limpar", command=limparNumeros, state=tk.DISABLED)
botaoLimpar.grid(row=5, column=0, pady=10)
#botaoLimpar.pack(pady=10)

# Adiciona um botão "Voltar ao Início"
botaoInicio02 = tk.Button(pagina02, text="Voltar Ao Inicio", command=lambda: mostrarPagina(pagina01))
botaoInicio02.grid(row=6, column=0, padx=10, pady=10)
#botaoInicio02.pack(side=tk.LEFT, padx=10, pady=10)

# Adiciona um botão "Fechar"
botaoFechar02 = tk.Button(pagina02, text="Fechar", command=fecharPagina)
botaoFechar02.grid(row=7, column=0, padx=10, pady=10)
#botaoFechar.pack(side=tk.RIGHT, padx=10, pady=10)

#----- FINAL DA JANELA 02 -----


#----- INICIO DA JANELA 03 -----

# Adiciona um rótulo à pagina03
rotulo03 = tk.Label(pagina03, text="CREDITOS")
rotulo03.pack(pady=10)

texto01 = tk.Label(pagina03, text="Versao:1.1")
texto01.pack(pady=10)

texto02 = tk.Label(pagina03, text="Criador: Davi Menezes")
texto02.pack(pady=10)

texto03 = tk.Label(pagina03, text="Uso livre, foda-se os direitos autorais! \n\nSe tiver afim de ajudar dando money, fique a vontade. \nMas se foda pra achar nossa carteira. \n\nFavor se for usar o codigo fonte, deixa os creditos!")
texto03.pack(pady=10)

# Criar botão para inicio - ir para outra pagina.
botaoInicio03 = tk.Button(pagina03, text="Voltar Ao Inicio", command=lambda: mostrarPagina(pagina01))
botaoInicio03.pack(pady=10)

#----- FINAL DA JANELA 03 -----

#----- INICIO DA JANELA -----
#----- FINAL DA JANELA -----

janela.mainloop()