# Megacentros de datos para IA en la Patagonia argentina

## Incentivos a la inversión en un contexto de crisis hídrica: una controversia sociotécnica abierta

**Universidad Nacional de San Martín — Escuela de Ciencia y Tecnología**
**Ciencia, Tecnología y Sociedad — Trabajo Práctico Final**
**2.º cuatrimestre de 2026**

- **Docentes:** [completar]
- **Integrantes:** [completar]
- **Comisión:** [completar]
- **Fecha de entrega:** [completar]

---

## Resumen

Este trabajo analiza, desde el enfoque CTS, la instalación proyectada de megacentros de datos para inteligencia artificial (IA) en la Patagonia argentina. El Estado nacional promueve esa actividad con beneficios fiscales de treinta años (el proyecto de "Súper RIGI") mientras Neuquén y Chubut atraviesan emergencias hídricas, las empresas no informan cuánta agua usarán y las provincias reconocen que no tienen normas específicas. Sostenemos que no se trata de un problema técnico que pueda resolver un experto, sino de una **controversia sociotécnica abierta**, en la que se discute quién define el riesgo, con qué conocimiento y quién captura los beneficios. Para mostrarlo recorremos cuatro ejes: la problemática como problema social complejo (Massarini y Schnek; Funtowicz y Ravetz), el modelo de desarrollo que supone el régimen de incentivos (Sábato y Botana; Mazzucato; Kreimer y Zabala), la disputa por la definición del riesgo hídrico (Beck; Sunstein; Skill y Grinberg; Latour) y la supuesta neutralidad de la tecnología (Pedace, Schleider y Balmaceda; Yuk Hui).

**Palabras clave:** centros de datos, inteligencia artificial, agua, riesgo, RIGI, Patagonia, controversia sociotécnica.

---

## Índice

1. Introducción
2. Una problemática social compleja, no un problema técnico
3. Qué modelo de desarrollo supone el Súper RIGI
4. La disputa por la definición del riesgo hídrico
5. La "nube" no es neutral ni inmaterial
6. Una controversia abierta: estado de situación
7. Conclusión
8. Bibliografía

**Cuadro 1. Ejes de análisis y articulación con el programa**

| Eje de análisis | Unidad | Autores y conceptos |
|---|---|---|
| El caso como problemática social compleja | 1 | Massarini y Schnek (problemática compleja, actores y discursos); Funtowicz y Ravetz (ciencia posnormal, comunidad de pares extendida) |
| El modelo de desarrollo detrás de los incentivos | 2 y 3 | Sábato y Botana (triángulo, extra-relaciones); Mazzucato (Estado emprendedor); Kreimer y Zabala (construcción del problema, quién habla por quién) |
| La definición del riesgo | 4 | Beck (riesgo dependiente del conocimiento, rechazo causal); Sunstein (costo-beneficio, principio precautorio); Skill y Grinberg (postura pragmática y precautoria); Latour (escala, mapeo de controversias) |
| La neutralidad de la tecnología | 5 | Pedace, Schleider y Balmaceda (¿mejora para quién?); Yuk Hui (*pharmakon*, caja negra) |

---

## 1. Introducción

El 10 de octubre de 2025 OpenAI y la empresa Sur Energy firmaron una carta de intención para "explorar" un centro de datos de hasta 500 MW en la Patagonia, con una inversión potencial de hasta USD 25.000 millones, bajo el nombre de Stargate Argentina (DatacenterDynamics, 2025). A ese anuncio se sumaron otros. En julio de 2026 el gobierno de Chubut presentó junto a la empresa polaca Green Capital el Atlas GigaHub, en la Zona Franca de Trelew, que prevé unos 300 MW de capacidad informática en 2029 y unos 3.000 MW en 2033 (EQSnotas, 2026). En Neuquén, además, se evalúa un centro de datos junto a la central térmica de Loma de la Lata, abastecido con gas de Vaca Muerta (Noticias Ambientales, 2026).

