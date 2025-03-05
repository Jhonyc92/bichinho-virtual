# Comando para importar a função de tempo
import time

# Classe principal do programa
class BichinhoVirtual:
    
    # Função para iniciar a Classe BichinhoVirtual
    def __init__(self, nome, fome = 50, saude = 50, humor = 100):
        
        self.nome = nome
        
        self.fome = fome
        
        self.saude = saude
        
        self.humor = humor
        
    # Função responsável pela alimentação do Bichinho Virtual
    def alimentar(self, quantidade):
        
        self.fome -= quantidade
        
        if self.fome < 0:
            
            self.fome = 0
            
        self.atualizar_humor()
        
    # Função responsável pela brincadeira do Bichinho Virtual
    def brincar(self, tempo):
        
        self.saude += tempo
        
        if self.saude > 100:
            
            self.saude = 100
            
        self.atualizar_humor()
        
    # Função para exibir os Status do Bichinho Virual
    def status(self):
        
        print(f"Nome: {self.nome}")
        
        print(f"Fome: {self.fome}")
        
        print(f"Saúde: {self.saude}")
        
        print(f"Humor: {self.humor}")
        
    # Função para atualizar os Status do Bichinho Virtual
    def atualizar_humor(self):
        
        self.humor = 100 - (abs(self.fome - 50) + abs(self.saude - 50)) // 2
        
        if self.humor > 100:
            
            self.humor = 100
            
# Criando o bichinho
meu_bichinho = BichinhoVirtual("Buddy")

# Loop Principal
while True:
    
    meu_bichinho.status()
    
    acao = input("O que você quer fazer? (alimentar/brincar/sair): ")
    
    if acao == "alimentar":
        
        quantidade = int(input("Quantidade de comida: "))
        
        meu_bichinho.alimentar(quantidade)
        
    elif acao == "brincar":
        
        tempo = int(input("Tempo de brincadeira: "))
        
        meu_bichinho.brincar(tempo)
        
    elif acao == "sair":
        
        break
        
    else:
        
        print("Ação inválida!")
        
    # Simulação do tempo passando
    meu_bichinho.fome += 5
    
    meu_bichinho.saude -= 5
    
    meu_bichinho.atualizar_humor()
    
    time.sleep(2)  # Pausa de 2 segundos
