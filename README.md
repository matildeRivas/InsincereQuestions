# Plan de Acción Hito 1

### Motivación
Podemos ver que la caracterizacion hecha previamente no es la mas adecuada y ademas no es muy descriptiva. La motivacion es poder realizar una caracterizacion de
las preguntas de manera que sea lo mas representativa posible y siga con el modelo de pregunta insincera o no.

### Hipotesis
* ¿Podemos reconocer ciertos patrones en las preguntas ya marcadas en el dataset?
* ¿Es posible generar grupos o categorias se pueden identificar dentro del dataset, tanto las marcadas sinceras como las que no? 
* ¿Tienen palabras comunes ambas etiquetas dentro del dataset dado?
* ¿Se pueden establecer claras diferencias entre preguntas incinceras y sinceras?
* (Mas importante de todas) ¿Se puede automatizar el proceso de clasificacion de nuestras etiquetas en el dataset?

### Como hacerlo (plan de accion)?
1. Primero generar un analisis de los datos sin preprocesar. A esto nos referimos como:
    - Contar n-gramas, generar word clouds de los n-gramas en cada tipo del dataset (insincero y sincero).
    - Ver su metadata, es decir, evaluar caracteristicas que tienen una pregunta insincera con respecto a su estructura como palabra (largo de estos, su promedio de palabras unicas usadas, etc...)
    - Generar word clouds de palabras unicas en cada tipo del dataset.
    - (Tambien puede ser graficos y no solo wordclouds de estas cosas)
2. A partir de esto poder realizar las categorias que queremos y ver correlacion entre ambas exploraciones de los datos generadas. Ademas podemos ver las
similitudes y differencias entre ambas categorias ya asignadas con anterioridad.

3. Ver como serian los speech de declaraciones con estas categorias en otros trabajos como tweeter, facebook, comentarios de emol, etc... (Deseable)

4. Sacar el ruido de las preguntas marcadas como sinceras para que no afecten la creacion de las categorias.

5. Generar los tags y concluir con respecto a las hipotesis planteadas
## Link al dataset
El dataset puede ser encontrado en: https://www.kaggle.com/c/quora-insincere-questions-classification

#Parte 2: Reunión con los profes
1. Ver librerias de prediccion de sentimientos en las frases, de n-gramas, lexicones, de emociones. El score de los n-gramas, topic models (algoritmos para ver el topico con cierta distribución de probablidad).
-> Añadir estas features para mejorar la predicción, y realizar experimentos sobre estas features para ver cuales son las que ganamos más información.
2. Hacer experimentos, con la añadición de el analisis
3. Ver emotion lexicons sobre las palabras.