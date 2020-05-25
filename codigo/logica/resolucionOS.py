import platform

#buscar la forma de ejecutar segun sistema operativo
#bucar la forma de importar modulo segun sistema operativo
def check_sis():
    sis = platform.system()

    if sis == 'Linux':
        print('estas en {}'.format((sis)))

    elif sis == 'Windows':
        print('estas en {}'.format((sis)))

    return sis

def resolucion_win():
    #consultar si es una buena practica importar modulos en funciones

    import _ctypes

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    return  ancho,alto

def resolucion_linux():
    #consultar si es una buena practica importar modulos en funciones
    import subprocess

    size = (None, None)
    args = ["xrandr", "-q", "-d", ":0"]
    proc = subprocess.Popen(args,stdout=subprocess.PIPE)
    for line in proc.stdout:
        if isinstance(line, bytes):
            line = line.decode("utf-8")
            if "Screen" in line:
                size = (int(line.split()[7]),  int(line.split()[9][:-1]))
    return size

def  set_resolucion():
    #sis = check_sis()
    global SISTEMA
    if SISTEMA == 'Linux':
        size=resolucion_linux()

    elif SISTEMA == 'Windows':
        sizeresolucion_win()


    #restablecemos la resolucion, para nuesta app
    size=tuple(map(lambda x: x - 100,size))
    return size

'''usaremos esta variable com oglobal para almacenar le sistema operativo 
para futuros usos '''
SISTEMA = check_sis()

