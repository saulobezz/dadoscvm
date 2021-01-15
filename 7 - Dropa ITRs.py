import pandas as pd

# DROPAR LINHAS ITRs
def drop_itrs():
    print('Apagando linhas duplicadas dos ITRs...')
    tipos1 = ['bpa','bpp']
    for tps in tipos1:
        df = pd.read_csv('./zips/dfs/concats/%s/%s_itr_all.csv' % (tps,tps), sep=';', encoding='iso-8859-1')
        frame = df.sort_values(by=['DT_REFER','DT_FIM_EXERC','VERSAO']).drop_duplicates(subset=['DENOM_CIA','CD_CONTA','DS_CONTA','DT_FIM_EXERC'],keep='last')
        frame.to_csv('./zips/final_itr' + '/%s_itr.csv'% (tps), sep=';', encoding='iso-8859-1',index=False,columns=['DT_FIM_EXERC','CD_CVM','DENOM_CIA','CD_CONTA','DS_CONTA','VL_CONTA'],float_format='%.0f')
    print ("Arquivos Feitos... DROPAR LINHAS ITRs CONCATENADOS BPA BPP")

    tipos2 = ['dfc_md','dfc_mi','dmpl','dre','dva']
    for tps in tipos2:
        df = pd.read_csv('./zips/dfs/concats/%s/%s_itr_all.csv' % (tps,tps), sep=';', encoding='iso-8859-1')
        frame = df.sort_values(by=['DT_REFER','DT_INI_EXERC','DT_FIM_EXERC','VERSAO']).drop_duplicates(subset=['DENOM_CIA','CD_CONTA','DS_CONTA','DT_FIM_EXERC'],keep='last')
        frame.to_csv('./zips/final_itr' + '/%s_itr.csv'% (tps), sep=';', encoding='iso-8859-1',index=False,columns=['DT_FIM_EXERC','CD_CVM','DENOM_CIA','CD_CONTA','DS_CONTA','VL_CONTA'],float_format='%.0f')
    print ("Arquivos Feitos... DROPAR LINHAS ITRs CONCATENADOS DFC_MD DFC_MI DMPL DRE DVA")
drop_itrs()
print("Linhas Duplicadas Apagadas")
print("Executar: 8 - Dropa DFPs")
input("Press enter to exit")
