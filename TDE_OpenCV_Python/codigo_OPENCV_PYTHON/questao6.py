import cv2
imagem = cv2.imread("imagem.jpg")

altura, largura = imagem.shape[:2]

print("Tamanho original:")
print("Largura:", largura)
print("Altura:", altura)

imagem_50 = cv2.resize(
    imagem,
    (int(largura * 0.5), int(altura * 0.5))
)

imagem_25 = cv2.resize(
    imagem,
    (int(largura * 0.25), int(altura * 0.25))
)

nova_largura = int(input("Digite a nova largura: "))
nova_altura = int(input("Digite a nova altura: "))


imagem_usuario = cv2.resize(
    imagem,
    (nova_largura, nova_altura)
)


cv2.imshow("Imagem Original", imagem)
cv2.imshow("50% do tamanho original", imagem_50)
cv2.imshow("25% do tamanho original", imagem_25)
cv2.imshow("Tamanho definido pelo usuario", imagem_usuario)

cv2.waitKey(0)
cv2.destroyAllWindows()