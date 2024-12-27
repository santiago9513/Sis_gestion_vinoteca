# **Sistema de Gestión de Vinoteca Virtual**
**Desarrollado en Python**  
**Proyecto Final - Programación II**  
**Universidad Nacional de Entre Ríos**  
**Tecnicatura Universitaria en Desarrollo Web**  

**Tecnologías Utilizadas:**  
- Python
- Flask: Framework web para Python
- Flask-RESTful: Extensión para crear APIs RESTful
- Archivos JSON  
- Visual Studio Code 

---

## **Descripción del Proyecto**  
Este proyecto esta enfocado en la implementación de modelos de datos y lógica interna para consultas expuestas como servicios web. El aplicativo permite realizar consultas sobre una base de datos de una vinoteca virtual contenida en un archivo JSON. Los servicios web y el soporte para Flask fueron proporcionados como parte del enunciado inicial. 

---

## **Objetivo del Proyecto**  
El objetivo principal fue desarrollar y codificar los modelos de datos que representan las entidades de la vinoteca: **Bodega**, **Cepa** y **Vino** desde los diagramas UML correspondientes. Estas entidades heredan de una clase abstracta llamada **EntidadVineria**, que define atributos y comportamientos comunes. También se implementó la lógica necesaria para recuperar información del archivo JSON, convertirla en objetos de dichas clases y retornarla a través de los servicios web proporcionados.

Se desarrolló además un motor de búsqueda apoyado en la clase **Vinoteca**, que centraliza las consultas realizadas sobre la base de datos JSON. Dicha clase actúa como una entidad encargada de gestionar y optimizar el acceso a los datos, permitiendo que las entidades del modelo interactúen directamente con la base de datos a través de sus métodos estáticos.

---
## **Ejecución y Pruebas**

### **Instalacion de dependencias:**
El aplicativo está soportado por el framework Flask, por lo que deberá previamente tenerlo instalado para poder correrlo. Para instalarlo corra el siguiente comando por consola: 

*pip3 install flask*

*pip3 install Flask-RESTful*

### **Servicios**
Los servicios que este aplicativo ofrece son los siguientes: 
1. http://localhost:5000/api/bodegas/<id> 
Se obtiene la información de una bodega, los vinos y cepas que esta 
ofrece. 
2. http://localhost:5000/api/bodegas 
Se consulta el listado completo de bodegas, las cepas y la cantidad de 
vinos que estas ofrecen. 
3. http://localhost:5000/api/cepas/<id> 
Se obtiene la información de una cepa y los vinos y bodegas que la 
ofrecen en sus botellas. 
4. http://localhost:5000/api/cepas 
Se consulta el listado completo de cepas y los vinos y bodegas que las 
ofrecen en sus botellas. 
5. http://localhost:5000/api/vinos/<id> 
Se obtiene la información de un vino, la bodega que lo produce, las cepas 
en las que se lo ofrece, y las partidas con las que se cuenta para él. 
6. http://localhost:5000/api/vinos 
Se consulta el listado completo de vinos, las bodegas que los producen, 
las cepas en las que se los ofrece, y las partidas con las que se cuenta 
para ellos.

Los servicios 2., 4. y 6. pueden recibir los parámetros opcionales orden y reverso (que únicamente puede tomar los valores si o no), los cuales indiquen el campo por el cual las listas deben ser ordenadas y si el orden debe ser el regular o inverso. Además, el 
servicio 6 puede tomar el parámetro adicional anios el cual indique que se recuperen los vinos que incluyan la partida indicada.

### **Pruebas**
URL: http://127.0.0.1:5000/api/bodegas/a0900e61-0f72-67ae-7e9d-4218da29b7d8

Resultado Esperado: 

{"id":"a0900e61-0f72-67ae-7e9d-4218da29b7d8","nombre":"Casa La 
Primavera Bodegas y Viñedos","cepas":["Chardonnay","Malbec","Cabernet 
Suavignon","Merlot"],"vinos":["Profugo","Oveja Black","Sin Palabra"]} 


URL: http://127.0.0.1:5000/api/cepas/33ccaa9d-4710-9942-002d-1b5cb9912e5d 

Resultado Esperado: 

{"id":"33ccaa9d-4710-9942-002d
1b5cb9912e5d","nombre":"Chardonnay","vinos":["Profugo (Casa La 
Primavera Bodegas y Viñedos)","Oveja Black (Casa La Primavera Bodegas 
y Viñedos)","Sin Palabra (Casa La Primavera Bodegas y 
Viñedos)","Sottano (Bodega Sottano)"]} 

URL: http://127.0.0.1:5000/api/vinos/4823ad54-0a3a-38b8-adf6-795512994a4f 

Resultado Esperado: 

{"id":"4823ad54-0a3a-38b8-adf6
795512994a4f","nombre":"Abducido","bodega":"La 
Iride","cepas":["Cabernet 
Suavignon","Malbec"],"partidas":[2024,2023,2022]} 

URL: http://127.0.0.1:5000/api/vinos?anio=2020&orden=nombre&reverso=no 

Resultado Esperado: 

[{"id":"ea3d6c45-e747-2e86-ddf8-0746cc13f21c","nombre":"Familia 
Gascon","bodega":"Escorihuela Gascon","cepas":["Cabernet 
Suavignon","Malbec","Merlot"],"partidas":[2020,2021]},{"id":"205db14f
c0c0-a286-0a5e-0daa7a3f37f0","nombre":"Sin Palabra","bodega":"Casa La 
Primavera Bodegas y Viñedos","cepas":["Chardonnay","Cabernet 
Suavignon","Malbec","Merlot"],"partidas":[2022,2021,2020]}] 

URL: http://127.0.0.1:5000/api/vinos?anio=2020&orden=nombre&reverso=si 

Resultado Esperado:

[{"id":"205db14f-c0c0-a286-0a5e-0daa7a3f37f0","nombre":"Sin 
Palabra","bodega":"Casa La Primavera Bodegas y 
Viñedos","cepas":["Chardonnay","Cabernet 
Suavignon","Malbec","Merlot"],"partidas":[2022,2021,2020]},{"id":"ea3d
 6c45-e747-2e86-ddf8-0746cc13f21c","nombre":"Familia 
Gascon","bodega":"Escorihuela Gascon","cepas":["Cabernet 
Suavignon","Malbec","Merlot"],"partidas":[2020,2021]}]



