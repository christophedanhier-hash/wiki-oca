# 🤖 Analyse Cowork (Microsoft Copilot)

> **Source :** Microsoft Copilot (Cowork) — Analyse des documents sources T600 de l'Observatoire Centre Ardenne
> **Pilote :** Christophe Danhier
> **Date :** Mai 2026

Cette section présente le travail d'analyse produit par **Microsoft Copilot** sur les documents sources du T600 (schémas, notes, procédures de Christian Wanlin et Jean-Paul Dumoulin).

---

## 📋 Documents produits

| Document | Description | Taille | Lien |
|----------|-------------|:------:|:----:|
| **Rapport d'Analyse T600 — Phase 01** | Analyse intégrée multi-agents : architecture système, sous-systèmes (Mega 2560, Nano/Uno, ESP8266, SkyPikit, RF24), protocoles, incohérences documentaires, glossaire, chronologie, plan d'action | 804 lignes | [Drive](https://drive.google.com/file/d/1R3mILbQozql28b2XHHhfe6nAaLel0u3w/view) |
| **Rapport d'Analyse des Risques — T600** | 3 risques critiques identifiés (fin de course, autoguideur, parafoudre) avec analyse complète (P×I), coûts de résolution (~1 425€) et priorités | 854 lignes | [Drive](https://drive.google.com/file/d/1o4iGobLAWGTTBx835uHHXQWDXFvHr3eG/view) |
| **Document de Référence T600** | Manuel technique consolidé : architecture, sécurité, démarrage (8 étapes), utilisation, arrêt (4 niveaux), maintenance, dépannage, annexes | 1 129 lignes | [Drive](https://drive.google.com/file/d/1IitbCRybI5_Nqat2KgGhP_ydNVnk-fEG/view) |

---

## 🔍 Points forts de l'analyse Cowork

### 1. Analyse des Risques avec Coûts

L'analyse Cowork a identifié **3 risques critiques** avec chiffrage :

| # | Risque | Criticité | Coût solution |
|:-:|--------|:---------:|:-------------:|
| **R1** | Absence capteurs fin de course AD/DEC | 🔴 25/25 — Critique | ~125 € |
| **R2** | Autoguideur non documenté | 🟡 12/25 — Élevé | ~500 € |
| **R3** | Absence parafoudre type 2 | 🔴 20/25 — Critique | ~800 € |
| | **Total investissement recommandé** | | **~1 425 €** |

### 2. Corrections réseau critiques

Détection d'**adresses IP erronées** dans la documentation Hermes (sous-réseau `192.168.1.x` au lieu de `192.168.0.x`), permettant la correction avant mise en production des documents.

### 3. Détails techniques précis

- Brochage ST-6 détaillé avec couleurs
- Code firmware ISR pour fins de course
- Protocole pulse guide pour l'autoguidage
- Paramètres LesveDomeNet exhaustifs
- Sémantique Output/Input IPX800 expliquée

### 4. Pédagogie et formation

- Objectifs SMART
- QCM 10 questions avec corrigé
- Annexe formateur avec pièges classiques
- Note de service de validation auteur

---

## 📊 Comparaison avec l'analyse Hermes (Bureau Gérard)

Voir la page **[Analyse comparative Hermes vs Cowork](comparative.md)** pour le détail complet des similitudes, différences et forces de chaque approche.

---

*Documents sources disponibles sur le Google Drive OCA — dossier `08 - Espace OCA/Bkp`*
