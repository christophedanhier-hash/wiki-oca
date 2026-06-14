# 📊 Analyse comparative : Hermes vs Cowork

> **Date :** 12 juin 2026
> **Objet :** Comparaison des deux productions documentaires du T600

Deux approches d'IA ont été utilisées pour analyser les documents sources du T600 et produire une documentation technique complète. Cette page compare leurs résultats.

---

## 1. Périmètre

| Source | Version | Date | Relecture Jean-Paul |
|--------|:-------:|:----:|:-------------------:|
| **Hermes** (Bureau Gérard + LEO) | Doc technique v1.0 / Formation v1.0 | 12 juin 2026 | ❌ Non |
| **Cowork** (Microsoft Copilot) | Doc technique v1.2 / Formation v1.1 | 29 mai 2026 | ✅ 11 corrections intégrées |

---

## 2. ✅ Similitudes (convergences)

Les deux analyses arrivent aux mêmes conclusions sur les points suivants :

| Domaine | Détail |
|---------|--------|
| 🏗️ **Architecture IPX800** | .236 (carte Wi-Fi cimiers), .237 (carte alim IPX), .238 (IPX800 principal) |
| 🔌 **Procédures** | Démarrage en 8 étapes, extinction en 4 niveaux |
| 💻 **Logiciel** | NINA 3.0, LesveDomeNet, AnyDesk, Foscam FI9831P-T600 |
| 🗺️ **Réseau** | Switch WiFi dôme, SSID wireless2.4G_A84620 |
| 🔧 **Cartes moteur** | Alcyone-5 (shield Arduino), MAIA-4 (driver TB67H303HG), ELECTRA-5 (carte mère) |
| 🔗 **Cimiers** | NRF24L01, batterie, ACS712 30A, détecteur de pluie |
| 🛡️ **Lacunes communes** | BOM mécanique absente, autoguideur non documenté, pas de schémas câblage complets |

---

## 3. ❌ Différences

### 3.1 Erreurs dans Hermes à corriger

| # | Sujet | Hermes (erroné) | Cowork (correct) | Impact |
|:-:|-------|:---------------:|:----------------:|:------:|
| **D1** | 🔢 Sous-réseau IPX800 | `192.168.1.236/.237/.238` | **`192.168.0.236/.237/.238`** | 🔴 Opérateur se connecte à des IP mortes |
| **D2** | 🔄 Ordre extinction Niveau 2 | Relais direct après Mécanique | **Arrêt info (T600-NUC-TELE) avant Relais** | 🔴 Risque corruption fichiers acquisition |
| **D3** | 🌡️ Sonde température NUC | Non documentée | `192.168.0.234` | 🟡 Surveillance température boîtier pilier manquante |
| **D4** | 🕹️ Pilotage manuel cimiers | Non documenté | Interrupteurs physiques de secours | 🟡 Procédure de secours absente |

### 3.2 Contenu présent dans Cowork mais absent d'Hermes

| # | Élément | Valeur ajoutée |
|:-:|---------|----------------|
| **M1** | Brochage ST-4 détaillé (6 broches, couleurs) | Référence câblage autoguidage précise |
| **M2** | Code firmware ISR fins de course | Détection/arrêt par interruption matérielle |
| **M3** | Code pulse guide autoguidage | Protocole de communication NINA→monture |
| **M4** | Analyse risques avec coûts (~1 425€) | Budget concret pour traiter R1+R2+R3 |
| **M5** | Annexe formateur + pièges classiques | Pédagogie transmission savoir-faire |
| **M6** | QCM évaluation (10 questions + corrigé) | Validation des acquis mesurable |
| **M7** | Objectifs SMART formation | Cadre pédagogique professionnel |
| **M8** | Paramètres LesveDomeNet détaillés | Dome diameter, Park, Home, Watchdog 30s/3° |
| **M9** | Diagnostic télémétrique cimiers (4 axes) | Énergie/Data/Commutation/Environnement |
| **M10** | Sémantique Output/Input IPX800 | Concept fondamental expliqué clairement |
| **M11** | Cinématique cimiers SYS:IP .236 | Commande type pour pilotage |
| **M12** | Note de service à JP Dumoulin | Trace formelle de validation auteur |
| **M13** | Synthèse changements v1.1→v1.2 | Contexte d'évolution documentaire |

