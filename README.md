# Proyecto Final Python C1 — OdontoCare

## Introducción

El objetivo principal de este proyecto es integrar los distintos contenidos del curso y aplicarlos al desarrollo de una solución backend completa y funcional. Para ello, el estudiante deberá implementar un sistema que combine los siguientes componentes fundamentales:

* **Framework Backend**: Desarrollo de una API REST utilizando Flask, organizada de forma profesional mediante Blueprints para asegurar modularidad y escalabilidad.
* **Persistencia de Datos**: Uso de una base de datos SQLite, gestionada a través de SQLAlchemy como ORM para modelar entidades, relaciones y operaciones CRUD.
* **Seguridad**: Implementación de un mecanismo de autenticación basado en tokens, garantizando el acceso seguro a los distintos recursos del sistema.
* **Cliente Externo**: Creación de un script independiente en Python que consuma los servicios de la API utilizando la biblioteca `requests`, demostrando la correcta interacción entre cliente y servidor.
* **Arquitectura Distribuida y Comunicación entre Servicios**: Creación de imágenes en Docker.

Este objetivo busca consolidar las competencias del nivel C1, permitiendo al estudiante demostrar su capacidad para diseñar, desarrollar e integrar un backend completo con un enfoque profesional.

---

## Escenario del Proyecto

Una red de clínicas dentales ha decidido modernizar sus operaciones creando una aplicación a la medida para gestionar las citas de los pacientes y la disponibilidad de los odontólogos. Actualmente, el sistema se maneja de forma manual, lo que provoca errores frecuentes, duplicidad de información y falta de trazabilidad en los procesos administrativos.

Como desarrollador backend asignado al proyecto, tu misión consiste en diseñar y construir una solución integral, robusta y escalable, que permita cubrir todas las necesidades del nuevo sistema de gestión **OdontoCare**. Para ello, se requiere el desarrollo de una API RESTful profesional, siguiendo buenas prácticas de arquitectura de software, seguridad y persistencia de datos.

El sistema debe permitir la administración eficiente de la información mediante los siguientes módulos esenciales:

* Pacientes
* Doctores
* Centros médicos o clínicas
* Citas médicas

Toda la información gestionada por la API debe persistir en una base de datos confiable. Además, el acceso a los recursos debe estar controlado mediante un mecanismo de autenticación basado en tokens (JWT o similar), garantizando que solo los usuarios autorizados puedan interactuar con los datos.

El formato de comunicación de todos los servicios será exclusivamente **JSON**, por lo que cada endpoint debe responder consistentemente en este formato, tanto en operaciones exitosas como en el manejo de errores.

El estudiante deberá definir y organizar adecuadamente la estructura del proyecto. Adicionalmente, deberá incluir un archivo `requirements.txt` para cada proyecto, en el cual se especifiquen todas las librerías y dependencias necesarias, incorporando aquellas que considere pertinentes para el correcto desarrollo de la actividad.

---

## Objetivos Principales del Sistema

* Diseñar una API RESTful organizada, modular y mantenible.
* Implementar operaciones CRUD para pacientes, doctores, centros y citas.
* Garantizar la persistencia de la información en una base de datos (SQL o NoSQL).
* Incorporar un sistema de autenticación segura por tokens.
* Asegurar que todas las respuestas se entreguen en formato JSON.
* Aplicar buenas prácticas como validación de datos, manejo de excepciones, paginación y documentación básica del API.
* Implementar una arquitectura distribuida basada en contenedores Docker.

---

## Arquitectura de la Solución

Para garantizar un desarrollo ordenado, escalable y alineado con buenas prácticas de ingeniería de software, la API debe implementarse utilizando una arquitectura modular basada en **Blueprints de Flask**. Esto permitirá separar la lógica del sistema por dominios funcionales, facilitando su mantenimiento, comprensión y reutilización.

