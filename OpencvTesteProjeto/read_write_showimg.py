#Biblioteca OpenCv
import cv2
#armazenando o caminho da imagem em uma variável
caminho_imagem = "imagens/catimage.jpg"
#Lendo a imagem, e armazenando em uma variável
img = cv2.imread(caminho_imagem)
#Mostrando a imagem (passando como pârametros o nome da janela de exibição, e o nome da variavel)
cv2.imshow('window', img)
#Tempo que a janela será exibida (0 = até qualquer interação do usuário) - unidade em milisegundos
cv2.waitKey(0)
#Salvando na pasta a imagem
cv2.imwrite("imagens/novaimagem.jpg", img)