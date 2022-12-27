q = int(input())
T = float(input())
C = int(input())
n = int(input())

Vp = 0
for i in range(q):
    Vi = T * (i + 1) + T * C
    Vp += Vi
    print(i + 1,"%.2f" % round(Vi, 2),"%.2f" % round(Vp, 2))

Vt = Vp
print("%.2f" % round(Vt, 2))

m = soma = 0
while Vt - soma >= n:
    soma += n
    print(soma)
    m += 1

print(m)
print("BATERIA DE TESTES TERMINADA")