La solución no debe concentrar todo el código en un solo archivo. En su lugar, se exige una estructura organizada que distribuya la lógica en módulos claros y coherentes. La API deberá estructurarse, como mínimo, con los siguientes componentes:

---

### auth_bp — Autenticación y Gestión de Usuarios

Encargado de todas las operaciones relacionadas con el acceso seguro al sistema. Debe incluir:

* Registro de usuarios autorizados.
* Inicio de sesión mediante validación de credenciales.
* Generación y validación de tokens de autenticación (JWT).
* Manejo de errores de acceso.

Este módulo garantiza que todas las acciones dentro del sistema sean realizadas solo por usuarios autenticados.

---

### admin_bp — Administración y Gestión de Centros, Pacientes y Doctores

Módulo orientado a tareas administrativas, encargado de configurar los elementos base del sistema. Debe incluir:

* Creación de entidades principales: centros médicos, pacientes y doctores.
* Carga de datos, tanto masiva como individual, utilizando archivos en formato JSON cuando sea requerido.
* Opciones de consulta para todos los tipos de registros, permitiendo:

  * Búsqueda individual por ID.
  * Visualización opcional de una lista completa de registros.

Este módulo está diseñado para usuarios con roles administrativos o de gestión.

---

### citas_bp — Gestión Operativa de Citas

Responsable del núcleo funcional de **OdontoCare**: la planificación, administración y control de citas médicas. Debe incluir:

* Creación, actualización, consulta y eliminación de citas.
* Validación de disponibilidad de doctores y centros.
* Reglas operativas para evitar conflictos en la agenda.
* Respuestas en formato JSON con mensajes claros y estructurados.

Este módulo será el más utilizado durante la operación diaria d

**Nota**: El resto de la actividad se encuentra descrito en el enunciado del ejercicio. El estudiante debe leer detenidamente cada uno de los puntos de la actividad para desarrollar correctamente el ejercicio. 

---

## Requisitos de Entrega y Demostración

La entrega final del proyecto no solo incluye el código fuente, sino también la demostración práctica y la evidencia del correcto funcionamiento del sistema basado en microservicios.

---

### Código Funcional (Fork en Git)

El requisito fundamental es la entrega del código fuente completo y funcional.

* **Plataforma**: El código debe estar alojado en un repositorio Git.
* **Contenido**: El repositorio debe incluir todos los componentes del sistema **OdontoCare**, siguiendo la arquitectura distribuida definida, con servicios independientes para **Usuarios/Administración** y **Citas**.
* El estudiante debe desarrollar y presentar un conjunto de scripts que demuestren de forma práctica el funcionamiento de los servicios y su correcta interacción.

---

### Pruebas de Integración (Opcional)

De forma opcional, se pueden incluir o desarrollar pruebas de integración que validen la comunicación entre los distintos servicios y el acceso externo a los endpoints expuestos.

Las pruebas de integración podrán incluir cualquiera de los siguientes métodos:

* Scripts que realicen llamadas directas a los endpoints del servicio (utilizando librerías HTTP o comandos como `curl`).
* Implementación de pruebas unitarias utilizando **unittest** o el módulo **flask.testing**.

---

### Documentación de Pruebas de Endpoints

Se deberá entregar documentación o scripts que incluyan, de forma clara y ordenada, la siguiente información para cada prueba de endpoint realizada:

* **Endpoint utilizado**: Ruta completa del servicio REST.
* **Archivo de entrada**: Cuerpo de la solicitud enviado, obligatoriamente en formato **JSON**.

---

### Video Explicativo

Se requiere una demostración visual, clara y concisa del aplicativo desarrollado.

**Requisitos del video:**

* **Duración máxima**: 5 minutos.
* **Contenido**: Debe evidenciar claramente el funcionamiento completo del aplicativo, incluyendo la interacción entre los microservicios.
* **Funcionamiento**: Mostrar el flujo de trabajo del sistema, desde la inicialización de los servicios hasta la creación de una cita médica, destacando la comunicación RESTful entre los módulos.

