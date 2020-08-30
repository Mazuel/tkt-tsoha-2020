# tkt-tsoha-2020


## Keskustelufoorumi

Osoite: https://tsoha-messageforum.herokuapp.com/

### Perusidea

Peruskäyttäjillä mahdollisuus luoda omia keskusteluja, joihin muut voivat kirjoittaa, ja liittyä muiden aloittamiin keskusteluihin. Sisäänkirjautumiseen vaaditaan käyttäjätunnus, jota varten pitää rekisteröityä.
Sivustolla on eri käyttäjärooleja, jotka voivat hallinnoida sivustoa eri tavoin:
 - Admin-tason käyttäjä hallinnoida muita käyttäjiä ja poistaa aihealueita sekä keskusteluita.
 - Moderator-tason käyttäjä voi poistaa muiden lähettämiä viestejä.
 - User-tason käyttäjä voi luoda aihealueita, keskusteluja, sekä lähettää viestejä ja tutkailla muiden profiileja.  
 
### Toteutetut toiminnot

- [x] Luoda uusi käyttäjä/kirjautua sisään sivustolle
- [x] Uuden aihealueen luominen
- [x] Etsiä muita käyttäjiä ja tutkia heidän profiilejaan.
- [x] Mahdollisuus luoda uusia keskusteluja liittyen tiettyyn aiheeseen
- [x] Käyttäjäroolit (Admin, Moderator, User)
- [x] Poistaa omia viestejä tai muiden viestejä mikäli kirjautuneen käyttäjän rooli on vähintään Moderator
- [x] Poistaa aihealueita ja keskusteluita Admin-käyttäjänä

### Nykyinen tila
Pääkäyttäjän tunnus (admin:Sala1234) \
Sovellukseen voi luoda käyttäjän joka on oletuksena rooliltaan normaali käyttäjä ja kirjautua sillä sisään. Sovelluksessa on myös yksi admin-käyttäjä, jonka roolia ei voi muuttaa,
mutta sen kautta voi hallinoida muiden käyttäjien rooleja. Ainostaan admin-tason käyttäjä voi poistaa aihealueita (topics) ja luotuja keskusteluja (threads). Sivustolla voi tutkia myös
muiden käyttäjien profiileja, joissa näkyy pienimuotoista statistiikkaa kuten esim. lähetetyt viestit ja aloitetut keskustelut. Profiileja voi tutkia joko käyttäjähaun kautta tai klikkaamalla
jonkun keskustelun viestissä olevaa käyttäjänimeä, joka ohjaa kyseisen käyttäjän profiiliin.

 

