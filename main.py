import tkinter as tk
import numpy as np

def plano_cartesiano(canvas):
    
    largura = canvas.winfo_width()
    altura = canvas.winfo_height()
    x = largura // 2
    y = altura // 2
    
    canvas.create_line(0, y, largura, y, fill="black") 
    canvas.create_line(x, 0, x, altura, fill="black")
    for i in range(0, largura, 50):
        canvas.create_line(i, y - 5, i, y + 5, fill="black")  
        canvas.create_text(i, y + 15, text=f'{i - x}', font=("Arial", 8), fill="black") 
    for i in range(0, altura, 50):
        canvas.create_line(x - 5, i, x + 5, i, fill="black") 
        canvas.create_text(x + 15, i, text=f'{y - i}', font=("Arial", 8), fill="black")  

def mostrar_vetor(canvas, origem, vetor, cor):
    canvas.create_line(origem[0], origem[1], origem[0] + vetor[0], origem[1] - vetor[1], arrow=tk.LAST, fill=cor)
    return (origem[0] + vetor[0], origem[1] - vetor[1])

def produto_escalar(vetor1, vetor2):
    return np.dot(vetor1, vetor2)

def projetar(vetor_a, vetor_b):
    escala = produto_escalar(vetor_a, vetor_b) / np.dot(vetor_b, vetor_b)
    return escala * vetor_b  

def medida_angular(vetor1, vetor2):
    produto = produto_escalar(vetor1, vetor2)
    normaV1 = np.linalg.norm(vetor1)
    normaV2 = np.linalg.norm(vetor2)
    cos_theta = produto / (normaV1 * normaV2)
    radiano = np.arccos(cos_theta)
    graus = np.degrees(radiano)  
    return graus

def norma(vetor):
    return np.linalg.norm(vetor)

def area_paralelogramo(vetor1, vetor2):
    produto_vetorial = np.cross(vetor1, vetor2)
    area = np.linalg.norm(produto_vetorial)
    return area

def soma():
    try:
        P1x = float(entradaP1X.get())
        P1y = float(entradaP1Y.get())
        P2x = float(entradaP2X.get())
        P2y = float(entradaP2Y.get())
        
        Q1x = float(entradaQ1X.get())
        Q1y = float(entradaQ1Y.get())
        Q2x = float(entradaQ2X.get())
        Q2y = float(entradaQ2Y.get())

        testeV1 = np.array([P2x - P1x, P2y - P1y])
        testeV2 = np.array([Q2x - Q1x, Q2y - Q1y])
    
        resultado_soma = testeV1 + testeV2
        
        canvas.delete('all')  
        plano_cartesiano(canvas) 
        
        origem = (350, 350)
        mostrar_vetor(canvas, origem, testeV1, cor='red')
        mostrar_vetor(canvas, origem, testeV2, cor='green')
        mostrar_vetor(canvas, origem, resultado_soma, cor='blue')

        canvas.create_text(100, 10, text=f'Vetor 1: {testeV1}', font=("Arial", 10), fill="black")
        canvas.create_text(100, 30, text=f'Vetor 2: {testeV2}', font=("Arial", 10), fill="black")

        normaV1 = norma(testeV1)
        normaV2 = norma(testeV2)
        canvas.create_text(120, 50, text=f'Norma Vetor 1: {normaV1:.2f}', font=("Arial", 10), fill="black")
        canvas.create_text(120, 70, text=f'Norma Vetor 2: {normaV2:.2f}', font=("Arial", 10), fill="black")

        resultado_projecao = projetar(testeV1, testeV2)
        canvas.create_text(140, 90, text=f'Projeção: {resultado_projecao}', font=("Arial", 10), fill="black")
        
        resultado_produto_escalar = produto_escalar(testeV1, testeV2)
        canvas.create_text(100, 110, text=f'Produto Escalar: {resultado_produto_escalar}', font=("Arial", 10), fill="black")
        
        angulo = medida_angular(testeV1, testeV2)
        canvas.create_text(100, 130, text=f'Medida angular: {angulo:.2f} graus', font=("Arial", 10), fill="black")


        area_para = area_paralelogramo(testeV1, testeV2)
        canvas.create_text(100, 150, text=f'Area do Paralelogramo: {area_para:.2f}', font=("Arial", 10), fill="black")
        
    except ValueError:
        canvas.create_text(100, 20, text='Sem valores', font=("Arial", 10), fill="red")

