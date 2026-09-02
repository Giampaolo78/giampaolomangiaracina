---
title: Sei agenti non sono sei volte un agente
date: 2026-06-30
slug: sei-agenti-non-sono-sei-volte-un-agente
excerpt: La capacità di una squadra di AI cresce in linea retta col numero di agenti. Il coordinamento cresce al quadrato. I conti che faccio prima di aggiungere un agente, e la topologia che li tiene sotto controllo.
---

Sei agenti che si parlano non sono sei volte un agente. Sono quindici canali di
comunicazione: N per N meno uno, diviso due. Con sette agenti i canali sono ventuno;
con dieci, quarantacinque. La capacità cresce in linea retta. Il coordinamento cresce
al quadrato. È la stessa curva che ha affondato i progetti software ogni volta che a
un ritardo si è risposto aggiungendo persone.

## Il secondo conto, quello che nessuno fa

Una catena di cinque agenti, ognuno affidabile al 90%, non è affidabile al 90%. È
affidabile al 59%: 0,9 elevato alla quinta. Gli errori si moltiplicano a ogni
passaggio, non si annullano.

| Affidabilità del singolo passo | Catena di 3 | Catena di 5 | Catena di 8 |
|---|---|---|---|
| 90% | 73% | 59% | 43% |
| 95% | 86% | 77% | 66% |
| 99% | 97% | 95% | 92% |

C'è un dettaglio che rende il conto ancora peggiore. Ogni passaggio di consegne tra
agenti è un riassunto, e ogni riassunto perde informazione. Quattro passaggi in catena
e l'output è la fotocopia di una fotocopia: l'accuratezza non crolla per un errore
grande, si erode in una sequenza di perdite piccole che nessuna metrica di fine catena
intercetta.

## Cosa ho visto nella mia squadra

La squadra con cui lavoro è un caposquadra AI, tre specialisti AI e io. Cinque nodi:
con messaggi punto a punto sarebbero dieci canali. La prima notte, con un coordinamento
ancora immaturo, il sistema ha fallito esattamente lì: richieste perse tra un canale e
l'altro, uno specialista fermo 75 minuti ad aspettare una risposta che era finita
altrove.

La correzione non è stata «meno agenti». È stata cambiare topologia. Gli agenti hanno
smesso di spedirsi riassunti e hanno cominciato a lavorare su bacheche condivise: uno
spazio che ogni agente legge e scrive, dove la verità sta nell'artefatto e non nei
messaggi che rimbalzano. Il coordinamento torna lineare — ogni agente ha un canale
solo, la bacheca — e ogni fallimento diventa una regola meccanica. Nelle classi di
errore che ho meccanizzato, le recidive sono zero. Il sistema è open-source:
[claude-code-dialogue](https://github.com/Giampaolo78/claude-code-dialogue).

## Quando un agente in più si ripaga

Il criterio che uso: quel passaggio è controllabile da solo? Se la sua uscita ha un
riscontro esterno al modello — compila, il test passa, il numero torna, il modello
batte il riferimento su dati mai visti — l'agente in più tronca la propagazione
dell'errore e si ripaga. È così che il modello costruito dalla squadra ha battuto lo
scoring di riferimento in 18 finestre temporali su 18: ogni consegna aveva un
riscontro oggettivo prima di diventare l'input della successiva.

Se invece è un altro modello che commenta il precedente senza riscontro esterno, stai
comprando latenza e token, e a volte amplifichi un errore detto con sicurezza. Far
rivedere la risposta di un modello da un altro modello abbassa gli errori solo se i
due sbagliano in modo indipendente — e GPT, Claude e Gemini condividono buona parte
dei dati di addestramento e dei bias. Su un caso ambiguo, spesso concordano sulla
risposta sbagliata.

## La regola

Il multi-agente conviene in due casi: sottotask indipendenti che girano in parallelo,
o un controllo oggettivo tra un passo e l'altro. Fuori da lì, una catena di agenti è
un solo modello che parla con sé stesso, più lentamente e più caro.

La metrica da mettere accanto ad accuratezza, latenza e costo non è il numero di
agenti. È la profondità della catena di consegne, e quanta informazione sopravvive a
ogni passaggio. Aggiungere un agente è banale. Aggiungerlo senza aprire un nuovo
canale è il problema di design.
