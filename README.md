# CuraDeudaTest
Cura Deuda API Exercise

1. Obtiene una copia de la información expuesta en el sitio de SEPOMEX

2.Modelar las tablas para la información de SEPOMEX. 
  a.Separa la información en, por lo menos, 3 tablas: Estado, Municipio, Colonia 
  b.Relaciona tus tablas por medio de sus identificadores diseñados por SEPOMEX 

3.Desarrollar una técnica de carga de los datos a partir de la información de SEPOMEX 
que pueda ejecutarse a demanda (seed script). 

4.Crear un API para obtener los datos del registro de cada recurso modelado. 
  a.El intercambio de datos se debe dar por medio de la estructura JSON. 

5.Permitir al API por lo menos: 
  a.Búsqueda de colonias por CP 
  b.Búsqueda de colonias, municipios, estados por nombre 
  c.Adición de nuevos registros a los recursos. 

6.Agregar el manejo de errores.

# Pasos para ejecutar de manera local

1. En una carpeta vacía crear un entorno virtual, en mi caso usando el comando:
  ## python3 -m venv cura-deuda-env
  
2. Intalar las librerias necesarias usando PIP:
  ## pip3 install -r requirements.txt
  
3. En mi caso tengo instalado mysql, se necesita crear una base de datos vacía y los datos de conexión colocarnos en en archivo database.py que esta dentro de el directorio models.

4. Una vez creado activado nuestro entorno virtual y habiendo instalando las librerias necesarias, corremos el proyecto con el comando:
  ## python3 app.py
  
5. Si queremos hacer uso del seed script podemos ejecutar el archivo seed_script.py
  ## python3 seed_script.py
  
6. Listo, podemos hacer uso de los endpoints, estos secomunican mediante JSON.

# Usando los endpoints

- Por ejemplo para consultar localhost:5000/state/ usando GET, mediente JSON le mandamos el {"state": "mexico"}
- Por ejemplo para consultar localhost:5000/township/ usando GET, mediente JSON le mandamos el {"township": "amecameca"}
- Por ejemplo para consultar localhost:5000/suburb/ usando GET, mediente JSON le mandamos el {"suburb": "sacromonte"}
- Por ejemplo para consultar localhost:5000/suburb/postal_code/ usando GET, mediente JSON le mandamos el {"postal_code": "56900"}

y para usar los endpoints con método POST:

- Por ejemplo para consultar localhost:5000/state usando POST, mediente JSON le mandamos el {"code": "123", "description": "nuevoEstado"}
- Por ejemplo para consultar localhost:5000/township usando POST, mediente JSON le mandamos el {"code": "02", "description": "amecameca", "state_code": "123"}
- Por ejemplo para consultar localhost:5000/suburb usando POST, mediente JSON le mandamos el {"code": "56900", "description": "sacromonte", "township_code": "02"}