## Explicación de estructuración de directorios del proyecto

### odontocare

Contiene el microservicio auth_and_admin_bp, que ofrece los servicios de autenticación y de gestión administrativa.

#### módulo auth_and_admin_bp

Este módulo contiene el microservicio auth_and_admin_bp, que sirve para la autenticación (auth), y la gestión administrativa de las distintas entidades del proyecto (a excepción de la creación de las citas).

##### admin_bp

En este directorio consta todo lo relacionado con la gestión administrativa de la plataforma Odontocare.

###### addresses

Contiene tanto los recursos (endpoints) como los servicios para la gestión de las direcciones.

###### centers

Contiene tanto los recursos (endpoints) como los servicios para la gestión de los centros médicos.

###### doctors

Contiene tanto los recursos (endpoints) como los servicios para la gestión de los doctores.


###### patients

Contiene tanto los recursos (endpoints) como los servicios para la gestión de los pacientes.

###### user_roles

Contiene tanto los recursos (endpoints) como los servicios para la gestión de los roles de usuario.

###### users

Contiene tanto los recursos (endpoints) como los servicios para la gestión de los usuarios.

###### exceptions

Contiene tanto las excepciones personalizadas.

###### already_exists:

Contiene las excepciones personalizadas para el caso de que ya exista una entidad (con el mismo identificador o atributos).

###### authorization:

Contiene las excepciones para la gestión relacionada con authorización, como cuando el usuario tiene un rol que no está autorizado.

###### not_found:

Contiene las excepciones para cuando no se encuentra una entidad (por id o atributos de los campos especificados).

##### healthcheck

Contiene tanto los recursos (endpoints) como los servicios para la comprobación de si el microservicio está con estado saludable (health).

### models

Contiene los modelos que representan las entidades de la aplicación de autenticación y administración.

#### app.py

Contiene los blueprints de la aplicación

### Dockerfile

Contiene las instrucciones (que serán capas) para contruir la imagen para la aplicación.

### extensions.py

Contiene la instanciación del ORM de base de datos (SQLAlchemy)

### requeriments.txt

Contiene las dependencias a instalar para la aplicación.

### first_configs.py

Contiene la creación del primer usuario administrador de la plataforma Odontocare, con las variables recuperadas del archivo de entorno .env:

ADMIN_FIRST_APP_USER_USERNAME

ADMIN_FIRST_APP_USER_PASSWORD

### run.py

Contiene la inicialización de la aplicación especificando la IP (host) y puerto por el que escuchará.

### .env:

Archivo de entorno (.env) que se debe crear (no viene por defecto en el repositorio ya que está ignorado).

Se debe crear obligatoriamente con las siguientes variables de configuración:

SECRET_KEY (con una clave secreta para hashing de las contraseñas de los usuarios)

ADMIN_FIRST_APP_USER_USERNAME (con el nombre del primer usuario administrador)

ADMIN_FIRST_APP_USER_PASSWORD (con la primera contraseña del usuario administrador)

ejemplo:

SECRET_KEY = secreto
ADMIN_FIRST_APP_USER_USERNAME = username
ADMIN_FIRST_APP_USER_PASSWORD = password

#### módulo cites_bp

Este módulo contiene el microservicio cites_bp, que sirve para la gestión de las citas, y los estados posibles de las citas.

###### appointment_statuses

Contiene tanto los recursos (endpoints) como los servicios para la gestión de los estados de las citas médicas.

###### appointments

Contiene tanto los recursos (endpoints) como los servicios para la gestión de las citas médicas.

###### auth

Contiene los servicios para el login contra el microservicio de auth_and_admin_bp (autenticación y gestión administrativa de la clínica).

###### decorators

Contiene los decoradores que sirven para comprobar si cumple los requisitos de autenticación, y require_role para ver si está autorizado a ver un recurso.

