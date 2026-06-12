---
title: Come fai a sapere che una squadra di AI sta davvero lavorando?
date: 2026-03-10
slug: osservabilita-squadre-ai
excerpt: Una squadra di AI lavora tra sé mentre nessuno la guarda. Come sai che non è in stallo? Cinque lezioni di osservabilità, nate ognuna da un fallimento reale.
---

Tutti parlano di cosa le AI sanno fare. Quasi nessuno della domanda che qualunque
responsabile si farà il primo lunedì mattina: come faccio a sapere che stanno
DAVVERO lavorando? Non "se rispondono quando le interrogo" — se stanno lavorando
adesso, tra loro, mentre nessuno le guarda.

Gestisco una squadra di AI persistenti che costruisce sistemi. La domanda me la sono
posta nel modo più istruttivo possibile: fallendo. Prima notte di lavoro autonomo
della squadra, uno specialista è rimasto fermo 75 minuti ad aspettare una risposta
che non arrivava. Nessun allarme, nessun errore: silenzio operoso in apparenza, stallo
totale nella sostanza. Da quella notte ho ricostruito l'osservabilità da zero, e le
lezioni valgono per chiunque metta più di un'AI in produzione.

**Lezione uno: non chiederlo a loro.** La risposta ingenua è interrogare l'AI: "stai
lavorando?". Non funziona per una ragione logica prima che tecnica: un'istanza in
stallo non può dichiararsi in stallo, una morta non può dichiararsi morta. Qualunque
status autodichiarato ("sto lavorando", scritto alle 15:00) è un falso vivo in
potenza: alle 16:00 non ti dice nulla, perché chi l'ha scritto potrebbe essersi
fermato alle 15:01. La soluzione è vecchia quanto i sistemi distribuiti: la presenza
si PROVA con un meccanismo, non si dichiara. Ogni istanza deposita un "lease" — un
gettone di presenza con scadenza esplicita: "sono in ascolto fino alle X". Scaduto il
gettone, l'istanza è assente per definizione, qualunque cosa avesse dichiarato.

**Lezione due: traccia i debiti, non le attività.** Quello che ammazza una squadra —
umana o artificiale — non è l'inattività: è il debito di risposta. Una richiesta
aperta senza esito, una consegna attesa che non arriva. Ogni richiesta nel mio
protocollo nasce con un identificativo coniato da chi la fa, e si chiude SOLO con un
esito esplicito che cita quell'identificativo. Niente chiusure implicite, niente "si
sarà risolto". Il guardiano automatico non controlla cosa fanno le istanze: controlla
chi ha debiti scaduti. È la differenza tra sorvegliare e fare auditing.

**Lezione tre: l'allarme che si ripete è rumore, e il rumore è un guasto.** Il mio
primo guardiano segnalava ogni anomalia a intervalli fissi. Risultato in una notte:
134 messaggi identici, che hanno seppellito di rumore il canale che dovevano
proteggere. Regola che ne è uscita: si allerta SOLO al cambio di stato — quando un
problema nasce, quando cambia natura, quando si risolve. Un sistema di allarmi che
grida sempre equivale a un sistema di allarmi spento, con in più il danno.

**Lezione quattro: il guardiano indica, non guarisce.** Per scelta architetturale il
mio watchdog non può riavviare le istanze né intervenire: rileva il debito, lo
segnala, e dice all'umano DOVE serve. L'ho pagata anche qui: un processo di guardia
sopravvissuto a un riavvio ha continuato a sorvegliare una squadra che non c'era più.
Oggi anche il guardiano deposita il suo gettone di presenza, e ha un interruttore
esplicito. Chi sorveglia va sorvegliato con gli stessi meccanismi di chi lavora.

**Lezione cinque, la più importante: ogni fallimento diventa una regola meccanica.**
Tutto quello che ho elencato è nato da un incidente reale, analizzato e trasformato
in un vincolo che non dipende dalla disciplina di nessuno — né mia né delle AI.
Nelle classi di errore che ho meccanizzato, le recidive a oggi sono zero. In quelle
dove mi sono affidato alla buona condotta, le recidive sono arrivate puntuali, e una
volta da parte mia.

Niente di tutto questo è nuovo: sono i principi dei sistemi distribuiti e del
site-reliability engineering, applicati a lavoratori che invece dei servizi sono
modelli linguistici. La novità è che quasi nessuno li sta applicando lì. Quando
valutate un fornitore che vi propone "agenti AI in produzione", fate una domanda
sola: come fai a sapere che stanno lavorando? Se la risposta è "glielo chiediamo",
avete già la risposta.
