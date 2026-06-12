---
title: Squadra di AI o AI con assistenti? Quando serve l'una e quando l'altra
date: 2025-12-31
slug: squadra-o-assistenti
excerpt: Squadra di AI persistenti o un'AI con assistenti usa-e-getta? Sono due cose diverse, e sbagliare la scelta costa caro.
---

Nel mio lavoro ci sono due modi molto diversi di far collaborare più AI, e vedo
continuamente venderli come se fossero la stessa cosa. Non lo sono, e sbagliare la
scelta costa caro in entrambe le direzioni.

La metafora che uso è accademica. Il primo modo è il professore col suo laboratorio:
un'AI principale che per un compito grosso ingaggia assistenti usa-e-getta — "tu
cerca di qua, tu verifica di là, tu leggi questi cento file" — raccoglie i risultati
e li integra. Gli assistenti non hanno memoria, non hanno responsabilità, finito il
compito spariscono. Il secondo modo è un consiglio di professori ordinari: ognuno ha
una cattedra (i dati, il modello, le decisioni), una memoria che cresce nel tempo, e
risponde del suo dominio davanti agli altri. E sopra tutti c'è un rettore — l'essere
umano — che firma le delibere che contano.

Il primo modo si chiama tecnicamente "subagent", il secondo è quello che io chiamo
dialogue system: istanze pari, persistenti, con nome e mandato. Li ho usati entrambi,
a fondo, e la risposta onesta su quale sia meglio è: dipende, e il confine è netto.

Per distribuire lavoro parallelo che TU hai già definito — cercare in cento posti,
verificare cinquanta casi, esplorare tre alternative — gli assistenti usa-e-getta sono
nettamente superiori. Niente coordinamento, niente attese, niente fraintendimenti:
fan-out, raccolta, fine. Chi vi propone una "squadra di agenti persistenti" per un
problema così vi sta vendendo complessità che pagherete senza usarla.

La squadra di pari serve quando il problema ha un'altra forma: quando nessuno — voi
compresi — può tenere in testa tutto il sistema, e ogni pezzo richiede qualcuno che
lo conosca a fondo e lo difenda nel tempo. Lì la persistenza paga tre dividendi che
gli assistenti non possono dare: contesto accumulato (lo specialista dei dati ricorda
PERCHÈ una scelta è stata fatta tre giorni fa), revisione incrociata vera (chi
controlla il mio lavoro non condivide i miei bias di contesto), e responsabilità
(un'istanza con un nome e un dominio difende le sue misure — la mia mi ha contraddetto
più di una volta, con ragione).

Il prezzo, però, va detto: il coordinamento tra pari è un costo vivo. Nella prima
notte del mio progetto più grande il coordinamento ha fallito in modi seri — richieste
perse, uno specialista fermo 75 minuti ad aspettare una risposta che non arrivava. Ogni
fallimento è stato trasformato in una regola meccanica del protocollo, e in quelle
classi di errore le recidive finora sono zero. Ma chi vi racconta la squadra di AI
senza raccontarvi il costo del coordinamento vi sta mostrando solo metà del conto.

E il rettore non è decorativo. Nel mio sistema le azioni irreversibili — pubblicare,
consolidare, spendere — richiedono la firma umana per contratto. Non è sfiducia
nell'AI: è la stessa ragione per cui nelle aziende serie la firma sui bonifici non ce
l'ha lo stagista brillante.

Regola pratica, se dovete scegliere: se il problema è "tanto lavoro definito da
distribuire", assistenti usa-e-getta. Se il problema è "un sistema troppo grande per
una testa sola, che deve restare in piedi nel tempo", squadra di pari con un umano che
firma. Se chi vi consiglia non vi fa questa distinzione, chiedetegli perché.
