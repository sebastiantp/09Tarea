# Tarea nro. 9
## FI3104B - Métodos Numéricos para la Ciencia y la Ingeniería
#### Prof. Valentino González

## P1

En 1929 Edwin Hubble comparó la velocidad de recesión de las _Nebulosas_ (la
idea de galaxias lejanas era aún reciente asi que se les llamaba nebulosas) con
las distancias entre estas _Nebulosas_ y la Tierra. Las distancias fueron
medidas usando el método de las _Cefeidas_, que son estrellas de luminosidad
variables cuyo período y luminosidad están fuertemente correlacionados. La
llamada relación período–luminosidad había sido recientemente calibrada.

Hubble no fue el primero en calcular esta relación pero su trabajo fue de los
más influyentes de la época, convenciendo al mundo de la expansión del Universo.

El archivo ubicado en este repositorio: `data/hubble_original.dat` contiene las
mediciones originales que Hubble utilizó en este trabajo. Su modelo es bastante
simple:

<img src="eqs/hubble_law.png" height="30px"/>

> Latex: `v = H_0 * D`

Donde H<sub>0</sub> es la _constante de Hubble_ y generalmente se expresa en
unidades de km / s / Mpc (Mpc: Mega parsec, 3.086e24 cm). Utilice los datos
originales para derivar la constante de Hubble incluyendo su intervalo de
confianza al 95%.

> Nota:
>
>    1. Note que este no es exactamente un modelo lineal, ya que no hay una
>       constante para la intersección con el eje y, solo una pendiente. En este
>       caso es fácil derivar la ecuacion para el parámetro H<sub>0</sub> que
>       minimiza &chi;<sup>2</sup>.
>    1. El resultado es diferente si se modela v = H * D; ó D = v / H. No hay
>       motivo para preferir uno sobre el otro, por lo que debe buscar una
>       alternativa que sea simétrica.
>    1. Note que no se proveen los errores de medición. En este caso, una
>       simulación de Bootstrap es una buena alternativa para generar el
>       intervalo de confianza en su estimación de H<sub>0</sub>. Si bien el
>       número de simulaciones recomendado es N * log(N)^2, la muestra es
>       pequeña y vale la pena utilizar un N mayor.


## P2

A pesar de lo influyente de su trabajo, Hubble cometió un gran error en su
estimación de H<sub>0</sub>. El error deriva de utilizar una calibración
equivocada de la relación período–luminosidad (entre otras cosas).

Una estimación más reciente de la constante de Hubble se obtiene con los datos
ubicados en el archivo: `data/SNIa.dat` (Freedman et al. 2000) que utiliza Super
Novas tipo I para estimar distancias para una muestra de galaxias. Entre otras
ventajas, el método permite estimar distancias muy superiores a las que se
pueden medir con el método de las Cefeidas.

Vuelva a estimar la constante de Hubble para estos datos incluyendo su intervalo
de confianza del 95%. Comente.


## P3

El archivo `data/DR9Q.dat` es una sección recortada del catálogo de cuasares del
_Data Release 9_ del _Sloan Digital Sky Survey (SDSS)_. Encuentre la línea recta
que mejor modela la relación entre el flujo en la banda _i_ y la banda _z_,
incluyendo los intervalos de confianza al 95% para los parámetros de la línea
recta.

> Notas
>
>    1. El flujo en la banda _i_ se encuentra en la 80º columna, su error en la 81º
>       columna. La banda _z_ y su error se encuentran en las siguientes dos
>       columnas.
>    1. Para leer el archivo le puede servir la rutina `np.loadtxt` con su
>       parametro `usecols`, vea la ayuda.
>    1. Las unidades del flujo son _nmaggies_ que es una unidad inventada por
>       SDSS tal que 1 nmaggie ~ 3.631e-6 Jy. Transforme todo a unidades de 1e-6
>       Jy para hacer su fiteo (asegúrese de convertir correctamente los flujos
>       y los errores asociados).
>    1. En este caso se tienen los errores de medición en las dos cantidades,
>       utilice una simulación de Monte Carlo para estimar los intervalos de
>       confianza de los parámetros del modelo lineal.
>    1. Para fitear una linea recta simple le puede servir la rutina
>       `np.polyfit`


__Otras Notas.__

- La tarea no pide explícitamente ningún gráfico pero para hacer un informe
  completo Ud. debe decidir qué es interesante y crear las figuras
  correspondientes.

- Utilice `git` durante el desarrollo de la tarea para mantener un historial de
  los cambios realizados. La siguiente [*cheat
  sheet*](https://education.github.com/git-cheat-sheet-education.pdf) le puede
  ser útil. Evaluar el uso efectivo de `git`. Recuerde hacer cambios
  significativos pero relativamente pequeños y guardar seguido.  Evite hacer
  `commits` de código que no compila y deje mensajes que permitan entender los
  cambios realizados.

- Evaluaremos su uso correcto de python. Si define una función relativamente
  larga o con muchos parámetros, recuerde escribir el *doctsring* que describa
  los parametros y que es lo que hace la función.  También recuerde usar nombres
  explicativos para las variables y las funciones.  El mejor nombre es aquel que
  permite entender que hace la función sin tener que leer su implementación.

- Los códigos entregados deben pasar las reglas de
  [PEP8](https://www.python.org/dev/peps/pep-0008/). En la línea de comando
  puede intentar `pep8 <script.py>` y asegurarse de que no hay errores ni
  advertencias. Los comandos `pep8 --show-source <script.py>` y `pep8
  --show-pep8 <script.py>` que vimos en clase le pueden ser útiles. Si es de
  aquellos que resuelven su tarea usando el `ipython notebook`, entonces exporte
  la tarea a un archivo normal de `python` y asegúrese de que pasa el test de
  PEP8.

- La tarea se entrega como un *pull request* en github. El *pull request* debe
  incluir todos los códigos usados además de su informe.

- El informe debe ser entregado en formato *pdf*, este debe ser claro sin
  información ni de más ni de menos.
