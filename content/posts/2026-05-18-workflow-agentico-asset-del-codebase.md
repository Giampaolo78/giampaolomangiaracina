---
title: Il workflow agentico di un team non è un tool: è un asset del codebase
date: 2026-05-18
slug: workflow-agentico-asset-del-codebase
excerpt: Il salto di maturità non è imparare a usare l'agente: è trattare il contesto che gli dai come un asset del codebase — versionato, revisionato, misurato.
---

La domanda che mi ha fatto un developer di un team che accompagno è la più utile
che si possa fare: "il modo in cui usiamo i coding agent è in linea con quello che
fanno le software house serie, o ci stiamo raccontando una storia?". La risposta
lunga è diventata un percorso di lavoro. La risposta corta sta in una frase: il
salto di maturità non è "imparare a usare l'agente" — è trattare il **contesto che
dai all'agente come un asset del codebase**: versionato, revisionato, misurato, come
qualunque altro artefatto di ingegneria.

Un coding agent senza contesto è un consulente brillante al primo giorno: ogni
sessione riparte da zero, riscopre le convenzioni, rifà le stesse domande, ripete
gli stessi errori. La differenza tra un team che "usa l'AI" e un team che lavora in
modo agentico sta tutta in cosa trova l'agente quando apre il repository. Nei team
che seguo questo contesto è strutturato in **quattro documenti**, dal più stabile
al più vivo — e la separazione non è burocrazia: ogni documento risponde a una
domanda diversa e cambia a una velocità diversa.

**1. La costituzione — quali regole non si negoziano MAI.** Stack ammesso e vietato,
sicurezza (mai segreti nel repo), zone intoccabili del codice, regole di
configurazione che nessuno — umano o agente — può modificare per "far passare" un
controllo. Cambia raramente, è il DNA del progetto, e vale per QUALUNQUE agente,
anche quelli che adotterete tra due anni.

**2. L'entry point operativo — come si lavora qui, oggi.** Un file alla radice del
repository, sotto le 300 righe (oltre quella soglia, misurata sul campo, l'agente
inizia a ignorare pezzi): comandi essenziali, convenzioni, link agli altri documenti.
Cambia spesso, ed è giusto così: i principi sono stabili, l'operativo no. La
separazione tra 1 e 2 esiste esattamente per questo.

**3. Un solo entry point, molti nomi.** Agenti diversi cercano file di ingresso
diversi. La tentazione è duplicare il contenuto per ciascuno; il risultato, nel
giro di un mese, è garantito: due versioni che dicono cose diverse. La regola è
una sola fonte di verità — un solo file fisico, gli altri nomi sono alias che
puntano lì.

**4. La mappa del codebase — i topic che l'entry point può solo linkare.** Quando il
progetto ha più di un confine architetturale, o regole trasversali che ricorrono in
più punti (testing, sicurezza, deployment), quel contesto non può stare nelle 300
righe: vive in una documentazione strutturata per topic, con un formato fisso, che
l'entry point cita per riferimento. E con una regola di igiene precisa: il drift —
la mappa che non corrisponde più al codice — si tratta come un bug, non come una
seccatura.

Sopra questa base sta il framework che dà il nome al pattern: Spec-Driven
Development — prima si scrive cosa il sistema deve fare, poi l'agente lo costruisce
contro quella specifica. Sul nuovo si applica in modo rigido; sull'esistente con
pragmatismo, caso per caso. Ma il punto da portare a casa è un altro: **SDD è un
framework, non uno strumento**. Gli strumenti — quello di oggi, quello di
quest'anno, quello che lo sostituirà — passeranno tutti. La struttura del contesto
resta, e si porta dietro il suo valore da un agente all'altro.

Da dove si comincia, in pratica? Tre passi, uno per settimana: una pagina di contesto
operativo per il repository più attivo; il task ricorrente più noioso convertito in
una procedura che l'agente esegue da solo; un guardrail deterministico sul file che
nessuno deve toccare. Piccoli, misurabili, e dopo il terzo il team non torna più
indietro.

Accompagno team di sviluppo in questo passaggio. La parte difficile non è la
tecnologia: è convincersi che il contesto va ingegnerizzato come il codice. Dopo,
tutto il resto è in discesa.
