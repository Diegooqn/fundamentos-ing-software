## Sets (set())
- Se usa para verificar duplicados/membresia sin recorrer toda la lista
- El loop doble compara todo en la lista, haciendo que con gran cantidad de elementos, sus operaciones sean demasiado grandes. En cambio con el "Set", va de manera "lineal", pues no se devuelve a comparar.

## Big O
O(n): si se duplica el tamaño de la lista, el trabajo se duplica. Crecimiento proporcional, una linea recta.
O(n²): si se duplica el tamaño de la lista, el trabajo se multiplica por 4 (porque es n × n). Si se multiplica por 10, el trabajo se multiplica por 100.