###### dtos

Contiene las clases del otro microservicio, que en este caso no serán modelos, sino Data Transfer Objects (DTO) para la gestión y facilidad de gestión de los objetos a enviar y recibidos del microservicio de autenticación y administración.

###### enums

Contiene los Enums relacionados con el microservicio de citas, que en este caso es para las acciones a realizar sobre una cita médica, y del estado de una cita médica respectivamente.

###### exceptions

Contiene tanto las excepciones personalizadas.

###### already_exists:

Contiene las excepciones personalizadas para el caso de que ya exista una entidad (con el mismo identificador o atributos).

###### authorization:

Contiene las excepciones para la gestión relacionada con authorización, como cuando el usuario tiene un rol que no está autorizado.

###### not_found:

Contiene las excepciones para cuando no se encuentra una entidad (por id o atributos de los campos especificados).

###### action_already_applied:

Contiene las excepciones para si una acción ya se ha aplicado sobre una entidad.

###### invalid:

Contiene las excepciones para si una acción a aplicar no es válida.

##### healthcheck

Contiene tanto los recursos (endpoints) como los servicios para la comprobación de si el microservicio está con estado saludable (health).

##### models

Contiene los modelos de esta aplicación como MedicalAppointment y MedicalAppointmentStatus.

#### app.py

Contiene los blueprints de la aplicación

### Dockerfile

Contiene las instrucciones (que serán capas) para contruir la imagen para la aplicación.

### extensions.py

Contiene la instanciación del ORM de base de datos (SQLAlchemy)

### requeriments.txt

Contiene las dependencias a instalar para la aplicación.

### .env:

Archivo de entorno (.env) que se debe crear (no viene por defecto en el repositorio ya que está ignorado).

Se debe crear obligatoriamente con las siguientes variables de configuración:

SECRET_KEY (con una clave secreta para hashing de las contraseñas de los usuarios)

ejemplo:

SECRET_KEY = secreto

### run.py

Contiene la inicialización de la aplicación especificando la IP (host) y puerto por el que escuchará.

#### módulo cargador_inicial

Este módulo contiene la estructura de carpetas necesarias, junto al script carga_inicial.py, para hacer la primera creación de una cita médica a través del fichero de datos csv dades.csv.

##### converters

Este módulo contiene los convertidores (converters) para convertir las filas (rows) recuperadas del DataFrame del CSV mediante Pandas a instancias de entidad (genera entidades) de su clase de Modelo respectiva.

##### data

Este directorio contiene el fichero de datos csv a importar dades.csv con los datos a importar para cada entidad a crear y de cada tipo de entidad.

##### dtos

Contiene las clases del otro microservicio, que en este caso no serán modelos, sino Data Transfer Objects (DTO) para la gestión y facilidad de gestión de los objetos a enviar y recibidos del microservicio de autenticación y administración, y del de citas.

### models

Contiene los modelos que representan las entidades del módulo de cargador_inicial, que es el Token para representar un token de JWT.

### services:

Contiene los servicios para crear entidades haciendo peticiones hacia el microservicio de autenticación y administración (todos los que no sirvan para crear estado de cita ni el de para crear citas médicas), y también hacia el microservicio de citas (los que sirvan para crear estado de cita ni el de para crear citas médicas).

### util:

Tiene una utilidad para leer los datos del archivo csv.

### .env:

Archivo de entorno (.env) que se debe crear (no viene por defecto en el repositorio ya que está ignorado).

Se debe crear obligatoriamente con las siguientes variables de configuración:

ADMIN_FIRST_APP_USER_USERNAME (con el nombre del primer usuario administrador)

ADMIN_FIRST_APP_USER_PASSWORD (con la primera contraseña del usuario administrador)

ejemplo:

ADMIN_FIRST_APP_USER_USERNAME = username
ADMIN_FIRST_APP_USER_PASSWORD = password

### carga_inicial.py

