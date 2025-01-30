### 1. **Bejelentkezés és Felhasználói Munkamenet**
- A felhasználó bejelentkezését egy biztonságos rendszeren keresztül végezzük, ahol a jelszavak **bcrypt** algoritmussal lesznek titkosítva az adatbázisban.
- A rendszer **bejelentkezési tokennel** működik, melynek lejárati ideje **2 perc**. A token lejárta után a felhasználó újra be kell jelentkezzen. Egy **újraküldés gomb** is biztosítja a token újbóli generálását.
  
### 2. **Árajánlat Készítő Rendszer**
- Az **adminisztrációs felületen** az árajánlat készítőhez tartozó tételek kezelhetők. Itt lehetőség van új tételek felvitelére, meglévők módosítására, és törlésére. Minden tételhez tartozik egy **egység (kg, liter, darab, stb.) és egy ár**.
- Az admin felületen az **"Árajánlat típusok"** és **"Kiegészítő szolgáltatások"** bővíthetősége is biztosított.
- Az **árajánlat generátor oldalon** a felhasználó a tételek listájából válogathatja ki azokat, amelyek az árajánlatba kerülnek. Az **egyedi mennyiség** és **egység** beállítások is megoldhatóak (pl. kilogramm, liter, stb.).
- A kiválasztott tételek végösszegét a rendszer **automatikusan számolja ki**.
- A rendszer lehetővé teszi az árajánlatok **PDF formátumban történő exportálását**.
  - A PDF fejlécén szerepeljen a **cég neve**, **cég logója** és **a cég adatai**.
  - Az árajánlatoknak legyen **egyedi azonosítójukkal**, és ezek kereshetők legyenek a **státusz és a cég neve alapján**.
- A **PDF sablon** testreszabására létrejön egy admin felület, ahol a cégadatokat és a logót is könnyedén beállíthatóak.

### 3. **Adatbázis Szerkezet és Táblák**
- A **"quotes"** táblában a következő adatokat tároljuk:
  - **Cég neve**
  - **Cég székhelye** (irányítószám, település, utca, házszám)
  - **Adószám**
  - **Kapcsolattartó email címe és telefonszáma**
  
- A **"orders"** táblában szereplő **order_type** és **status** oszlopoknak egy másik tábla adott sorának azonosítójára kell hivatkozni. Az admin felületen lehetőség lesz ezek módosítására.
  
- **Árajánlatok tételei**: Az árajánlatokhoz kapcsolódó tételek adatbázisban való tárolásához a **quote_items** táblát hozunk létre. Ebben tároljuk a következő adatokat:
  - Árajánlathoz kapcsolódó tétel azonosítója
  - Mennyiség
  - Egység
  - Ár

### 4. **Térképes Megjelenítés és Megrendelések Kezelése**
- A fúrási pontokat egy térképen jelenítjük meg, és a felhasználó **település neve** alapján tud keresni. A **popup ablakban** megjelennek a következő adatok:
  - Település neve
  - Utca, ház szám
  - Fúrás állapota
  - Kút mélysége
  - Vízhozam
  - Munkanapok száma
  - Megjegyzés
- Az **admin felületen** lehetőség lesz új fúrási pontok hozzáadására, meglévők módosítására.

### 5. **Funkciók és Interakciók**
- Az admin felületen az összes szükséges funkció és beállítás elérhető lesz.
  - A **tételek kezelése**, **árfolyam frissítések**, **megrendelések típusa**, **kiegészítő szolgáltatások**, **cégadatok** mind egyszerűen módosíthatók.
- A **felhasználói felület** színvilága a **kék, barna és zöld** színeket fogja használni, melyek a víz, föld és fű színeit reprezentálják. Az **érzékeny információk** biztonságos módon lesznek tárolva és elérhetők.
  
### 6. **Backend és Technológiai Stack**
- A backend fejlesztéséhez **Flask** alkalmazást használunk, amely biztosítja az API-kat és a funkciók kezelését.
- Az adatok **AJAX használatával** fognak frissülni (pl. mentés, küldés), és minden művelet után egy popup ablak jelezni fogja a sikeres műveletet a jobb alsó sarokban.
  
### 7. **További Fejlesztési Lehetőségek**
- A rendszer **folyamatosan bővíthető és módosítható**, így ha bármilyen új igény merül fel, az könnyen integrálható.
- A rendszer úgy van kialakítva, hogy gyorsan reagáljon a felhasználói igényekre, és a jövőbeni fejlesztések egyszerűen hozzáadhatók.