El Estado nacional acompaña esta expansión con el Régimen de Incentivo para Grandes Inversiones en Nuevas Industrias, conocido como "Súper RIGI". El proyecto apunta expresamente a los grandes centros de datos de IA: exige una inversión mínima de USD 1.000 millones por proyecto y ofrece una alícuota de Ganancias del 15 % (frente al 35 % general), exención total de derechos de importación y estabilidad de esos beneficios por 30 años. A las provincias que adhieran les impide cobrar más de 0,5 % de Ingresos Brutos (Tarricone, 2026). La Cámara de Diputados lo aprobó el 24 de junio de 2026 por 130 votos contra 106, y desde entonces está trabado en el Senado.

Mientras tanto, la región atraviesa una crisis hídrica. Neuquén declaró en octubre de 2025 la Emergencia Hídrica, Social y Productiva y la prorrogó por 180 días en agosto de 2026, con embalses y caudales en valores históricamente bajos (Noticias NQN, 2026). Chubut declaró su propia emergencia hídrica en agosto de 2026, después de que el caudal del río Chubut cayera hasta un 77 % en algunos puntos de medición; las cuencas del Chubut y del Senguer abastecen a más del 70 % de la población provincial (La Izquierda Diario, 2026).

Los centros de datos usan agua para refrigerar sus equipos y grandes cantidades de electricidad. Sin embargo, ninguno de los proyectos informó cuánta agua necesitará ni de dónde la tomará, y la Secretaría de Ambiente y Recursos Naturales de Neuquén reconoció que "de momento, no hay normativas específicas" para estas instalaciones (Viano y Calmels, 2026).

La pregunta que guía el trabajo es la siguiente: **¿quién define, y con qué conocimiento, si es aceptable promover una industria de alto consumo de agua y energía en una región en emergencia hídrica, y quién se queda con los beneficios y con los riesgos de esa decisión?** Nuestra hipótesis es que el caso no puede tratarse como un asunto técnico reservado a especialistas, porque combina incertidumbre alta, intereses en conflicto y valores en disputa. Es una controversia sociotécnica, y hoy sigue abierta.

## 2. Una problemática social compleja, no un problema técnico

Massarini y Schnek (2015) distinguen el problema de las ciencias naturales, que es teórico, general y simple, de la **problemática social compleja**, que es práctica, particular y compleja. La complejidad no depende de la cantidad de elementos sino de que estén interdefinidos: no se los puede aislar sin destruir el problema. En nuestro caso, la pregunta "¿cuánta agua consume un centro de datos?" es un problema técnico acotado. En cambio, decidir si conviene instalarlo en Trelew o en Confluencia depende al mismo tiempo de la tecnología de refrigeración, del estado de las cuencas, de quiénes más usan esa agua (riego, consumo humano, *fracking*), de la matriz eléctrica, del régimen fiscal y de los derechos de las comunidades que viven allí. Ninguna de esas dimensiones se entiende sin las otras.

Las autoras proponen un método de cuatro pasos para abordar este tipo de problemáticas: identificar a los actores, interpretar sus discursos, analizar cómo se relacionan (incluidas las relaciones de poder) y lograr una comprensión general. El Cuadro 2 resume los dos primeros pasos.

**Cuadro 2. Actores y discursos**

| Actor | Qué sostiene | Qué es el agua en su discurso |
|---|---|---|
| Gobierno nacional | La IA es una oportunidad histórica y hay que atraer la inversión con incentivos y sin trabas regulatorias | Una ventaja comparativa del territorio |
| Gobiernos provinciales (Neuquén, Chubut) | La región es un "microclima ideal" para industrias tecnológicas; "la tecnología avanza mucho más rápido que la regulación" (Etcheverry, citado en Viano y Calmels, 2026) | Un recurso a administrar |
| Empresas (Sur Energy, Green Capital, OpenAI como compradora) | La refrigeración será de circuito cerrado y el impacto, mínimo; las cifras se definirán en estudios futuros | Un insumo cuyo uso se optimiza |
| Comunidades mapuche y asambleas | Ya falta agua y territorio; denuncian "terricidio" (Indymedia Argentina, 2026) | Un bien común y parte del territorio |
| Organizaciones y especialistas (Fundación Vía Libre, Observatorio Petrolero Sur) | El régimen es "a medida de los grandes inversores" y genera "economías de enclave" (Viano y Calmels, 2026) | Un bien público sin información ni control |
| Senadores de bloques aliados y sector industrial | Aceptan el régimen si incluye compras a proveedores nacionales y generación eléctrica propia | No aparece en su agenda |

