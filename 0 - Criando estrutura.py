import os

diretorios = ['cias',
             'dfp','itr','fre','fca',
             'final_itr','final_dfp']
for d in diretorios:
    os.makedirs('./zips/%s' % d, exist_ok = True)
for d in ['itr','dfp']:
    os.makedirs('./zips/cias/%s' % d, exist_ok = True)
for d in ['itr','dfp']:
    os.makedirs('./zips/%s/%s/%s_con' % (d,d,d), exist_ok = True)
for d in ['fre','fca']:
    os.makedirs('./zips/%s/%s' % (d,d), exist_ok = True)

tipos = ['bpa','bpp','dfc_md','dfc_mi','dmpl','dre','dva']
for d in ['itr','dfp']:
    for t in tipos:
        os.makedirs('./zips/dfs/%s/%s' % (d,t), exist_ok = True)
tipos = ['bpa','bpp','dfc_md','dfc_mi','dmpl','dre','dva','alls']
for t in tipos:
    os.makedirs('./zips/dfs/concats/%s' % t, exist_ok = True)
print("Estrutura Criada")
print("Executar: 1 - Download compactados")
input("Press enter to exit")
