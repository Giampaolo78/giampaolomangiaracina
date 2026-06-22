---
title: Ho reso open-source il sistema con cui le mie AI lavorano come una squadra
date: 2026-06-22
slug: claude-code-dialogue
excerpt: Una squadra di AI persistenti che si coordinano scrivendosi, con tracciabilità totale e l'umano al comando. Il sistema che lo rende possibile gira interamente sulla tua macchina, e da oggi è open-source.
---

Da mesi scrivo di una squadra di AI che lavora in parallelo: non una sola intelligenza, ma più AI
persistenti — ognuna con un nome e un dominio di cui risponde — che si coordinano **scrivendosi
tra loro**, mentre io resto al comando. Oggi rendo open-source il sistema che lo rende possibile:

**[claude-code-dialogue](https://github.com/Giampaolo78/claude-code-dialogue)** — licenza MIT.

## Cos'è

Il coordinamento di una squadra di istanze di Claude Code che lavorano insieme sullo stesso
progetto. Le AI si parlano su bacheche condivise dove ogni richiesta, risposta e consegna resta
agli atti: di qualunque decisione si può ricostruire chi l'ha presa, quando e su quale evidenza.
È la tracciabilità che ai progetti fatti con l'AI di solito manca.

Gira interamente sulla tua macchina: i messaggi sono file sul tuo disco, niente server, niente
database, niente account. I tuoi dati restano dove sono.

## Come si installa

Cloni il repo e dici al tuo Claude Code di leggere `SETUP.md` e installarlo: fa lui i passaggi —
crea l'ambiente, aggancia il progetto, conferma. In alternativa c'è `install.sh`, a mano. La
dipendenza esterna è una sola; il resto è libreria standard di Python.

## Perché lo apro

Una squadra di AI persistente e tracciabile, che orchestri tu e con la firma umana sulle
decisioni che contano, non ha motivo di restare chiusa dentro il mio progetto. Apro le fondamenta
perché chi vuole possa costruirci sopra.

## Dove sta andando

Oggi la squadra vive su una macchina. Il passo successivo è farla lavorare tra macchine e persone
diverse: il mio agente che parla col tuo, ciascuno coi dati del proprio umano, senza fondere i
due lati. È la parte su cui sto lavorando; questo che apro oggi è la base da cui parte.

Lo mantengo insieme ad [addictive.dev](https://github.com/addictivedev). È MIT: prendetelo e
costruiteci sopra.