En cuanto al tercer paso, los discursos no pesan lo mismo. El de las empresas y los gobiernos llega al Congreso en forma de proyecto de ley, mientras que el de las comunidades circula por medios alternativos y asambleas. Llama la atención la última fila: la negociación en el Senado giró en torno a la energía y a los proveedores locales, pero el agua, que es el centro del reclamo territorial, no figura entre los cambios discutidos (Sieira, 2026).

Este escenario coincide con lo que Funtowicz y Ravetz (2000) llaman **ciencia posnormal**: situaciones en las que los hechos son inciertos, hay valores en disputa, lo que está en juego es mucho y las decisiones son urgentes. Los tres rasgos están presentes. La incertidumbre no es solo técnica (qué tecnología de refrigeración se usará), sino también metodológica y epistemológica: nadie sabe cómo evolucionarán las cuencas en los próximos treinta años, que es justamente el plazo de estabilidad que el régimen garantiza a los inversores. Para estos casos los autores proponen una **comunidad de pares extendida**, es decir, que la evaluación de la calidad del conocimiento incluya a quienes serán afectados por la decisión y no solo a los expertos acreditados. En el caso analizado ocurre lo contrario: el compromiso de largo plazo se discute antes de que existan los estudios y sin los afectados en la mesa.

## 3. Qué modelo de desarrollo supone el Súper RIGI

El argumento oficial puede resumirse así: si llega la inversión en infraestructura de IA, llegará el desarrollo. Es una versión actualizada del **modelo lineal** que critica López Cerezo (2017), según el cual más tecnología produce por sí sola más riqueza y más bienestar. Los autores de la Unidad 2 permiten examinar ese supuesto.

Para Sábato y Botana (1968), la innovación es el resultado de un sistema de relaciones entre tres vértices: el gobierno, la infraestructura científico-tecnológica y la estructura productiva. Lo que importa no es cada vértice por separado sino las **inter-relaciones** entre ellos. Si aplicamos el triángulo al caso, el resultado es incompleto. El gobierno ejerce su capacidad de acción, pero la orienta a otorgar beneficios y no a formular demandas a la ciencia y la tecnología locales. La estructura productiva está representada por empresas extranjeras que traerán diseñados sus equipos, su *software* y sus modelos. Y la infraestructura científico-tecnológica argentina (universidades, CONICET, INVAP, ARSAT) prácticamente no aparece. Lo que se fortalece son las **extra-relaciones**: cada vértice local se vincula con el exterior y no con los otros dos. Sábato y Botana advertían que ese es el rasgo de los países que quedan como espectadores del desarrollo tecnológico. Coincide con la descripción de Alan Rocha, del Observatorio Petrolero Sur, que habla de "economías de enclave" que emplean "a 50 o 60 personas" (Viano y Calmels, 2026). Green Capital, en cambio, estima entre 500 y 700 puestos directos en operación y entre 9.000 y 11.000 en el pico de construcción (EQSnotas, 2026). La diferencia entre ambas cifras ya es parte de la controversia.

Mazzucato (2013) agrega una segunda crítica. Su tesis es que los grandes saltos tecnológicos, incluidas Internet y las tecnologías del iPhone, fueron posibles porque el Estado asumió riesgos que el sector privado evitaba y fijó una **misión**. El Estado emprendedor no se limita a "reducir el riesgo" del privado: dirige, invierte y participa de los resultados. El Súper RIGI propone lo opuesto. El Estado resigna recaudación durante treinta años y garantiza estabilidad, pero no define una misión propia (por ejemplo, capacidad de cómputo para la ciencia local o formación de recursos humanos) ni se asegura un retorno. Es el Estado que Mazzucato describe como mero facilitador, que socializa los costos y deja que las ganancias se privaticen. Vicente y López Bedogni (2022) ofrecen un contraste con un ejemplo argentino: ARSAT fue una política orientada a una misión cuyo valor estuvo en el proceso de aprendizaje y en la acumulación de capacidades nacionales, no en tener la tecnología más avanzada.

