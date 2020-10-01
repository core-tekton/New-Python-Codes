dic = {}
dic['orange'] = 50
dic['Apple'] = 60
print(dic)
print(dic['Apple'])
dic['Apple'] = dic['Apple']+20
print(dic['Apple'])


dicti = {}
li = ['J','E','E','V','A','N']
for i in li:
    if i in dicti:
        dicti[i]=dicti[i]+1
    else:
        dicti[i]=1
print(dicti)

dicti = {}
li = ['J','E','E','V','A','N']
for i in li:
    dicti[i] = dicti.get(i,0)+1
print(dicti)

dictin={'a':23, 'b':34 , 'c':43}
for a,b in dictin.items():
    print(a,b)

stuff = dict()
print(stuff.get('candy',-1))