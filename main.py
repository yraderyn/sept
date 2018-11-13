import re
with open('imenice/reizlaz2.txt', 'r', encoding = 'utf-8') as korpus: #otvara fajl na kojem se nalaze sve leme imenice za koje ce program da proveri jesu li prefigirane; poredjane po frekventnosti
    with open('glagoli/glagoli.txt', 'r', encoding = 'utf-8') as fajl_sa_glagolima: #otvara fajl sa lemama glagola
        recnik = [red[:-1] for red in korpus.readlines()] #od fajla sa imenicama pravi listu
        listaglagola=[red[:-1] for red in fajl_sa_glagolima.readlines()]
        listaprefiksa = ['protiv', 'raza', 'polu', 'pred', 'pret', 'samo', 'mimo', 'među', 'bez', 'bes', 'van', 'pod', 'pot', 'pra', 'pre', 'pri', 'raz', 'ras', 'raš', 'nad', 'nat', 'nuz', 'nus', 'oda', 'iza', 'po', 'do', 'iz', 'is', 'iž', 'iš', 'uz', 'us', 'na', 'ne', 'su', 'sa', 'od', 'za', 'ot', 'ob', 'op', 'o', 'u', 's', 'z']
        listasufiksa = ['evljanin', 'ijacija', 'ionizam', 'ionista', 'ovnjača', 'ovština', 'evština', 'ajlija', 'anstvo', 'ancija', 'aonica', 'arijum', 'arnica', 'atizam', 'ašnica', 'ekanja', 'encija', 'enjača', 'eskara', 'edžija', 'ijanac', 'ikovac', 'instvo', 'ionist', 'ionica', 'istika', 'jetica', 'ljanin', 'obanja', 'ovište', 'ovnica', 'otinja', 'turača', 'turina', 'uljaga', 'uljača', 'uljina', 'uljica', 'urdija', 'urlija', 'uskara', 'uskera', 'ušnica', 'uština', 'čurina', 'avina', 'avica', 'avnik', 'agija', 'adija', 'ajica', 'alija', 'alica', 'aljka', 'ander', 'anija', 'janin', 'anica', 'arija', 'arina', 'arica', 'arnik', 'atika', 'atura', 'ahija', 'acija', 'ačija', 'benik', 'elica', 'eljak', 'endra', 'enica', 'enjak', 'erina', 'esija', 'esina', 'etika', 'etina', 'ešina', 'ijada', 'ijana', 'ijera', 'ilije', 'ilica', 'iljka', 'inica', 'injak', 'injac', 'ioner', 'ionaš', 'išnik', 'etica', 'kelja', 'kinja', 'kovac', 'lište', 'njava', 'njača', 'ovača', 'evača', 'ovilo', 'ovina', 'evina', 'ovica', 'evica', 'ovlje', 'evlje', 'ovnik', 'olija', 'olina', 'olica', 'oljak', 'onica', 'onjak', 'orija', 'osija', 'otina', 'otica', 'udija', 'uljak', 'unica', 'urija', 'urina', 'usina', 'ušina', 'ušica', 'čanin', 'džija', 'ština', 'avac', 'avka', 'adak', 'adba', 'azan', 'ajka', 'ajko', 'alac', 'alje', 'anac', 'anik', 'anin', 'anka', 'ance', 'anče', 'anja', 'arak', 'arac', 'arak', 'arij', 'arka', 'aroš', 'ater', 'ator', 'aćka', 'ačka', 'ašin', 'aška', 'ašce', 'bina', 'vica', 'dura', 'ejac', 'elac', 'elin', 'elja', 'enac', 'enik', 'ence', 'eraj', 'erak', 'erac', 'erda', 'etak', 'etin', 'ečak', 'ešce', 'ivač', 'idba', 'izam', 'ijan', 'ijat', 'ijer', 'ilac', 'ilja', 'inac', 'inka', 'inče', 'inja', 'inje', 'ista', 'itak', 'itet', 'itis', 'ićak', 'ičar', 'ičić', 'ična', 'išan', 'iška', 'ište', 'jeha', 'kost', 'lama', 'leta', 'lija', 'lica', 'ljag', 'ljaj', 'nina', 'nica', 'nost', 'njak', 'ovac', 'evac', 'ovik', 'ović', 'ević', 'ovka', 'ojka', 'ujko', 'olan', 'olet', 'onik', 'onja', 'otak', 'ošta', 'stvo', 'telj', 'ulja', 'unac', 'unče', 'urak', 'urda', 'utak', 'utin', 'juca', 'udža', 'ušak', 'ušar', 'ušac', 'ušić', 'uška', 'cija', 'čaga', 'čija', 'čina', 'čica', 'čuga', 'čura', 'džik', 'štak', 'ava', 'aga', 'ada', 'aža', 'aik', 'aja', 'aje', 'aka', 'alo', 'alj', 'ana', 'and', 'ant', 'ara', 'aća', 'ača', 'eza', 'elj', 'ent', 'esa', 'est', 'eta', 'eto', 'eut', 'eša', 'ivo', 'ija', 'ije', 'ika', 'ilo', 'ina', 'ing', 'ino', 'ist', 'ica', 'iša', 'jak', 'eha', 'juh', 'kan', 'lac', 'luk', 'nik', 'nja', 'nje', 'oba', 'ovo', 'evo', 'uza', 'oje', 'ost', 'ota', 'oća', 'oša', 'tak', 'tva', 'tor', 'uga', 'uža', 'ulj', 'ura', 'uca', 'uša', 'čak', 'čić', 'dža', 'av', 'ag', 'ad', 'aj', 'ak', 'an', 'en', 'ao', 'ar', 'at', 'ać', 'ac', 'ač', 'aš', 'ba', 'va', 'ež', 'ez', 'en', 'er', 'et', 'eš', 'id', 'ik', 'im', 'in', 'ir', 'it', 'ić', 'uć', 'ic', 'iš', 'ja', 'je', 'jo', 'uh', 'ka', 'ki', 'ko', 'la', 'le', 'lo', 'mo', 'no', 'ov', 'on', 'or', 'os', 'ot', 'oč', 'oš', 'st', 'ta', 'ća', 'će', 'ug', 'un', 'ur', 'us', 'ut', 'uh', 'uš', 'ca', 'ce', 'ča', 'če', 'ša', 'a', 'e', 'o']
        listaprefiksasuslovima = ['is', 'us', 'ras', 'nus', 'bes', 'op', 'ot', 'pot', 'nat', 'pret', 'z', 'iš', 'raš', 'š', 'iž', 'ž', 'iza', 'raza', 'oda']
        listakulprefiksa = ['protiv', 'polu', 'pred', 'samo', 'mimo', 'među', 'bez', 'van', 'pod', 'pra', 'pre', 'pri', 'raz', 'nad', 'nuz', 'po', 'do', 'iz', 'uz', 'na', 'ne', 'su', 'sa', 'od', 'za', 'ob', 'o', 'u', 's']
        listainfinitiva = ['avati', 'evati', 'ivati', 'ovati', 'isati', 'ijati', 'nuti', 'kati', 'ati', 'iti', 'eti', 'ti']
        lj_lista = ['blj', 'vlj', 'plj', 'mlj']
        
        # s obzirom da odredjeni alomorfi imaju odredjena okruzenja u kojem se javljaju
        # potrebno je videti da li je taj uslov zadovoljen pre nego sto se rec proverava
        def alomorf(prefiks): 
            stip = ['is', 'us', 'ras', 'nus', 'bes', 'pret', 'ot', 'pot', 'nat', 'op']
            štip = ['iš', 'raš', 'š']
            žtip = ['iž', 'š']
            atip = ['iza', 'raza', 'oda']
            if prefiks in listaprefiksasuslovima:
                if prefiks in stip:
                    a = re.match('[ptkhfcč]', rec[len(prefiks):])
                    if a:
                        return True
                elif prefiks == 'z':
                    a = re.match('[bdg]', rec[len(prefiks):])
                    if a :
                        return True
                elif prefiks in štip:
                    a = re.match('[čć]', rec[len(prefiks):])
                    if a:
                        return True
                elif prefiks in žtip:
                    a = re.match('[dž|đ]', rec[len(prefiks):])
                    if a:
                        return True
                elif prefiks in atip:
                    a = re.findall('[zbsš]', rec[len(prefiks):])
                    if a:
                        return True
            elif prefiks in listakulprefiksa:
                return True
            else:
                return False

        def provera_glagola(osnova_gpt):
            for nastavak_za_infinitiv in listainfinitiva:
                potencijalni_glagol = osnova_gpt + nastavak_za_infinitiv
                if potencijalni_glagol in listaglagola:
                    uslov = 33
                    return uslov
                    break

        def prefiksator(rec):
            global uslov, prefiks, prefiks2, sufiks, potencijalni_glagol, rec_za_proveru
            for prefiks in listaprefiksa:
                #svaka rec pocinje sa varijablom uslov na nuli. 
                #U zavisnosti od ispunjenog uslova se vrednost ove varijable menja.
                uslov = 0 
                #PRVI USLOV - potencijalna osnova se nalazi u recniku
                if rec.startswith(prefiks) and alomorf(prefiks) == True:  
                    #drugim uslovom u if petlji se izbacuju sve kratke reci koje lako mogu ispuniti PRVI USLOV
                    #ali koje svakako nisu prefigirane (npr. 'sa', gde 's-' bi se prepoznalo kao prefiks, a '-a' kao rec srpskog jezika)
                    if rec[len(prefiks):] in recnik and len(rec[len(prefiks):]) > 1:
                        uslov = 1
                    if uslov==0:
                        #DRUGI USLOV - na potencijalnu osnovu se moze dodati drugi prefiks tako da dobijena rec bude leksikalizovana
                        for prefiks2 in listaprefiksa: 
                            if prefiks2 + rec[len(prefiks):] in recnik and prefiks != prefiks2 and len(rec[len(prefiks):]) > 1 and len(rec[len(prefiks2):]) > 1 and alomorf(prefiks2) == True: #treci uslov u if petlji: ne zelimo da se prefiks menja samim sobom.
                                uslov = 2
                                break
                    if uslov == 0: #ako ni prvi ni drugi uslov nisu ispunjeni, proverava se zavrsava li se rec na sufiks
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
                                                if prefiks2 + potencijalni_glagol[len(prefiks):] in listaglagola and prefiks != prefiks2 and len(potencijalni_glagol[len(prefiks):]) > 1 and len(potencijalni_glagol[len(prefiks2):]) > 1 and alomorf(prefiks2) == True:  # treci uslov u if petlji: ne zelimo da se prefiks menja samim sobom. Za cetvrti i peti uslov pogledati liniju 49
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
                                                provera_glagola(osnova_gpt)
                                                if uslov == 0:
                                                    for jotovano in lj_lista:
                                                        if osnova_gpt.endswith(jotovano):
                                                            osnova_gpt = osnova_gpt[:-2]
                                                            provera_glagola(osnova_gpt)
                                                if uslov == 0:
                                                    if osnova_gpt.endswith('đ'):
                                                        osnova_gpt = osnova_gpt[:-1] + 'd'
                                                        provera_glagola(osnova_gpt)
                                                if uslov == 0:
                                                    if osnova_gpt.endswith('ć'):
                                                        osnova_gpt = osnova_gpt[:-1] + 't'
                                                        provera_glagola(osnova_gpt)
                                                if uslov == 0:
                                                    if osnova_gpt.endswith('šlj'):
                                                        osnova_gpt = osnova_gpt[:-1] + 'sl'
                                                        provera_glagola(osnova_gpt)
                                                if uslov == 0:
                                                    if osnova_gpt.endswith('j'):
                                                        osnova_gpt = osnova_gpt[:-1]
                                                        provera_glagola(osnova_gpt)
                                                if uslov == 0:
                                                    if osnova_gpt.endswith('š'):
                                                        osnova_gpt = osnova_gpt[:-1] + 's'
                                                        provera_glagola(osnova_gpt)
                                                if uslov == 0:
                                                    if osnova_gpt.endswith('č'):
                                                        osnova_gpt = osnova_gpt[:-1] + 'c'
                                                        provera_glagola(osnova_gpt)
                                                if uslov == 0:
                                                    if osnova_gpt.endswith('č'):
                                                        potencijalni_glagol = osnova_gpt[:-1] + 'ći'
                                                        if potencijalni_glagol in listaglagola:
                                                            uslov = 33
                                                            break
                                    else:
                                        pass
                                if uslov!=0:
                                    break
                                if uslov==0:
                                    uslov=3
                                    break
                    if uslov == 0:
                        pass
                    else:
                        if uslov == 1:
                            print('naso1')
                            return uslov, prefiks
                        if uslov == 2:
                            print('naso2')
                            return uslov, prefiks, prefiks2
                        if uslov == 3 or uslov == 32 or uslov == 31 or uslov == 33:
                            print('naso'+ str(uslov))
                            return uslov, prefiks, sufiks, potencijalni_glagol
                        break
        with open('uslov1.txt', 'w', encoding = 'utf-8') as izlaz_1:
            with open('uslov2.txt', 'w', encoding = 'utf-8') as izlaz_2:
                with open('uslov3.txt', 'w', encoding = 'utf-8') as izlaz_3:
                    with open('uslov32.txt', 'w', encoding = 'utf-8') as izlaz_32:
                        with open('uslov31.txt', 'w', encoding='utf-8') as izlaz_31:
                            with open('uslov33.txt', 'w', encoding='utf-8') as izlaz_33:
                                for rec in recnik:
                                    prefiksator(rec)
                                    if uslov == 1:
                                        izlaz_1.write(rec + ' : ' + prefiks + '\n')
                                    if uslov == 2:
                                        izlaz_2.write(rec + ' : ' + prefiks + ' (' + prefiks2 + ')\n')
                                    if uslov == 3:
                                        izlaz_3.write(rec + ' : ' + prefiks + ' : ' + sufiks + '\n')
                                    if uslov == 33:
                                        izlaz_33.write(rec + ' : ' + prefiks + ' : ' + sufiks + ' (' + potencijalni_glagol + ')\n')
                                    if uslov ==32:
                                        izlaz_32.write(rec + ' : ' + prefiks + ' : ' + sufiks + ' (' + potencijalni_glagol + ')\n')
                                    if uslov ==31:
                                        izlaz_31.write(rec + ' : ' + prefiks + ' : ' + sufiks + ' (' + potencijalni_glagol + ')\n')