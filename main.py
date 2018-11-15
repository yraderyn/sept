from prefiksi import prefiksator

if __name__ == '__main__':

	listaprefiksa = ['protiv', 'raza', 'polu', 'pred', 'pret', 'samo', 'mimo', 'među', 'bez', 'bes', 'van', 'pod', 'pot', 'pra', 'pre', 'pri', 'raz', 'ras', 'raš', 'nad', 'nat', 'nuz', 'nus', 'oda', 'iza', 'po', 'do', 'iz', 'is', 'iž', 'iš', 'uz', 'us', 'na', 'ne', 'su', 'sa', 'od', 'za', 'ot', 'ob', 'op', 'o', 'u', 's', 'z']
	listasufiksa = ['evljanin', 'ijacija', 'ionizam', 'ionista', 'ovnjača', 'ovština', 'evština', 'ajlija', 'anstvo', 'ancija', 'aonica', 'arijum', 'arnica', 'atizam', 'ašnica', 'ekanja', 'encija', 'enjača', 'eskara', 'edžija', 'ijanac', 'ikovac', 'instvo', 'ionist', 'ionica', 'istika', 'jetica', 'ljanin', 'obanja', 'ovište', 'ovnica', 'otinja', 'turača', 'turina', 'uljaga', 'uljača', 'uljina', 'uljica', 'urdija', 'urlija', 'uskara', 'uskera', 'ušnica', 'uština', 'čurina', 'avina', 'avica', 'avnik', 'agija', 'adija', 'ajica', 'alija', 'alica', 'aljka', 'ander', 'anija', 'janin', 'anica', 'arija', 'arina', 'arica', 'arnik', 'atika', 'atura', 'ahija', 'acija', 'ačija', 'benik', 'elica', 'eljak', 'endra', 'enica', 'enjak', 'erina', 'esija', 'esina', 'etika', 'etina', 'ešina', 'ijada', 'ijana', 'ijera', 'ilije', 'ilica', 'iljka', 'inica', 'injak', 'injac', 'ioner', 'ionaš', 'išnik', 'etica', 'kelja', 'kinja', 'kovac', 'lište', 'njava', 'njača', 'ovača', 'evača', 'ovilo', 'ovina', 'evina', 'ovica', 'evica', 'ovlje', 'evlje', 'ovnik', 'olija', 'olina', 'olica', 'oljak', 'onica', 'onjak', 'orija', 'osija', 'otina', 'otica', 'udija', 'uljak', 'unica', 'urija', 'urina', 'usina', 'ušina', 'ušica', 'čanin', 'džija', 'ština', 'avac', 'avka', 'adak', 'adba', 'azan', 'ajka', 'ajko', 'alac', 'alje', 'anac', 'anik', 'anin', 'anka', 'ance', 'anče', 'anja', 'arak', 'arac', 'arak', 'arij', 'arka', 'aroš', 'ater', 'ator', 'aćka', 'ačka', 'ašin', 'aška', 'ašce', 'bina', 'vica', 'dura', 'ejac', 'elac', 'elin', 'elja', 'enac', 'enik', 'ence', 'eraj', 'erak', 'erac', 'erda', 'etak', 'etin', 'ečak', 'ešce', 'ivač', 'idba', 'izam', 'ijan', 'ijat', 'ijer', 'ilac', 'ilja', 'inac', 'inka', 'inče', 'inja', 'inje', 'ista', 'itak', 'itet', 'itis', 'ićak', 'ičar', 'ičić', 'ična', 'išan', 'iška', 'ište', 'jeha', 'kost', 'lama', 'leta', 'lija', 'lica', 'ljag', 'ljaj', 'nina', 'nica', 'nost', 'njak', 'ovac', 'evac', 'ovik', 'ović', 'ević', 'ovka', 'ojka', 'ujko', 'olan', 'olet', 'onik', 'onja', 'otak', 'ošta', 'stvo', 'telj', 'ulja', 'unac', 'unče', 'urak', 'urda', 'utak', 'utin', 'juca', 'udža', 'ušak', 'ušar', 'ušac', 'ušić', 'uška', 'cija', 'čaga', 'čija', 'čina', 'čica', 'čuga', 'čura', 'džik', 'štak', 'ava', 'aga', 'ada', 'aža', 'aik', 'aja', 'aje', 'aka', 'alo', 'alj', 'ana', 'and', 'ant', 'ara', 'aća', 'ača', 'eza', 'elj', 'ent', 'esa', 'est', 'eta', 'eto', 'eut', 'eša', 'ivo', 'ija', 'ije', 'ika', 'ilo', 'ina', 'ing', 'ino', 'ist', 'ica', 'iša', 'jak', 'eha', 'juh', 'kan', 'lac', 'luk', 'nik', 'nja', 'nje', 'oba', 'ovo', 'evo', 'uza', 'oje', 'ost', 'ota', 'oća', 'oša', 'tak', 'tva', 'tor', 'uga', 'uža', 'ulj', 'ura', 'uca', 'uša', 'čak', 'čić', 'dža', 'av', 'ag', 'ad', 'aj', 'ak', 'an', 'en', 'ao', 'ar', 'at', 'ać', 'ac', 'ač', 'aš', 'ba', 'va', 'ež', 'ez', 'en', 'er', 'et', 'eš', 'id', 'ik', 'im', 'in', 'ir', 'it', 'ić', 'uć', 'ic', 'iš', 'ja', 'je', 'jo', 'uh', 'ka', 'ki', 'ko', 'la', 'le', 'lo', 'mo', 'no', 'ov', 'on', 'or', 'os', 'ot', 'oč', 'oš', 'st', 'ta', 'ća', 'će', 'ug', 'un', 'ur', 'us', 'ut', 'uh', 'uš', 'ca', 'ce', 'ča', 'če', 'ša', 'a', 'e', 'o']
	listainfinitiva = ['karati', 'uckati', 'uljiti', 'ušiti', 'arati', 'avati', 'evati', 'ivati', 'ovati', 'isati', 'irati', 'ijati', 'nuti', 'kati', 'ati', 'iti', 'eti', 'ti']
	lj_lista = ['blj', 'vlj', 'plj', 'mlj']


	# leme glagola
	with open('glagoli.txt', 'r', encoding = 'utf-8') as fajl_sa_glagolima:
		listaglagola=[red[:-1] for red in fajl_sa_glagolima.readlines()]

	# sve leme imenica za koje ce program da proveri jesu li prefigirane, poredjane po frekventnosti
	with open('reizlaz2.txt', 'r', encoding = 'utf-8') as korpus:
		recnik = [red[:-1] for red in korpus.readlines()]


	for rec in recnik:
		prefiksator(rec, listaprefiksa, recnik, listasufiksa, listainfinitiva, listaglagola)
