#Biblioteca Opencv
import cv2
#armazenando caminho da imagem em uma variável
caminho_imagem = "Imagens/catimage.jpg"
#lendo a imagem e armazenando em uma variavel, assim como alguns exemplos de variações usando o opencv
img = cv2.imread(caminho_imagem)
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgbimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#Mostrando as imagens na tela
cv2.imshow("window", img)
cv2.imshow("window-gray", grayimg)
cv2.imshow("window-rgb", rgbimg)
cv2.imshow("window-hsv", hsvimg)
cv2.waitKey(0)

