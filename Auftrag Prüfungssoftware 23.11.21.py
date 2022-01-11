for i in range(0, 3): #wie viele Versuche man haben kann
    antwort = input("Was ist die Hauptstadt der Schweiz? ") #Gibt eine Stadt ein
    if antwort == "Bern": #wenn sie Bern 
        print("Gratulation, sie haben die Prüfung bestanden!") #gibt sie aus das sie die Prüfung bestanden haben
        break #Loops wird abgebrochen
    elif i == 2: # sonst
        print("Sie haben die Prüfung leider nicht bestanden.") #gibt aus das sie die Prüfung nicht bestanden haben
    else:
        print("Leider Falsch, sie haben noch " + str(2 - i) + " Versuche") #gibt aus wie viele Versuche sie noch haben