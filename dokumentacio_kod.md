IS_PRIME FÜGGVÉNY
Az első függvénnyel ellenőrzöm, hogy egy adott szám prím-e.
Az 1-gyet, ahogyan a feladat is kéri, azt nem kezelem prímként.
A függvény első soraiban ellenőrzöm, hogy 1, vagy 0-e az érték.
Ha igen, akkor vissza is térek False értékkel, hiszen akkor
nem prím. Ha 2 az érték, akkor visszatérek igazzal.
Ha pedig a szám osztható kettőbel, akkor pedig biztosan nem
prím, hiszen 1, önmaga, illetve a 2 is osztója, ezáltal biztosan nem
prím. A 2-re ez szintén igaz, de az már előtte le lett kezelve,
ezért ha az input 2, akkor eddig el sem jut a kód, emiatt
lesz jó a 2 esetére is ez. Ha pedig páratlan, akkor
megnézem 3-tól az értékeket, hiszen 3-ig le lettek kezelve.
A while ciklust maximum az inputban megadott értékig viszem, hiszen
n inputnak n-nél nagyobb osztója nem lehet. A jelenlegi érték
esetében mindig megvizsgálom, hogy az megvan-e maradék nélkül
az inputban kapott számban. Ha megvan, akkor találtunk egy
olyan számot, ami osztója az inputnak, és nem is az 1, hiszen az nem lehet,
mert 3-ról indult a ciklus, és nem is az n, hiszen mivel négyzetre emelve
kezelem a ciklust. Ha pedig nem osztható az inputtal az adott szám, akkor
a jelenlegi értéket tovább kell növelni 1-gyel. Ha lefut a ciklus, és
nem tértünk vissza False-al, akkor pedig csak prím lehet, hiszen 
mindent végigvizsgálva nem találtunk további osztót.

GET_PRIME_N FÜGGVÉNY
A függvény inputban az n-edik értéket kapja meg, és az ahanyadik prímet kell visszaadnia.
Az előző függvényt amiatt csináltam, hogy azt itt fel tudjam használni. Felvettem egy
countert, ami n-ig fog számolni, és az adott ciklusban mindig megnézegetem, hogy a jelenlegi szám
az prím-e. Ha igen, akkor a számlálót megnövelem, mindezt addig, ameddig nem érjük el az inputot.
A ciklus első sorában pedig növelem a jelenlegi számot, hiszen azt bármilyen kondíció esetén 
léptetni kell. Amikor megtaláltuk az adott prímet, akkor pedig visszatérek az értékkel,
majd alatta egy printtel kiíratom a konzolra az eredményt.