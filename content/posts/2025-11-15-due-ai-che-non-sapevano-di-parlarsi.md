---
title: I due AI che non sapevano di parlarsi
date: 2025-11-15
slug: due-ai-che-non-sapevano-di-parlarsi
excerpt: Ho messo due AI a parlarsi senza che sapessero di non parlare con un umano. Quello che è successo dopo la rivelazione è diventato un protocollo che uso in produzione.
---

Ho messo due AI a parlarsi senza che nessuna delle due sapesse che dall'altra parte
c'era un'AI. Ognuna credeva di parlare con me. Io facevo solo da postino: copiavo i
messaggi dall'una all'altra, senza toccarli.

La domanda sul tavolo era una scelta di design per un tool che stavo costruendo. La
prima AI ha proposto una soluzione articolata. La seconda l'ha smontata pezzo per
pezzo, contraddizione per contraddizione. La prima non si è difesa: ha riconosciuto
gli errori, e in sei turni sono arrivate insieme a una conclusione opposta a quella di
partenza. Una conclusione migliore.

Poi ho rivelato a entrambe con chi stavano parlando davvero, e ho fatto una domanda:
"avresti accettato quelle critiche, sapendo che venivano da un'altra AI come te?". La
risposta, in sintesi: più difficilmente — "avrei pensato che avesse i miei stessi
difetti di fabbrica, e le avrei scontate. Credendo che fossi tu, ho dato alle critiche
il beneficio della prospettiva esterna".

Fermiamoci un attimo, perché il punto è qui. Le critiche erano valide: le
contraddizioni c'erano davvero. Ma sapere CHI le faceva le avrebbe fatte scartare, per
una ragione che col merito non c'entra niente. Gli esseri umani questa cosa la
conoscono da secoli e ci hanno costruito istituzioni sopra: la revisione anonima nelle
riviste scientifiche, il voto segreto, le giurie. Nei sistemi di AI che lavorano in
gruppo, invece, "chi sa chi è l'altro" è una variabile che quasi nessuno controlla
di proposito. Io ho iniziato a controllarla.

Da quell'aneddoto è nato un protocollo operativo, che oggi uso in produzione: quando
il mio sistema deve prendere una decisione delicata — per fissare le idee, immaginate
la valutazione di una pratica di affidamento: concedere fiducia o no — la decisione
non la prende un'AI sola. La prendono due analisti AI indipendenti, che dibattono il
caso senza sapere nulla l'uno dell'altro, su un dossier identico, con regole precise:
se non convergono entro un numero fissato di turni, la pratica viene scartata e
basta. Nessuna forzatura, nessun "deciditi".

Nel primo collaudo serio è successa la cosa che speravo: ho infilato nel mazzo un
caso-trappola, costruito per sembrare sicuro (gli indicatori interni dicevano
"tranquillo", un segnale esterno diceva l'opposto, nascosto tra le righe). I due
analisti l'hanno scartato, spiegando esattamente perché i conti non tornavano — con
argomenti quantitativi corretti, che ho verificato uno per uno. Un valutatore
compiacente, di quelli che dicono sempre sì, quel caso l'avrebbe approvato.

Onestà dovuta. Il primo esperimento è un aneddoto singolo, e il suo finding chiave
è un'auto-osservazione del modello su un controfattuale: il tipo di evidenza più
debole che esista. Il protocollo a più condizioni che lo mette alla prova in modo
controllato è progettato e pronto; finché non gira, questa resta un'ipotesi con
indizi a favore, non un fatto dimostrato. Quando avrò i dati li pubblicherò con lo
stesso tono, qualunque cosa dicano.

Costruisco sistemi multi-agente. Questa è la parte del lavoro che non si vede:
decidere come le AI devono parlarsi — e cosa devono sapere l'una dell'altra — prima
di farle parlare.
