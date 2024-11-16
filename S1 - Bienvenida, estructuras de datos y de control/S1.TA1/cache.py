def calificar_ejercicio1(lista_ventas):
    # Caso 1: no existe la lista.
    if lista_ventas is None:
        raise NotImplementedError("No declaraste una variable llamada lista_ventas.")

    # Caso 2: el código se ejecuta con errores
    if not isinstance(lista_ventas, list):
        raise RuntimeError("Tu variable lista_ventas no es de tipo lista.")

    # Caso 3: no es una lista.
    assert type(lista_ventas) == list, f"Tu variable lista_ventas no es de tipo {list.__name__}."

    # Caso 4: la lista contiene valores de tipo incorrecto
    for i in lista_ventas:
        assert type(i) == int, f"Tu lista contiene valores que no son de tipo {int.__name__}."

    # Caso 5: la lista no contiene todos los valores correctos
    try:
        assert lista_ventas.count(20) >= 2
        assert lista_ventas.count(21) >= 2
        assert lista_ventas.count(22) >= 1
        assert lista_ventas.count(27) >= 1
    except AssertionError as e:
        e.args += ("Tu lista no contiene toda la información de la tabla.",)
        raise e

    # Caso 6: la lista contiene valores que no existen en la columna
    assert len(set(lista_ventas)) == 4, "Tu lista contiene valores incorrectos."

    # Caso 7: la lista tiene el tamaño incorrecto
    assert len(lista_ventas) == 6, "Tu lista tiene un tamaño mayor al esperado."

    # Caso 8: la lista es correcta
    try:
        assert lista_ventas[0] == 20
        assert lista_ventas[1] == 21
        assert lista_ventas[2] == 22
        assert lista_ventas[3] == 20
        assert lista_ventas[4] == 21
        assert lista_ventas[5] == 27
    except AssertionError as e:
        e.args += ("Los valores de tu lista están desordenados.",)
        raise e

    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio2(lista_ventas, mes_a_actualizar, ventas_mes_a_actualizar):
    # Base variables
    base_lista_ventas = [20, 21, 22, 20, 21, 27]
    base_mes_a_actualizar = 4
    base_ventas_mes_a_actualizar = 18

    try:
        # Caso 1: no existe la lista.
        if lista_ventas is None:
            raise NotImplementedError("No existe una variable llamada lista_ventas.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(lista_ventas, list):
            raise RuntimeError("Tu variable lista_ventas no es de tipo lista.")
        
        # Caso 3: el código modifica los parametros del problema
        if mes_a_actualizar != base_mes_a_actualizar or ventas_mes_a_actualizar != base_ventas_mes_a_actualizar:
            raise AssertionError("Tu código no debe modificar los datos del problema.")
        
        # Caso 4: no es una lista.
        assert type(lista_ventas) == list, f"Tu variable lista_ventas no es de tipo {list.__name__}."
        
        # Caso 5: el código no utiliza las variables mes_a_actualizar y ventas_mes_a_actualizar
        if "mes_a_actualizar" not in locals() or "ventas_mes_a_actualizar" not in locals():
            raise RuntimeError("Tu código no utiliza las variables mes_a_actualizar y/o ventas_mes_a_actualizar.")
        
        # Caso 6: la lista contiene valores de tipo incorrecto
        for i in lista_ventas:
            assert type(i) == int, f"Tu lista contiene valores que no son de tipo {int.__name__}."
        
        # Caso 7: la lista tiene el tamaño incorrecto
        assert len(lista_ventas) == 6, "Tu lista no tiene el tamaño correcto."

        # Caso 8: la lista es correcta
        try:
            assert lista_ventas[0] == 20
            assert lista_ventas[1] == 21
            assert lista_ventas[2] == 22
            assert lista_ventas[mes_a_actualizar - 1] == ventas_mes_a_actualizar
            assert lista_ventas[4] == 21
            assert lista_ventas[5] == 27
        except AssertionError as e:
            e.args += ("Tu respuesta es incorrecta. Es posible que no hayas modificado la posición correcta.",)
            raise e
    
    finally:
        # Restaurar variables base originales
        lista_ventas[:] = base_lista_ventas
        mes_a_actualizar = base_mes_a_actualizar
        ventas_mes_a_actualizar = base_ventas_mes_a_actualizar
    
    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio3(mejores_ventas, lista_ventas, n):
    # Base variables
    base_lista_ventas = [20, 21, 22, 20, 21, 27]
    base_n = 3

    try:
        # Caso 1: no existe la lista.
        if mejores_ventas is None:
            raise NotImplementedError("No declaraste una variable llamada mejores_ventas.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(mejores_ventas, list):
            raise RuntimeError("Tu variable mejores_ventas no es de tipo lista.")

        # Caso 3: el código modifica los parametros del problema
        if n != base_n:
            raise AssertionError("Tu código no debe modificar los datos del problema.")

        # Caso 4: no es una lista.
        assert type(mejores_ventas) == list, f"Tu variable mejores_ventas no es de tipo {list.__name__}."

        # Caso 5: el código no utiliza las variables lista_ventas y n
        if "lista_ventas" not in locals() or "n" not in locals():
            raise RuntimeError("Tu código no utiliza las variables lista_ventas y/o n.")

        # Caso 6: la lista contiene valores de tipo incorrecto
        for i in mejores_ventas:
            assert type(i) == int, f"Tu lista contiene valores que no son de tipo {int.__name__}."

        # Caso 7: la lista tiene el tamaño incorrecto
        assert len(mejores_ventas) == n, "Tu lista no tiene el tamaño correcto."

        # Caso 8: la lista no contiene los valores correctos
        try:
            assert mejores_ventas.count(22) >= 1
            assert mejores_ventas.count(21) >= 1
            assert mejores_ventas.count(27) >= 1
        except AssertionError as e:
            e.args += ("Tu lista no contiene los valores correctos.",)
            raise e

        # Caso 9: la lista es correcta
        try:
            assert mejores_ventas[0] >= mejores_ventas[1]
            assert mejores_ventas[1] >= mejores_ventas[2]
        except AssertionError as e:
            e.args += ("Tu lista no está en orden descendente.",)
            raise e

        # Caso 10: la lista no está ordenada
        try:
            assert mejores_ventas[0] == 27
            assert mejores_ventas[1] == 22
            assert mejores_ventas[2] == 21
        except AssertionError as e:
            e.args += ("Tu respuesta es incorrecta.",)
            raise e

    finally:
        # Restaurar variables base originales
        lista_ventas[:] = base_lista_ventas
        n = base_n
    
    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

import math

def calificar_ejercicio4(primera_mitad, segunda_mitad, nombres):
    # Base variables
    base_nombres = nombres = ["Sara", "Juan", "Alberto", "Ana", "Enrique", "Lola"]

    try:
        # Caso 1: no se declaró la lista
        if primera_mitad is None:
            raise NotImplementedError("No declaraste una variable llamada primera_mitad.")
        
        if segunda_mitad is None:
            raise NotImplementedError("No declaraste una variable llamada segunda_mitad.")

        # Caso 2: el código se ejecuta con errores
        if not isinstance(primera_mitad, list):
            raise RuntimeError("Tu variable primera_mitad no es de tipo lista.")
        
        if not isinstance(segunda_mitad, list):
            raise RuntimeError("Tu variable segunda_mitad no es de tipo lista.")

        # Caso 3: el código modifica los parámetros del problema
        if nombres != base_nombres:
            raise AssertionError("Tu código no debe modificar los datos del problema.")

        # Caso 4: no es una lista
        assert type(primera_mitad) == list, f"Tu variable primera_mitad no es de tipo {list.__name__}."
        assert type(segunda_mitad) == list, f"Tu variable segunda_mitad no es de tipo {list.__name__}."

        # Caso 5: el código no utiliza la lista nombres
        if "nombres" not in locals():
            raise RuntimeError("Tu código no utiliza la lista nombres.")

        # Caso 6: la lista contiene valores de tipo incorrecto
        for i in primera_mitad:
            assert type(i) == str, f"Tu lista primera_mitad contiene valores que no son de tipo {str.__name__}."
        
        for i in segunda_mitad:
            assert type(i) == str, f"Tu lista segunda_mitad contiene valores que no son de tipo {str.__name__}."

        # Caso 7: las listas tienen el tamaño incorrecto
        mitad = math.ceil(len(nombres) / 2)
        assert len(primera_mitad) == mitad, "Tu lista primera_mitad no tiene el tamaño correcto."
        assert len(segunda_mitad) == len(nombres) - mitad, "Tu lista segunda_mitad no tiene el tamaño correcto."

        # Caso 8: la lista no contiene los valores correctos
        try:
            assert "Alberto" in primera_mitad
            assert "Ana" in primera_mitad
            assert "Enrique" in primera_mitad
        except AssertionError as e:
            e.args += ("Tu lista primera_mitad no contiene los valores correctos.",)
            raise e
        
        try:
            assert "Juan" in segunda_mitad
            assert "Lola" in segunda_mitad
            assert "Sara" in segunda_mitad
        except AssertionError as e:
            e.args += ("Tu lista segunda_mitad no contiene los valores correctos.",)
            raise e

        # Caso 9: las listas son correctas
        try:
            assert primera_mitad == sorted(primera_mitad)
        except AssertionError as e:
            e.args += ("Tu lista primera_mitad no está ordenada alfabéticamente.",)
            raise e
        
        try:
            assert segunda_mitad == sorted(segunda_mitad)
        except AssertionError as e:
            e.args += ("Tu lista segunda_mitad no está ordenada alfabéticamente.",)
            raise e

    finally:
        # Restaurar variables base originales
        nombres[:] = base_nombres
    
    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio5(lista_abc, lista_abecedario):
    try:
        # Caso 1: no existe la lista.
        if lista_abc is None:
            raise NotImplementedError("No declaraste una variable llamada lista_abc.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(lista_abc, list):
            raise RuntimeError("Tu variable lista_abc no es de tipo lista.")
        
        # Caso 3: no es una lista.
        assert type(lista_abc) == list, f"Tu variable lista_abc no es de tipo {list.__name__}."
        
        # Caso 4: el código no utiliza la lista lista_abecedario
        if "lista_abecedario" not in locals():
            raise RuntimeError("Tu código no utiliza la lista lista_abecedario.")
        
        # Caso 5: la lista contiene valores de tipo incorrecto
        for i in lista_abc:
            assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."
        
        # Caso 6: la lista no contiene los valores esperados
        try:
            assert lista_abc.count('a') >= 1
            assert lista_abc.count('b') >= 1
            assert lista_abc.count('c') >= 1
        except AssertionError as e:
            e.args += ("Tu lista no contiene los valores correctos.",)
            raise e
        
        # Caso 7: la lista tiene el tamaño incorrecto
        assert len(lista_abc) == 3, "Tu lista no tiene el tamaño correcto."
        
        # Caso 8: la lista es correcta
        try:
            assert lista_abc[0] == 'a'
            assert lista_abc[1] == 'b'
            assert lista_abc[2] == 'c'
        except AssertionError as e:
            e.args += ("Los valores de tu lista están desordenados.",)
            raise e
    
    finally:
        # Restaurar variables base originales
        lista_abecedario = ["a", "b", "c", ["d", "e", ["f", "g"]]]

    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio6(lista_de, lista_abecedario):
    try:
        # Caso 1: no existe la lista.
        if lista_de is None:
            raise NotImplementedError("No declaraste una variable llamada lista_de.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(lista_de, list):
            raise RuntimeError("Tu variable lista_de no es de tipo lista.")
        
        # Caso 3: no es una lista.
        assert type(lista_de) == list, f"Tu variable lista_de no es de tipo {list.__name__}."
        
        # Caso 4: el código no utiliza la lista lista_abecedario
        if "lista_abecedario" not in locals():
            raise RuntimeError("Tu código no utiliza la lista lista_abecedario.")
        
        # Caso 5: la lista contiene valores de tipo incorrecto
        for i in lista_de:
            assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."
        
        # Caso 6: la lista no contiene los valores esperados
        try:
            assert lista_de.count('d') >= 1
            assert lista_de.count('e') >= 1
        except AssertionError as e:
            e.args += ("Tu lista no contiene los valores correctos.",)
            raise e
        
        # Caso 7: la lista tiene el tamaño incorrecto
        assert len(lista_de) == 2, "Tu lista no tiene el tamaño correcto."
        
        # Caso 8: la lista es correcta
        try:
            assert lista_de[0] == 'd'
            assert lista_de[1] == 'e'
        except AssertionError as e:
            e.args += ("Los valores de tu lista están desordenados.",)
            raise e
    
    finally:
        # Restaurar variables base originales
        lista_abecedario = ["a", "b", "c", ["d", "e", ["f", "g"]]]

    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio7(lista_fgh, lista_abecedario):
    try:
        # Caso 1: no existe la lista.
        if lista_fgh is None:
            raise NotImplementedError("No declaraste una variable llamada lista_fgh.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(lista_fgh, list):
            raise RuntimeError("Tu variable lista_fgh no es de tipo lista.")
        
        # Caso 3: no es una lista.
        assert type(lista_fgh) == list, f"Tu variable lista_fgh no es de tipo {list.__name__}."
        
        # Caso 4: el código no utiliza la lista lista_abecedario
        if "lista_abecedario" not in locals():
            raise RuntimeError("Tu código no utiliza la lista lista_abecedario.")
        
        # Caso 5: la lista contiene valores de tipo incorrecto
        for i in lista_fgh:
            assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."
        
        # Caso 6: la lista no contiene los valores esperados
        try:
            assert lista_fgh.count('f') >= 1
            assert lista_fgh.count('g') >= 1
            assert lista_fgh.count('h') >= 1
        except AssertionError as e:
            e.args += ("Tu lista no contiene los valores correctos.",)
            raise e
        
        # Caso 7: la lista tiene el tamaño incorrecto
        assert len(lista_fgh) == 3, "Tu lista no tiene el tamaño correcto."
        
        # Caso 8: la lista es correcta
        try:
            assert lista_fgh[0] == 'f'
            assert lista_fgh[1] == 'g'
            assert lista_fgh[2] == 'h'
        except AssertionError as e:
            e.args += ("Los valores de tu lista están desordenados.",)
            raise e
    
    finally:
        # Restaurar variables base originales
        lista_abecedario = ["a", "b", "c", ["d", "e", ["f", "g"]]]

    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio8(lista_a_j, lista_abc, lista_de, lista_fgh):
    try:
        # Caso 1: no existe la lista.
        if lista_a_j is None:
            raise NotImplementedError("No declaraste una variable llamada lista_a_j.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(lista_a_j, list):
            raise RuntimeError("Tu variable lista_a_j no es de tipo lista.")
        
        # Caso 3: no es una lista.
        assert type(lista_a_j) == list, f"Tu variable lista_a_j no es de tipo {list.__name__}."
        
        # Caso 4: el código no utiliza las listas lista_abc, lista_de y lista_fgh
        if "lista_abc" not in locals() or "lista_de" not in locals() or "lista_fgh" not in locals():
            raise RuntimeError("Tu código no utiliza las listas lista_abc, lista_de y/o lista_fgh.")
        
        # Caso 5: la lista contiene valores de tipo incorrecto
        for i in lista_a_j:
            assert type(i) == str, f"Tu lista contiene valores que no son de tipo {str.__name__}."
        
        # Caso 6: la lista no contiene los valores esperados
        try:
            assert lista_a_j.count('a') >= 1
            assert lista_a_j.count('b') >= 1
            assert lista_a_j.count('c') >= 1
            assert lista_a_j.count('d') >= 1
            assert lista_a_j.count('e') >= 1
            assert lista_a_j.count('f') >= 1
            assert lista_a_j.count('g') >= 1
            assert lista_a_j.count('h') >= 1
            assert lista_a_j.count('i') >= 1
            assert lista_a_j.count('j') >= 1
        except AssertionError as e:
            e.args += ("Tu lista no contiene los valores correctos.",)
            raise e
        
        # Caso 7: la lista tiene el tamaño incorrecto
        assert len(lista_a_j) == 10, "Tu lista no tiene el tamaño correcto."
        
        # Caso 8: la lista es correcta
        try:
            assert lista_a_j[0] == 'a'
            assert lista_a_j[1] == 'b'
            assert lista_a_j[2] == 'c'
            assert lista_a_j[3] == 'd'
            assert lista_a_j[4] == 'e'
            assert lista_a_j[5] == 'f'
            assert lista_a_j[6] == 'g'
            assert lista_a_j[7] == 'h'
            assert lista_a_j[8] == 'i'
            assert lista_a_j[9] == 'j'
        except AssertionError as e:
            e.args += ("Los valores de tu lista están desordenados.",)
            raise e
    
    finally:
        # Restaurar variables base originales
        lista_abecedario = ["a", "b", "c", ["d", "e", ["f", "g"]]]
        lista_abc = lista_abecedario[:3]
        lista_de = lista_abecedario[3][:2]
        lista_fgh = lista_abecedario[3][2] + ["h"]

    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio9(indice, tupla_primos, a_buscar):
    # Base variables
    base_a_buscar = 73

    try:
        # Caso 1: no existe la variable.
        if indice is None:
            raise NotImplementedError("No declaraste una variable llamada indice.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(indice, int):
            raise RuntimeError("Tu variable indice no es de tipo int.")
        
        # Caso 3: el código modifica los parámetros del problema
        if a_buscar != base_a_buscar:
            raise AssertionError("Tu código no debe modificar los datos del problema.")
        
        # Caso 4: no es de tipo int.
        assert type(indice) == int, f"Tu variable indice no es de tipo {int.__name__}."
        
        # Caso 5: el código no utiliza las variables tupla_primos y a_buscar
        if "tupla_primos" not in locals() or "a_buscar" not in locals():
            raise RuntimeError("Tu código no utiliza las variables tupla_primos y/o a_buscar.")
        
        # Caso 6: la respuesta es correcta
        assert indice == 20, "Tu respuesta es incorrecta."
    
    finally:
        # Restaurar variables base originales
        a_buscar = 73
    
    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio10(tupla_secuencia, tupla_primos, lim_inferior, lim_superior):
    # Base variables
    base_lim_inferior = 3
    base_lim_superior = 53

    try:
        # Caso 1: no existe la tupla.
        if tupla_secuencia is None:
            raise NotImplementedError("No declaraste una variable llamada tupla_secuencia.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(tupla_secuencia, tuple):
            raise RuntimeError("Tu variable tupla_secuencia no es de tipo tupla.")
        
        # Caso 3: el código modifica los parámetros del problema
        if lim_inferior != base_lim_inferior or lim_superior != base_lim_superior:
            raise AssertionError("Tu código no debe modificar los datos del problema.")
        
        # Caso 4: no es una tupla.
        assert type(tupla_secuencia) == tuple, f"Tu variable tupla_secuencia no es de tipo {tuple.__name__}."
        
        # Caso 5: el código no utiliza las variables tupla_primos, lim_inferior y lim_superior
        if "tupla_primos" not in locals() or "lim_inferior" not in locals() or "lim_superior" not in locals():
            raise RuntimeError("Tu código no utiliza las variables tupla_primos, lim_inferior y/o lim_superior.")
        
        # Caso 6: la tupla contiene valores de tipo incorrecto
        for i in tupla_secuencia:
            assert type(i) == int, f"Tu tupla contiene valores que no son de tipo {int.__name__}."
        
        # Caso 7: la tupla no contiene los límites correctos
        assert tupla_secuencia[0] == lim_inferior, "Tu tupla no inicia en el límite inferior."
        assert tupla_secuencia[len(tupla_secuencia)-1] == lim_superior, "Tu tupla no termina en el límite superior."
        
        # Caso 8: la tupla tiene el tamaño incorrecto
        assert len(tupla_secuencia) == 8, "Tu tupla no tiene el tamaño correcto."
        
        # Caso 9: la tupla es correcta
        try:
            assert tupla_secuencia[0] == 3
            assert tupla_secuencia[1] == 7
            assert tupla_secuencia[2] == 13
            assert tupla_secuencia[3] == 19
            assert tupla_secuencia[4] == 29
            assert tupla_secuencia[5] == 37
            assert tupla_secuencia[6] == 43
            assert tupla_secuencia[7] == 53
        except AssertionError as e:
            e.args += ("Tu respuesta es incorrecta.",)
            raise e
    
    finally:
        # Restaurar variables base originales
        lim_inferior = 3
        lim_superior = 53
    
    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio11(tupla_pedidos, pedidos_semana_1, pedidos_semana_2, pedidos_semana_3):
    # Base variables
    base_pedidos_semana_1 = (3, 2)
    base_pedidos_semana_2 = (2, 4)
    base_pedidos_semana_3 = (1, 1)

    try:
        # Caso 1: no existe la tupla.
        if tupla_pedidos is None:
            raise NotImplementedError("No declaraste una variable llamada tupla_pedidos.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(tupla_pedidos, tuple):
            raise RuntimeError("Tu variable tupla_pedidos no es de tipo tupla.")
        
        # Caso 3: el código modifica los parámetros del problema
        if pedidos_semana_1 != base_pedidos_semana_1 or pedidos_semana_2 != base_pedidos_semana_2 or pedidos_semana_3 != base_pedidos_semana_3:
            raise AssertionError("Tu código no debe modificar los datos del problema.")
        
        # Caso 4: no es una tupla.
        assert type(tupla_pedidos) == tuple, f"Tu variable tupla_pedidos no es de tipo {tuple.__name__}."
        
        # Caso 5: el código no utiliza las variables pedidos_semana_1, pedidos_semana_2 y pedidos_semana_3
        if "pedidos_semana_1" not in locals() or "pedidos_semana_2" not in locals() or "pedidos_semana_3" not in locals():
            raise RuntimeError("Tu código no utiliza las variables pedidos_semana_1, pedidos_semana_2 y/o pedidos_semana_3.")
        
        # Caso 6: la tupla contiene valores de tipo incorrecto
        for i in tupla_pedidos:
            assert type(i) == tuple, f"Tu tupla contiene valores que no son de tipo {tuple.__name__}. Es posible que no tengas las tuplas anidadas."
        
        # Caso 7: la lista no contiene los valores esperados
        try:
            assert tupla_pedidos.count((3, 2)) >= 1
            assert tupla_pedidos.count((2, 4)) >= 1
            assert tupla_pedidos.count((1, 1)) >= 1
        except AssertionError as e:
            e.args += ("Tu lista no contiene los valores correctos.",)
            raise e
        
        # Caso 8: la tupla tiene el tamaño incorrecto
        assert len(tupla_pedidos) == 3, "Tu tupla no tiene el tamaño correcto."
        
        # Caso 9: la tupla es correcta
        try:
            assert tupla_pedidos[0] == (3, 2)
            assert tupla_pedidos[1] == (2, 4)
            assert tupla_pedidos[2] == (1, 1)
        except AssertionError as e:
            e.args += ("Los valores de tu tupla están desordenados.",)
            raise e
    
    finally:
        # Restaurar variables base originales
        pedidos_semana_1 = (3, 2)
        pedidos_semana_2 = (2, 4)
        pedidos_semana_3 = (1, 1)
    
    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio12(total_pedidos_semana_s, tupla_pedidos, s):
    # Base variables
    base_s = 2

    try:
        # Caso 1: no existe la variable.
        if total_pedidos_semana_s is None:
            raise NotImplementedError("No declaraste una variable llamada total_pedidos_semana_s.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(total_pedidos_semana_s, int):
            raise RuntimeError("Tu variable total_pedidos_semana_s no es de tipo int.")
        
        # Caso 3: el código modifica los parámetros del problema
        if s != base_s:
            raise AssertionError("Tu código no debe modificar los datos del problema.")
        
        # Caso 4: no es un int.
        assert type(total_pedidos_semana_s) == int, f"Tu variable total_pedidos_semana_s no es de tipo {int.__name__}."
        
        # Caso 5: el código no utiliza la variable tupla_pedidos
        if "tupla_pedidos" not in locals():
            raise RuntimeError("Tu código no utiliza la variable tupla_pedidos.")
        
        # Caso 6: la respuesta es correcta
        assert total_pedidos_semana_s == 6, "Tu respuesta es incorrecta."
    
    finally:
        # Restaurar variables base originales
        s = 2
    
    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio13(dicc_meses):
    try:
        # Caso 1: no existe el diccionario.
        if dicc_meses is None:
            raise NotImplementedError("No existe una variable llamada dicc_meses.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(dicc_meses, dict):
            raise RuntimeError("Tu variable dicc_meses no es de tipo diccionario.")
        
        # Caso 3: no es un diccionario.
        assert type(dicc_meses) == dict, f"Tu variable dicc_meses no es de tipo {dict.__name__}."
        
        # Caso 4: el código no utiliza el diccionario dicc_meses
        if "dicc_meses" not in locals():
            raise RuntimeError("Tu código no utiliza el diccionario dicc_meses.")
        
        # Caso 5: el diccionario contiene valores de tipo incorrecto
        for i in dicc_meses.keys():
            assert type(i) == str, f"Tu diccionario contiene llaves que no son de tipo {str.__name__}."
        
        for j in dicc_meses.values():
            assert type(j) == int, f"Tu diccionario contiene valores que no son de tipo {int.__name__}."
        
        # Caso 6: el diccionario tiene el tamaño incorrecto
        assert len(dicc_meses) == 12, "Tu diccionario no tiene el tamaño correcto."
        
        # Caso 7: el diccionario no contiene los valores/llaves correctos/as
        assert set(dicc_meses.keys()) == {'Diciembre', 'Noviembre', 'Octubre', 'Septiembre', 'Agosto', 'Julio', 'Junio', 'Mayo', 'Abril', 'Marzo', 'Febrero', 'Enero'}, "Las llaves de tu diccionario no son correctas."
        assert set(dicc_meses.values()) == {31, 31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 28}, "Los valores de tu diccionario no son correctos."
        
        # Caso 8: el diccionario es correcto
        try:
            assert dicc_meses['Enero'] == 31
            assert dicc_meses['Febrero'] == 28
            assert dicc_meses['Marzo'] == 31
            assert dicc_meses['Abril'] == 30
            assert dicc_meses['Mayo'] == 31
            assert dicc_meses['Junio'] == 30
            assert dicc_meses['Julio'] == 31
            assert dicc_meses['Agosto'] == 31
            assert dicc_meses['Septiembre'] == 30
            assert dicc_meses['Octubre'] == 31
            assert dicc_meses['Noviembre'] == 30
            assert dicc_meses['Diciembre'] == 31
        except AssertionError as e:
            e.args += ("Tu respuesta es incorrecta.",)
            raise e
    
    # Restaurar variables base originales
    finally:
        dicc_meses = {"Enero": 31, "Febrero": 28, "Marzo": 31, "Abril": 30, "Mayo": 31, "Julio": 31, "Agosto": 31, "Septiembre": 30, "Noviembre": 30}
    
    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio14(matriz):
    try:
        # Caso 1: no existe el diccionario.
        if matriz is None:
            raise NotImplementedError("No declaraste una variable llamada matriz.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(matriz, dict):
            raise RuntimeError("Tu variable matriz no es de tipo diccionario.")
        
        # Caso 3: no es un diccionario.
        assert type(matriz) == dict, f"Tu variable matriz no es de tipo {dict.__name__}."
        
        # Caso 4: el diccionario contiene valores de tipo incorrecto
        for i in matriz.keys():
            assert type(i) == tuple, f"Tu diccionario contiene llaves que no son de tipo {tuple.__name__}."
        
        for j in matriz.values():
            assert type(j) == int, f"Tu diccionario contiene valores que no son de tipo {int.__name__}."
            assert j == 1, "Tu diccionario representa casos en los que la familia no comprará la consola."
        
        # Caso 5: el diccionario tiene el tamaño incorrecto
        assert len(matriz) == 9, "Tu diccionario no tiene el tamaño correcto."
        
        # Caso 6: el diccionario es correcto
        assert set(matriz.keys()) == {(1, 2), (1, 4), (1, 5), (2, 5), (3, 1), (3, 4), (4, 1), (4, 3), (4, 5)}, "Las llaves de tu diccionario no son correctas."
    
    finally:
        # Restaurar variables base originales
        pass
    
    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")

def calificar_ejercicio15(prediccion_familia, matriz, h, t):
    # Base variables
    base_h = 5
    base_t = 2
    try:
        # Caso 1: no existe la variable.
        if prediccion_familia is None:
            raise NotImplementedError("No declaraste una variable llamada prediccion_familia.")
        
        # Caso 2: el código se ejecuta con errores
        if not isinstance(prediccion_familia, int):
            raise RuntimeError("Tu variable prediccion_familia no es de tipo int.")
        
        # Caso 3: el código modifica los parámetros del problema
        if h != base_h or t != base_t:
            raise AssertionError("Tu código no debe modificar los datos del problema.")
        
        # Caso 4: no es un int.
        assert type(prediccion_familia) == int, f"Tu variable prediccion_familia no es de tipo {int.__name__}."
        
        # Caso 5: el código no utiliza la variable matriz
        if "matriz" not in locals():
            raise RuntimeError("Tu código no utiliza la variable matriz.")
        
        # Caso 6: la respuesta es correcta
        assert prediccion_familia == 1, "Tu respuesta es incorrecta. Recuerda que debes representar con un 0 el caso en el que la familia no comprará la consola."  
    
    finally:
        # Restaurar variables base originales
        h = 5
        t = 2
    
    # Mensaje de felicitaciones
    print("Felicidades, realizaste este ejercicio correctamente.")