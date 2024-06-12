import time # modulo time mide tiempo 
import logging # modulo de registro de  mensajes


# config de logger

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# la linea de logging configura el registro de mensajes de nivel INFO, critical y demas
# se define el formato en fecha, hora %(asctime)s, el nivel del menasje %(levelname)s INFO y warning y el mensaje %(message)s

def timeit(func): # decorador que mide le tiempo
    def wrapper (*args,**kwargs): # Esta línea define una función llamada wrapper que acepta cualquier número de argumentos posicionales *args y argumentos con nombre **kwargs
        start_time = time.time() # registro del tiempo de inicio
        result  = func(*args, **kwargs) # ejecuta la  info decorada
        end_time = time.time() # registra el tiempo de finalizacion
        elapsed_time = end_time - start_time # tiempo transcurrido
        logging.info(f"{func.__name__} executed in {elapsed_time:.4f} seconds") # registra el tiempo de ejecucion
        return result # retorna el resultado de la funcion result
    return wrapper # retorna el decorador



def logit (func): # decaorador que registra la eejcucion de la funcion
    def wrapper(*args,**kwargs): 
        logging.info(f"Runnig{func.__name__}") 
        result = func(*args,**kwargs) 
        logging.info(f"Completaed{func.__name__}") 
        return result
    return wrapper