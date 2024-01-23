---
title: "Website relaunched"
description: "After quite a while I decided to refactor my website by using new technologies."
date: 2023-07-26
draft: false
toc: false
image: images/hugo.jpg
slug: website-relaunched
categories:
    - tech
---

My old website is from summer 2013 and celebrates its 10th anniversary this year. At that time, jquery was brand new and I tried it out. Since the site was static at first, but I wanted to create some posts dynamically, I used Dokuwiki in the backend. The rendered HTML pages were then injected into the site. PHP was running in the background for Dokuwiki, contact form and some scripts. But I think it was time to change some things here.

## New Techstack

Times have changed. Wordpress is the de-facto standard everywhere and site-generators like Wix make it easy to create websites for non-techies. However running dynamic Content Management Systems is error prone and offers an attack surface. Therefore, if you don't have much time to maintain a website, static sites make sense, as they offer rather less time to maintain. As I am playing around with Go lately, I wanted to give Hugo a try to see, how well the workflow with Github Actions runs in practise. 

My techstack therefore is pretty simple:

 - Hosting: Github Pages, Github Actions for Workflow
 - Static Site Generator: Hugo
 - Theme: hugo-theme-stack