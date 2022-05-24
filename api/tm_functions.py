import cv2
import numpy as np
from matplotlib import pyplot as plt


## Esta funcion nos permite visualizar los matching del algoritmo.
## Parametros
## -image Imagen original a la cual quiere hacerse el Matching.
## -template_image Parte de la imagen que queremos matchear en la imagane original (ejemplo un logo).
## -th Es el umbral Que utiliza el algoritmo para dar como valida un matching, mientras mayor sea el umbral mas exigente es.
def match_and_show(image,template_image,th):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template_image,0)
    h, w = template.shape[::]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    ## plt.imshow(res, cmap='gray')
    cv2.imshow("Image Analysis", res) ## Esto muestra el resultado de las convoluciones
    threshold = th #Pick only values above 0.8. For TM_CCOEFF_NORMED (metodo usado pero se puedn usar otros y habria que cambiar el th), larger values = good fit.
    print("Resultado de la convolution")
    print(res)
    loc = np.where( res >= threshold)
    print(loc[0].shape)
    print(loc[1].shape)
    #Outputs 2 arrays. Combine these arrays to get x,y coordinates - take x from one array and y from the other.

    #Reminder: ZIP function is an iterator of tuples where first item in each iterator is paired together,
    #then the second item and then third, etc.

    if loc[0].shape and loc[0].shape == (0,):
        print("No se encontro el objeto")

    print(loc)

    count = 0
    for pt in zip(*loc[::-1]):   #-1 to swap the values as we assign x and y coordinate to draw the rectangle.
        count += 1
        #Draw rectangle around each object. We know the top left (pt), draw rectangle to match the size of the template image.
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (50, 255, 0), 2,)  #Red rectangles with thickness 2.
        #cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (50, 255, 0), 2,)

    print(count)

    #cv2.imwrite('images/template_matched.jpg', img_rgb)
    cv2.imshow("Matched image", img_rgb)
    cv2.waitKey()
    cv2.destroyAllWindows()

#match_and_show("mcdonalds_nuevo.png","mcdonalds_template_1.png",0.95)

## Esta funcion es similar a match_and_show sin embargo esta no devuelve visualizacion y tambien agregamos un output de la cantidad de matches que encontramos.
## -image Imagen original a la cual quiere hacerse el Matching.
## -template_image Parte de la imagen que queremos matchear en la imagane original (ejemplo un logo).
## -th Es el umbral Que utiliza el algoritmo para dar como valida un matching, mientras mayor sea el umbral mas exigente es.
def template_detector(image,template,th=0.95):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template,0)
    h, w = template.shape[::]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    ## plt.imshow(res, cmap='gray')
    #cv2.imshow("Image Analysis", res) ## Esto muestra el resultado de las convoluciones
    threshold = th #Pick only values above 0.8. For TM_CCOEFF_NORMED (metodo usado pero se puedn usar otros y habria que cambiar el th), larger values = good fit.

    loc = np.where( res >= threshold)
    #Outputs 2 arrays. Combine these arrays to get x,y coordinates - take x from one array and y from the other.

    #Reminder: ZIP function is an iterator of tuples where first item in each iterator is paired together,
    #then the second item and then third, etc.
    if loc[0].shape and loc[1].shape == (0,):
        print("No se encontro el objeto")
        result = False
    else:
        print("Se encontro uno o mas objetos")
        result = True
    return loc[0].shape[0]

#print(template_detector("mcdonalds_nuevo.png","mcdonalds_template_1.png",0.98))
## Esta funcion nos permite encontra el umbral perfecto para un matching especificos
## -image Imagen original a la cual quiere hacerse el Matching.
## -template_image Parte de la imagen que queremos matchear en la imagane original (ejemplo un logo).
## -true_label La cantidad real de matches que deben existir en la Imagen
## -start Debemos crear una lista con  umbrales, start es el inicio de esta lista, si es 0.5 significa que la lista comienza con 0.5.
## -steps Los steps que tendra la lista de umbrales a probar, por ejemplo si es 0,025 ira de 0,025 en 0,025.
## -start y -steps estan por defecto en 0.5 y 0.025, son los valores mas comunes para probar, pero puedes cambiarlos a tu gusto
def search_best_th(image,template_image,true_label,start = 0.5,end=1,steps=0.025):
    th_list = np.arange(start,end,steps)
    good_th = []

    for i in range(len(th_list)):
        result = template_detector(image,template_image,th_list[i])
        print(f"Probando el th: {th_list[i]}")
        if result == true_label:
            good_th.append(th_list[i])

    return good_th

## Agregar comandos por consola para lanzar cada una de estas funciones
