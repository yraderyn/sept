import re

def alomorf(prefiks, rec): 
    """
    Proverava da li je zadovoljen uslov okruženja za javljanje određenih alomorfa.
    """
    listaprefiksasuslovima = ['is', 'us', 'ras', 'nus', 'bes', 'op', 'ot', 'pot', 'nat', 'pret', 'z', 'iš', 'raš', 'š', 'iž', 'ž', 'iza', 'raza', 'oda']
    listakulprefiksa = ['protiv', 'polu', 'pred', 'samo', 'mimo', 'među', 'bez', 'van', 'pod', 'pra', 'pre', 'pri', 'raz', 'nad', 'nuz', 'po', 'do', 'iz', 'uz', 'na', 'ne', 'su', 'sa', 'od', 'za', 'ob', 'o', 'u', 's']
    stip = ['is', 'us', 'ras', 'nus', 'bes', 'pret', 'ot', 'pot', 'nat', 'op']
    štip = ['iš', 'raš', 'š']
    žtip = ['iž', 'š']
    atip = ['iza', 'raza', 'oda']

    if prefiks in listaprefiksasuslovima:
        if prefiks in stip and re.match('[ptkhfcč]', rec[len(prefiks):]):
            return True
        elif prefiks == 'z' and re.match('[bdg]', rec[len(prefiks):]):
            return True
        elif prefiks in štip and re.match('[čć]', rec[len(prefiks):]):
            return True
        elif prefiks in žtip and re.match('[dž|đ]', rec[len(prefiks):]):
            return True
        elif prefiks in atip and re.findall('[zbsš]', rec[len(prefiks):]):
            return True
    elif prefiks in listakulprefiksa:
        return True
    else:
        return False

def provera_glagola(osnova_gpt, listainfinitiva, uslov):
    for nastavak_za_infinitiv in listainfinitiva:
        potencijalni_glagol = osnova_gpt + nastavak_za_infinitiv
        if potencijalni_glagol in listaglagola:
            uslov = 33
            return uslov
            break

def prvi_uslov(rec, prefiks, recnik):
    """
    Proverava da li se potencijalna osnova se nalazi u recniku.
    Isključuje sve kratke nizove (npr. 'sa', gde bi se 's-' se prepoznalo kao prefiks a '-a' kao rec srpskog jezika).         
    """
    if rec[len(prefiks):] in recnik and len(rec[len(prefiks):]) > 1:
        return 1
    else:
        return 0

def drugi_uslov(prefiks, rec, listaprefiksa, recnik):
    """
    Proverava da li se na potencijalnu osnovu moze dodati drugi prefiks tako da dobijena rec bude leksikalizovana.         
    """
    for prefiks2 in listaprefiksa:
        if prefiks2 + rec[len(prefiks):] in recnik and prefiks != prefiks2 and len(rec[len(prefiks):]) > 1 and len(rec[len(prefiks2):]) > 1 and alomorf(prefiks2, rec) == True: #treci uslov u if petlji: ne zelimo da se prefiks menja samim sobom.
            return 2
        else:
            return 0


