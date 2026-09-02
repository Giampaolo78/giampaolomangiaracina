---
title: Il modello è la parte più facile da sostituire
date: 2026-07-27
slug: il-modello-e-la-parte-piu-facile-da-sostituire
excerpt: Un modello si cambia in un pomeriggio. Quello che non si cambia è tutto ciò che gli sta intorno — dove vive lo stato, come è isolata la memoria, cosa resta quando il processo cade a metà. È lì che si decide se un sistema di agenti regge, ed è la decisione che i team prendono per ultima.
---

Il dibattito pubblico resta fermo sulla classifica: quale modello ragiona meglio,
quale costa meno per token. Ma un modello si cambia in un pomeriggio. Ciò che non si
cambia è l'impalcatura intorno — l'*harness*, per chi usa il nome inglese: dove vive
lo stato, come è isolata la memoria tra un compito e l'altro, chi possiede l'ambiente
in cui l'agente esegue.

## Il minuto 140

Un agente che lavora per tre ore su un compito lungo — migrare uno schema,
riconciliare un archivio, produrre un report da cento fonti — cade al minuto 140.
Timeout, riavvio, limite di contesto. Cosa succede?

Nella maggior parte dei sistemi che vedo: si riparte da zero, e i 140 minuti sono
persi. Nel caso peggiore si riparte a metà, e le operazioni già fatte vengono rifatte:
un record scritto due volte, una mail spedita due volte.

La risposta è vecchia quanto l'ingegneria backend: punti di ripristino, stato
persistente fuori dal processo, operazioni che si possono ripetere senza danno.
Macchine a stati, code durevoli. Non è un problema nuovo e non è specifico degli
agenti: cambia il nome, non la sostanza. Ma è la decisione che separa una demo da un
sistema, ed è quella che i team prendono per ultima, dopo aver scelto il modello che
si vede in classifica.

## Tre pattern, una domanda

Oggi in produzione si contendono il campo tre schemi: esecuzione gestita dal fornitore
del modello, esecuzione durevole su infrastruttura propria, orchestrazione di più
agenti per ruoli. Non si distinguono per qualità del modello. Si distinguono per chi
paga il costo operativo e per cosa succede quando il processo cade a metà.

Nel sistema con cui lavoro la scelta è stata la più semplice possibile: lo stato sono
file su disco. Ogni messaggio tra agenti, ogni consegna, ogni decisione è un file.
Nessun server, nessun database, nessuna sessione da cui dipendere. Un agente che cade
riparte leggendo la bacheca, e trova esattamente dove era rimasto — perché la verità
sta nell'artefatto, non nella memoria del modello.

## Il test del cambio di fornitore

C'è un modo rapido per capire quanto del vostro sistema è vostro. Immaginate di
cambiare fornitore del modello domani mattina. Cosa sopravvive?

Sopravvivono — se esistono — i prompt versionati, le specifiche, l'insieme di casi su
cui misurate l'accuratezza, i controlli automatici che vincolano cosa l'agente può
fare, il registro delle correzioni fatte da persone. Non sopravvivono i pesi del
modello, che non erano vostri comunque: il laboratorio che li addestra li vende
identici a voi e ai vostri concorrenti, allo stesso prezzo. Tutto ciò che è
noleggiabile è già di tutti.

Per la maggior parte dei team che incontro l'inventario di ciò che sopravvive è vicino
a zero. Si sposta il flusso su un nuovo strumento e si riparte, perché non c'era un
metodo: c'era un'abitudine legata a un'interfaccia. Chi cambia strumento agentico ogni
sei mesi non sta cavalcando una transizione. Sta dimostrando di non aver accumulato
niente che sopravviva al cambio.

## Ogni correzione è un dato

Da qui una lettura diversa del «tenere l'umano nel giro». Non è solo prudenza: è il
meccanismo con cui la conoscenza dell'organizzazione viene catturata. Ogni volta che
una persona corregge l'agente, quella correzione è un dato. Se viene registrata dove
l'agente la rilegge, l'errore non si ripete. Se va persa in una chat, lo stesso errore
lo pagate due volte.

[A maggio](/post/workflow-agentico-asset-del-codebase/) ne ho scritto dal lato del
codice: il contesto che dai all'agente è un asset del codebase, versionato e
revisionato. Questo è lo stesso principio un piano più in basso. Un agente che produce
lavoro senza lasciare traccia è un interinale più veloce, non capitale. Diventa
capitale quando l'impalcatura in cui opera registra cosa ha fatto, perché, e cosa è
stato corretto.

L'affidabilità non esce dal modello. Esce dall'architettura che lo contiene.
