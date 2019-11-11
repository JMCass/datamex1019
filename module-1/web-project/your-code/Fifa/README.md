

```python
Utilizé la base de datos FIFA 19 complete player dataset de https://www.kaggle.com/karangadiya/fifa19

PASO 1

Los pasos realizados fueron los siguientes:
        -Ubicar las columnas que contenían valores vacíos
        -Rellenar cada una de esas columnas
        -Cambiar el nombre de algunas columnas para tener un mejor manejo de la información
        -Eliminar columnas que no resultan relevantes para el proyecto
        -Sacar una tabla con tablas descriptivas de la base de datos
        -Limpiar la base de datos para que aquellas columnas con strings pudieran pasar a ser int o float
        para realizar cálculos
        -Generé gráficos para tener una visualización más clara sobre el contenido de la base de datos
        
PASO 2
        -Encontré la página https://www.pesmaster.com/ de donde realizaría web scraping
        -La página contiene información similar a la de FIFA, pero con otras valoracions tanto de clubes como de jugadores
        -Me dediqué exclusivamente a scrapear los nombres y valoraciones de todos los equipos presentes en el juego
        tanto selecciones como clubes
        -Generé un archivo CSV para cada scraping que hice
        -Generé un merge de todos mis archivos CSV dentro de una base general denominada PESDataBase
        -Esta base de datos me serviría como base para hacer un merge con la base de Fifa, pero al no estar completa
        decidí simplemente dejarla pendiente para que en ella le genere un merge con toda la información de los jugadores
        
    
PASO 3
        -No encontré API libres para trabajar con la estadística de los jugadores o clubes de donde buscaba obtener información de su cantidad de goles
        asistencias, lesiones, tarjetas, partidos jugados, partidos suspendidos, etc.
        -Encontré una serie de archivos JSON en GitHub sobre resultados históricos de algunas ligas, pero no sobre los jugadores
        -Trabajé sobre algunos archivos JSON para visualizarlos, pero el resto no los utilicé,,
        -Los siguientes pasos serán encontrar la información que necesito desde una API o archivo JSON y completarla con la base de datos PESDataBase y,
        posteriormente, hacer un merge con fifadb para tener una base de datos robusta que me permita hacer una comparación entre jugadores, salarios, etc.



```
