# Mining data from danish news sites
### Scraping danish news sites and posting the results

Jeg hygger mig med at lave små scripts til at mine data fra forskellige sider. Denne gang er det nyheder fra sider. Jeg har lagt hårdt ud med politik sektionen fra DR over de sidste 3000 dage.

Følgende biblioteker bruges:
```
pip install beautifulsoup4
pip install afinn

pip install textblob
```

Efter at have kigget på flere måder at træne en klassifikationsalgoritme valgte jeg [TextBlob](https://textblob.readthedocs.io/en/dev/ "TextBlob ReadTheDocs")
som var relativt let at arbejde med i forhold til de data der var scraped fra DR.

Derudover har jeg tilføjet et par scripts jeg har brugt til at træne en Naive Bayes model til at skille positive fra negative nyheder.
Ud af de ca _26k_ nyheder i .csv filen valgte jeg dem med en [Afinn](https://github.com/fnielsen/afinn "Afinn på GitHub") værdi på over 2 og under -2 som i alt var omkring 2,4k nyheder. Dem shufflede jeg og delte i træningssæt og testsæt. Med Naive Bayes modellen er der en nøjagtighed på 93%.

> Hvad nu?


![DR logo](https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/DR_logo.svg/1280px-DR_logo.svg.png "DR logo")
