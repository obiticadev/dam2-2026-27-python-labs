"""Ejercicio 48: Cuentas bancarias con movimientos.

Nivel: Alto.

Enunciado: Un banco guarda sus cuentas en un diccionario cuyas claves son los números de
cuenta y cuyos valores son diccionarios con el "titular", el "saldo" y una lista de
"movimientos", donde cada movimiento es una tupla (tipo, importe). Escribe:

- abrir_cuenta(banco, numero, titular, saldo_inicial=0), que cree la cuenta (con un
  movimiento ("apertura", saldo_inicial)) y devuelva (True, mensaje) o (False, motivo)
  si el número ya existe;

- ingresar(banco, numero, importe) y retirar(banco, numero, importe), que validen que la
  cuenta existe, que el importe es positivo y, en la retirada, que hay saldo suficiente,
  anoten el movimiento ("ingreso" o "retirada") y devuelvan (ok, mensaje);
  transferir(banco, origen, destino, importe), que compruebe antes que ambas cuentas
  existen y que hay saldo suficiente para no dejar la operación a medias, y anote los
  movimientos "transferencia enviada" y "transferencia recibida";

- mostrar_extracto(banco, numero), que muestre los movimientos y el saldo;

- y saldo_total(banco), que sume los saldos de todas las cuentas.

Prueba el programa con tres cuentas y varias operaciones, entre ellas al menos tres
erróneas.

Organización de la plantilla:
- cuentas.py: desarrolla aquí las funciones del enunciado.
- principal.py: prepara aquí los datos, las pruebas y el programa principal.
"""