Por último, Kreimer y Zabala (2006) sostienen que los problemas sociales no existen con independencia de los actores que los definen como tales, y que en esa definición se disputa "quién tiene el derecho legítimo de hablar" en nombre de los demás. En el debate público, el problema se formuló como una **carrera por atraer inversiones**: lo que hay que resolver es qué beneficios ofrecer para que los centros de datos vengan. Formulado así, el agua queda como un dato secundario y las comunidades, como un obstáculo. Las organizaciones territoriales proponen otra definición, la del **acceso al agua en una región en emergencia**, pero su necesidad es "traducida" por otros. Es significativo que la lonko Liliana Romero, de la comunidad Fvta Trayén, lo diga en términos que ningún estudio técnico registra: "Ya no nos queda territorio" (Viano y Calmels, 2026).

## 4. La disputa por la definición del riesgo hídrico

### 4.1. Riesgos que dependen del conocimiento

Beck (1998) plantea que los riesgos de la modernización no se perciben directamente: dependen del conocimiento científico para existir socialmente. Los afectados pierden así su "soberanía cognitiva", porque no pueden determinar por sus propios medios si están en riesgo. En nuestro caso, un vecino de Trelew no tiene forma de saber cuánta agua usará el Atlas GigaHub. Solo la empresa puede producir ese dato, y todavía no lo hizo.

Green Capital afirma que usará refrigeración líquida directa al chip en circuito cerrado, con una "reducción del consumo de agua superior al 90 % frente a sistemas convencionales", pero admite que "las cifras precisas de consumo para cada etapa y las fuentes específicas de abastecimiento todavía están siendo definidas" (EQSnotas, 2026). Sur Energy también habla de "tecnología de circuito cerrado", sin informar volúmenes. A un año del anuncio, no se conocen públicamente las necesidades hídricas de Stargate ni si usará agua del río Limay (Sternik, 2026).

Aquí se ve lo que Beck llama **rechazo causal**: mientras el riesgo no esté demostrado, se actúa como si no existiera. Un porcentaje de reducción sin un valor de base no permite calcular nada, pero funciona como lo que el autor denomina "tranquilizante simbólico". Además, los afectados solo pueden reclamar si aprenden a hablar el lenguaje técnico (metros cúbicos, megavatios, eficiencia hídrica), lo que confirma su dependencia del conocimiento ajeno.

Para dimensionar el problema solo hay estimaciones externas. Una nota de *La Nación* cita un promedio de 7,1 m³ de agua por MWh para centros de datos de Estados Unidos, es decir, más de 2,5 millones de litros anuales por megavatio (Viano y Calmels, 2026). A escala global, Li, Yang, Islam y Ren (2025) proyectan que la demanda de IA podría implicar extracciones de entre 4.200 y 6.600 millones de m³ de agua en 2027. Ninguna de estas cifras es un dato de los proyectos patagónicos, y los diseños de circuito cerrado prometen valores mucho menores. Que la discusión deba apoyarse en promedios de otro país es en sí mismo el problema: los únicos que pueden producir el dato local son quienes tienen interés en que el proyecto se apruebe.

### 4.2. Postura pragmática y postura precautoria

Skill y Grinberg (2013) analizan la controversia por el glifosato distinguiendo dos posturas, que también ordenan nuestro caso (Cuadro 3).

**Cuadro 3. Dos posturas frente al riesgo**

