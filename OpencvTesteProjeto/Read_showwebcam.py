#Biblioteca Opencv
import cv2
#Armazenando a Webcam em uma variável
webcam = cv2.VideoCapture(0)
#variável booleana que permite a exibição da webcam enquanto for verdadeiro
ret = True
while ret:
    ret, frame = webcam.read()
    cv2.imshow("window webcam", frame)
    ##A webcam fechará quando o usuário digitar a tecla "q"
    if cv2.waitKey(40) & 0xFF == ord('q'): 
       break
#Excluindo o espaço reservado na memória para exibição da webcam
webcam.release()
cv2.destroyAllWindows()