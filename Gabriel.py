import random
import json
import os

class NotaFiscal:
    def __init__(self, numero, valor, peso, volume):
        self.numero = numero
        self.valor = valor      # em reais
        self.peso = peso        # em kg
        self.volume = volume    # em m³

    def __repr__(self):
        return f"NF-{self.numero} | R${self.valor:.2f} | {self.peso}kg | {self.volume}m³"

class ClassificadorNotas:
    def __init__(self):
        self.notas = []

    def carregar_notas_aleatorias(self, quantidade=20):
        self.notas = []
        for i in range(1, quantidade + 1):
            valor = round(random.uniform(100, 10000), 2)
            peso = round(random.uniform(0.5, 100), 2)
            volume = round(random.uniform(0.01, 2), 2)
            self.notas.append(NotaFiscal(i, valor, peso, volume))
        print(f"{quantidade} notas fiscais carregadas aleatoriamente.")

    def carregar_de_arquivo(self, caminho):
        if not os.path.exists(caminho):
            print("Arquivo não encontrado.")
            return

        with open(caminho, 'r') as f:
            data = json.load(f)
        self.notas = []
        for item in data:
            nf = NotaFiscal(item['numero'], item['valor'], item['peso'], item['volume'])
            self.notas.append(nf)
        print(f"{len(self.notas)} notas carregadas de {caminho}.")

    def salvar_para_arquivo(self, caminho):
        data = [{
            "numero": nf.numero,
            "valor": nf.valor,
            "peso": nf.peso,
            "volume": nf.volume
        } for nf in self.notas]

        with open(caminho, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"{len(data)} notas salvas em {caminho}.")

    def classificar_por_valor(self):
        categorias = {
            "baixo": [],
            "medio": [],
            "alto": []
        }
        for nf in self.notas:
            if nf.valor < 1000:
                categorias["baixo"].append(nf)
            elif nf.valor < 5000:
                categorias["medio"].append(nf)
            else:
                categorias["alto"].append(nf)
        return categorias

    def classificar_por_peso(self):
        categorias = {
            "leve": [],
            "medio": [],
            "pesado": []
        }
        for nf in self.notas:
            if nf.peso < 5:
                categorias["leve"].append(nf)
            elif nf.peso < 30:
                categorias["medio"].append(nf)
            else:
                categorias["pesado"].append(nf)
        return categorias

    def classificar_por_volume(self):
        categorias = {
            "pequeno": [],
            "medio": [],
            "grande": []
        }
        for nf in self.notas:
            if nf.volume < 0.1:
                categorias["pequeno"].append(nf)
            elif nf.volume < 1.0:
                categorias["medio"].append(nf)
            else:
                categorias["grande"].append(nf)
        return categorias

    def gerar_relatorio(self, classificacao):
        print("\n--- RELATÓRIO DE CLASSIFICAÇÃO ---")
        for categoria, notas in classificacao.items():
            print(f"\nCategoria '{categoria.upper()}': {len(notas)} notas")
            for nf in notas:
                print(" ", nf)

    def resumo_geral(self):
        print("\n--- RESUMO GERAL ---")
        print(f"Total de notas: {len(self.notas)}")
        print(f"Valor total: R${sum(nf.valor for nf in self.notas):,.2f}")
        print(f"Peso total: {sum(nf.peso for nf in self.notas):,.2f} kg")
        print(f"Volume total: {sum(nf.volume for nf in self.notas):,.2f} m³")

def menu():
    print("""
📦 BOT DE SEPARAÇÃO DE NOTAS FISCAIS 📑

1. Carregar notas aleatórias
2. Carregar notas de arquivo JSON
3. Salvar notas em arquivo JSON
4. Classificar por valor
5. Classificar por peso
6. Classificar por volume
7. Mostrar resumo geral
8. Listar todas as notas
9. Sair
""")

def executar():
    bot = ClassificadorNotas()
    while True:
        menu()
        escolha = input("Escolha uma opção: ").strip()
        if escolha == '1':
            qtd = input("Quantas notas deseja gerar? ")
            bot.carregar_notas_aleatorias(int(qtd))
        elif escolha == '2':
            caminho = input("Caminho do arquivo JSON: ")
            bot.carregar_de_arquivo(caminho)
        elif escolha == '3':
            caminho = input("Salvar em (ex: notas.json): ")
            bot.salvar_para_arquivo(caminho)
        elif escolha == '4':
            resultado = bot.classificar_por_valor()
            bot.gerar_relatorio(resultado)
        elif escolha == '5':
            resultado = bot.classificar_por_peso()
            bot.gerar_relatorio(resultado)
        elif escolha == '6':
            resultado = bot.classificar_por_volume()
            bot.gerar_relatorio(resultado)
        elif escolha == '7':
            bot.resumo_geral()
        elif escolha == '8':
            for nf in bot.notas:
                print(nf)
        elif escolha == '9':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar()