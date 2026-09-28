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

objetos = [] 

for contorno in contornos: 

    area = cv2.contourArea(contorno) 

    if area > 3000: 
        objetos.append(contorno) 

resultado = imagem.copy() 

cv2.drawContours( 
    resultado, 
    objetos, 
    -1, 
    (0, 255, 0), 
    2 
) 

print("Objetos detectados:", len(objetos)) 

cv2.imshow("Imagem Binaria", binaria) 
cv2.imshow("Objetos Detectados", resultado) 

cv2.waitKey(0) 
cv2.destroyAllWindows()