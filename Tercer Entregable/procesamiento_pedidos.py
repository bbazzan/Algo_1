from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"

# funcion que a partir de una cola de pedidos, un diccionario de stock de productos y un diccionario de precios de productos, 
# procesa los pedidos y devuelve una lista de diccionarios con la forma:
# [{"id":<id_pedido>, "cliente":<nombre_cliente>, "productos":<productos_pedido>, "precio_total":<total_pedido>, "estado":<estado>}, ...]
# el estado serea 'completo' o 'incompleto' dependiendo de si todos los productos solicitados estaban en el stock o no

def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
  
  res = []
  
  while not pedidos.empty():
    pedido = pedidos.get()
    productos = pedido["productos"]
    precio_total = 0
    estado = ""
      
    for producto, cantidad in productos.items():
      if cantidad > stock_productos[producto]:
        estado = "incompleto"
        productos[producto] = stock_productos[producto]
        cantidad = stock_productos[producto]
        stock_productos[producto] = 0
        precio_total += precios_productos[producto] * cantidad
      else:
        stock_productos[producto] -= cantidad
        precio_total += precios_productos[producto] * cantidad
        
    pedido["productos"] = productos
    pedido["precio_total"] = precio_total
      
    if estado == "incompleto":
      pedido["estado"] = "incompleto"
    else:
      pedido["estado"] = "completo"
    
    res.append(pedido)
  
  return res

if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input  
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}