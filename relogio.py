import matplotlib.pyplot as plt
import numpy as np

# 1. Dados exatos do relógio da Bae Seok-ryu (Soma exata de 24 horas)
atividades = [
    'Terra dos Sonhos\n(꿈나라)', 
    'Manhã\n(아침)', 
    'Jogar Videogame\n(게임하기)', 
    'Olhar pro nada\n(멍때리기)', 
    'Almoço\n(점심)', 
    'Assistir TV\n(TV보기)', 
    'Soneca\n(낮잠자기)', 
    'Gibiteca\n(만화방 가기)', 
    'Tempo Livre\n(자유시간)', 
    'Meditação\n(명상)'
]
horas = [5, 1, 3, 2.5, 1, 2, 3, 2, 2, 2.5]

# Tudo em branco com linhas pretas finas como no papel do dorama
cores = ['#ffffff'] * len(atividades)

fig, ax = plt.subplots(figsize=(9, 9))

# Gerar o gráfico rodando no sentido horário (counterclock=False)
# Começando exatamente à meia-noite no topo (startangle=90)
wedges, texts = ax.pie(
    horas, 
    labels=atividades, 
    startangle=90, 
    counterclock=False, 
    colors=cores,
    textprops=dict(color="#2b2b2b", fontsize=10, weight="bold", ha="center", va="center"),
    labeldistance=0.7  # Coloca os textos dentro das fatias, exatamente como ela fez
)

# Estilização das bordas (linhas pretas bem finas)
plt.setp(wedges, edgecolor='#404040', linewidth=1.2)

# 2. Criar a linha externa do relógio com os números de 1 a 24
circulo_externo = plt.Circle((0, 0), 1.05, edgecolor='#404040', facecolor='none', linewidth=1.5)
ax.add_artist(circulo_externo)

# Adicionar os marcadores de horas (1-24) ao redor do círculo
for h in range(1, 25):
    # Calcular o ângulo para cada hora no relógio de 24h
    angulo = np.deg2rad(90 - (h * 360 / 24))
    x = 1.12 * np.cos(angulo)
    y = 1.12 * np.sin(angulo)
    
    # Destacar a meia-noite (24) no topo
    if h == 24:
        ax.text(x, y, str(h), fontsize=13, weight="bold", ha='center', va='center', color='black')
    else:
        ax.text(x, y, str(h), fontsize=10, ha='center', va='center', color='#333333')

# Título oficial em Coreano e Inglês igual à folha dela
ax.set_title("배석류 백수계획표\nTODAY'S TIME TABLE", fontsize=16, weight="bold", pad=30, color='#1a1a1a')

# Customização técnica para não cortar as bordas
ax.axis('equal')  
plt.tight_layout()

# Mostrar na tela
plt.show()