| | Postura pragmática | Postura precautoria |
|---|---|---|
| Quiénes | Gobierno nacional, gobiernos provinciales, empresas | Comunidades mapuche, asambleas, organizaciones ambientales |
| Argumento central | Con buena tecnología (circuito cerrado) el riesgo es bajo o inexistente | En una región en emergencia, la falta de información es razón suficiente para no avanzar |
| El agua es | Un insumo productivo | Un bien común |
| Conocimiento válido | Estudios de las empresas y evaluaciones futuras | También el saber territorial: quien vive junto al río sabe que bajó |
| Frente a la incertidumbre | Posterga la definición: "se verá en el estudio de impacto" | La usa para reclamar el principio precautorio |
| Modelo de desarrollo | Inserción global mediante grandes inversiones | Decisión local sobre los bienes comunes |

Igual que en el caso del glifosato, la postura pragmática usa la incertidumbre para postergar y la precautoria, para exigir que se actúe. La segunda cuenta con respaldo legal: la Ley General del Ambiente establece que, ante peligro de daño grave o irreversible, la ausencia de información o de certeza científica no puede usarse como razón para postergar medidas de protección (Ley 25.675, art. 4). El Convenio 169 de la OIT, aprobado por la Ley 24.071, obliga además a consultar a los pueblos indígenas antes de adoptar medidas que los afecten. La pregunta que Skill y Grinberg toman de la literatura, "¿el conocimiento de quién es el que cuenta?", sigue sin respuesta institucional.

### 4.3. Una objeción desde el costo-beneficio

Sunstein (2006) desconfía de las decisiones basadas en el temor. Sostiene que las personas evaluamos mal los riesgos por la **heurística de disponibilidad** (damos más peso a lo que recordamos con facilidad) y propone el análisis de costo-beneficio para corregir esos errores. Desde su mirada se podría objetar que la alarma por los centros de datos es exagerada, que el *fracking* o el riego usan mucha más agua y que rechazar la inversión también tiene costos.

La objeción es atendible y conviene tomarla en serio. Pero aun aceptando el criterio de Sunstein, el caso no lo cumple. Un análisis de costo-beneficio necesita datos sobre los costos, y aquí el consumo de agua y su fuente no se conocen. Del lado de los beneficios hay cifras en disputa (el empleo) y una carta de intención que no es un contrato. Lo que falta, entonces, no es racionalidad en el público sino información para decidir. Sunstein reconoce además que el análisis es "un punto de partida" y que la ciencia no resuelve las cuestiones normativas. Beck va un paso más allá: los enunciados sobre riesgos contienen siempre afirmaciones del tipo "así queremos vivir", que ningún cálculo puede sustituir.

### 4.4. La escala: la nube tiene dirección

Latour (2011) observa que la crisis ecológica nos desborda por un problema de escala y que nadie ve "lo global": solo existen visiones locales conectadas por instrumentos y redes. El caso lo ilustra bien. Una consulta a un sistema de IA hecha desde cualquier lugar del mundo parece inmaterial, pero se procesa en un edificio concreto que toma agua de una cuenca concreta. La "nube" tiene dirección postal. Lo que para la empresa es una ubicación con buen clima y energía barata, para una comunidad es el único lugar donde puede vivir.

Latour propone no huir de las controversias sino **mapearlas** preguntando a cada actor qué mundo está ensamblando, con quiénes se alinea y con qué entes propone vivir. El mundo que ensamblan los proyectos incluye chips, gasoductos, parques eólicos, exenciones fiscales y contratos de cómputo. El de las comunidades incluye ríos, animales, huertas y vecinos. El río Limay y el río Chubut aparecen en los dos, pero con papeles distintos, y no son un fondo pasivo: su caudal condiciona lo que cualquiera de los actores puede hacer.

La experiencia regional muestra que la participación puede modificar el diseño técnico. En Uruguay, el proyecto de Google preveía consumir unos 7.600 m³ diarios de agua potable; tras el reclamo social y un litigio por acceso a la información en plena sequía, la empresa lo rediseñó con enfriamiento por aire (El Observador, 2023). En Chile, el Segundo Tribunal Ambiental ordenó en 2024 rehacer la evaluación del centro de datos de Google en Cerrillos e incorporar el cambio climático al análisis hídrico (Cooperativa, 2024). En ambos casos, la tecnología "posible" cambió cuando los afectados lograron intervenir.

