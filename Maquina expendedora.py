#MAQUINA DE CAFE
print("===== NESCAFÉ =====")
print("""[1] Capuchino:            &/2.50
[2] Café negro:           &/2.00
[3] Café con leche:       &/1.50
[4] café caramelizado:    &/2.00
[5] chocolate caliente:   &/2.00""")

saldo = float(input("INGRESE MONEDA: "))
print("SU SALDO ES DE: ",saldo)
print("\n")
print("""====SUGAR====
      [1] Alto
      [2] Medio
      [3] bajo""")
sugar = int(input("INGRESE NIVEL DE AZUCAR: "))
print("\n")
case = int(input("Ingrese N° de pedido: "))

match case:
    case 1:
        
        if(saldo <= 2.49):
                    print("\n")
                    print("NO CUENTA CON EL SALDO SUFICIENTE")
                    print("\n")
        if(saldo >= 2.50 and case == 1):
                    print("Se esta despachando Capuchino, espere unos segundos...")
                    print("SU VUELTO ES: &/", saldo-2.50)
                    if (sugar == 1):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAPUCHINO ALTO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 2):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAPUCHINO MEDIO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 3):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAPUCHINO BAJO EN AZUCAR ☆☆☆☆☆☆")        
        else:
            masvalor1 = float(input("INGRESE MAS SALDO: "))
            print("SU SALDO ES:: ",masvalor1+saldo)
            if(masvalor1 >= 2.50 and case == 1):
                    print("Se esta despachando Capuchino, espere unos segundos...")
                    print("SU VUELTO ES: &/", masvalor1+saldo-2.00)
                    if (sugar == 1):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAPUCHINO ALTO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 2):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAPUCHINO MEDIO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 3):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAPUCHINO BAJO EN AZUCAR ☆☆☆☆☆☆") 

    case 2:

        if(saldo <= 1.99):
                    print("\n")
                    print("NO CUENTA CON EL SALDO SUFICIENTE")
                    print("\n")
        if(saldo >= 2.00 and case == 2):
                    print("Se esta despachando Café negro, espere unos segundos...")
                    print("SU VUELTO ES: &/", saldo-2.00)
                    if (sugar == 1):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE NEGRO ALTO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 2):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE NEGRO MEDIO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 3):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE NEGRO BAJO EN AZUCAR ☆☆☆☆☆☆") 
        else:
            masvalor2 = float(input("INGRESE MAS SALDO: "))
            print("SU SALDO ES: ",masvalor2+saldo)
            if(masvalor2 >= 2.00 and case == 2):
                    print("Se esta despachando Café negro, espere unos segundos...")
                    print("SU VUELTO ES: &/", masvalor2+saldo-2.00)
                    if (sugar == 1):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE NEGRO ALTO EN AZUCAR ☆☆☆☆☆☆ ")
                    if (sugar == 2):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE NEGRO MEDIO EN AZUCAR ☆☆☆☆☆☆ ")
                    if (sugar == 3):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE NEGRO BAJO EN AZUCAR ☆☆☆☆☆☆ ") 

    case 3:

        if(saldo <= 1.49):
                    print("\n")
                    print("NO CUENTA CON EL SALDO SUFICIENTE")
                    print("\n")
        if(saldo >= 1.50 and case == 3):
                    print("Se esta despachando Café con leche, espere unos segundos...")
                    print("SU VUELTO ES: &/", saldo-1.50)
                    if (sugar == 1):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE CON LECHE ALTO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 2):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE CON LECHE MEDIO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 3):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE CON LECHE BAJO EN AZUCAR ☆☆☆☆☆☆")  

        else:
            masvalor3 = float(input("INGRESE MAS SALDO: "))
            print("SU SALDO ES: ",masvalor3+saldo)
            if(masvalor3 >= 1.50 and case == 3):
                    print("Se esta despachando Café con leche, espere unos segundos...")
                    print("SU VUELTO ES: &/", masvalor3+saldo-2.00)
                    if (sugar == 1):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE CON LECHE ALTO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 2):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE CON LECHE MEDIO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 3):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE CON LECHE BAJO EN AZUCAR ☆☆☆☆☆☆") 


    case 4:

        if(saldo <= 1.99):
                    print("\n")
                    print("NO CUENTA CON EL SALDO SUFICIENTE")
                    print("\n")
        if(saldo >= 2.00 and case == 4):
                    print("Se esta despachando café caramelizado, espere unos segundos...")
                    print("SU VUELTO ES: &/", saldo-2.00)
                    if (sugar == 1):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE CARAMELIZADO ALTO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 2):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE CARAMELIZADO MEDIO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 3):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE CARAMELIZADO BAJO EN AZUCAR ☆☆☆☆☆☆")  


        else:
            masvalor4 = float(input("INGRESE MAS SALDO: "))
            print("SU SALDO ES: ",masvalor4+saldo)
            if(masvalor4 >= 2.00 and case == 4):
                    print("Se esta despachando café caramelizado, espere unos segundos...")
                    print("SU VUELTO ES: &/", masvalor4+saldo-2.00)
                    if (sugar == 1):
                            print(" ☆☆☆☆☆☆ DISFRUTE SU CAFE CARAMELIZADO ALTO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 2):
                            print("☆☆☆☆☆☆ DISFRUTE SU CAFE CARAMELIZADO MEDIO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 3):
                            print(" ☆☆☆☆☆☆DISFRUTE SU CAFE CARAMELIZADO BAJO EN AZUCAR ☆☆☆☆☆☆") 

    case 5:

        if(saldo <= 1.99):
                    print("\n")
                    print("NO CUENTA CON EL SALDO SUFICIENTE")
                    print("\n")
        if(saldo >= 2.00 and case == 5):
                    print("Se esta despachando chocolate caliente, espere unos segundos...")
                    print("SU VUELTO ES: &/", saldo-2.00)
                    print("\n")
                    if (sugar == 1):
                            print("☆☆☆☆☆☆ DISFRUTE SU CHOCOLATE CALIENTE ALTO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 2):
                            print("☆☆☆☆☆☆ DISFRUTE SU CHOCOLATE CALIENTE MEDIO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 3):
                            print("☆☆☆☆☆☆ DISFRUTE SU CHOCOLATE CALIENTE BAJO EN AZUCAR ☆☆☆☆☆☆") 

        else:
            masvalor5 = float(input("INGRESE MAS SALDO: "))
            print("SU SALDO ES: ",masvalor5+saldo)
            if(masvalor5 >= 2.00 and case == 5):
                    print("Se esta despachando chocolate caliente, espere unos segundos...")
                    print("SU VUELTO ES: &/", masvalor5+saldo-2.00)
                    print("\n")
                    if (sugar == 1):
                            print("☆☆☆☆☆☆ DISFRUTE SU CHOCOLATE CALIENTE ALTO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 2):
                            print("☆☆☆☆☆☆ DISFRUTE SU CHOCOLATE CALIENTE MEDIO EN AZUCAR ☆☆☆☆☆☆")
                    if (sugar == 3):
                            print("☆☆☆☆☆☆ DISFRUTE SU CHOCOLATE CALIENTE BAJO EN AZUCAR ☆☆☆☆☆☆") 