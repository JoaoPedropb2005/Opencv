#Biblioteca Opencv
import cv2
#armazenando caminho da imagem em uma variável
caminho_imagem = "Imagens/catimage.jpg"
#Lendo a imagem, e convertendo seu esquema de cores para cinza
img = cv2.imread(caminho_imagem)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#limiarizando a imagem (valores <= 80 se transformarão em preto, valores > 80 se transformarão em branco (255))
ret, thresholding_img = cv2.threshold(gray_img, 80, 225, cv2.THRESH_BINARY)
#usando o blur na imagem para suavizar os contornos da figura
thresholding_img = cv2.blur(thresholding_img, (10, 10))
#aplicando o thresholding na imagem com blur
ret, thresholding_img = cv2.threshold(thresholding_img, 80, 225, cv2.THRESH_BINARY)
#usando o thresholding adaptável
thresholding_adaptive = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)
#mostrando as imagens na tela
cv2.imshow("window", img)
cv2.imshow("window-grey", gray_img)
cv2.imshow("window-thresholding", thresholding_img)
cv2.imshow("window-adaptive", thresholding_adaptive)
cv2.waitKey(0)