## 5. La "nube" no es neutral ni inmaterial

Pedace, Schleider y Balmaceda (2023) discuten la idea de que la IA sea objetiva y neutral, y proponen hacer siempre tres preguntas: para quién es una mejora, quién se beneficia y quién evalúa. Aplicadas a la infraestructura, las respuestas son incómodas. La capacidad de cómputo instalada en la Patagonia serviría sobre todo a usuarios y empresas de otros países. Los beneficios fiscales favorecen a los inversores. Y la evaluación ambiental quedaría en manos de provincias que admiten no tener normas ni, probablemente, los equipos técnicos para auditar a empresas de esa escala. La opacidad que los autores señalan en los algoritmos se repite en la infraestructura: no se conocen los consumos, los contratos ni el contenido de la carta de intención.

Yuk Hui (2023) permite pensar esta ambivalencia con la noción de ***pharmakon***: la tecnología es al mismo tiempo remedio y veneno, y no se pueden elegir sus efectos buenos ignorando los malos. Los centros de datos pueden traer inversión, conectividad y empleo calificado, y a la vez competir por el agua y la energía de la región. Hui describe además la industrialización como una metafísica que reduce los seres a "elementos calculables". Es lo que denuncian las comunidades cuando advierten que el agua pasa a ser tratada como un insumo más de la cadena de producción de IA. Siguiendo a Simondon, Hui agrega que el rechazo a la técnica nace muchas veces de que se la presenta como una caja negra. La salida no es entonces oponerse a los centros de datos por principio, sino abrir esa caja: publicar consumos, fuentes y condiciones, e integrar la decisión técnica a la discusión pública.

## 6. Una controversia abierta: estado de situación

A octubre de 2026 nada está definido.

- **Stargate Argentina** sigue siendo una carta de intención. Emiliano Kargieman, fundador de Sur Energy, reconoció: "La realidad concreta es que no avanzamos todavía de la carta de intención a un contrato firme". No hay obras ni presentación ante el RIGI, y el emplazamiento evaluado (departamento Confluencia, cerca del río Limay) no está confirmado (Sternik, 2026).
- **Atlas GigaHub** está en etapa de proyecto. La empresa remite los volúmenes y las fuentes de agua a estudios de impacto ambiental e hidrogeológicos todavía no presentados (EQSnotas, 2026).
- **El Súper RIGI** tiene media sanción, pero el 2 de septiembre el oficialismo no reunió las firmas para el dictamen en el Senado. Los cambios negociados exigen generación eléctrica propia a los proyectos electrointensivos y un piso de compras a proveedores nacionales, por lo que, si se aprueba, deberá volver a Diputados (Sieira, 2026). No encontramos registro de que se haya tratado en el recinto.
- **Las emergencias hídricas** siguen vigentes en Chubut; la de Neuquén vencía a mediados de octubre.
- **No hay regulación específica** en ninguna de las provincias involucradas.

En términos de Latour, la controversia no se cerró: los actores siguen disputando qué cuenta como hecho. Tiene además una particularidad, que es que la decisión sobre los incentivos se está tomando antes de que existan los datos y las reglas. Si el régimen se aprueba en esos términos, la estabilidad por treinta años puede cerrar la controversia por la vía legal sin que se haya cerrado por la vía del conocimiento.

## 7. Conclusión

El caso de los megacentros de datos en la Patagonia muestra que una decisión presentada como económica y técnica es, en realidad, una controversia sociotécnica. Es una problemática compleja en el sentido de Massarini y Schnek, y reúne las condiciones de la ciencia posnormal: incertidumbre alta, valores en disputa y mucho en juego.

El análisis del modelo de desarrollo indica que el régimen de incentivos reproduce el supuesto lineal de que la inversión trae por sí sola el desarrollo. Con el triángulo de Sábato y Botana se ve que la infraestructura científico-tecnológica local queda afuera, y con Mazzucato, que el Estado asume costos sin fijar una misión ni asegurarse un retorno.

