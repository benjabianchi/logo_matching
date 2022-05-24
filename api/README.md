# Microservicio para reconocimiento de logo

Este microservicio es capaz de reconocer si un logo especifico se encuentra en una imagen, utilizando 3 parametros.

- Imagen Original: Imagen en la cual se quiere buscar el logo.
- Logo: El logo que se va a buscar en la imagen original.
- Threshold: Umbral de confianza que usa el algoritmo de reconocimiento, mientras mas alto mas exigente sera en la busqueda (por ende menos resultados).


## Opciones para lanzar el microservicio

### Creando la imagen desde cero

Primero debemos tener el repo en nuestra PC y tambien docker.

- Instalar docker en windows: [Instalar Docker en Windows](https://docs.docker.com/desktop/windows/install/)
- Instalar docker en Mac: [Instalar Docker en Mac](https://docs.docker.com/desktop/mac/install/)

Luego debemos usar la terminal y ubicarnos en el folder inicial donde esta el archivo docker-compose.yml

- Primero debes crear la imagen con el siguiente comando:
```
docker-compose build
 ```

- Luego podemos lanzar el servicio completo con el comando:
```
docker-compose up
 ```
