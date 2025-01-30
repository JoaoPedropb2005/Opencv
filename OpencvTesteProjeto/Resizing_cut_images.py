#Biblioteca Opencv
import cv2
#Armazenando caminho da imagem em uma variável
caminho_imagem = "Imagens/catimage.jpg"
#Armazenando as imagens em variáveis
img = cv2.imread(caminho_imagem)
#imagem redimensionada -parametros-> (nome, (largura, altura))
imgresized = cv2.resize(img, (426, 296))
#imagem cortada -parametros-> nome[altura:altura, largura:largura]
imgcuted = img[67:134, 30:220]
#mostrando as dimensões das imagens (altura, largura e cores)
print(img.shape)
print(imgresized.shape)
#exibindo as imagens 
cv2.imshow("window", img)
cv2.imshow("window-resized", imgresized)
cv2.imshow("window-cuted", imgcuted)
cv2.waitKey(0)