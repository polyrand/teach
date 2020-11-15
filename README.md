# Materiales Pyton

> Materiales y ejercicios utilizados para enseñar Python.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/polyrand/teach/HEAD)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polyrand/teach/)

## Ejercicios

En ese repositorio están también las soluciones a los ejercicios que se harán en el curso, pero se trata de hacerlos sin mirarlas. Las soluciones están en los archivos con el nombre: NN_xNN. Siendo N = un número. Por ejemplo:

```
04_funciones.ipynb: Archivo con la documentación para enseñar el tema 04_funciones
04_x01.ipynb: Archivo con la solución al ejercicio 01 del tema 04_funciones
04_x02.ipynb: Archivo con la solución al ejercicio 02 del tema 04_funciones

05_estructuras_de_datos.ipynb: Archivo con la documentación para enseñar el tema 05
05_x01.py: Archivo con la solución al ejercicio 02 del tema 05
05_x02.py: Archivo con la solución al ejercicio 02 del tema 05
```

## Instalación

Para una instalación completa. Clonar el repositorio, crear un nuevo entorno virtual e instalar las dependencias.

```sh
git clone https://github.com/polyrand/teach.git
cd teach

###
# crear un entorno virtual
###

pip install -r requirements.txt
```

Esto instalará todas las dependecias. Tanto de desarollo como de ejecución de los notebooks. Para instalar solamente las librerias utilizadas en los notebooks:

```sh
git clone https://github.com/polyrand/teach.git
cd teach

###
# crear un entorno virtual
###

pip install -r requirements/main.txt
```

## Licencia de uso

Actualmente estos contenidos están bajo dos licencias diferentes.

* Apache 2.0: ``LICENSE_A``
* GPL v3: ``LICENSE_B``

Los elementos de este repositorio se podrán utilizar bajo la licencia Apache 2.0 (`LICENSE_A`) **excepto si se utilizan con motivos educativos o de formación**. Si se utilizan con este segundo fin, ya se con o sin ánimo de lucro, la licencia utlizada deberá ser GPL v3 (`LICENSE_B`). Por lo tanto se deberán citar todas las fuentes (incluídas en los materiales actuales), así como hacer el código de dicha actividad formativa abierto y disponible para todo el mundo.

## License

Currently these contents are under two different licenses.

* Apache 2.0: `` LICENSE_A``
* GPL v3: `` LICENSE_B``

The parts of this repository may be used under the Apache 2.0 license (`LICENSE_A`) **except if used for educational or training purposes**. If used for this second purpose, whether for profit or not, the license used must be GPL v3 (`LICENSE_B`). Therefore, all sources (included in current materials) must be cited, as well as making the code of said training activity open and available to everyone.

## Fuentes

Si consideras que alguno de los ejercicios proviene de una fuente no citada. Por favor abre una *pull request* para que lo modifique si es necesario.

## Historial de cambios

* 0.1.0
    * Primer versión

## Meta

Ricardo Ander-Egg Aguilar:

* [@ricardoanderegg](https://twitter.com/ricardoanderegg)
* [ricardoanderegg.com](http://ricardoanderegg.com/)
* [github.com/polyrand](https://github.com/polyrand/)
* [linkedin.com/in/ricardoanderegg](http://linkedin.com/in/ricardoanderegg)

## Contributing

1. Fork it (<https://github.com/polyrand/teach/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

