import random

roulette_numbers = {
    0: {'value': 0, 'color': 'green'},
    32: {'value': 32, 'color': 'red'},
    15: {'value': 15, 'color': 'black'},
    19: {'value': 19, 'color': 'red'},
    4: {'value': 4, 'color': 'black'},
    21: {'value': 21, 'color': 'red'},
    2: {'value': 2, 'color': 'black'},
    25: {'value': 25, 'color': 'red'},
    17: {'value': 17, 'color': 'black'},
    34: {'value': 34, 'color': 'red'},
    6: {'value': 6, 'color': 'black'},
    27: {'value': 27, 'color': 'red'},
    13: {'value': 13, 'color': 'black'},
    36: {'value': 36, 'color': 'red'},
    11: {'value': 11, 'color': 'black'},
    30: {'value': 30, 'color': 'red'},
    8: {'value': 8, 'color': 'black'},
    23: {'value': 23, 'color': 'red'},
    10: {'value': 10, 'color': 'black'},
    5: {'value': 5, 'color': 'red'},
    24: {'value': 24, 'color': 'black'},
    16: {'value': 16, 'color': 'red'},
    33: {'value': 33, 'color': 'black'},
    1: {'value': 1, 'color': 'red'},
    20: {'value': 20, 'color': 'black'},
    14: {'value': 14, 'color': 'red'},
    31: {'value': 31, 'color': 'black'},
    9: {'value': 9, 'color': 'red'},
    22: {'value': 22, 'color': 'black'},
    18: {'value': 18, 'color': 'red'},
    29: {'value': 29, 'color': 'black'},
    7: {'value': 7, 'color': 'red'},
    28: {'value': 28, 'color': 'black'},
    12: {'value': 12, 'color': 'red'},
    35: {'value': 35, 'color': 'black'},
    3: {'value': 3, 'color': 'red'},
    26: {'value': 26, 'color': 'black'}
}



def spinner():
    spin = random.choice(list(roulette_numbers.keys()))
    return roulette_numbers[spin]


def serie_apolo():
    round_color = 0
    red_count = 0
    black_count = 0
    color_over = 0 
    first_over_c = 0
    # color_apostado = ""
    # apuesta_color = 1
    
    
    
    # datos para la serie de tiros:
    
    max_lost = -1000 # perdida máxima   # entrando con mil en iro 1265 se pasa de 18 tiros y pierde.
    max_win = 1000 # ganancia máxima
    
    balance = 0
    perdida = 0
    
    over_18 = 0 # 1700 necesita
    over_20 = 0
    over_22 = 0
    over_24 = 0
    over_26 = 0
    over_28 = 0
    over_30 = 0
    
    spin = 0 # n° de tiro
    round = 0 # n° de vuelta sin ganar
    
    dozena_apostada = 1 # TODO qui se puede decir que evalue algunos tiros antes y despues elija, como durante el juego 
    apuesta_dozen= 1 # apuesta inicial
    
    
    ## resgistro de dozenas
    first = 0
    second = 0
    third = 0
    
    # TODO
    # registro de par/impar
       
    first_over_18 = 0
    
    # mientras sea el tiro 22 sin ganar y el balance no se pase de perdidas o ganancias
    while balance < max_win and balance > max_lost:
        print()
        result = spinner() # tira la bola
        
        print(result)
        print()
        
        spin += 1 
        round += 1
        round_color += 1
        
        
        if round > 18:
            over_18 += 1
            if over_18 == 1:
                first_over_18 = spin
            
        if round > 20:
            over_20 += 1
        if round > 22: # entrando con 1 en la ronda 23 se pierden $11389 en el spin n° 13479
            over_22 += 1
        if round > 24:
            over_24 += 1
            
        if round > 26:
            over_26 += 1
        if round > 28:
            over_28 += 1
        if round > 30:
            over_30 += 1
        
        
        
        
        
        # comprueba qué COLOR es el resultado
        
        if result['color'] == "red":
            red_count = 0
            black_count += 1
        elif result['color'] == "black":
            red_count += 1
            black_count = 0
        else:
            red_count +=1
            black_count +=1
            
        number = 9 
        if red_count == number or black_count == number:
            color_over += 1
            if color_over == 1:
                first_over_c = spin
            
            round_color = 0
            print(f'RED: {red_count} | BLACK: {black_count}')

            print(f"ROUND color repeated {color_over}  TIMES")
        
        print("########################")
        
        
        

        print(f'# n°: {spin}')
        print(f'APUESTA: ${apuesta_dozen}')

        print()
        print(f'COLOR OVER {number} times: {color_over} |RED: {red_count} | BLACK: {black_count}')

        print(f'first over color: {first_over_c}')
        print(f'DOZENA over 18 times: {over_18}')
        print(f'first over 18: {first_over_18}')


        print(f'dozen over 20  times: {over_20}')
        print()
        print(f'round: {round}')
        print(f'DOCENA APOSTADA: {dozena_apostada}')
        
        
        
        """if color_apostado == "red" or color_apostado == "black":
            color= result['color']
            print(f' El color {color_apostado} no ha salido hace mucho, apostaremos ${apuesta_color}')
            if result['color'] == color_apostado:
                {f'GANASTE! salio el color {color}'}
                balance += apuesta_color
            else:
                balance -= apuesta_color
                apuesta_color += apuesta_color
                print({f':( perdiste! salio el color {color}'})x
                               
        if red > 9:
            color_apostado = "red"
        elif black > 9:
            color_apostado = "black"
        """
             
        
        
        # comprueba qué docena es el resultado
        # 
        if result['value'] == 0:
            dozen = 0
        elif result['value'] < 13:
            dozen = 1
        elif result['value'] < 25:
            dozen = 2
        else: dozen = 3
        
        
        #  resgistro de dozenas reinicia la cuenta
        if dozen == 1:
            first = 0
            second += 1
            third += 1
        elif dozen == 2:
            second = 0
            first += 1
            third += 1
        elif dozen == 3:
            third = 0 
            first += 1
            second += 1
        else:
            first += 1
            second += 1    
            third += 1

        
        # si gana:
        if dozen == dozena_apostada:
            round = 0 # vuelta a empezar la cuenta de veces sin salir la docena
            
            cambio = (apuesta_dozen*2)
            balance += cambio
            print(f"ganaste! tu balance es de  ${balance}")


            apuesta_dozen= 1
            perdida = 0

            # encontrar docena menos concurrida
            dozena = max(first, second, third)
            if dozena == first:
                dozena_apostada = 1
            elif dozena == second:
                dozena_apostada = 2
            elif dozena == third:
                dozena_apostada = 3
                
            
                
                
                
                           
        # si pierde
        else:
            print ("perdiste :(")
            # cambios en el balance $$
            perdida += apuesta_dozen
            balance -= apuesta_dozen                     
            print(f'tu balance actual es de: ${balance}')
            
            # nueva apuesta
            if perdida % 2 == 0:
                apuesta_dozen= (perdida+2)/2
            else:
                apuesta_dozen= (perdida+1)/2   

            print()
            
            print("########################")
     
serie_apolo()        