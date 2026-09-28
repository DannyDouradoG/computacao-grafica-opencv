import cv2 

imagem = cv2.imread("objetos.jpeg") 

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) 

suave = cv2.blur(cinza, (5, 5)) 

_, binaria = cv2.threshold( 
    suave, 
    150, 
    255, 
    cv2.THRESH_BINARY_INV 
) 

kernel = cv2.getStructuringElement( 
    cv2.MORPH_ELLIPSE, 
    (21, 21) 
) 

binaria = cv2.morphologyEx( 
    binaria, 
    cv2.MORPH_CLOSE, 
    kernel 
) 

contornos, _ = cv2.findContours( 
    binaria, 
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE 
) 

area_minima = 3000 

areas_validas = [] 

resultado = imagem.copy() 

for contorno in contornos: 

    area = cv2.contourArea(contorno) 

    if area > area_minima: 

        areas_validas.append(area) 

        cv2.drawContours( 
            resultado, 
            [contorno], 
            -1, 
            (0, 255, 0), 
            2 
        ) 

objetos_detectados = len(contornos) 

objetos_validos = len(areas_validas) 

if objetos_validos > 0: 

    maior_area = max(areas_validas) 
    menor_area = min(areas_validas) 
    area_total = sum(areas_validas) 

else: 

    maior_area = 0 
    menor_area = 0 
    area_total = 0 

print() 
print("----- RESUMO DA IMAGEM -----") 
print("Objetos detectados:", objetos_detectados) 
print("Objetos válidos:", objetos_validos) 
print("Maior área:", maior_area) 
print("Menor área:", menor_area) 
print("Área total:", area_total) 

cv2.imshow("Imagem Original", imagem) 
cv2.imshow("Imagem Binaria", binaria) 
cv2.imshow("Objetos Validos", resultado) 

cv2.waitKey(0) 
cv2.destroyAllWindows()