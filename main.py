from conta import Conta

if __name__ == "__main__":
    conta = Conta(123, "Nico", 50.0, 1000.0)
    conta2 = Conta(124, "Marco", 100.0, 1000.0)

    conta.extrato()
    conta.deposita(100)
    conta.extrato()
    conta.saca(90)
    conta.extrato()
    conta2.extrato()
    conta2.transfere(60, conta)
    conta.extrato()
    conta2.extrato()
