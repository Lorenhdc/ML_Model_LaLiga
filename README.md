# ML_Model_LaLiga
> El objetivo de este proyecto de Machine Learning es predecir el resultado de un partido de fútbol a partir de ciertas
> variables de cada equipo que se enfrenta que hemos considerado relevantes para ello (% de puntos, posición en liga, promedio
> de goles a favor, etc). Para nuestro caso, nos hemos enfocado en La Liga española, para la cual hemos recolectado datos de
> todos los partidos jugados entre las temporadas 2000-01 hasta 2020-21.
>
> Seguidamente, hemos separado nuestro datos en el dataset de train con los datos pertenecientes desde 2000-01 al 2012-13, los
> cuales vamos a emplear para entrenar nuestro modelo regresión logística, el cual será de adaptado para un tipo de clasificación
> multiclase ['Gana Local', 'Gana Visitante', 'Empate'], y el dataset de test son los datos a predecir con nuestro modelo ya
> entrenado para ver su nivel de acierto ('Accuracy').
>
> Finalmente, cruzaremos nuestras predicciones con las cuotas de la Casa de Apuestas BET365 para cada partido y veremos
> cuál hubiera sido el premio para aquellas jornadas que hubieramos hecho pleno de acierto y a partir de ahí, establecer un plan
> de apuestas sostenido y rentable en el medio y largo plazo.
