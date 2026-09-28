import cv2
imagem = cv2.imread("imagem.jpg")


blur_3 = cv2.blur(imagem, (3, 3))

blur_5 = cv2.blur(imagem, (5, 5))

blur_9 = cv2.blur(imagem, (9, 9))

cv2.imshow("Imagem Original", imagem)
cv2.imshow("Blur 3x3", blur_3)
cv2.imshow("Blur 5x5", blur_5)
cv2.imshow("Blur 9x9", blur_9)

cv2.waitKey(0)
cv2.destroyAllWindows()