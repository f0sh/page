---
title: "Website relaunched"
description: "Nach einer ganzen Weile habe ich mich entschieden meine Seite mit aktuellen Technologien neuzubauen."
date: 2023-07-26
draft: false
toc: false
image: images/hugo.jpg
slug: website-relaunched
categories:
    - tech
---

Meine alte Webseite ist aus Sommer 2013 und feiert dieses Jahr 10 jähriges Jubiläum. Damals gab es Google+ noch 😂 und jquery war ganz neu, das ich damals ausprobiert habe. Da die Seite zuerst statisch war, ich aber gerne einige Beiträge dynamisch erzeugen wollte, habe ich im Backend Dokuwiki verwendet. Die gerenderten HTML Seiten wurden dann in die Site injected. Im Hintergrund lief PHP für Dokuwiki, Kontaktformular und einige Scripte. Ich denke aber es war nun an der Zeit einige Dinge hier umzukrempeln.

## Neuer Techstack

Zeiten ändern sich. Wordpress ist fast überall der de-facto Standard und Website-Generatoren wie Wix machen es auch Nicht-Techies leicht, Websites zu erstellen. Der Betrieb dynamischer Content Management Systeme ist jedoch fehleranfällig und bietet Angreifern eine Fläche. Wenn man nicht viel Zeit für die Pflege einer Website hat, sind statische Websites sinnvoll, da sie weniger Zeit für die Pflege benötigen und eben keine große Angriffsläche bieten. Da ich in letzter Zeit auch ein bisschen mit der Programmiersprache Go herumspiele, wollte ich Hugo mal ausprobieren, um zu sehen, wie gut der Workflow mit Github Actions in der Praxis funktioniert.

Mein Techstack ist daher sehr einfach:

- Hosting: Github Pages, Github Actions für Workflow 
- Static Site Generator: Hugo
- Theme: hugo-theme-stack