class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class RotaEntrega:
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, nome_loja):
        nova_loja = Loja(nome_loja)
        nova_loja.proximo = self.inicio
        self.inicio = nova_loja

    def inserir_na_posicao(self, nome_loja, posicao):
        nova_loja = Loja(nome_loja)

        if posicao == 0: 
            nova_loja.proximo = self.inicio
            self.inicio = nova_loja
            return

        atual = self.inicio
        indice = 0

        while atual is not None and indice < posicao - 1:
            atual = atual.proximo
            indice += 1

        if atual is None:
            raise IndexError("Posição inválida: fora da lista.")

        nova_loja.proximo = atual.proximo
        atual.proximo = nova_loja

    def imprimir_rota(self):
        atual = self.inicio
        while atual:
            print(f" {atual.nome}")
            atual = atual.proximo


rota = RotaEntrega()
rota.inserir_inicio("Loja D")
rota.inserir_inicio("Loja B")
rota.inserir_inicio("Loja A")


rota.inserir_na_posicao("Loja C", 2)

print(" Rota final:")
rota.imprimir_rota()

# Saída esperada:
# Loja A
# Loja B
# Loja C
# Loja D