### 3.3 Contenu présent dans Hermes mais absent de Cowork

| # | Élément | Valeur ajoutée |
|:-:|---------|----------------|
| **H1** | Analyse astro-optique complète (303 lignes) | Focale, monture, backfocus, collimation |
| **H2** | Recommandations P1/P2/P3 avec dépendances | Feuille de route actions prioritaires |
| **H3** | Analyse firmware (6 plateformes, 15 lacunes) | Panorama complet de l'embarqué |
| **H4** | Analyse hardware (33 composants) | Inventaire matériel systématique |
| **H5** | Tableau traçabilité assertion→source | Fiabilité par assertion (✅/⚠/❌) |
| **H6** | Maintenance calendaire (H/M/T/A) | Plan de maintenance structuré |
| **H7** | Points de vigilance permanents | Risques → actions correctives |
| **H8** | Graphe dépendances entre actions | Ordonnancement des correctifs |
| **H9** | Évaluation état du système par sous-système | Vue d'ensemble du niveau de maturité |
| **H10** | Glossaire complet (sigles cimiers, encodeur) | Référence terminologique |
| **H11** | Rapport de croisement (18 convergences) | Validation croisée des analyses |
| **H12** | Fiches sources ethnographe structurées (5 fiches) | Données sources exploitables |

---

## 4. Lacunes communes

Les deux approches s'accordent sur ces lacunes critiques :

| Lacune | Priorité | Commentaire |
|--------|:--------:|-------------|
| BOM mécanique (câbles, calibres) | 🔴 Haute | Données non présentes dans les sources |
| Capteurs fin de course AD/DEC | 🔴 Critique | Risque collision destructrice |
| Autoguideur | 🔴 Haute | Pas d'imagerie longue pose possible |
| Schémas de câblage complets | 🟡 Haute | Maintenance complexe sans |
| Firmware sources (Arduino, ESP) | 🔴 Critique | Binaires seuls, pas de code source |
| Mise en station (polar alignment) | 🟡 Haute | Procédure fondamentale absente |
| Parafoudre Type 2 | 🔴 Critique | Risque destruction électronique par foudre |

---

## 5. Forces de chaque approche

### Hermes (Bureau Gérard + LEO)

| Force | Pourquoi c'est utile |
|-------|---------------------|
| **Analyse multi-spécialistes** | 6 agents spécialisés (astro-optique, hardware, firmware, ethnographe, rédacteur, formateur) |
| **Traçabilité rigoureuse** | Chaque assertion remonte à une source (✅/⚠/❌) |
| **Analyse technique poussée** | Optique, firmware, hardware traités en profondeur |
| **Cycle documentaire complet** | Extraction → validation → croisement → assemblage |
| **Automatisation possible** | Skills réutilisables pour tout projet technique |

### Cowork (Microsoft Copilot)

| Force | Pourquoi c'est utile |
|-------|---------------------|
| **Analyse des risques chiffrée** | Budget, coûts, priorisation concrète |
| **Erreurs détectées** | IP sous-réseau, ordre extinction, sonde manquante |
| **Détail opérationnel** | Brochage ST-4, code ISR, paramètres LesveDomeNet |
| **Pédagogie structurée** | Objectifs SMART, QCM, annexe formateur |
| **Validation terrain** | Relecture Jean-Paul avec 11 corrections intégrées |

---

## 6. Plan d'incorporation

Les forces de Cowork seront intégrées dans la prochaine version de la documentation Hermes :

| Action | Priorité |
|--------|:--------:|
| 🔴 Corriger `192.168.1.x` → `192.168.0.x` partout | Immédiate |
| 🔴 Réordonnancer extinction : Méca → **Info** → Relais → Énergie | Immédiate |
| 🟡 Ajouter sonde température `192.168.0.234` | Haute |
| 🟡 Ajouter pilotage manuel cimiers (interrupteurs) | Haute |
| 🟡 Ajouter brochure ST-4, code ISR, pulse guide | Moyenne |
| 🟡 Ajouter analyse risques avec coûts | Moyenne |
| 🟡 Ajouter QCM + objectifs SMART + annexe formateur | Moyenne |

---

*Analyse comparative produite par le Bureau Gérard — 12 juin 2026*
