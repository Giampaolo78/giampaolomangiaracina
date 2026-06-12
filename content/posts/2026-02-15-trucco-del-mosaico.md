---
title: Far capire un video a un'AI senza GPU: il trucco del mosaico
date: 2026-02-15
slug: trucco-del-mosaico
excerpt: Far capire a una macchina cosa succede in un video, senza GPU e senza cloud: trasformare il flusso in una sola immagine.
---

C'è un problema che chiunque lavori con le telecamere conosce: far capire a una
macchina COSA sta succedendo in un video — non quali oggetti ci sono, ma cosa sta
accadendo — costa carissimo. O servono GPU dedicate, o si manda tutto in cloud
pagando per ogni secondo analizzato, con la latenza e le questioni privacy che ne
seguono. Sui dispositivi economici — uno smartphone di fascia bassa, una telecamera
IP, un piccolo computer da quadro elettrico — la comprensione video semplicemente non
gira.

Sto sperimentando un'architettura che aggira il problema invece di affrontarlo di
forza. L'idea è semplice al punto da sembrare una furbata: **trasformare il video in
una singola immagine**.

Funziona così. Sul dispositivo economico gira solo un rilevatore di oggetti
velocissimo e "stupido" — vede componenti, attrezzi, mani, dispositivi di protezione,
trenta volte al secondo, ma non capisce niente di quello che vede. Ogni pochi secondi,
il sistema prende una manciata di fotogrammi e li impagina in un mosaico: una griglia
di miniature, in ordine di tempo, con sopra stampate le etichette di ciò che il
rilevatore ha visto e di come si muoveva ("avvitatore: velocità alta, 3 giri al
secondo"). Quel mosaico — una sola immagine statica, leggibile anche da un occhio
umano — viene dato a un modello AI piccolo, che non deve più riconoscere nulla (le
etichette sono già scritte): deve solo inferire l'azione. "Sta fissando il pannello
laterale. Ha smesso da due minuti." Il suo output testuale, infine, arriva a un
modello intelligente che ragiona e decide se intervenire.

Il risultato sperimentale che mi ha sorpreso è il terzo passaggio. Nei test
comparativi, lo stesso modello intelligente che riceveva l'immagine grezza descriveva
la scena ma NON vedeva il problema ("lavorazione energica", davanti a un'operazione
fuori sequenza che avrebbe imposto di smontare tutto); ricevendo solo il testo
strutturato, lo stesso modello identificava l'errore con precisione ("sequenza
violata: il pannello prima del telaio che deve sostenerlo") e suggeriva l'intervento
immediato. Separare la percezione dal ragionamento non è un compromesso imposto
dall'hardware povero: è un vantaggio. Chi ragiona, ragiona meglio su informazione
già digerita.

Tre proprietà di questa architettura che per un'azienda contano più della tecnica.
La prima: il mosaico è ispezionabile — un umano lo guarda e vede ESATTAMENTE ciò che
ha visto il modello; quando qualcosa va male, il debug è guardare una figura, non
scavare in una scatola nera. La seconda: il riferimento di latenza è umano — un
supervisore in carne e ossa reagisce in 3-6 secondi, il ciclo del mosaico chiude in
5-7; per gli eventi davvero critici (fumo, una caduta) il rilevatore veloce lancia
l'allarme immediato senza aspettare nessuno. La terza: i volti e le targhe si possono
sfocare al primo passaggio, sul dispositivo — quello che esce verso i modelli è già
anonimizzato.

La stessa struttura si adatta a domini diversi ricalibrando solo i due estremi: cosa
rilevare e quali azioni riconoscere. Supervisione di un assemblaggio industriale,
monitoraggio del territorio (la buca segnalata da sei giorni), supporto alla
fisioterapia (l'angolo del ginocchio che non raggiunge l'obiettivo), coaching sportivo
tra un punto e l'altro. L'infrastruttura nel mezzo non cambia.

Onestà dovuta: siamo a livello di proof of concept — quattro test controllati, dati
in parte sintetici, nessun deployment in produzione. I numeri che ho citato sono
misure di laboratorio, e il fine-tuning del lettore di mosaici è lavoro davanti, non
dietro. Ma il principio — comprare comprensione video al prezzo di una lettura di
immagini — ha retto a ogni test fatto finora, e il prossimo passo è metterlo alla
prova su flussi reali.

Costruisco sistemi dove modelli piccoli e modelli intelligenti si dividono il lavoro.
La parte difficile non è mai il modello: è decidere cosa deve viaggiare tra l'uno e
l'altro.
