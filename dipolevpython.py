from visual import *

qe = 1.6e-19  # Q carga del electron

scene.title="Vectores de Campo Electrico" #Titulo de la imagen
scene.range = 2e-13 #escala a la que estara

cargas = [ sphere( pos = (-1e-13,0,0), Q = qe, color=color.red, radius = 6e-15 ),#carga positiva
	 sphere( pos = ( 1e-13,0,0), Q = -qe, color=color.blue, radius = 6e-15 ),] #carga negativa

def getcampo(posicion):
	campo = vector(0,0,0)
	for c in cargas:
		campo = campo + (posicion-c.pos) * 8.988e9 * c.Q / mag(posicion-c.pos)**3
	return campo

while True:
	posicion = scene.mouse.getclick().pos
	campo = getcampo(posicion)
	magnitud = mag(campo)
	rojo = maximum( 1-1e17/magnitud, 0 )
	azul = minimum( 1e17/magnitud, 1 )
	if rojo >= azul:
		azul = azul/rojo
		rojo = 1.0
	else:
		rojo = rojo/azul
		azul = 1.0
	arrow( pos=posicion, axis=campo * (4e-14/1e17),shaftwidth = 6e-15,color=(rojo,0,azul))
