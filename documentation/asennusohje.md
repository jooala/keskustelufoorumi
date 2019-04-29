# Asennusohje

Kloonaa GitHub-projekti itsellesi

## Konfigurointi

Varmista, että sinulla on seuraavat työvälineet:

- Python (vähintään versio 3.5 tai uudempi)
- Pythonin PIP

## Käynnistäminen

Ohjelma käynnistetään komennolla
```
py run.py
```

Sovellus aukeaa selaimeen osoitteeseen: http://127.0.0.1:5000

### Heroku

- PostgreSQL-tietokantahallintajärjestelmä

Asennetaan komennolla:
```
pip install psycopg2
```
##### Herokuun lisääminen:
```
heroku config:set HEROKU=1
```
```
heroku pg:psql
```
```
heroku addons:add heroku-postgresql:hobby-dev
```
## 

