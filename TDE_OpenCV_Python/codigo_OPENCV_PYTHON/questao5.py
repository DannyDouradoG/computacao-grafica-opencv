import cv2
imagem=cv2.imread("imagem.jpg")
imagem_cinza=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
cv2.imshow("imagem Colorida", imagem)
cv2.imshow("Imagem em Escala de Cinza", imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
