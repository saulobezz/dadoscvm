import pandas as pd
import os

# POR EMPRESA CODIGO CVM CD_CVM
tipos = ['bpa','bpp','dfc_md','dfc_mi','dmpl','dre','dva']
listas = ['itr', 'dfp']

def empresa():
    print('Separando por empresas...')
    codigo_cvm = []
    for lts in listas:
        for tps in tipos:
            df = pd.read_csv('./zips/final_%s/%s_%s.csv' % (lts,tps,lts), sep=';', encoding='iso-8859-1')
            for cd in df['CD_CVM']:
                codigo_cvm.append(cd)

    cdcvm = list(dict.fromkeys(codigo_cvm))
    for lts in listas:
        for tps in tipos:
            df = pd.read_csv('./zips/final_%s/%s_%s.csv' % (lts,tps,lts), sep=';', encoding='iso-8859-1')
            for cd in cdcvm:
                os.makedirs('./zips/cias/%s/%s' % (lts, cd), exist_ok = True)
                frame = df.query('CD_CVM == @cd')
                frame.to_csv('./zips/cias/%s/%s/%s.csv' % (lts,cd,tps), sep=';', encoding='iso-8859-1',index=False,float_format='%.0f')
empresa()
print("Criados arquivos por empresa")
print("Acessar ZIPS/CIAS/ ITR OU DFP E ESCOLHER A EMPRESA POR CÓDIGO CVM")
input("Press enter to exit")