El análisis del riesgo indica que lo que se disputa no es solo cuánta agua se usará, sino quién tiene autoridad para decirlo. Hoy el dato lo producen las empresas, no se publicó, y las comunidades afectadas no participan de la decisión. Incluso con el criterio más favorable a la inversión, el del costo-beneficio de Sunstein, faltan los números necesarios para decidir.

No concluimos que los centros de datos deban rechazarse. Como plantea Yuk Hui, la tecnología es ambivalente y la tarea es abrir la caja negra. De los autores trabajados se desprenden al menos cuatro condiciones para una decisión legítima: (1) información pública y verificable sobre el consumo y las fuentes de agua y energía antes de otorgar beneficios; (2) evaluación ambiental acumulativa por cuenca, que considere los otros usos y el cambio climático; (3) participación efectiva de las comunidades afectadas, incluida la consulta previa a los pueblos indígenas, en el sentido de una comunidad de pares extendida; y (4) contrapartidas que conecten los proyectos con el sistema científico-tecnológico local, para que el triángulo no quede abierto.

Queda una pregunta que el trabajo no puede responder: si un Estado que resigna capacidad fiscal y regulatoria durante treinta años podrá corregir el rumbo cuando el conocimiento sobre las cuencas cambie.

---

## 8. Bibliografía

### Bibliografía de la materia

- Beck, U. (1998). *La sociedad del riesgo. Hacia una nueva modernidad*. Paidós. (Obra original publicada en 1986).
- Funtowicz, S. y Ravetz, J. (2000). *La ciencia posnormal. Ciencia con la gente*. Icaria.
- Hui, Y. (2023). Anders, Simondon y el devenir de lo poshumano. *Pensar Jusbaires*, junio-julio, 40-55.
- Kreimer, P. y Zabala, J. P. (2006). ¿Qué conocimiento y para quién? Problemas sociales, producción y uso social de conocimientos científicos sobre la enfermedad de Chagas en Argentina. *Redes, 12*(23), 49-78.
- Latour, B. (2011). Esperando a Gaia. Componer el mundo común mediante las artes y la política. *Cuadernos de Otra Parte*.
- López Cerezo, J. A. (2017). *Ciencia, tecnología y sociedad*. [completar edición usada por la cátedra]
- Massarini, A. y Schnek, A. (coords.) (2015). *Ciencia entre todxs. Tecnociencia en contexto social. Una propuesta de enseñanza*. Paidós.
- Mazzucato, M. (2013). *El Estado emprendedor. Mitos del sector público frente al privado*. RBA.
- Pedace, K., Schleider, T. y Balmaceda, T. (2023). Inteligencia artificial y sesgos. El caso de la predicción del embarazo adolescente en Salta. *Revista CTS, 18*(53), 9-26.
- Sábato, J. y Botana, N. (1968). La ciencia y la tecnología en el desarrollo futuro de América Latina. *Revista de la Integración*, (3), 15-36.
- Skill, K. y Grinberg, E. (2013). Controversias sociotécnicas en torno a las fumigaciones con glifosato en Argentina. Una mirada desde la construcción social del riesgo. En G. Merlinsky (comp.), *Cartografías del conflicto ambiental en Argentina* (pp. 91-117). CICCUS.
- Sunstein, C. R. (2006). *Riesgo y razón. Seguridad, ley y medioambiente*. Katz.
- Vicente, M. E. y López Bedogni, G. (2022). Ciencia, Tecnología y demandas socio-productivas. Los Programas RIOSP e ImpaCT.AR. *Ciencia, Tecnología y Política, 5*(8).

### Fuentes sobre el caso

