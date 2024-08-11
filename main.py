from datetime import datetime, timedelta
import os
import platform

def converter_para_datetime(data_str):
    return datetime.strptime(data_str, "%d/%m/%Y")

def esta_na_semana_atual(data_str):
    # Converte a string para um objeto datetime
    data = converter_para_datetime(data_str)
    
    # Obtém a data e hora atuais
    agora = datetime.now()
    
    # Obtém a data do início da semana atual (segunda-feira)
    inicio_da_semana = agora - timedelta(days=agora.weekday())
    
    # Obtém a data do final da semana atual (domingo)
    fim_da_semana = inicio_da_semana + timedelta(days=6)
    
    # Verifica se a data fornecida está dentro do intervalo da semana atual
    return inicio_da_semana <= data <= fim_da_semana
    
def clear():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')

VENDAS = 'vendas.txt'
COMPRAS = 'compras.txt'
RELATORIOS = 'relatorios.txt'
def set_record(file_name,message):
    with open(file_name, 'a') as file:
        file.write(str(message))

def get_record(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        return content

def setVenda():
    clear()
    print('\nDigite o total da venda: ', end='')
    venda = input()
    if venda.find(','):
        venda.replace(',','.')
    try:
        float(venda)
    except:
        input('\nFormato Inválido! Digite Enter para continuar')
    else:
        confirm = input('Tem certeza? digite 1 para confirmar o valor da venda ou qualquer outra tecla para alterar o valor: ')
        if confirm != '1':
            setVenda()
        else:    
            agora = datetime.now()
            hora_atual = agora.strftime("%d/%m/%Y")
            message = venda+';'+hora_atual if os.stat(VENDAS).st_size == 0 else '\n'+venda+';'+hora_atual
            set_record(VENDAS,message)
            clear()
            input('\nVenda Cadastrada com sucesso! Digite Enter para continuar')

def setCompra():
    clear()
    print('\nDigite o total da compra: ', end='')
    compra = input()
    if compra.find(','):
        compra.replace(',','.')
    try:
        float(compra)
    except:
        input('\nFormato Inválido! Digite Enter para continuar')
    else:
        confirm = input('Tem certeza? digite 1 para confirmar o valor da venda ou qualquer outra tecla para alterar o valor: ')
        if confirm != '1':
            setCOmpra()
        else:    
            agora = datetime.now()
            hora_atual = agora.strftime("%d/%m/%Y")
            message = compra+';'+hora_atual if os.stat(COMPRAS).st_size == 0 else '\n'+compra+';'+hora_atual
            set_record(COMPRAS,message)
            clear()
            input('\nCompra Cadastrada com sucesso! Digite Enter para continuar')

def relatorioSemanal():
    clear()
    vendas = list(get_record(VENDAS).split('\n'))
    compras = list(get_record(COMPRAS).split('\n'))
    for venda in vendas:
        if not esta_na_semana_atual(venda.split(';')[1]):
            vendas.remove(venda)
    for compra in compras:
        if not esta_na_semana_atual(compra.split(';')[1]):
            compras.remove(compra)
    despesas = sum(float(x.split(';')[0]) for x in compras)
    receita = sum(float(x.split(';')[0]) for x in vendas)
    resultado = float(receita) - float(despesas)
    definicao = 'Lucro' if resultado >= 0 else 'Prejuízo' 
    print('Receita total arrecadada nessa semana até agora =', receita,'\n' + 'Total de despesas dessa semana =', '\n',despesas, '\n' + definicao + '=', '{:.2f}'.format(resultado))
    input('\nDigite Enter para continuar')

while True:
    clear()
    print('Bem Vindo ao ERP da MM Coffe, escolha uma opção abaixo:')
    print()
    print('1 - Digite um para dar baixa em uma venda\n\n2 - Digite dois para dar baixa em uma compra\n\n3 - digite três para gerar um relatório semanal\n\n4 - Digite quatro para gerar um relatório mensal\n\n5 - Digite cinco para gerar um relatório histórico geral\n\n6 - digite seis para sair\n\n')
    option = input()
    if option == '6':
        print('\n\nObrigado por usar nosso Sistema ERP!\n\n')
        break
    elif option == '1':
        clear()
        setVenda()
    elif option == '2':
        clear()
        setCompra()
    elif option == '3':
        relatorioSemanal()