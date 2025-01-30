#Biblioteca OpenCv
import cv2
#armazenando o caminho da imagem em uma variável
caminho_video = "Videos/Catvideo.mp4"
#lendo o video e armazenando-o em uma variável
video = cv2.VideoCapture(caminho_video)
#variavel booleana que permite a execução do vídeo até o final
ret = True
#enquanto "ret" for verdade, os quadros do video serão exibido
while ret:
    ret, frame = video.read()
    if ret: 
        cv2.imshow('windowvideo', frame)
        #frame / second = waitkey
        cv2.waitKey(40)
#libera o espaço armazenado na memória para a execução do vídeo
video.release()
cv2.destroyAllWindows()