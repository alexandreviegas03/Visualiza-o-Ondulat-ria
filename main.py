import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import Tk, Scale, Label, Button, HORIZONTAL

# Define um intervalo de tempo de 0 a 2 segundos com 1000 pontos
tempo = np.linspace(0, 2, 1000)



# Função que gera uma onda sinusoidal com parâmetros ajustáveis
def onda(amplitude, frequencia, fase, tempo, deslocamento):
    return amplitude * np.cos(2 * np.pi * frequencia * (tempo - deslocamento) + fase)

# Criando a figura com 3 subgráficos
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))

# Configuração do primeiro gráfico: Onda 1 isolada
ax1.set_xlim(0, 2)  # Define os limites do eixo X
ax1.set_ylim(-5, 5)  # Define os limites do eixo Y
linha_onda1, = ax1.plot([], [], label="Onda 1", color="b")  # Cria a linha da Onda 1
ax1.set_title("Onda 1 Isolada")  # Define o título do gráfico
ax1.legend()  # Adiciona legenda

# Configuração do segundo gráfico: Onda 2 isolada
ax2.set_xlim(0, 2)  # Define os limites do eixo X
ax2.set_ylim(-5, 5)  # Define os limites do eixo Y
linha_onda2, = ax2.plot([], [], label="Onda 2", color="r")  # Cria a linha da Onda 2
ax2.set_title("Onda 2 Isolada")  # Define o título do gráfico
ax2.legend()  # Adiciona legenda

# Configuração do terceiro gráfico: Interferência entre as ondas
ax3.set_xlim(0, 2)  # Define os limites do eixo X
ax3.set_ylim(-5, 5)  # Define os limites do eixo Y
linha_interferencia, = ax3.plot([], [], label="Interferência", color="g", linestyle="--")  # Cria a linha da interferência
ax3.set_title("Interferência Entre as Ondas")  # Define o título do gráfico
ax3.legend()  # Adiciona legenda

# Função para inicializar os gráficos (necessário para animação)
def init():
    linha_onda1.set_data([], [])  # Inicializa a linha da Onda 1 sem dados
    linha_onda2.set_data([], [])  # Inicializa a linha da Onda 2 sem dados
    linha_interferencia.set_data([], [])  # Inicializa a linha da interferência sem dados
    return linha_onda1, linha_onda2, linha_interferencia

# Função para atualizar a animação dos gráficos
def update(frame):
    deslocamento = frame / 50  # Calcula o deslocamento ao longo do tempo
    A1, f1, p1 = slider_amp1.get(), slider_freq1.get(), slider_fase1.get()  # Obtém os parâmetros da Onda 1
    A2, f2, p2 = slider_amp2.get(), slider_freq2.get(), slider_fase2.get()  # Obtém os parâmetros da Onda 2

    # Calcula as ondas com os parâmetros ajustados
    onda1 = onda(A1, f1, p1, tempo, deslocamento)
    onda2 = onda(A2, f2, p2, tempo, deslocamento)
    interferencia = onda1 + onda2  # Calcula a interferência entre as ondas

    # Atualiza os gráficos com os novos valores
    linha_onda1.set_data(tempo, onda1)
    linha_onda2.set_data(tempo, onda2)
    linha_interferencia.set_data(tempo, interferencia)

    return linha_onda1, linha_onda2, linha_interferencia

# Criando a animação com intervalo de atualização definido
ani = FuncAnimation(fig, update, frames=200, init_func=init, interval=50)

# Interface gráfica com tkinter para ajustar os parâmetros
janela = Tk()
janela.title("Ajuste de Parâmetros e Visualização de Ondas")  # Título da janela

# Adicionando sliders para ajustar amplitude, frequência e fase da Onda 1
Label(janela, text="Amplitude Onda 1").pack()
slider_amp1 = Scale(janela, from_=1, to=5, resolution=0.1, orient=HORIZONTAL)
slider_amp1.pack()

Label(janela, text="Frequência Onda 1").pack()
slider_freq1 = Scale(janela, from_=0.1, to=10, resolution=0.1, orient=HORIZONTAL)
slider_freq1.pack()

Label(janela, text="Fase Onda 1").pack()
slider_fase1 = Scale(janela, from_=0, to=2 * np.pi, resolution=0.1, orient=HORIZONTAL)
slider_fase1.pack()

# Adicionando sliders para ajustar amplitude, frequência e fase da Onda 2
Label(janela, text="Amplitude Onda 2").pack()
slider_amp2 = Scale(janela, from_=1, to=5, resolution=0.1, orient=HORIZONTAL)
slider_amp2.pack()

Label(janela, text="Frequência Onda 2").pack()
slider_freq2 = Scale(janela, from_=0.1, to=10, resolution=0.1, orient=HORIZONTAL)
slider_freq2.pack()

Label(janela, text="Fase Onda 2").pack()
slider_fase2 = Scale(janela, from_=0, to=2 * np.pi, resolution=0.1, orient=HORIZONTAL)
slider_fase2.pack()

# Botão para reiniciar a animação com novos valores
Button(janela, text="Atualizar Animação", command=lambda: ani.event_source.start()).pack()

# Função para exibir os gráficos da animação
def mostrar_grafico():
    plt.show()

# Botão para exibir os gráficos animados
Button(janela, text="Exibir Gráficos", command=mostrar_grafico).pack()

# Inicia a interface gráfica do tkinter
janela.mainloop()