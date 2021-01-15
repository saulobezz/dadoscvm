import shutil as shl
import zipfile as zf
import os

# DESCOMPACTAR
def descompactar():
    cvm_lista = ['dfp','itr']
    tipos = ['bpa', 'bpp', 'dfc_md', 'dfc_mi', 'dmpl', 'dre', 'dva']
    print('Descompactando...')
    for cvm_lts in cvm_lista:
        for ano in range(2010,2021):
            if os.path.isfile('./zips/%s/' % cvm_lts + '%s_cia_aberta_%d.zip' % (cvm_lts,ano)):
                with zf.ZipFile('./zips/%s/' % cvm_lts + '%s_cia_aberta_%d.zip' % (cvm_lts,ano), 'r') as zip_ref:
                    print('Arquivo existe:', '%s_cia_aberta_%d.zip' % (cvm_lts,ano))
                    zip_ref.extractall('./zips/%s/%s/' % (cvm_lts,cvm_lts))
                    for tps in tipos:
                        shl.copy('./zips/%s/%s/' % (cvm_lts,cvm_lts) + '%s_cia_aberta_%s_con_%d.csv' % (cvm_lts,tps,ano),'./zips/%s/%s/%s_con' % (cvm_lts,cvm_lts,cvm_lts))
                        continue
            else:
                print('Arquivo nao existe:', '%s_cia_aberta_%d.zip' % (cvm_lts,ano))
                continue
    print('Descompactado feito...')
descompactar()
print('Descompactação feita...')
print("Executar: 4 - Alterar BPA e BPP")
input("Press enter to exit")
