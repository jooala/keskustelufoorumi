# Oleelliset käyttötapaukset

## Ennen kirjautumista
* Kävijä voi selailla keskustelupalstalla kategorioita, aiheita sekä viestejä.
```sql
SELECT * From Categories;
```
```sql
SELECT * From Topics 
LEFT JOIN TopicsCategories ON TopicsCategories.topics_id = Topics.id
LEFT JOIN Categories ON Categories.id = TopicsCategories.categories_id
WHERE Categories.id = (valittu.id); # Valittu.id on minkä kategorian avasit.
```
```sql
SELECT * From Posts 
LEFT JOIN Topics ON Posts.topic_id = Topic.id
WHERE Posts.topic_id = (valittu.id); # Valittu.id on minkä aiheen avasit.
```

* Kävijä voi luoda uuden käyttäjätunnuksen
```sql
INSERT INTO Account(name, username, password, rank) VALUES (form.name.data, form.username.data, form.password.data, 'USER');
```
* Kävijä voi kirjautua sisään olemassa olevalla käyttäjätunnuksella
```sql
SELECT * FROM Account WHERE username = form.username.data AND password = form.password.data;
```
* Kävijä ei voi avata toisten kävijöiden profiilia

## Kirjautumisen jälkeen
* Käyttäjä voi muuttaa profiilissa asetuksiaan
```sql
UPDATE Account SET name = form.name.data WHERE Account.id = current_user.id;
```
* Käyttäjä voi luoda uusia aiheita foorumille
```sql
INSERT INTO Topics(date_created, date_modified, name, desc, account_id) VALUES (current_timestamp(), current_timestamp(), form.name.data, form.desc.data, current_user.id);
```
```sql
INSERT INTO TopicsCategories(topics_id, categories_id) VALUES (topics_id, categories_id);
```
* Käyttäjä voi kirjoittaa viestejä aiheisiin
```sql
INSERT INTO Posts(date_created, date_modified, message, account_id, topic_id) VALUES (current_timestamp(), current_timestamp(), form.message.data, current_user.id, topic.id);
```
* Käyttäjä voi selata toisten profiileja
```sql
SELECT * FROM Account WHERE id = (valittu.id); # valittu.id on minkä profiilin avasit.
```
* Käyttäjä voi kirjautua ulos
* Voi tehdä kaikkea mitä kävijä pystyy

## Pääkäyttäjä
* Voi muuttaa kategorian nimeä ja kuvausta
```sql
UPDATE Categories SET name = form.name.data, desc = form.desc.data WHERE id = (valittu.id); # valittu.id on minkä kategorian kohtaa muutat.
```
* Voi luoda uusia kategorioita
```sql
INSERT INTO Categories(date_created, date_modified, name, desc) VALUES (current_timestamp(), current_timestamp(), form.name.data, form.desc.data);
```
* Voi poistaa kategorioita
```sql
DELETE FROM Categories WHERE id = (valittu.id); # valittu.id on minkä kategorian kohdasta klikkaat.
```
* Voi tehdä kaikkea mitä tavallinen käyttäjä ja kävijä pystyy


