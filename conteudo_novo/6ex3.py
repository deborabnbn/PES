# 3 – Crie uma classe chamada ContaBancaria com:
# • Atributos: titular e saldo.
# • Um método chamado depositar que recebe um valor e adiciona ao saldo.
# • Um método chamado sacar que recebe um valor e subtrai do saldo (não precisa
# validar o saldo).
# • Um método chamado mostrar_saldo que retorna o saldo atual.
# Teste criando uma conta, fazendo depósitos, saques e exibindo o saldo.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular 
        self.saldo = saldo
    
    def depositar (self, valor):
        self.saldo = (self.saldo + valor)

    def Sacar (self, valor_saque):
        self.saldo_final = (self.saldo - valor_saque)

    def Mostrar_saldo (self):
        return self.saldo_final
        
Conta = ContaBancaria("Debora", 20000)
Conta.depositar(1000)
Conta.Sacar(500)
print ("O saldo atual da conta é", Conta.Mostrar_saldo())

