---
title: L'accuratezza media è la metrica di chi vende
date: 2026-09-01
slug: accuratezza-media-metrica-di-chi-vende
excerpt: «Accuracy migliorata fino al 50%». Rispetto a cosa? Il numero medio misura il caso medio in un problema dove il valore vive nei casi peggiori. Il conto che lo dimostra, e cosa chiedo al posto della percentuale.
---

«Accuratezza del forecasting migliorata fino al 50%.» Fino al 50% rispetto a cosa?

Senza il punto di partenza quel numero non misura niente. Passare da un errore del
40% al 20% e passare da un riferimento scelto male a uno meno peggio producono
entrambi «50% di miglioramento», e raccontano due storie opposte. «Fino al» poi è un
tetto, non una media: è il caso migliore osservato una volta, non quello che vi
aspettate la settimana prossima.

[Ad aprile](/post/valutare-un-predittore/) ho scritto le quattro domande che faccio
prima di fidarmi di un predittore. Questo è il seguito: perché anche quando le
risposte ci sono, la *media* resta il numero sbagliato.

## Il costo dell'errore ha una forma

Dove l'output è testo, sbagliare è quasi gratis: cancellate la frase e riscrivete.
Dove l'output muove qualcosa — un ordine, un lotto, un turno, un rimborso — l'errore
resta, e i conti sono asimmetrici.

Caso costruito apposta. Un classificatore smista 10.000 eventi al giorno con
un'accuratezza del 99%. Sono 100 errori al giorno, 36.500 l'anno. Se gli eventi
critici sono l'1% del totale — cento al giorno — e il modello sbaglia proprio su
quelli il 30% delle volte, l'accuratezza aggregata resta al 99%: i 30 errori critici
si perdono nei 10.000. Ma il sistema fallisce il 30% dei casi che giustificavano la
sua esistenza. Trenta al giorno. Undicimila l'anno.

| | Eventi al giorno | Errori | Accuratezza |
|---|---|---|---|
| Classe ordinaria | 9.900 | 70 | 99,3% |
| Classe critica | 100 | 30 | **70%** |
| **Aggregato** | **10.000** | **100** | **99%** |

Il 99% è vero. Ed è il numero che nasconde esattamente il problema. L'accuratezza
aggregata è una metrica di vanità: misura il caso medio in un problema dove il valore
vive nelle code.

## Le tre cose che mancano sempre

Un numero su cui contare ha tre ingredienti, e nel claim tipico non ce n'è uno: il
**riferimento** (meglio di un forecast manuale? di una media mobile a sette giorni? un
forecast ingenuo batte già molti modelli «AI»), la **metrica e l'orizzonte** (un errore
a quattro settimane sull'aggregato e un errore a un giorno sul singolo articolo non
sono confrontabili), la **distribuzione dell'errore** sugli elementi che pesano.
Un'accuratezza media alta può nascondere proprio gli errori che fanno danno.

Un numero su cui contare è un numero che un altro può ricostruire: dataset,
riferimento, finestra temporale, criterio. «Fino al 50%» non si ricostruisce. È una
cifra costruita per convincere, non per essere verificata.

## Cosa chiedo al posto della percentuale

Un campione di audit conservato. Non «l'accuratezza è 94%», ma: ecco 200 casi
ricontrollati a mano, con la decisione del modello, la decisione giusta e il
ragionamento attaccato. Un campione così non riassume, espone. Ci si chiede «dove
cede» invece di «quanto spesso indovina». Lo si riapre quando cambia il modello,
quando i dati si spostano, quando qualcuno contesta una singola etichetta. La
percentuale invece va rifatta da capo, e fino ad allora non si sa più se è vera.

È così che lavoro. Il sistema predittivo costruito dalla mia squadra non «fa il 95%»:
batte il riferimento in 18 finestre temporali su 18, su dati mai visti, con un
protocollo di valutazione alla cieca e i criteri scritti prima di guardare i
risultati. Le quattro ipotesi che la squadra ha falsificato — due erano mie — sono
agli atti con lo stesso metodo. Non è una percentuale: è un registro che chiunque può
riaprire.

## La domanda che chiude

La distanza tra un'automazione che regge e una demo che colpisce sta qui: la prima vi
dà gli ingredienti del numero, la seconda vi dà solo il numero. Prima di fidarvi di
un'accuratezza chiedete: misurata come, su quali dati, contro quale alternativa, e —
soprattutto — quanto costa l'1% in cui sbaglia, e chi se ne accorge.