Es el script principal del cargador_inicial, que lee las variables de entorno (.env), hace login con el primer usuario administrador de la plataforma Odontocare. A continuación, lee los datos del archivo dades.csv, instancia los convertidores (converters) a instancias de sus respectivas Entidades, generando entidades o instancias de Entidad.

Finalmente, creando las entidades llamando al servicio correspondiente, que hará una petición al microservicio de autenticación y administración (auth_and_admin_bp) si no se trata de la creación de un estado de cita, o de la creación de una cita médica. En caso de tratarse de la creación de un estado de cita médica, o de la creación de una cita médica, llama a microservicio de citas (cites_bp).

### Dockerfile:

Contiene las instrucciones (que serán capas) para contruir la imagen para la aplicación.

### requeriments.txt

Contiene las dependencias a instalar para la aplicación.

### run.py

Contiene la inicialización de la aplicación del script de cargador_inicial.

## .gitignore:

Contiene los archivos a ignorar.

## docker-compose.yml:

Define los servicios de la plataforma auth_and_admin_bp, cites_bp y carga_inicial, y su creación de imagen y configuración de contenedor, una red de Docker para que se puedan comunicar, y también hacia Internet y descargar las dependencias.

## video:

En esta carpeta, se contendrá el vídeo de la explicación.

## postman_endpoints_test:

En esta carpeta, se contienen los tests de endpoints realizados con Postman.

# Referencias:

## Decorators / Decoradores:

https://aula.uoc.edu/courses/70601/pages/python-c1-tema-3-3c-autenticacio-basica-de-tokens-i-autoritzacio?module_item_id=2621295

https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments

## bcrypt:

https://pypi.org/project/bcrypt/

https://github.com/pyca/bcrypt/

https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/

https://dev.to/abbyesmith/password-hashing-using-bcrypt-in-python-2i08

## datetime:

https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat

## Detectar si es instancia:

https://stackoverflow.com/questions/624926/how-do-i-detect-whether-a-variable-is-a-function

## Cambiar de puerto:

https://www.geeksforgeeks.org/python/how-to-change-port-in-flask-app/

## SQL Alchemy:

https://docs.sqlalchemy.org/en/20/tutorial/data_select.html

https://docs.sqlalchemy.org/en/20/tutorial/data_select.html#the-where-clause

https://aula.uoc.edu/courses/70601/pages/python-c1-tema-3-3b-persistencia-de-dades-amb-sqlalchemy?module_item_id=2621293

## HTTP / REST:

### Servidors i Clients HTTP:

https://aula.uoc.edu/courses/70601/pages/python-c1-tema-1-1a-servidors-i-clients-http?module_item_id=2621264

### Codis d'estat HTTP:

https://aula.uoc.edu/courses/70601/pages/python-c1-tema-1-1b-codis-destat-http?module_item_id=2621266

### Clients d'una API:

https://aula.uoc.edu/courses/70601/pages/python-c1-tema-1-1c-client-duna-api?module_item_id=2621268

### Eines externes per a APIs:

https://aula.uoc.edu/courses/70601/pages/python-c1-tema-1-1d-eines-externes-per-a-apis?module_item_id=2621269

## Flask:

### Creación de un servicio REST:

https://aula.uoc.edu/courses/70601/pages/python-c1-tema-2-2c-creacio-dun-servei-rest?module_item_id=2621278

### Controles de errores:

https://aula.uoc.edu/courses/70601/pages/python-c1-tema-2-2d-control-derrors-a-flask?module_item_id=2621281

### Datos al cuerpo de la petición:

https://aula.uoc.edu/courses/70601/pages/python-c1-tema-2-2e-maneig-de-dades-de-la-peticio?module_item_id=2621283

### Modularidad con Blueprints

https://aula.uoc.edu/courses/70601/pages/python-c1-tema-2-2f-modularitat-de-les-api-amb-blueprints?module_item_id=2621285