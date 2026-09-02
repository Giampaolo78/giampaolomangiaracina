---
title: Farsi trovare quando nessuno cerca più
date: 2026-08-21
slug: farsi-trovare-quando-nessuno-cerca-piu
excerpt: Chi chiede a un assistente AI non riceve dieci link, riceve tre nomi. Cosa decide quali, coi numeri degli studi che l'hanno misurato. E il passo successivo, che non è farsi citare ma farsi usare.
---

Chiedete a ChatGPT qual è il miglior software di fatturazione per una piccola impresa.
Non vi dà dieci link da aprire: vi dà una risposta, e fa tre nomi. Se la vostra
azienda è uno di quei tre, avete un cliente che non ha mai visitato il vostro sito. Se
non c'è, per quella persona non esistete — e non ve ne accorgete, perché non c'è
nessun clic da contare.

Questo lavoro ha un nome, GEO (Generative Engine Optimization): non si gareggia per un
elenco di link, si lavora per finire dentro la risposta. Ho passato le ultime
settimane sugli studi che l'hanno misurato. I numeri qui sotto sono loro, con la fonte.

## Cosa rende un contenuto citabile

Quando un modello cita una fonte se ne fa garante, quindi è conservativo: cita solo
ciò di cui si fida. Il paper che ha fondato il campo (Aggarwal et al., Princeton, KDD
2024, benchmark da 10.000 query) ha misurato cosa sposta quella fiducia: aggiungere
**statistiche** alza la visibilità nelle risposte del **40,6%**; virgolettati da fonti
autorevoli e citazioni esterne danno guadagni della stessa taglia. Una sola cosa la
abbassa: il riempimento di parole chiave che ha nutrito la SEO per vent'anni. Il
segnale non è il volume di parole, è la densità di prove.

E c'è un effetto che le aziende sottovalutano: i modelli premiano chi è già citato.
Uno studio su 275.000 riferimenti generati da GPT-4o (Algaba et al., NAACL 2025)
trova che oltre il 60% cade nell'1% delle fonti più citate — più del doppio di una
bibliografia umana. L'autorità si auto-rinforza: chi parte avanti, accelera.

## Non esiste «l'AI»

L'errore più comune è trattare l'AI come un bersaglio unico. Profound ha analizzato
680 milioni di citazioni: solo l'**11%** dei domini è citato sia da ChatGPT che da
Perplexity. Due superfici della stessa Google, AI Overviews e AI Mode, sulla stessa
domanda condividono il 13,7% degli URL. Search Atlas, su 5,5 milioni di risposte,
trova che il 35-40% delle domande produce insiemi di fonti completamente disgiunti
tra i tre motori principali.

Il motivo è strutturale. Perplexity cerca sul web a ogni domanda e premia la
freschezza. ChatGPT pesa l'autorevolezza storica e gli accordi di licenza con gli
editori. Claude si appoggia a Brave Search, non a Google: l'86,7% degli URL che cita
coincide con il ranking organico di Brave. «Comparire nell'AI» non è un obiettivo:
sono quattro obiettivi diversi.

## La citazione non è traffico

La SEO viveva di una metrica sola: il clic. Quella metrica si sta rompendo. Cloudflare
(agosto 2025) misura per il crawler di Claude un rapporto di **38.065 a 1** tra
contenuto ingerito e visite rimandate ai siti. Potete essere ovunque nelle risposte e
non vederlo su nessun cruscotto.

Secondo ribaltamento: Muck Rack stima che l'**85,5%** delle citazioni AI venga da
*earned media* — quello che dicono di voi gli altri, non il vostro sito. Reddit da
solo pesa il 40,1% delle citazioni fattuali nell'analisi Semrush su 150.000 citazioni
(il dato oscilla molto tra studi, dal 3% al 60%, ma il segno non cambia). Ottimizzare
solo le proprie pagine è curare la vetrina mentre la conversazione avviene altrove.

## Da citati a usati

Fin qui, contenuto. La frontiera è un'altra. Per un agente AI un'azienda può stare a
tre livelli: il modello vi conosce, il modello vi cita, il modello **vi usa**. Il
terzo è MCP, il protocollo aperto nato da Anthropic il 25 novembre 2024 e passato a
dicembre 2025 sotto la Linux Foundation con dentro OpenAI, Google e Microsoft:
esponete dati e azioni come uno strumento che l'agente interroga in tempo reale. In
sedici mesi: oltre 10.000 server pubblici, 97 milioni di download mensili degli SDK
(un indicatore di attività degli sviluppatori, non di installazioni uniche).

Non è teoria, per me: CityAdvisor.ai lo interrogo già così. È un server MCP con
venticinque strumenti — demografia, sicurezza, trasporti, confronto tra quartieri,
variazione nel tempo — e un agente li chiama dentro la conversazione, senza che
nessuno apra una pagina. E il commercio è già lì: Instant Checkout dentro ChatGPT
(OpenAI con Stripe, settembre 2025), Mastercard Agent Pay operativo da novembre 2025,
PayPal col primo server MCP ufficiale da aprile 2025.

## Il prerequisito

Esporre i dati a un agente non li rende corretti: li rende raggiungibili. Un prezzo
sbagliato, uno stock vecchio, un nome incoerente diventano più accessibili, non più
veri — e l'agente li serve con sicurezza. La condizione non è «essere presenti». È
avere dati di cui ci si può fidare senza ricontrollarli. Chi non espone un'interfaccia
per gli agenti non viene penalizzato: è irraggiungibile. È la versione 2026
dell'essere de-indicizzati.
