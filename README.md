[![Build and deploy Python app to Azure Web App - Recomendaciones](https://github.com/CodeCraft-Solutions-DREAM-Lab/RecomendacionesDreamLab/actions/workflows/main_recomendaciones.yml/badge.svg)](https://github.com/CodeCraft-Solutions-DREAM-Lab/RecomendacionesDreamLab/actions/workflows/main_recomendaciones.yml)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

# Chatbot de recomendaciones del DREAM Lab

## Proyectos relacionados

-   Se puede consultar el frontend en el repositorio de [Frontend](https://github.com/CodeCraft-Solutions-DREAM-Lab/Front-End).
-   Asimismo, el backend se puede encontrar en el repositorio de [Backend](https://github.com/CodeCraft-Solutions-DREAM-Lab/Back-End).
-   El resto de los repositorios del proyecto se pueden encontrar en [CodeCraft Solutions: D.R.E.A.M. Lab](https://github.com/CodeCraft-Solutions-DREAM-Lab).

## Despliegue

Este API se encuentra desplegado como un App Service de Azure en la siguiente liga: [https://recomendaciones.azurewebsites.net](https://recomendaciones.azurewebsites.net).

## Configuración

1. Clona el repositorio utilizando Git. Si no tienes Git instalado, puedes descargarlo desde [https://git-scm.com/downloads](https://git-scm.com/downloads).

    Para clonar el repositorio, abre una terminal y ejecuta el siguiente comando:

    ```
    git clone https://github.com/CodeCraft-Solutions-DREAM-Lab/RecomendacionesDreamLab.git
    ```

2. Navega al directorio del proyecto.

    Usando la misma terminal con la que se clonó el repositorio, ejecuta el siguiente comando para cambiar el directorio activo en la terminal y que el resto de los comandos se corran dentro del proyecto:

    ```
     cd "RecomendacionesDreamLab"
    ```

3. Instala las dependencias del proyecto. Para poder correr este comando es necesario tener instalado Python con la versión `3.12` y pip. Puedes descargar Python desde [https://www.python.org/downloads/](https://www.python.org/downloads/) y pip siguiendo las instrucciones de [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/):

    ```
    pip install -r requirements.txt
    ```

4. Crea en la raiz del proyecto el archivo de las variables de entorno:

    4.1. Corre uno de estos dos comandos dependiendo de tu sistema operativo:

    > Unix (macOS, Linux):

    ```
    touch .env && nano .env
    ```

    > Windows

    ```
    echo. > .env && notepad .env
    ```

    4.2. Copia las siguientes variables en el archivo:

    ```
    API_KEY=<API_KEY de OpenAI>
    ```

> [!NOTE]
> Es necesario modificar los valores entre `< >` con los tuyos propios para que funcione la aplicación.
>
> Puedes consultar tu API Key de OpenAI en [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

## Inicio

Para iniciar el servidor, ejecuta:

```
python app.py
```