- Cooperativa (2024, 27 de febrero). *Tribunal Ambiental frenó proyecto de data center de Google en Cerrillos*. https://www.cooperativa.cl/noticias/site/artic/20240227/pags-amp/20240227154401.html
- DatacenterDynamics (2025, octubre). *OpenAI y Sur Energy preparan un proyecto de centro de datos en Argentina por valor de 25.000 millones de dólares*. https://www.datacenterdynamics.com/es/noticias/openai-sur-energy-preparan-proyecto-de-centro-de-datos-en-argentina-por-valor-de-25000-millones-de-d%C3%B3lares/
- El Observador (2023, 22 de noviembre). *Sin agua, con enfriamiento por aire y un edificio en lugar de dos: los detalles del proyecto de Google en Uruguay*. https://www.elobservador.com.uy/nota/sin-agua-con-enfriamiento-por-aire-y-un-edificio-en-lugar-de-dos-los-detalles-del-proyecto-de-google-en-uruguay-2023112116100
- EQSnotas (2026, 20 de septiembre). *Green Capital reveló cómo será el data center que proyecta en Chubut: agua, empleo, energía e inversión*. https://www.eqsnotas.com/politica/data-center-en-chubut--las-revelaciones-de-la-empresa-green-capital-sobre-agua--empleo-y-por-que-eligio-la-provincia_a6aafd11381fd63c19a75899e
- Indymedia Argentina (2026, 21 de septiembre). *Defensoras del agua en la Patagonia: la resistencia mapuche ante la expansión de data centers de IA en Argentina*. https://argentina.indymedia.org/2026/09/21/defensoras-del-agua-en-la-patagonia-la-resistencia-mapuche-ante-la-expansion-de-data-centers-de-ia-en-argentina/
- La Izquierda Diario (2026, 20 de agosto). *Agua para quién: crisis hídrica, RIGI y el mega data center de Trelew*. https://www.laizquierdadiario.com/Agua-para-quien-crisis-hidrica-RIGI-y-el-mega-data-center-de-Trelew
- Ley 24.071 (1992). Aprobación del Convenio 169 de la Organización Internacional del Trabajo sobre Pueblos Indígenas y Tribales en Países Independientes. Boletín Oficial de la República Argentina.
- Ley 25.675 (2002). Ley General del Ambiente. Boletín Oficial de la República Argentina.
- Li, P., Yang, J., Islam, M. A. y Ren, S. (2025). Making AI Less "Thirsty": Uncovering and Addressing the Secret Water Footprint of AI Models. *Communications of the ACM*. https://doi.org/10.1145/3724499
- Noticias Ambientales (2026). *Mujeres mapuche resisten la expansión de data centers de IA en la Patagonia argentina ante la crisis hídrica*. https://noticiasambientales.com/medio-ambiente/mujeres-mapuche-resisten-la-expansion-de-data-centers-de-ia-en-la-patagonia-argentina-ante-la-crisis-hidrica/
- Noticias NQN (2026, 10 de agosto). *Neuquén extiende la Emergencia Hídrica por otros 180 días: qué implica la medida*. https://www.noticiasnqn.com.ar/noticias/2026/08/10/347461-neuquen-extiende-la-emergencia-hidrica-por-otros-180-dias-que-implica-la-medida
- Sieira, P. (2026, 2 de septiembre). El Súper RIGI vuelve a trabarse en el Senado y abre un nuevo conflicto para Milei y Bullrich. *iProfesional*. https://www.iprofesional.com/politica/463625-super-rigi-vuelve-a-trabarse-en-el-senado-y-abre-conflicto-para-milei-y-bullrich
- Sternik, I. (2026, 10 de octubre). Stargate cumple un año: el megaanuncio de Javier Milei y Sam Altman todavía no camina. *Letra P*. https://www.letrap.com.ar/letrae/economia-digital/stargate-cumple-un-ano-el-megaanuncio-javier-milei-y-sam-altman-todavia-no-camina-n5427211
- Tarricone, M. (2026, 24 de junio). "Súper RIGI": las 3 claves del proyecto que aprobó la Cámara de Diputados. *Chequeado*. https://chequeado.com/el-explicador/super-rigi-las-3-claves-del-proyecto-que-trata-la-camara-de-diputados/
- Viano, L. y Calmels, J. (2026, 31 de marzo). Mega data centers en la Patagonia: promesas millonarias y alerta por la falta de regulación. *La Nación*. https://www.lanacion.com.ar/politica/mega-data-centers-en-la-patagonia-promesas-millonarias-y-alerta-por-la-falta-de-regulacion-nid31032026/
