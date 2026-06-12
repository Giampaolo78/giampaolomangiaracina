---
title: "Il nostro modello fa il 95%": come si valuta un sistema predittivo senza ingannarsi
date: 2026-04-25
slug: valutare-un-predittore
excerpt: «Il nostro modello fa il 95%» — da solo, quel numero non dice quasi niente. Le quattro domande che faccio sempre prima di fidarmi di un sistema predittivo.
---

Quando qualcuno vi dice "il nostro modello predittivo ha un'accuratezza del 95%",
quel numero — da solo — non significa quasi niente. Non perché sia falso: perché è
incompleto in modi che fanno comodo a chi lo presenta. Lavoro su sistemi predittivi e
ho codificato le quattro domande che faccio sempre, a me stesso prima che ai
fornitori. Le racconto su un caso equivalente al mio (il dominio reale del progetto è
riservato): un sistema che stima la probabilità che un pagamento non arrivi.

**Prima domanda: sa ordinare o sa anche pesare?** Sono due capacità diverse e quasi
tutti misurano solo la prima. La discriminazione è saper mettere in fila i casi: chi
è più a rischio di chi. La calibrazione è un'altra cosa: quando il modello dice
"80% di probabilità", l'evento deve poi verificarsi davvero l'80% delle volte. Un
modello può ordinare benissimo e pesare malissimo — e se le sue probabilità le usate
per decidere (concedere un fido, fissare una soglia), è il peso che vi rovina, non
l'ordine. Nel mio progetto il modello batte il riferimento di settore sulla
discriminazione in 18 finestre temporali su 18; sulla calibrazione il quadro è più
sottile, ed è esattamente il tipo di onestà che pretendo dai miei stessi report.

**Seconda domanda: il numero viene da UN test o dalla distribuzione dei test?** Il mio
sistema, su un certo periodo di prova, ha mostrato un errore di calibrazione
bassissimo: 0.0011. Numero da brochure. Poi l'abbiamo ricalcolato anno per anno: la
mediana era dieci volte più alta, con stagioni che oscillavano da 0.006 a 0.042. Quel
primo numero era una coda fortunata — vero, ma non rappresentativo. Chi vi mostra UN
numero su UN campione vi sta mostrando, nel migliore dei casi, il suo giorno buono.
Chiedete la mediana e gli estremi su finestre diverse.

**Terza domanda: il test sta nel futuro del modello?** Un sistema predittivo si
valuta SOLO su dati posteriori a tutto ciò che ha visto in addestramento — e la
verifica va ripetuta facendo scorrere la finestra nel tempo, addestra-sul-passato,
prova-sul-dopo, ancora e ancora. Ogni scorciatoia qui produce numeri gonfiati in modo
invisibile: basta una sola informazione "dal futuro" infilata per sbaglio in una
variabile, e il modello sembra un oracolo finché non va in produzione. Nel mio
progetto questa proprietà è verificata meccanicamente, colonna per colonna, non
promessa.

**Quarta domanda: i criteri sono stati scritti prima o dopo aver visto i risultati?**
È la più scomoda. Se esplori i dati finché non trovi un pattern e poi lo "validi"
sugli stessi dati, troverai sempre qualcosa: si chiama data mining bias, e l'unico
antidoto è strutturale — separare la finestra dove si SCOPRE dalla finestra dove si
CERTIFICA, e mettere per iscritto soglie, criteri e numerosità minime PRIMA di
guardare i risultati. Si chiama pre-registrazione. Nel mio progetto è prassi
obbligatoria, e di recente ha bocciato un'ipotesi a cui tenevo molto io: i criteri
erano congelati, i dati hanno detto l'opposto, l'ipotesi è caduta. Fa male il giusto,
e costa infinitamente meno che scoprirlo coi soldi veri.

C'è un principio dietro tutte e quattro le domande: scegliere, dove possibile,
problemi in cui la realtà ti corregge da sola e in fretta — domini dove ogni
previsione riceve il suo verdetto in giorni, non in trimestri. Il feedback rapido e
gratuito è il più potente strumento anti-illusione che esista: non puoi raccontarti
storie a lungo, se la realtà ti risponde ogni mattina.

Niente di tutto questo richiede matematica avanzata: richiede la disciplina di farsi
le domande quando le risposte potrebbero non piacere. È il lavoro. Il 95%, da solo,
è marketing.
