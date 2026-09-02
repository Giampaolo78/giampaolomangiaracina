---
title: Funzionava nel pilota, crolla in produzione. Il collo di bottiglia è il retrieval, non il modello
date: 2026-07-14
slug: il-collo-di-bottiglia-e-il-retrieval
excerpt: Un sistema che risponde sui documenti aziendali quasi mai sbaglia perché il modello è scarso. Sbaglia perché ha risposto bene al contesto sbagliato. Un conto che mostra dove sta la leva, e la metrica che manca in quasi tutti i progetti.
---

Un sistema che risponde a domande sui documenti aziendali (RAG: prima recupera i
passaggi pertinenti, poi il modello scrive la risposta a partire da quelli) funziona
nel pilota e crolla in produzione. Quasi sempre non è il modello: ha risposto bene, a
partire dal contesto sbagliato.

## Perché il pilota mente

Uso un caso costruito apposta, equivalente a quelli che incontro. Un'azienda di servizi
vuole interrogare i suoi documenti interni: contratti, verbali, report mensili. Il
pilota gira su 300 documenti scelti da chi lo costruisce. Con un corpus così piccolo,
il passaggio giusto entra tra i primi cinque candidati quasi per inerzia: c'è poco con
cui confonderlo. Il recupero sembra perfetto, le risposte sono brillanti, il pilota
viene approvato.

Poi si porta lo stesso sistema su 40.000 documenti disordinati. E la ricerca per
similarità comincia a pescare paragrafi vicini per vocabolario ma estranei alla
domanda. Chiedi «qual è il trend del margine sulla linea X» e torna il paragrafo più
denso di lessico finanziario — non quello che contiene la risposta. La similarità tra
vettori misura la prossimità semantica, non la rilevanza rispetto alla domanda di
business. Sono due cose diverse, e nel pilota la differenza non si vede.

## Il conto che mostra dove sta la leva

Chiamo *recall del recupero* la frequenza con cui il passaggio giusto entra tra i
candidati che il modello vede. Supponiamo che sia il 70%, e che il modello — quando ha
il contesto giusto — risponda bene il 95% delle volte.

- Accuratezza del sistema: 0,70 × 0,95 = **66%**.
- Cambio modello, passo al 99%: 0,70 × 0,99 = **69%**. Tre punti, per un modello che
  costa il doppio.
- Tengo il modello, porto il recall al 90%: 0,90 × 0,95 = **86%**. Venti punti.

Il tetto del sistema è il recall del recupero. Un modello più capace o embedding più
grandi non recuperano un passaggio che tra i candidati non è mai entrato. Eppure
quando il sistema sbaglia la prima reazione è cambiare modello — perché l'errore
*sembra* un'allucinazione, e invece è un recupero fallito.

## La metrica che manca

Il recall del recupero va misurato a parte, prima della generazione. Il metodo che uso
è banale e quasi nessuno lo applica: un insieme di riferimento di 100 domande vere,
ognuna con il passaggio che la risolve indicato a mano da chi conosce i documenti. Per
ogni domanda: il passaggio giusto è tra i primi k candidati, sì o no? Il numero che
esce è il tetto del sistema. Senza questa misura ogni errore viene attribuito al
modello, e si ottimizza lo strato sbagliato per mesi.

Il campione di 100 va costruito prima di scegliere l'architettura, e riaperto ogni
volta che cambia il corpus: 40.000 documenti oggi sono 55.000 tra un anno, e il recall
che era 90% non resta 90% da solo.

## Cosa alza il recall

Non la generazione. Il recupero ibrido: ricerca per parole chiave accanto a quella per
similarità (le sigle, i codici prodotto, i nomi propri la similarità li perde), filtri
sui metadati (data, reparto, tipo di documento) che restringono il campo prima ancora
di cercare, e la struttura del documento — un paragrafo con il suo titolo di sezione
dice più di un paragrafo nudo.

Non è rifinitura. È la differenza tra un sistema che indovina e uno che recupera. E la
domanda da fare a chi vi presenta un pilota che «funziona» è una sola: su quanti
documenti, e qual è il recall del recupero misurato a parte.