def subtracao():
    try:
        P1x = float(entradaP1X.get())
        P1y = float(entradaP1Y.get())
        P2x = float(entradaP2X.get())
        P2y = float(entradaP2Y.get())
        
        Q1x = float(entradaQ1X.get())
        Q1y = float(entradaQ1Y.get())
        Q2x = float(entradaQ2X.get())
        Q2y = float(entradaQ2Y.get())

        testeV1 = np.array([P2x - P1x, P2y - P1y])
        testeV2 = np.array([Q2x - Q1x, Q2y - Q1y])
        
        resultado_subtracao = testeV1 - testeV2
        
        canvas.delete('all')  
        plano_cartesiano(canvas)    
        mostrar_vetor(canvas, (350, 350), testeV1, cor='red')
        mostrar_vetor(canvas, (350, 350), testeV2, cor='green')
        mostrar_vetor(canvas, (350, 350), resultado_subtracao, cor='blue')
        
        canvas.create_text(100, 10, text=f'Vetor 1: {testeV1}', font=("Arial", 10), fill="black")
        canvas.create_text(100, 30, text=f'Vetor 2: {testeV2}', font=("Arial", 10), fill="black")

        normaV1 = norma(testeV1)
        normaV2 = norma(testeV2)
        canvas.create_text(120, 50, text=f'Norma Vetor 1: {normaV1:.2f}', font=("Arial", 10), fill="black")
        canvas.create_text(120, 70, text=f'Norma Vetor 2: {normaV2:.2f}', font=("Arial", 10), fill="black")

        resultado_projecao = projetar(testeV1, testeV2)
        canvas.create_text(140, 90, text=f'Projeção: {resultado_projecao}', font=("Arial", 10), fill="black")
        
        resultado_produto_escalar = produto_escalar(testeV1, testeV2)
        canvas.create_text(100, 110, text=f'Produto Escalar: {resultado_produto_escalar}', font=("Arial", 10), fill="black")
        
        angulo = medida_angular(testeV1, testeV2)
        canvas.create_text(100, 130, text=f'Medida angular: {angulo:.2f} graus', font=("Arial", 10), fill="black")


        area_para = area_paralelogramo(testeV1, testeV2)
        canvas.create_text(100, 150, text=f'Area do Paralelogramo: {area_para:.2f}', font=("Arial", 10), fill="black")

    except ValueError:
        canvas.create_text(100, 20, text='Sem valores', font=("Arial", 10), fill="red")

def inicializar():
    plano_cartesiano(canvas)

janela = tk.Tk()
janela.title('AVLC Projeto')
canvas = tk.Canvas(janela, width=700, height=700)
canvas.pack()
canvas.after(100, inicializar)

tk.Label(janela, text='Ponto 1 do Vetor 1:').pack()
entradaP1X = tk.Entry(janela)
entradaP1X.pack()
entradaP1Y = tk.Entry(janela)
entradaP1Y.pack()

tk.Label(janela, text='Ponto 2 do Vetor 1:').pack()
entradaP2X = tk.Entry(janela)
entradaP2X.pack()
entradaP2Y = tk.Entry(janela)
entradaP2Y.pack()

tk.Label(janela, text='Ponto 1 do Vetor 2:').pack()
entradaQ1X = tk.Entry(janela)
entradaQ1X.pack()
entradaQ1Y = tk.Entry(janela)
entradaQ1Y.pack()

tk.Label(janela, text='Ponto 2 do Vetor 2:').pack()
entradaQ2X = tk.Entry(janela)
entradaQ2X.pack()
entradaQ2Y = tk.Entry(janela)
entradaQ2Y.pack()

botao_soma = tk.Button(janela, text='Soma', command=soma)
botao_soma.pack()
botao_subtracao = tk.Button(janela, text='Subtração', command=subtracao)
botao_subtracao.pack()

janela.mainloop()