def prefiksator(rec, listaprefiksa, recnik, listasufiksa, listainfinitiva, listaglagola):
    global uslov, prefiks, prefiks2, sufiks, potencijalni_glagol, rec_za_proveru
    for prefiks in listaprefiksa:
        # varijabla koja prati da li je zadovoljen neki od uslova da se niz smatra prefiksom
        uslov = 0 

        if rec.startswith(prefiks) and alomorf(prefiks, rec) == True:  
            uslov = prvi_uslov(rec, prefiks, recnik)

            if uslov == 1:
                print('naso1')
                return uslov, prefiks
                break

            else:
                uslov = drugi_uslov(prefiks, rec, listaprefiksa, recnik)

                if uslov == 2:
                    print('naso2')
                    return uslov, prefiks, prefiks2
                    break
                
                else: #ako ni prvi ni drugi uslov nisu ispunjeni, proverava se zavrsava li se rec na sufiks
                     #program moze da prepozna da se rec zavrsava na vise sufiksa (npr. -ijacija i -a). 
                     #Zato je bitno uzeti ih sve u obzir, jer je kod u ranijim verzijama prestao da radi odmah posle prvog sufiksa.
                    lista_sufiksa_za_pojedinacnu_rec = list() 
                    for sufiks in listasufiksa:
                        if rec.endswith(sufiks):
                            lista_sufiksa_za_pojedinacnu_rec.append(sufiks)
                    for sufiks in lista_sufiksa_za_pojedinacnu_rec:
                        osnova_bez_sufiksa = rec[:(-len(sufiks))]
                        osnova_bez_sufiksa_i_prefiksa = osnova_bez_sufiksa[len(prefiks):]
                        if len(osnova_bez_sufiksa_i_prefiksa) > 1:
                            #umesto sufiksa dodaje jedan od nastavaka za infinitiv koje glagol moze imati. 
                            #Posle proverava da li je dobijeni glagol u listi.
                            for nastavak_za_infinitiv in listainfinitiva: 
                                potencijalni_glagol = osnova_bez_sufiksa + nastavak_za_infinitiv
                                if potencijalni_glagol in listaglagola:
                                    #odvojimo glagole koji zadovoljavaju 3. uslov na tri liste. 
                                    #U prvoj listi 31 ce biti oni gde glagol bez prefiksa ostaje leksikalizovan
                                    #U drugoj 32 ce biti reci kod kojih moze da se zameni prefiks
                                    #U trecoj idu reci koje ne zadovoljavaju ni jedan od ova dva uslova. 
                                    #Trecu listu cemo prelaziti i gledati sta moze da se spase i koje uslove treba jos da dodamo.
                                    if potencijalni_glagol[len(prefiks):] in listaglagola: 
                                        uslov = 31
                                        break
                                    else:
                                        for prefiks2 in listaprefiksa: 
                                            if prefiks2 + potencijalni_glagol[len(prefiks):] in listaglagola and prefiks != prefiks2 and len(potencijalni_glagol[len(prefiks):]) > 1 and len(potencijalni_glagol[len(prefiks2):]) > 1 and alomorf(prefiks2, lista_sufiksa_za_pojedinacnu_rec) == True:  # treci uslov u if petlji: ne zelimo da se prefiks menja samim sobom. Za cetvrti i peti uslov pogledati liniju 49
                                                uslov = 32
                                                break
                            if uslov == 0:
                                if sufiks.startswith('n'):
                                    osnova_bez_sufiksa = osnova_bez_sufiksa + 'n'
                                if osnova_bez_sufiksa.endswith('nut'):
                                    potencijalni_glagol = osnova_bez_sufiksa + 'i'
                                    if potencijalni_glagol in listaglagola:
                                        uslov = 33
                                elif osnova_bez_sufiksa.endswith('an'):
                                    potencijalni_glagol = osnova_bez_sufiksa[:-1] + 'ti'
                                    if potencijalni_glagol in listaglagola:
                                        uslov = 33
                                elif osnova_bez_sufiksa.endswith('en'):
                                    osnova_gpt = osnova_bez_sufiksa[:-2]
                                    uslov = provera_glagola(osnova_gpt, listainfinitiva, uslov)
                                    if uslov == 0:
                                        for jotovano in lj_lista:
                                            if osnova_gpt.endswith(jotovano):
                                                osnova_gpt = osnova_gpt[:-2]
                                                uslov = provera_glagola(osnova_gpt, listainfinitiva, uslov)
                                    if uslov == 0:
                                        if osnova_gpt.endswith('đ'):
                                            osnova_gpt = osnova_gpt[:-1] + 'd'
                                            uslov = provera_glagola(osnova_gpt, listainfinitiva, uslov)
                                    if uslov == 0:
                                        if osnova_gpt.endswith('ć'):
                                            osnova_gpt = osnova_gpt[:-1] + 't'
                                            uslov = provera_glagola(osnova_gpt, listainfinitiva, uslov)
                                    if uslov == 0:
                                        if osnova_gpt.endswith('šlj'):
                                            osnova_gpt = osnova_gpt[:-1] + 'sl'
                                            uslov = provera_glagola(osnova_gpt, listainfinitiva, uslov)
                                    if uslov == 0:
                                        if osnova_gpt.endswith('j'):
                                            osnova_gpt = osnova_gpt[:-1]
                                            uslov = provera_glagola(osnova_gpt, listainfinitiva, uslov)
                                    if uslov == 0:
                                        if osnova_gpt.endswith('š'):
                                            osnova_gpt = osnova_gpt[:-1] + 's'
                                            uslov = provera_glagola(osnova_gpt, listainfinitiva, uslov)
                                    if uslov == 0:
                                        if osnova_gpt.endswith('č'):
                                            osnova_gpt = osnova_gpt[:-1] + 'c'
                                            uslov = provera_glagola(osnova_gpt, listainfinitiva, uslov)
                                    if uslov == 0:
                                        if osnova_gpt.endswith('č'):
                                            potencijalni_glagol = osnova_gpt[:-1] + 'ći'
                                            if potencijalni_glagol in listaglagola:
                                                uslov = 33
                                                break
                            if uslov == 0:
                                uslov = 3
                                break
                            else:
                                break
            if uslov == 0:
                pass
            else:
                if uslov == 3 or uslov == 32 or uslov == 31 or uslov == 33:
                    print('naso'+ str(uslov))
                    return uslov, prefiks, sufiks, potencijalni_glagol
                break