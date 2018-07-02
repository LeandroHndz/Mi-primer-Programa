pokemon_elegido = input ("Elije un rival(Squirtle / Charmander / Bulbasur: ")

vida_pikachu = 100
vida_enemigo = 1

if pokemon_elegido == "Charmander":
    vida_enemigo = 90
    ataque_pokemon = 10

elif pokemon_elegido == "Squirtle":
    vida_enemigo = 100
    ataque_pokemon = 8

elif pokemon_elegido == "Bulbasur":
    vida_enemigo = 80
    ataque_pokemon = 9

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elgido = input ("que ataque elegiras? (Chispazo / Bola voltio: ")
    if ataque_elgido == "Chispazo":
        vida_enemigo -= 12
        print ("has usado Chispazo")
        print("el enemigo tiene {} de salud restante".format(vida_enemigo))

    elif ataque_elgido == "Bola voltio":
        vida_enemigo -= 10
        print ("has usado bola voltio")
        print("el enemigo tiene {} de salud restante".format(vida_enemigo))

    if pokemon_elegido == "Squirtle":
        vida_pikachu -= ataque_pokemon
        print (pokemon_elegido, " te ha atacado, te ha hecho {} de dano".format(ataque_pokemon))
        print("tienes {} de salud restante".format(vida_pikachu))

    elif pokemon_elegido == "Charmander":
        vida_pikachu -= ataque_pokemon
        print (pokemon_elegido, " te ha atacado, te ha hecho {} de dano".format(ataque_pokemon))
        print("tienes {} de salud restante".format(vida_pikachu))

    elif pokemon_elegido == "Bulbasur":
        vida_pikachu -= ataque_pokemon
        print(pokemon_elegido, " te ha atacado, te ha hecho {} de dano".format(ataque_pokemon))
        print("tienes {} de salud restante".format(vida_pikachu))

print("El combate a termindo")
if vida_enemigo <= 0:
    print ("has ganado")
if vida_pikachu <= 0:
    print ("has perdido")