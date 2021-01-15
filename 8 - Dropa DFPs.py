import pandas as pd

# DROPAR LINHAS DFPSs
def drop_dfps():
    print('Apagando linhas duplicadas dos DFPs...')
    tipos1 = ['bpa','bpp']
    for tps in tipos1:
        df = pd.read_csv('./zips/dfs/concats/%s/%s_dfp_all.csv' % (tps,tps), sep=';', encoding='iso-8859-1')
        frame = df.sort_values(by=['DT_REFER','DT_FIM_EXERC','VERSAO']).drop_duplicates(subset=['DENOM_CIA','CD_CONTA','DS_CONTA','DT_FIM_EXERC'],keep='last')
        frame.to_csv('./zips/final_dfp' + '/%s_dfp.csv'% (tps), sep=';', encoding='iso-8859-1',index=False,columns=['DT_FIM_EXERC','CD_CVM','DENOM_CIA','CD_CONTA','DS_CONTA','VL_CONTA'],float_format='%.0f')
    print ("Arquivos Feitos... DROPAR LINHAS DFPSs CONCATENADOS BPA BPP")

    tipos2 = ['dfc_md','dfc_mi','dmpl','dre','dva']
    for tps in tipos2:
        df = pd.read_csv('./zips/dfs/concats/%s/%s_dfp_all.csv' % (tps,tps), sep=';', encoding='iso-8859-1')
        frame = df.sort_values(by=['DT_REFER','DT_INI_EXERC','DT_FIM_EXERC','VERSAO']).drop_duplicates(subset=['DENOM_CIA','CD_CONTA','DS_CONTA','DT_FIM_EXERC'],keep='last')
        frame.to_csv('./zips/final_dfp' + '/%s_dfp.csv'% (tps), sep=';', encoding='iso-8859-1',index=False,columns=['DT_FIM_EXERC','CD_CVM','DENOM_CIA','CD_CONTA','DS_CONTA','VL_CONTA'],float_format='%.0f')
    print ("Arquivos Feitos... DROPAR LINHAS DFPs CONCATENADOS DFC_MD DFC_MI DMPL DRE DVA")
drop_dfps()
print("Linhas Duplicadas Apagadas")
print("Executar: 9 - Empresas")
input("Press enter to exit")
