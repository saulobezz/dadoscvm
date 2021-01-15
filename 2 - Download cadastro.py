import requests

# DOWNLOAD CADASTRO DAS CIAS ABERTAS
cvm_url = 'http://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv'
def cadastrados():
    print('Download lista de Cias Abertas...')
    response = requests.get(cvm_url)
    if response.status_code == requests.codes.OK:
        with open('./zips/cad_cia_aberta.csv', 'wb') as fp:
            fp.write(response.content)
cadastrados()
print('Download feito...')
print("Executar: 3 - Descompactar")
input("Press enter to exit")

