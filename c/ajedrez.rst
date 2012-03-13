El peor ajedrez del mundo
=========================

.. highlight:: c

El programa que analizaremos ahora es un sencillo juego de ajedrez.
Este código es más largo que los que hemos visto hasta ahora,
así que cópielo y péguelo en vez de tipearlo.

.. literalinclude:: programas/ajedrez.c

Cada pieza del ajedrez la representaremos con una letra:

* P es el peón,
* T es la torre,
* C es el caballo,
* A es el alfil,
* D es la dama, y
* R es el rey.

Las piezas blancas serán letras mayúsculas,
y las negras, minúsculas.

En cada turno,
el programa mostrará la disposición del tablero,
y pedirá a uno de los jugadores que ingrese su jugada:

.. code-block:: none

       0 1 2 3 4 5 6 7
      +---------------+
    a |t c . d r a . t|
    b |p p p . p p p p|
    c |. . . . . c . .|
    d |. . . p . . . .|
    e |. . A . P . a .|
    f |. . . . . D . .|
    g |P P P P . P P P|
    h |T C A . R . C T|
      +---------------+
    Juega blanco: 

La jugada se ingresa indicando la casilla donde está la pieza que se moverá,
y la casilla a la que se moverá.
Cada casilla se ingresa como sus coordenadas (una letra y un número),
y ambas casillas van separadas por un espacio.
Por ejemplo:

.. code-block:: none

    Juega blanco: f5 e6

Nuestro juego de ajedrez es realmente malo.
No hace cumplir las reglas,
por lo que se puede mover las piezas como a uno se le dé la gana.
¡Incluso el jugador blanco puede mover las piezas negras!

Si uno ingresa jugadas que no tengan sentido,
el programa puede fallar de maneras inesperadas.
¡Inténtelo!


Tipos enumerados
----------------
Un **tipo enumerado** es un tipo de datos
que puede respresentar sólo una lista de valores discretos
indicados por el programador.

Para crear un tipo enumerado,
en C se usa la sentencia ``enum``,
en la que se enumera cuáles son los valores posibles.
Por ejemplo::

    enum sexo {MASCULINO, FEMENINO};
    enum semaforo {ROJO, AMARILLO, VERDE};
    enum palo {CORAZON, PICA, TREBOL, DIAMANTE};

Al principio de nuestro programa,
creamos un tipo enumerado llamado ``enum color``,
que podemos usar cuando necesitemos guardar algún color::

    enum color {BLANCO, NEGRO, VACIO};

El valor ``VACIO`` nos permite usar variables ``enum color``,
por ejemplo, para almacenar el color que tiene la pieza
que está en una casilla,
siendo que podría no haber ninguna pieza en ella.

La verdad es que en C los tipos enumerados son una farsa.
Al declarar una variable de tipo ``enum color``,
realmente estamos declarando una variable entera,
y los valores ``BLANCO``, ``NEGRO`` y ``VACIO``
son en realidad los enteros 0, 1, y 2.

Al compilador le da lo mismo si uno mezcla los valores enumerados
con los enteros, y no descubrirá ningún error que podamos haber cometido.
Al final, usar un tipo enumerado sirve sólo
para hacer que el código sea más fácil de comprender.
Pero si cometemos alguna barbaridad como  ``color = -9000``,
que probablemente es un error lógico de nuestro programa,
el compilador hará oídos sordos.

En nuestro programa,
nosotros nos aprovechamos de la dualidad enum-entero
para cambiar el turno después de cada jugada.
Lo lógico habría sido hacerlo de este modo::

    if (turno == BLANCO)
        turno = NEGRO;
    else if (turno == NEGRO)
        turno = BLANCO;

Pero nosotros sabemos que ``BLANCO`` y ``NEGRO`` son 0 y 1,
por lo que podemos abreviarlo ingeniosamente
(pero no más claramente)::

    turno = 1 - turno;


Arreglos bidimensionales
------------------------

Variables globales
------------------

Funciones que no retornan nada
------------------------------
La sintaxis para crear una función en C
exige indicar de qué tipo es su valor de retorno.
Sin embargo, es posible crear una función que no retorne nada.

Para esto, hay que poner que su tipo de retorno es ``void``,
que se puede interpretar como «ningún tipo».

Hay varias razones por la que una función podría no retornar nada:
* la función hace entrada o salida (como ``imprimir_tablero``),
* la función actúa sobre variables globales (como ``mover_pieza``),
* la función debe «retornar» más de un valor,
  por lo que se usan los parámetros para entregar los valores
  (como ``leer_jugada``, explicado más adelante).


Macros con parámetros
---------------------

Declaraciones de funciones
--------------------------

Paso de parámetros por referencia
---------------------------------

Conversiones de caracteres
--------------------------