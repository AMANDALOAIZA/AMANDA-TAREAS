star = print ("Había una vez en el bosque, un cerdito llamado koko. Era muy curioso, un dia se aventuro, mientras caminaba se encontró dos caminos  que lo llevaran a distintos sitios , ir al BOSQUE o entrar a una CUEVA, que decides tu?")
opcion_1 = input ("BOSQUE o CUEVA  ?Que camino deberia escoger? : ").lower()
if opcion_1 == "bosque":
   print ("Cerdito  entra  al bosque y encontro un lobo feroz")
   Opcion_1_1 = input("CORRER o ENCONDERSE :").lower()
   if Opcion_1_1 == "correr" : 
         print ("Corres lo mas rapido que puedes, pero el lobo esta alcanzote")
         print ("alcanzas ver un pantano , que haras? :  " )
         continuamos = input ("LANZARTE al pantano o RODEARLO : ").lower()
         if continuamos == "lanzarte": 
          print ("te llenas de tanto lodo que el lobo le da asco comerte asi regresas a tu casa , has Ganado")
         elif continuamos == "rodearlo" :
          print ("lo rodeas pero el lobo te alcanza en el bosque , JUEGO PERDIDO ")
         else: print ("Introduce una opcion correcta por favor")
          
   elif Opcion_1_1 == "esconderse" :
         print ("te diriges hacia unos arboles grandes")
         print ("pero hay una colmena de abejas encima de ti que no te quiere alli")
         print (" que haras ? ESPANTAR a las abejas o dejar que te PIQUEN? ")
         continuamos = input ("ESPANTAR o PICAR : " ).lower()
         if continuamos == "espantar" :
             print ("te agitas y el lobo te ve , fin del juego") 
         elif continuamos == "picar" :
             print ("  Estas adolorido pero el lobo no te ve, regresas a tu casa")
         else : print (" por favor elige una opcion correcta")
         
   else : print ("Por favor coloca una opcion valida")
   
elif opcion_1 == "cueva" : 
    print ("  A medida que entras a la cueva te das cuenta que cada vez esta mas oscura")
    print ("asi que consigues una Antorcha , decides SEGUIR adentrando a la cueva o REGRESAR ?")
    Opcion_1_2 = input (" SEGUIR o REGRESAR :").lower()
    if Opcion_1_2 == "seguir" :
        print ("sigues caminando , la antorcha se apaga pero aun logras ver poco")
        print ("Pero cada vez, ves menos asi debes decidir si Caminar mas adentro o , desviarte")
        continuamos = input ("CAMINAR o DESVIARTE : ").lower()
        if continuamos == "caminar" :
            print ("caes en un hueco, lastima  haz perdido")
        elif continuamos == "desviarte" :
            print ("consigues otra ruta  , te demoras mas pero logras salir de la cueva")
            print ("Igual has perdido el juego ")
        else : ("Por favor coloca una opcion valida")
    elif Opcion_1_2 == "regresar" :
         print("opss el lobo te estaba esperando , asi que debes correr o pelear")
         continuamos = input ("CORRER o PELEAR : ").lower()
         if continuamos == "correr" :
          print ("el lobo te alcanza , eres muy lento")
         elif continuamos == "pelear" :
          print ("NO eres contrincante para el lobo , pero logras herirlo y huir")
         else : print ("por favor escribe una opcion valida")
    else : ("  por favor escribe una opcion valida")
else : (" por favor escribe una opcion valida")