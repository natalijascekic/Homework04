#za dati broj vratiti listu pozicija na kojima se pojavljuje u nizu
#dace nam na kojim je pozicijama broj koji trazimo


niz=[1,2,3,4,5,5,8,9,5,3,2,7]
broj=5
pozicije=[]

for i in range(len(niz)):
    if niz[i]== broj:

        pozicije.append(i)

print(pozicije)