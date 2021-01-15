import requests
import os

# DOWNLOAD DFP ITR FRE FCA
def download():
    cvm_lista = ['dfp','itr','fre','fca']
    cvm_url = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/%s/DADOS/%s_cia_aberta_%d.zip'

    print('Verificando existencia de arquivos...')
    print('Fazendo Download...')
    for cvm_lts in cvm_lista:
        for ano in range(2010,2021):
            response = requests.get(cvm_url % (cvm_lts,cvm_lts,ano))
            print (response)
            if response.status_code == requests.codes.OK:
                print('Download:','./zips/%s/%s_cia_aberta_%d.zip' % (cvm_lts,cvm_lts,ano))
                with open('./zips/%s/%s_cia_aberta_%d.zip' % (cvm_lts,cvm_lts,ano), 'wb') as fp:
                    fp.write(response.content)
download()
print("Download feito...")
print("Executar: 2 - Download cadastro")
input("Press enter to exit")
