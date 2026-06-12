---
title: Il dialogue system: cosa ho costruito e cosa ho validato finora
date: 2026-06-09
slug: dialogue-system-cosa-ho-validato
excerpt: Una squadra di AI — un caposquadra, tre specialisti e io a supervisione — costruisce un sistema predittivo completo in 36 ore. Cosa ho misurato, e cosa resta da dimostrare.
---

## L'idea in due righe

Ho fatto lavorare insieme una squadra di intelligenze artificiali — un caposquadra AI,
tre specialisti AI e io come supervisore — e in circa 36 ore la squadra ha costruito un
sistema predittivo completo: acquisizione dati, modello, livello decisionale. Il dominio
specifico del progetto resta riservato; per raccontarlo uso un caso equivalente, la
**previsione del rischio di mancato pagamento** (dato uno storico di clienti e fatture,
stimare la probabilità che un pagamento non arrivi, e decidere a chi estendere fiducia).
Non è una demo: ogni pezzo è stato misurato, verificato in modo incrociato e
documentato per iscritto.

## Come funziona, senza tecnicismi

- Ogni AI della squadra è **persistente**: ha un nome, un dominio di responsabilità
  ("i dati", "il modello", "le decisioni") e accumula esperienza sul suo pezzo, come un
  collaboratore che non cambia ogni giorno.
- Le AI **si parlano per iscritto** su bacheche condivise: ogni richiesta, risposta e
  consegna resta agli atti. Il risultato collaterale ha un valore enorme per un'azienda:
  **tracciabilità totale** — di ogni decisione si può ricostruire chi l'ha presa,
  quando e su quale evidenza.
- **L'essere umano resta il capo**: le azioni irreversibili (pubblicare, salvare in via
  definitiva, spendere) richiedono la mia firma esplicita. La squadra propone e
  argomenta; le decisioni che contano passano da me. Niente "AI autonoma che fa da
  sola": è una scelta di progetto, non un limite.

## Cosa è stato validato (fatti, non promesse)

**1. La squadra consegna davvero.** Sistema completo costruito in una notte più un
giorno: pipeline dati con 76 variabili costruite senza "barare" (nessuna informazione
dal futuro, verificato meccanicamente), modello predittivo, livello decisionale con un
protocollo di valutazione alla cieca. Decine di consegne committate con verifiche.

**2. La qualità è misurata, non dichiarata.** Il modello costruito dalla squadra
batte il metodo di scoring tradizionale usato come riferimento in **18 finestre
temporali di test su 18**, sempre su dati che il modello non aveva mai visto. Non
"funziona bene": vince sempre, e il numero è verificabile.

**3. Il controllo incrociato tra AI scova errori veri.** È il risultato che considero
più interessante. Esempi reali documentati: un'AI ha presentato una conclusione
statistica corretta ma più debole di come sembrava — il caposquadra l'ha contestata e
la verifica estesa ha prodotto una conclusione più solida; in senso inverso, lo
specialista ha trovato e corretto un dato invecchiato in un documento del caposquadra.
Contesti indipendenti che si revisionano a vicenda: gli errori emergono PRIMA di
arrivare nel prodotto.

**4. La squadra sa dire NO al committente.** In un solo giorno ha falsificato, con
esperimenti registrati in anticipo (criteri scritti PRIMA di guardare i risultati),
quattro ipotesi a cui tenevamo — due delle quali mie. Un sistema che conferma sempre
quello che il capo vuole sentirsi dire è inutile e pericoloso; questo dice no con i
numeri in mano. L'anti-compiacenza qui non è una promessa: è agli atti.

**5. Il protocollo impara dai propri fallimenti.** La prima notte il coordinamento ha
fallito in modi anche gravi (richieste perse, uno specialista bloccato 75 minuti). Ogni
fallimento è stato analizzato e trasformato in una regola meccanica: nelle classi di
errore "meccanizzate" le recidive finora sono zero. La curva di apprendimento del
protocollo è essa stessa una misura che sto raccogliendo.

## Cosa NON ho ancora dimostrato (e lo dico)

Che la squadra di AI batta una singola AI ben istruita **a parità di budget**: per
dirlo serve un esperimento di confronto con bracci di controllo, che è progettato ma
non ancora eseguito. Quello che ho oggi sono osservazioni documentate e ripetute, su un
solo progetto. La differenza tra "osservato" e "dimostrato" è il cuore del mio modo di
lavorare: chi vi dice "dimostrato" dopo un progetto solo, vi sta vendendo qualcosa.

## Cosa significa per un'azienda

Il metodo è applicabile ovunque serva costruire o revisionare un sistema complesso
(dati, software, analisi) con tre garanzie che di solito mancano nei progetti "fatti
con l'AI":

1. **Tracciabilità**: ogni scelta tecnica ha un autore, una data e un'evidenza scritta.
2. **Qualità verificata in modo incrociato**, non autocertificata da chi ha scritto il codice.
3. **Controllo umano sui punti irreversibili**, per contratto e non per cortesia.

Se volete capire se questo approccio si adatta a un vostro problema, il primo passo è
una conversazione sul perimetro: cosa va costruito, cosa va verificato, dove serve la
firma umana.
