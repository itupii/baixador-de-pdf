#                                               IMPORTS
from csv import reader
import PyPDF2
from ast import If
from datetime import date
import webbrowser
from googletrans import Translator 
import requests

#                                               TRATAMENTO DE DATA
trad = Translator()
today = date.today()

# dia = today.strftime('%d')
# mouth = today.strftime('%B')
# mes = trad.translate(mouth,dest="pt").text
# ano = today.strftime('%Y')

dia = '07'
mes = 'Setembro'
ano = '2022'

#                                               TRATAMENTO DE CADERNO

tipos_caderno= ['cidade','exec1','exec2']

#                                               FUNÇÃO DOWNLOAD DO PDF

def baixar_pdf(url ,endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open (endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Download finalizado salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()
        
#                                           Download e alocação dos pdf por caderno em pastas
print('\nCaderno: Cidade')
qt_pag_cidade = int(input('Digite a quantidade de paginas : '))
print('\nCaderno: Executivo 1')
qt_pag_exec1 = int(input('Digite a quantidade de paginas : '))
print('\nCaderno: Executivo 2')
qt_pag_exec2 = int(input('Digite a quantidade de paginas : '))


for caderno in tipos_caderno:
    if caderno == tipos_caderno[0]:
        print(f'\nEsse é pra ser o caderno "Cidade", Recebo: {caderno}\n')

        a = 0
        while a < qt_pag_cidade:
            a = a + 1
            b = str(a)
            num = b.zfill(4)
            url = f'http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{mes}/{dia}/{caderno}/pdf/pg_{num}.pdf'
            # print(url)
            baixar_pdf(url, f'CIDADE_pag_{num}')
    if caderno == tipos_caderno[1]:
        print(f'\n Esse é pra ser o caderno "Exec1", Recebo: {caderno}\n')

        a = 0
        while a < qt_pag_exec1:
            a = a + 1
            b = str(a)
            num = b.zfill(4)
            url = f'http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{mes}/{dia}/{caderno}/pdf/pg_{num}.pdf'
            # print(url)
            baixar_pdf(url, f'EXERC1_pag_{num}')
    
    if caderno == tipos_caderno[-1]:
        print(f'\n Esse é pra ser o caderno "Exec2", Recebo: {caderno}\n')
        
        a = 0
        while a < qt_pag_exec2:
            a = a + 1
            b = str(a)
            num = b.zfill(4)
            url = f'http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{mes}/{dia}/{caderno}/pdf/pg_{num}.pdf'
            # print(url)
            baixar_pdf(url, f'EXERC2_pag_{num}')

#                                               Aqui é possivel conferir o PDF pelo terminal- Descomente e teste

# a = 0
# while a < qt_pag:
#     a = a + 1
#     b = str(a)
#     num = b.zfill(4)
# #                                               TRATAMENTO DE PDF
#     pdf = open(f'PDF/PDF_CIDADE/pag_{num}', 'rb')
#     reader = PyPDF2.PdfFileReader(pdf)
#     pagina = reader.getPage(0)

#     print(f'-==--=-=-=-=-=-=-=-=-==--=-=-=-PAGINA PAG_{num} -==--=-=-=-=-=-=-=-=-==--=-=-=-')
#     print(pagina.extractText())
