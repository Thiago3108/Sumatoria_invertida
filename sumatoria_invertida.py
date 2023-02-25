# Programa para invertir numeros

print("---------------------------")
print("-----Invertir numeros------")
print("---------------------------")

#input

n = int(input("digite el numero de tres cifras: ")) #137

#procesing

mod = n % 10    # 3cer digito
de = n // 10 
mod2 = de % 10  # 2do digito 
de2 = de // 10  # 1er digito

ni = mod*100 + mod2*10 + de2*1
#output

print("---------------------------")
print("---------RESULTADO---------")
print("---------------------------")
print("numero invertido: " + str(ni))