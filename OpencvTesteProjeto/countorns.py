import cv2
import numpy as np

# Caminho da imagem
caminho_imagem = "exemplo.jpg"  # Substitua pelo caminho correto da sua imagem

# Carregar a imagem original
imagem = cv2.imread(caminho_imagem)

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem.")
    exit()

# Converter para escala de cinza
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar limiarização (thresholding) para binarizar a imagem
_, imagem_thresh = cv2.threshold(imagem_gray, 127, 255, cv2.THRESH_BINARY)

# Encontrar os contornos
contornos, _ = cv2.findContours(imagem_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterar sobre os contornos e calcular a área de cada um
for contorno in contornos:
    area = cv2.contourArea(contorno)  # Calcular a área do contorno
    if area > 200:  # Filtrar contornos com área maior que 200 pixels²
        print(f"Contorno com área {area} pixels² será envolvido em um retângulo.")
        
        # Obter o retângulo delimitador para o contorno
        x, y, largura, altura = cv2.boundingRect(contorno)

        # Desenhar o retângulo na imagem original
        cv2.rectangle(imagem, (x, y), (x + largura, y + altura), (0, 255, 0), 2)  # Retângulo verde com espessura de 2

# Mostrar a imagem com os retângulos desenhados
cv2.imshow("Imagem com Retângulos Filtrados", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()