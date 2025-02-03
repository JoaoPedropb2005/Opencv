import cv2

caminho_imagem = "Imagens/whiteboardimage.jpg"

img = cv2.imread(caminho_imagem)
print(img.shape)

cv2.line(img, (200,150), (120, 90), (255, 0, 0), 2)

cv2.rectangle(img, (90, 50), (140, 60), (0, 255, 0), 4)

cv2.circle(img, (90, 120), 25, (0, 0, 255), 4)

cv2.putText(img, "inserindo texto!", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.imshow("window", img)
cv2.waitKey(0)