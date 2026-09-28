import cv2

# Carrega a imagem
imagem = cv2.imread("objetos.jpeg")

# Converte para escala de cinza
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplica diferentes valores de threshold
_, th100 = cv2.threshold(
    cinza, 100, 255, cv2.THRESH_BINARY
)

_, th150 = cv2.threshold(
    cinza, 150, 255, cv2.THRESH_BINARY
)

_, th200 = cv2.threshold(
    cinza, 200, 255, cv2.THRESH_BINARY
)

# Threshold invertido
_, th_inv = cv2.threshold(
    cinza, 150, 255, cv2.THRESH_BINARY_INV
)

# Mostra os resultados
cv2.imshow("Imagem Original", imagem)
cv2.imshow("Escala de Cinza", cinza)
cv2.imshow("Threshold 100", th100)
cv2.imshow("Threshold 150", th150)
cv2.imshow("Threshold 200", th200)
cv2.imshow("Threshold Invertido", th_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()