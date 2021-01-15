import pandas as pd
import glob

# Concatenar os tipos BPA BPP DFC_MD DFC_MI DMPL DRE DVA
def concatena_csvs():
    listas = ['dfp','itr']
    tipos = ['bpa','bpp','dfc_md','dfc_mi','dmpl','dre','dva']
    print('Concatenando arquivos...')
    for lts in listas:
        for tps in tipos:
            csv = './zips/dfs/%s/%s' % (lts,tps)
            all_files = glob.glob(csv + '/*.csv')
            li = []
            for files in all_files:
                df = pd.read_csv(files, sep=';', encoding='iso-8859-1')
                li.append(df)
            frame = pd.concat(li,axis=0,ignore_index=True)
            frame.to_csv('./zips/dfs/concats' + '/%s/%s_%s_all.csv'% (tps,tps,lts), sep=';', encoding='iso-8859-1',index=False,float_format='%.0f')
concatena_csvs()
print("Arquivos concatenados")
print("Executar: 7 - Dropa ITRs")
input("Press enter to exit")
