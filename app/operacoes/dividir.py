# app/operacoes/dividir.py
class ClasseDivisao:
    @staticmethod
    def realizar_operacao(a, b):
        if b == 0:
            return "Erro: Divisão por zero"
        return a / b
