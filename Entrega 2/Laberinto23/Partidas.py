from Juego import Juego

juego = Juego()
partida = int(input("Qué partida quieres jugar: 1 2 3 4\n"))

if (partida == 1):
    #En esta partida nos encontramos en la habitación 3, abrimos y cogemos la daga del baúl. Por último, usamos la daga para forzar la puerta
    laberinto = juego.laberinto4Habitaciones()
    juego.abrirPuertas()#Aunque ejecutemos este comando la puerta con cerradura no se abrirá
    laberinto.hijos[2].entrar()
    laberinto.hijos[2].hijos[0].abrir()
    daga = laberinto.hijos[2].hijos[0].coger(0)
    laberinto.hijos[2].norte.entrar()
    daga.Forzar(laberinto.hijos[0].sur)
    laberinto.hijos[0].sur.entrar()

if (partida == 2):
    #En esta partida nos encontamos en la habitación 2, ahora en vez de abrir la puerta con la daga usamos la bomba que hemos cogido del baul
    laberinto = juego.laberinto4Habitaciones()
    juego.activarBombas()
    hab2 = laberinto.hijos[1]
    hab2.entrar()
    baul= hab2.hijos[0]
    baul.abrir()
    bomba = baul.coger(0)#cogemos el primer elemento que contiene el baul. En este caso una bomba
    hab1 = laberinto.hijos[0]
    hab1.entrar()
    hab1.sur.entrar()
    bomba.Reventar(hab1.sur)
    hab1.sur.entrar()

if (partida == 3):
    #En esta partida nos encontamos en la habitación 3 al pasar por la puerta que la une con la habitación cuatro la bomba revienta
    laberinto = juego.laberinto4Habitaciones()
    juego.activarBombas()
    hab3 = laberinto.hijos[2]
    hab3.entrar()
    hab3.este.entrar()

if (partida == 4):
    #En esta partida nos encontamos en la habitación 3 pero la bomba no esta activa, podemos pasar a la habitación cuatro pero salimos ardiendo
    laberinto = juego.laberinto4Habitaciones()
    #juego.activarBombas()
    juego.abrirPuertas()
    hab3 = laberinto.hijos[2]
    hab3.entrar()
    hab3.este.entrar()
    hab4 = laberinto.hijos[3]
    hab4.entrar()





