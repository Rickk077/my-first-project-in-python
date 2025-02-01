import time
print("seja bem vindo ao facebook\n")
time.sleep(1.5)
act1 = str(input("ja tenho uma conta (entrar) , criar uma conta (criar)\n"))
if act1 == "entrar":
    print("erro recarregue a pagina\n")
elif act1 == "criar":
        usuario=input("digite um nome de usuario\n")
        time.sleep(2)
print(f"seu nome e: {usuario}")
time.sleep(1)
nomecrt = str(input("nome de usuario correto?Sim(s) Nao(n)\n"))
if nomecrt == "s":
   time.sleep(1)
   senha1=input("crie uma senha:\n")
   time.sleep(1)
   senha2=input("confirme sua senha\n")
   if senha2 != senha1:
       print("erro reinicie a pagina")
   else:
       print("conta criada com suscesso")
elif nomecrt == "n":
    print("porfavor reinicie a pagina")