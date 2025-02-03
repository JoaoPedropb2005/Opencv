#Biblioteca Opencv
import cv2
#Biblioteca numpy
import numpy as np
#armazenando o endereço de imagem em uma variável
caminho_imagem = "Imagens/zebraimage.jpg"
#lendo a imagem
img = cv2.imread(caminho_imagem)
#Usando a função Canny para detecção de bordas na imagem
edge_img = cv2.Canny(img, 100, 200)
#usando as funções dilate e erode para aumentar e diminuir a espessura de apresentação da borda
dilate_img = cv2.dilate(edge_img, np.ones((3,3), dtype=np.int8))
erode_img = cv2.erode(edge_img, np.ones((2,2), dtype=np.int8))
#apresentando as imagens na tela
cv2.imshow("window", img)
cv2.imshow("window-edge", edge_img)
cv2.imshow("window-dilate", dilate_img)
cv2.imshow("window-erode", erode_img)
cv2.waitKey(0)