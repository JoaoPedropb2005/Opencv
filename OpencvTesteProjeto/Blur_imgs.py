#Biblioteca Opencv
import cv2
#Armazenando o endereço da imagem em uma Variável
caminho_imagem = "Imagens/elephantimage.jpg"
#definindo o valor do blur em uma variável
blur_lvl = 7
blur_lvl_high = 50
#lendo a imagem e definindo o blur da imagem usando diferentes funções (blur, gaussian blur, median blur)
img = cv2.imread(caminho_imagem)
imgblur = cv2.blur(img,(blur_lvl,blur_lvl))
img_gaussianblur = cv2.GaussianBlur(img, (blur_lvl, blur_lvl), 3)
img_medianblur = cv2.medianBlur(img, blur_lvl)
#mostrando as imagens na tela
cv2.imshow("window0-img", img)
cv2.imshow("window-blur", imgblur)
cv2.imshow("Window-gaussian_blur", img_gaussianblur)
cv2.imshow("window-median_blur", img_medianblur)
cv2.waitKey(0)