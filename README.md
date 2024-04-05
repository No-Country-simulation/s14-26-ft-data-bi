# s14-26-ft-data-bi

## Proyecto Data-BI: Proyecto de Reconocimiento de Emociones

### Descripcion
El proyecto de Reconocimiento de Emociones en el Aula tiene como objetivo principal analizar y comprender el estado emocional de los estudiantes durante una clase específica. Para lograr esto, se propone grabar las interacciones en el aula y extraer datos relevantes sobre las emociones expresadas por los estudiantes.

### Objetivos 
* Grabar sesiones de clase para capturar la interacción y las expresiones emocionales de los estudiantes.
* Analizar los datos recopilados para identificar patrones de emociones dentro del aula.
* Utilizar técnicas de análisis de datos para comprender cómo las emociones afectan el rendimiento y la participación de los estudiantes.
* Proponer recomendaciones o intervenciones basadas en los hallazgos para mejorar el ambiente emocional y el aprendizaje en el aula.

### Estructura del proyecto 
* data: Contiene los datos utilizados en el proyecto.
    * imagenes: Imágenes utilizadas para el reconocimiento de emociones.
    * pruebas: Contiene videos de las clases grabadas y los resultados del análisis. 
        * reconocidos: Imágenes reconocidas por el modelo.
        * emociones: Imágenes clasificadas por emociones.
    * resultados: Resultados del análisis de datos.
* modelos: Contiene los modelos entrenados utilizados en el proyecto.
* src: Contiene los archivos fuente del proyecto.
    * Archivos .py para la captura de imágenes, entrenamiento del modelo y pruebas.

### Instalacion y uso
1. Clona este repositorio en tu maquina local
```
git clone https://github.com/tu-usuario/s14-26-ft-data-bi.git
```
2. Crea tu entorno virtual
```
python3 -m venv env
```
3. Activa el entorno virtual
    * En wimdows
    ```
    venv\Scripts\activate
    ```
    * En macOS y Linux
    ```
    source venv/bin/activate
    ```
4. Instala las dependencias del proyecto
```
pip install -r requirements.txt
```
5. Crea la carpeta pruebas en el directorio data, en esta carpeta subiras todos los videos
```
mkdir pruebas
```
6. Dentro de la carpeta pruebas crearas la carpeta emociones y reconocidos que seran donde se guardaran las imagenes que se necesitan para entrenar el modelo a partir de los videos
```
mkdir emociones
```
```
mkdir reconocidos
```

### Contribución
¡Se agradecen las contribuciones! Si deseas colaborar en el proyecto, por favor sigue estos pasos:

1. Crea una nueva rama (git checkout -b feature/nueva-caracteristica).
2. Realiza tus cambios y haz commit de ellos (git commit -am 'Añade nueva característica').
3. Haz push de tu rama (git push origin feature/nueva-caracteristica).
4. Abre un Pull Request y describe tus cambios detalladamente.



