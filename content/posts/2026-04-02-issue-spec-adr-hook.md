---
title: Issue, spec, ADR, hook: le distinzioni che tengono in piedi un team che lavora con l'AI
date: 2026-04-02
slug: issue-spec-adr-hook
excerpt: Issue, spec, ADR, guardrail: cinque distinzioni banali da enunciare e costose da ignorare, che tengono in piedi un team che lavora con l'AI.
---

Quando un team inizia a lavorare sul serio con i coding agent, i problemi che
incontra non sono quasi mai di tecnologia. Sono di confini: cose diverse trattate
come se fossero la stessa cosa. Nel lavoro con i team ho distillato cinque
distinzioni — banali da enunciare, costose da ignorare — che da sole evitano la
maggior parte dei deragliamenti.

**1. L'issue è effimera, la spec è persistente.** L'issue nel tracker dice chi fa
cosa e a che punto è: nasce, si chiude, muore. La specifica dice come il sistema si
deve comportare: vive accanto al codice e si aggiorna a ogni cambiamento, per sempre.
Il deragliamento classico è scrivere il comportamento del sistema DENTRO l'issue: sei
mesi dopo, la verità sul sistema è sparpagliata in cinquanta ticket chiusi che
nessuno rileggerà. La regola: l'issue referenzia la spec, non la duplica. La casa
della spec è il repository.

**2. Le decisioni architetturali si superano, non si correggono.** Ogni decisione
rilevante — uno stack scelto, un pattern adottato, un trade-off accettato — merita un
documento di quattro sezioni: contesto, decisione, alternative considerate,
conseguenze. E quel documento è immutabile: se la decisione cambia, non si edita il
vecchio file — se ne scrive uno nuovo che cita e supera il precedente. Sembra
pignoleria; è memoria. Un team (e un agente) che può leggere PERCHÈ tre mesi fa si
è scelto A invece di B smette di riaprire le stesse discussioni e di rifare gli
stessi errori.

**3. La prosa consiglia, il guardrail vieta.** Scrivere "non toccare la
configurazione del linter" nel documento di contesto è un consiglio: l'agente
tendenzialmente lo segue, ma sotto pressione — o in una sessione lunga — può
scivolare. Il blocco meccanico che intercetta la modifica PRIMA che avvenga è un
divieto: non dipende dalla buona condotta di nessuno. La maturità di un setup
agentic si misura da quante regole critiche sono migrate dalla prima categoria alla
seconda. Tutto ciò che è davvero importante non si raccomanda: si rende impossibile.

**4. Si documenta il perché, non il come.** Il "come" l'agente lo sa fare, ed è la
parte che invecchia più in fretta: ogni dettaglio procedurale scritto oggi è un
candidato alla obsolescenza tra un mese. Il "perché" — i vincoli, le ragioni delle
scelte, cosa NON fare e per quale motivo — è ciò che guida l'agente quando incontra
un caso che nessuno aveva previsto. Corollario che sorprende sempre: i piani di
lavoro generati dall'AI non si archiviano. Sono materiale fluido, utile mentre serve;
le decisioni stabili che ne escono vivono nei documenti di architettura, il resto si
lascia andare. Archiviare tutto è la versione digitale di non buttare mai niente.

**5. Non tutto ciò che ricorre merita di diventare procedura.** La tentazione, una
volta scoperte le procedure codificate per l'agente, è codificare ogni cosa. Il
filtro che uso è a tre condizioni, tutte necessarie: ricorre almeno due-tre volte al
mese, ha un flusso definibile a priori, e il valore supera la fatica di scriverla e
mantenerla. Se ne manca una, meglio il prompt estemporaneo: una procedura scritta
male è debito tecnico travestito da automazione.

Nessuna di queste distinzioni è un'invenzione: issue tracking, decision record,
guardrail deterministici e documentazione del rationale esistono da decenni
nell'ingegneria del software. Quello che cambia con gli agenti è il costo di
ignorarle: un collega umano compensa l'ambiguità con il contesto che ha in testa;
l'agente no — amplifica la qualità di ciò che trova scritto, nel bene e nel male.
Il disordine documentale che prima rallentava, adesso si esegue.

Accompagno team di sviluppo in questo passaggio. Si parte sempre da qui: non dal
modello più potente, ma dai confini più chiari.
