from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
  #implementar función
  
  t = 0
  
  numero_disponible = fila.qsize() + 1
  
  caja1 = {
    'libre':True,
    'cliente':None,
    'tiempo_de_comienzo_de_atencion':0, #tiempo en el que comienza a atender al cliente actual
    'frecuencia_de_llamado':10,
    'tiempo_de_apertura': 1
  }
  caja2 = {
    'libre':True,
    'cliente':None,
    'tiempo_de_comienzo_de_atencion':0,
    'frecuencia_de_llamado':4,
    'tiempo_de_apertura': 3
  }
  caja3 = {
    'libre':True,
    'cliente':None,
    'tiempo_de_comienzo_de_atencion':0,
    'frecuencia_de_llamado':4,
    'tiempo_de_apertura': 2
  }
  
  while t <= min:
    # llegada de clientes
    if t % 4 == 0:
      fila.put(numero_disponible)
      numero_disponible += 1
      
    # retorno de clientes a fila
      
    if caja3['libre'] == False and t - caja3['tiempo_de_comienzo_de_atencion'] == 3:
      fila.put(caja3['cliente'])
      caja3['libre'] = True
      caja3['cliente'] = None
      caja3['tiempo_de_comienzo_de_atencion'] = 0
    
    # rececpción de clientes
    if t >= caja1['tiempo_de_apertura'] and t % 10 == 1 and not fila.empty():
      caja1['cliente'] = fila.get()
      caja1['libre'] = False
      caja1['tiempo_de_comienzo_de_atencion'] = t
      
    if t >= caja2['tiempo_de_apertura'] and t % 4 == 3 and not fila.empty():
      caja2['cliente'] = fila.get()
      caja2['libre'] = False
      caja2['tiempo_de_comienzo_de_atencion'] = t
      
    if t >= caja3['tiempo_de_apertura'] and t % 4 == 2 and not fila.empty():
      caja3['cliente'] = fila.get()
      caja3['libre'] = False
      caja3['tiempo_de_comienzo_de_atencion'] = t
    
    t += 1
  
  return

if __name__ == '__main__':
  fila: Queue = Queue()
  fila_inicial: int = int(input())
  for numero in range(1, fila_inicial+1):
    fila.put(numero)
  min: int = int(input())
  avanzarFila(fila, min)
  res = []
  for i in range(0, fila.qsize()):
    res.append(fila.get())
  print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)

