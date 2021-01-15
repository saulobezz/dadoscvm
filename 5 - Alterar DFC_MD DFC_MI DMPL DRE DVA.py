import pandas as pd
import os

# ALTERAR CSVS DFC_MD DFC_MI DMPL DRE DVA

def altera_dfc_md_dfc_mi_dmpl_dre_dva():
    listas = ['dfp','itr']
    tipos = ['dfc_md','dfc_mi','dmpl','dre','dva']
    for lts in listas:
        for tps in tipos:
            for ano in range(2010,2021):
                url = './zips/%s/%s/%s_cia_aberta_%s_con_%d.csv' % (lts,lts,lts,tps,ano)
                if os.path.isfile(url):
                    print('Arquivo existe:', lts, tps, ano,'Alterando')
                else:
                    print('Arquivo não existe:', lts, tps, ano)
                    continue
                df = pd.read_csv(url, sep=';', encoding='iso-8859-1',usecols=('CD_CVM','DENOM_CIA', 'CD_CONTA', 'DS_CONTA', 'VL_CONTA', 'DT_REFER', 'DT_INI_EXERC','DT_FIM_EXERC','VERSAO'),float_precision='round_trip')
                df.to_csv('./zips/dfs/%s/%s/%s_%s_%d.csv' % (lts,tps,lts,tps,ano), sep=';', encoding='iso-8859-1',index=False,columns=['CD_CVM','DENOM_CIA','CD_CONTA','DS_CONTA','VL_CONTA','DT_REFER','DT_INI_EXERC','DT_FIM_EXERC','VERSAO'],float_format='%.0f')
                print('Arquivo: ', lts, tps, ano, 'Alerado')
altera_dfc_md_dfc_mi_dmpl_dre_dva()
print('Alterações feita...')
print("Executar: 6 - Concatenar csvs")
input("Press enter to exit")
