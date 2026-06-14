# Documentation Technique — Telescope T600 OCA

!!! warning "Corrections appliquées (source : Analyse comparative Cowork)"
    Les corrections suivantes ont été intégrées suite à l'analyse comparative Hermes vs Cowork (juin 2026) :

    - **🔴 D1** — Sous-réseau IPX800 : `192.168.**0**.236/.237/.238` (et non 192.168.1.x)
    - **🔴 D2** — Ordre extinction Niveau 2 : Arrêt info avant coupure des relais
    - **🟡 D3** — Sonde température NUC ajoutée : `192.168.0.234`
    - **🟡 D4** — Pilotage manuel cimiers (interrupteurs de secours) documenté

    Voir [l'analyse comparative](cowork/comparative.md) pour le détail complet.

## Métadonnées

| Champ | Valeur |
|-------|--------|
| **Version** | 1.1 |
| **Date** | 12 juin 2026 |
| **Rédacteur** | Rédacteur Technique (Bureau Gérard) |
| **Audience** | Opérateurs, techniciens de maintenance, ingénieurs système |
| **Sources** | Fiches ethnographe (1–6b), Analyse Astro-Optique, Analyse Hardware, Analyse Firmware, Rapport de Croisement |
| **Statut** | Document initial — nombreuses sections marquées [LACUNE] nécessitant complément terrain |

---

## 1. Présentation / Contexte

### 1.1 Identifiant du système

Le **T600** est un télescope astronomique installé à **l'Observatoire Centre Ardennes (OCA)**, d'une ouverture de **600 mm** monté en configuration équatoriale allemande (GEM). Il est intégré dans un dôme motorisé de 4500 mm de diamètre avec coupole rotative et système de volets (cimiers) automatisé.

Le système a été conçu et réalisé par **Christian Wanlin** et **Jean-Paul Dumoulin**, combinant :
- Une **domotisation complète** basée sur l'automate IPX800
- Une **électronique de pilotage** par cartes Pléiades (Alcyone-5, Electra-5, Maia-4)
- Un **réseau WiFi/Ethernet** avec supervision à distance (AnyDesk, caméra Foscam)
- Des **microcontrôleurs Arduino** pour les communications radio (NRF24L01) des cimiers
- Un **watchdog environnemental** (Wemos D1 Mini + DS18B20)

### 1.2 État du système

| Aspect | Évaluation |
|--------|-----------|
| 🏗️ **Infrastructure électrique/réseau** | ✅ Bien documentée et fonctionnelle |
| 🔭 **Noyau astronomique** | ❌ Quasi-absent des sources |
| 🔌 **Procédures démarrage/extinction** | ✅ Bien documentées |
| 🛡️ **Sécurité** | ⚠️ Lacunes critiques identifiées (fin de course, parafoudre) |

> **Note importante :** L'infrastructure domotique est fonctionnelle, mais les spécifications optiques et les procédures astronomiques fondamentales (mise en station, alignement, collimation, autoguidage) ne sont **pas documentées** dans les sources disponibles. [LACUNE CRITIQUE]

---

## 2. Architecture système

### 2.1 Schéma blocs textuel — Vue d'ensemble

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            RÉSEAU GLOBAL T600                                    │
│  SSID: wireless2.4G_A84620 — Switch wifi dôme [A CONFIRMER : modèle switch]      │
│   ├── 192.168.0.236  → Commande cimiers (wifi)                                   │
│   ├── 192.168.0.237  → IPX800 Alimentation (ON/OFF)                              │
│   ├── 192.168.0.238  → IPX800 Relais E/S (Login: Admin / Oc@2018)                │
│   ├── 192.168.4.201  → Énergie & Environnement (Wemos D1 Mini + DS18B20)         │
│   ├── T600-NUC-TELE  → PC pilotage télescope (AnyDesk: 1 041 426 244)            │
│   └── T600-NUC       → PC 1er étage, alimente IPX800 (AnyDesk: 513 471 809)      │
└──────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────┐
│                          ALIMENTATION & DISTRIBUTION D'ÉNERGIE                   │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                   │
│  [Réseau EDF] ──► Variateur de fréquence (f=24.0 Hz) [A CONFIRMER : marque]      │
│                       └──► Moteur réducteur rotation dôme [A CONFIRMER : modèle]  │
│                                                                                   │
│  [Pilier 20V] ──► Sortie IPX800 #2                                                │
│      ├──► Alimentation Télescope 12V                                              │
│      └──► Alcyone-5 [12V-24V → régule 12V(drivers) + 9V(Arduino Uno)]            │
│               └──► Electra-5 [régule 5V + 3.3V]                                   │
│                       └──► Maia-4 [TB67H303HC, max 24V, 2.7A]                     │
│                                                                                   │
│  [PC T600-NUC 1er étage] ──► Alimentation IPX800 (Sortie #3)                      │
│                                                                                   │
│  [Batterie cimiers] ──► toujours en charge [A CONFIRMER : chimie, tension, Ah]   │
│      └──► Arduino Mega + NRF24L01 + Relais moteurs cimiers                       │
│                                                                                   │
│  [Watchdog] Wemos D1 Mini (ESP8266) + DS18B20                                     │
│      └──► Surveillance température dôme + supervision watchdog                    │
│                                                                                   │
└──────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────┐
│                             AUTOMATE CENTRAL — IPX800                            │
├──────────────────────────────────────────────────────────────────────────────────┤
│  8 sorties relais, entrées analogiques et digitales                               │
│  Version : non spécifiée (V4 ou V5 probable) [A CONFIRMER]                        │
│                                                                                   │
│  Sortie #1 : Rotation Coupole                                                      │
│  Sortie #2 : Pilier 20V & Télescope 12V                                           │
│  Sortie #3 : PC NUC T600                                                           │
│  Sortie #4 : Fermeture Cimiers                                                     │
│  Sortie #5 : Fermeture Cimiers URGENCE                                             │
│  Sortie #6 : Ouverture Cimiers                                                     │
│  Sortie #7 : Non documentée [LACUNE]                                               │
│  Sortie #8 : Non documentée [LACUNE]                                               │
│                                                                                   │
│  Commande ON/OFF globale : 192.168.0.237                                           │
│  Commande relais E/S     : 192.168.0.238                                           │
│  Relais d'alimentation   : Relais Keyes_SRly                                      │
└──────────────────────────────────────────────────────────────────────────────────┘

> **Sémantique IPX800 Output / Input :**  
> - **Output** = ORDRE envoyé par l'IPX800 (« mets sous tension »)  
> - **Input** = MESURE constatée (« la tension est bien présente en aval »)  
> - Output ON + Input ON = ligne saine  
> - Output ON + Input OFF = défaut aval (fusible, câble, contacteur) → STOP + diagnostic  

┌──────────────────────────────────────────────────────────────────────────────────┐
│                      CHAÎNE CIMIERS (Volets du dôme)                              │
├──────────────────────┬───────────────────────────────────────────────────────────┤
│  PARTIE FIXE          │ ÉMETTEUR                                                   │
│                       │ IPX800 ──► Relais Keyes ──► Arduino Uno                    │
│                       │                           └──► NRF24L01 TX                 │
│                       │                                                           │
│  PARTIE TOURNANTE     │ RÉCEPTEUR (sur batterie cimiers)                          │
│                       │ Arduino Mega + NRF24L01 RX                                 │
│                       │     ├──► Relais moteurs → Moteurs cimiers (x2…4?)         │
│                       │     ├──► Capteur ACS712 (mesure courant moteur) [CALIBRE ?]│
│                       │     ├──► Capteurs fin de course (GH, GB, DY, DB)           │
│                       │     ├──► Limiteur de courant [A CONFIRMER : type]          │
│                       │     └──► Détecteur de pluie [A CONFIRMER : type]           │
└───────────────────────┴───────────────────────────────────────────────────────────┘

> **Pilotage manuel des cimiers :** Les interrupteurs physiques à côté du boîtier permettent l'ouverture et la fermeture manuelle en secours du pilotage Wi-Fi.

┌──────────────────────────────────────────────────────────────────────────────────┐
│                     CHAÎNE ROTATION DÔME                                          │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                   │
│  PC T600-NUC-TELE                                                                 │
│   └──► USB ──► Interface Velleman PVM110N (timer interval: 60ms)                  │
│                  └──► Variateur de fréquence (f=24.0 Hz) [A CONFIRMER : modèle]   │
│                          └──► Moteur réducteur + Switch Home [A CONFIRMER : type] │
│                                                                                   │
│  RETOUR POSITION :                                                                 │
│   Encodeur Gray Code (Grayhill 654321) — roue 241mm, 16 trous                     │
│       └──► LesveDomeNet (lecture encodeur)                                        │
│       └──► Switch Home (position zéro = 310) [A CONFIRMER : unité]               │
│                                                                                   │
└──────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────┐
│                    CHAÎNE TÉLESCOPE / MONTURE (GEM)                               │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                   │
│  PC T600-NUC-TELE ──► ASCOM/NINA                                                  │
│   └──► Carte Pléiades : Alcyone-5 (Shield, alim principale)                       │
│           └──► Electra-5 (Motherboard, régul 5V/3.3V, port ST-4)                  │
│                   └──► Maia-4 (Driver TB67H303HC, encodeur quadrature)             │
│                            └──► Moteurs pas-à-pas axes AD/DEC                     │
│                                                                                   │
│  ÉLÉMENTS MANQUANTS CONFIRMÉS :                                                    │
│   ❌ Capteurs fin de course AD/DEC — absents                                      │
│   ❌ Autoguideur — non documenté ([LACUNE CRITIQUE])                              │
│                                                                                   │
└──────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────┐
│                       SUPERVISION & SÉCURITÉ                                      │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                   │
│  [Visuelle]   Caméra Foscam FI9831P-T600 (latence < 1s, Ethernet filaire)         │
│  [Distante]   AnyDesk sur les 2 PC NUC                                            │
│  [Watchdog]   Wemos D1 Mini + DS18B20 → surveillance thermique (192.168.4.201)   │
│  [Diodes]     Visualisation arrêts d'urgence déplacement télescope                │
│                                                                                   │
│  DÉFAUTS DE SÉCURITÉ CONFIRMÉS :                                                  │
│   ❌ Parafoudre Type 2 — absent ([LACUNE])                                        │
│   ❌ Capteurs fin de course AD/DEC — absents                                      │
│   ❌ Protection différentielle 30mA — non documentée                              │
│                                                                                   │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Cartographie réseau

| Adresse IP | Équipement | Fonction | Accès |
|------------|------------|----------|-------|
| 192.168.0.236 | Cimiers (wifi) | Commande ouverture/fermeture | WiFi |
| 192.168.0.237 | IPX800 Alimentation | Commande ON/OFF globale | Navigateur web |
| 192.168.0.238 | IPX800 Relais E/S | Gestion des sorties | Login: Admin / Oc@2018 |
| 192.168.4.201 | Wemos D1 Mini (ESP8266) | Température DS18B20 + watchdog | Web (endpoints [LACUNE]) |
| (variable) | T600-NUC-TELE | PC pilotage télescope | AnyDesk: 1 041 426 244 |
| (variable) | T600-NUC | PC 1er étage | AnyDesk: 513 471 809 |
| 192.168.0.234 | Sonde température NUC | Boîtier pilier | Web |
| SSID: wireless2.4G_A84620 | Switch wifi dôme | Distribution réseau | Psw: Admin2021$ |

---

## 3. Procédures pas-à-pas

### 3.1 Démarrage du système

> **Prérequis :** Accès au PC T600-NUC (1er étage) ou connexion AnyDesk à distance.

#### Étape 1 — Préparation physique
1. **Débrancher le câble de charge des cimiers** (la batterie est toujours en charge — risque d'arrachement mécanique si rotation avec câble branché)
2. **Enlever la bâche du télescope**
3. Si pilotage cimiers via IPX800 : mettre tension sur coffret cimier via wifi (192.168.0.236)

> ⚠️ **CRITIQUE :** L'état [CÂBLE BRANCHÉ] interdit catégoriquement toute initialisation de rotation du dôme. Risque majeur d'arrachement mécanique et de dommages structurels immédiats.

#### Étape 2 — Connexion au PC T600-NUC
- **Local (1er étage)** : connexion directe (mot de passe: `forets`)
- **Distant (AnyDesk)** : AnyDesk → T600-NUC (513 471 809, psw: `T6002024$#@`)

#### Étape 3 — Alimentation IPX800
1. Navigateur Edge → `192.168.0.237` (CMD-Ipx800-237)
2. Cliquer **ON** sur la ligne **D0** (état initial: "IPX800 éteint")
3. **Actualiser** → confirmer que le statut passe à "IPX800 allumé"

#### Étape 4 — Connexion IPX800 et activation des sorties
1. Nouvel onglet → `192.168.0.238` (Ipx800-238)
2. Login: `Admin`, mot de passe: `Oc@2018`
3. **Cliquer Out** → cliquer les **4 boutons sélectionnés** [A CONFIRMER : quels boutons exactement ?]
4. **Vérifier** :
   - **Output** = demandes (ce qu'on a activé)
   - **Input** = retour tension (appareil effectivement alimenté)

#### Étape 5 — Connexion au PC T600-NUC-TELE
- **Direct** (si local) ou **AnyDesk** : `1 041 426 244`, psw: `T600NUC2024$#@`

#### Étape 6 — Caméra Foscam
1. Démarrer **Foscam T6002021**
2. Compte local : login `foscamt600`, psw: `T6002021`
3. Device: `FI9831P-T600`
4. Compte myfoscam.com : login `jean-paul.dumoulin@skynet.be`, psw: `T6002021$`

#### Étape 7 — Vérification réseau
- Switch wifi dôme T600 (SSID: `wireless2.4G_A84620`, psw: `Admin2021$`) distribue :
  - Caméra dôme (Ethernet filaire)
  - Commande IPX800 (WiFi)

#### Étape 8 — Vérifications préalables (diagnostic télémétrique cimiers — 4 axes)
Avant toute utilisation astronomique, vérifier les **4 axes** de diagnostic :

**⚡ Énergie mobile** — NOMINAL attendu
- Module chargé / tension batterie nominale

**📊 Intégrité data** — NOMINAL attendu
- Réception correcte des télégrammes radio NRF24L01

**🔄 Commutation** — NOMINAL attendu
- État des relais Keyes_SRly (libres, physique cohérent)
- Cohérence des fins de course (GH, GB, DY, DB)

**🌧️ Environnement** — NOMINAL attendu
- Détecteur de pluie (signal inactif / pas de parasite)
- Température dôme (DS18B20 via 192.168.4.201) — pas d'anomalie thermique

#### Étape 9 — Ouverture des cimiers
1. Commande OUVERTURE CIMIERS via IPX800 (S6)
2. Vérifier courant moteur via capteur ACS712
3. Vérifier cohérence fins de course (capteurs GH, GB, DY, DB)
4. Surveiller via caméra Foscam (latence vidéo < 1s)
5. **Temps attendu** : ~90 secondes (temps shutter documenté)

#### Étape 10 — Autorisation rotation dôme
Conditions préalables strictes :
- ✅ Cimiers physiquement **100% ouverts**
- ✅ Câble chargeur formellement **débranché**
- ✅ Absence totale d'obstacle interne

**Post-lancement** (via LesveDomeNet) :
- Encodeur Grayhill : transitions régulières
- Position Home : cohérence (valeur: 310 [A CONFIRMER : unité])
- Vitesse de rotation : stable, sans variation
- Mécanique : aucun glissement, aucun bruit anormal

#### Étape 11 — Utilisation astronomique
1. Démarrer les applications (NINA, LesveDomeNet)
2. Effectuer les observations / acquisitions
3. Arrêter les applications avant fermeture

> ⚠️ **Note :** Les procédures de **mise en station**, **alignement stellaire**, **collimation** et **autoguidage** ne sont pas documentées dans les sources disponibles. Voir section 8 pour les actions recommandées.

### 3.2 Extinction et sécurisation

#### Niveau 1 — Mécanique (cimiers)
1. Commande **FERMETURE CIMIERS** via IPX800 (S4)
2. Vérifier fins de course (GH, GB, DY, DB)
3. Vérifier absence tension résiduelle sur moteurs
4. **Rebrancher le câble de charge de la batterie des cimiers**

#### Niveau 2 — Cerveau informatique (arrêt OS)
1. Sur l'écran du **T600-NUC-TELE** : clic **Arrêter**
2. Perte connexion AnyDesk si travail à distance
3. Attendre l'extinction complète du système (intégrité fichiers d'acquisition)

#### Niveau 3 — Relais (IPX800 — .238)
1. Connexion sur **T600-NUC** (AnyDesk: 513 471 809, psw: `T6002024$#@`)
2. Interface `192.168.0.238` → Désactiver **toutes** les sorties
3. Vérifier que toutes les lignes Output sont OFF

#### Niveau 4 — Énergie (IPX800 — .237)
1. Interface `192.168.0.237` → Commande **OFF**
2. Actualiser → Vérifier D0 (module IPX800 physiquement éteint)

> ⚠️ **Ordre validé par Jean-Paul Dumoulin (v1.2) :** l'arrêt informatique (Niveau 2) précède la coupure des relais (Niveau 3) — protège l'intégrité des fichiers d'acquisition. Le rebranchement du câble batterie fait partie intégrante du Niveau 1.

> ⚠️ [LACUNE] : Le Niveau 4 complet (détail des arrêts logiciels, services à stopper) n'est que partiellement documenté.

### 3.3 Niveaux de criticité opérationnelle

| Niveau | Risque | Action |
|--------|--------|--------|
| **Nominal** | Aucune interaction dangereuse | Actions de routine |
| **Alerte** | Risque potentiel si mauvaise séquence | Validation stricte ordre opérations |
| **Séquentiel** | — | Nécessite validation stricte |
| **Criticité Maximale** | Risque mécanique ou électrique immédiat | Arrêt immédiat / vérification prérequis |

---

## 4. Schémas et BOM

### 4.1 BOM identifiée (composants avec références)

| Réf. | Désignation | Référence / Fabricant | Qté | Remarque |
|:----:|-------------|----------------------|:---:|----------|
| H-001 | Automate IPX800 | GCE Electronics IPX800 V4/V5 | 1 | 8 sorties relais. Version à confirmer |
| H-002 | Wemos D1 Mini | ESP8266 (Wemos/Lolin) | 1 | Watchdog + sonde DS18B20 |
| H-003 | Arduino Uno R3 | Arduino.cc | 1 | Émetteur NRF24L01 (cimiers TX) |
| H-004 | Arduino Mega R3 | Arduino.cc | 1 | Récepteur NRF24L01 (cimiers RX) |
| H-005 | Module NRF24L01+ | Nordic Semiconductor | 2 | 1 TX + 1 RX. Version PA+LNA probable |
| H-006 | Sonde DS18B20 | Maxim Integrated / Dallas | 1 | Température OneWire |
| H-007 | Encodeur Gray Code | Grayhill 654321 | 1 | 16 positions, roue 241mm |
| H-008 | Interface USB → Analogique | Velleman PVM110N | 1 | Timer Interval: 60ms |
| H-009 | Driver moteur pas-à-pas | Toshiba TB67H303HC (sur Maia-4) | 1 | Courant max 2.7A, tension max 24V |
| H-010 | Carte Alimentation Pléiades | Alcyone-5 Shield | 1 | Input 12V-24V → Output 12V + 9V |
| H-011 | Carte Mère Pléiades | Electra-5 | 1 | Régulateurs 5V/3.3V, port ST-4 |
| H-012 | Carte Contrôleur Pléiades | Maia-4 | 1 | Driver TB67H303HC + encodeur quadrature |
| H-013 | Capteur courant | ACS712 (xxA) | 1 | Calibre exact non spécifié [A CONFIRMER] |
| H-014 | Relais power switch | Keyes SRly | 1 | Commande IPX800 |
| H-015 | Caméra IP | Foscam FI9831P-T600 | 1 | Supervision visuelle, latence < 1s |
| H-016 | Switch wifi dôme | (non spécifié) | 1 | SSID: wireless2.4G_A84620 [A CONFIRMER : modèle] |

### 4.2 BOM non référencée (composants identifiés sans référence fabricant)

| Désignation | Qté estimée | Rôle | Action requise |
|-------------|:-----------:|------|----------------|
| Variateur de fréquence | 1 | Rotation dôme (f=24.0 Hz) | Identifier marque/modèle |
| Moteur réducteur rotation dôme | 1 | Entraînement coupole | Identifier puissance, couple, rapport |
| Moteurs cimiers (x2…4) [A CONFIRMER] | 2–4 | Ouverture/fermeture volets | Identifier type, tension, courant |
| Moteurs pas-à-pas AD/DEC | 2 | Axes télescope | Identifier marque, couple, pas |
| Batterie cimiers | 1 | Alimentation partie tournante | Identifier chimie, tension, capacité |
| Alimentation Pilier 20V | 1 | Secteur → 20V DC | Identifier puissance (W) |
| Alimentation Télescope 12V | 1 | Secteur → 12V DC | Identifier puissance (W) |
| Switch Home dôme | 1 | Recalage position zéro | Type (microswitch/inductif/optique) |
| Capteurs fin course cimiers (GH, GB, DY, DB) | 4 | Limitation mécanique | Identifier type |
| Détecteur de pluie | 1 | Sécurité cimiers | Identifier type (résistif/optique) |
| Limiteur de courant cimiers | 1 | Protection moteurs | Identifier type et seuil |
| Diodes arrêts d'urgence | (NS) | Visualisation | Identifier type (LED + résistance) |
| Ventilation Alcyone-5 | 1 | Refroidissement si >19V | Identifier type (ventilateur 12V) |
| Chargeur batterie cimiers | 1 | Maintien charge | Identifier type, courant de charge |
| PC NUC T600 (1er étage) | 1 | Alimentation IPX800 + entrée OCA | Modèle non spécifié |
| PC NUC T600-TELE | 1 | Pilotage télescope | Modèle non spécifié |

### 4.3 Spécifications mécaniques connues

| Paramètre | Valeur | Statut |
|-----------|--------|--------|
| Diamètre coupole | 4500 mm | ✅ Confirmé |
| Rayon coupole (réel) | 2250 mm | ✅ Calculé |
| Dome Radius (NINA) | 750 mm | ⚠️ **Probablement un offset optique**, pas le rayon [A CONFIRMER] |
| Roue capteur Azimut | 241 mm | ✅ Confirmé |
| Nombre de trous (encodeur) | 16 | ✅ Confirmé → résolution ~22.5°/pas |
| Temps Shutter (cimiers) | 90 s | ✅ Confirmé |
| Tolérance position dôme | 10 (unité non spécifiée) | ⚠️ Unité inconnue [A CONFIRMER] |
| Position Park | 10 (unité non spécifiée) | ⚠️ Unité inconnue [A CONFIRMER] |
| Position Home | 310 (unité non spécifiée) | ⚠️ Unité inconnue [A CONFIRMER] |
| Variateur fréquence | 24.0 Hz | ✅ Confirmé |
| Timer interval Velleman | 60 ms | ✅ Confirmé |
| Dimensions GEM N/S | 50 mm | ⚠️ **Suspect** — probablement pas une dimension d'axe [A CONFIRMER] |
| Dimensions GEM E/W | 230 mm | ⚠️ Suspect [A CONFIRMER] |
| Dimensions GEM U/D | 2250 mm | ⚠️ Suspect — pourrait être la hauteur totale [A CONFIRMER] |
| GEM Axis Length | 44.3 mm | ⚠️ Incohérent avec un T600 [A CONFIRMER] |

### 4.4 Spécifications optiques — [LACUNE CRITIQUE]

| Paramètre | Valeur | Statut |
|-----------|--------|--------|
| **Ouverture (diamètre)** | **600 mm** | ✅ Confirmé |
| Focale | NON SPÉCIFIÉE | ❌ Manquant |
| Rapport f/D | NON SPÉCIFIÉ | ❌ Manquant |
| Type optique | NON SPÉCIFIÉ | ❌ Manquant |
| Matériau optique | NON SPÉCIFIÉ | ❌ Manquant |
| Traitements optiques | NON SPÉCIFIÉS | ❌ Manquant |
| Obstruction (secondaire) | NON SPÉCIFIÉE | ❌ Manquant |

> **Action requise :** Un relevé optique sur site est **impératif** avant toute utilisation scientifique. Voir section 8 Recommandations.

### 4.5 Brochage ST-4 (port autoguidage)

Le port ST-4 de la carte Electra-5 (broché sur embase RJ12 à 6 broches) permet le pilotage direct de la monture depuis un autoguideur :

- **Broche 1** (Blanc) — NC : Non connecté
- **Broche 2** (Noir) — GND : Masse
- **Broche 3** (Rouge) — RA+ : Correction A.D. vers l'est
- **Broche 4** (Vert) — DE+ : Correction DECL. vers le nord
- **Broche 5** (Jaune) — DE− : Correction DECL. vers le sud
- **Broche 6** (Bleu) — RA− : Correction A.D. vers l'ouest

---

## 5. Logique Firmware et I/O Mapping

### 5.1 Inventaire des microcontrôleurs

| MCU | Rôle | Alimentation | Adresse IP | Firmware |
|-----|------|-------------|------------|----------|
| **Wemos D1 Mini (ESP8266)** | Watchdog + sonde température | Non spécifiée (secteur ou IPX800) | 192.168.4.201 | ❌ Non disponible [LACUNE CRITIQUE] |
| **Arduino Uno** | Émetteur NRF24L01 (cimiers TX) | 9V régulé (Alcyone-5) | — | ❌ Non disponible [LACUNE CRITIQUE] |
| **Arduino Mega** | Récepteur NRF24L01 (cimiers RX) + pilotage relais | Batterie cimiers | — | ❌ Non disponible [LACUNE CRITIQUE] |
| **Maia-4 (TB67H303HC)** | Driver moteur pas-à-pas (encodeur quadrature) | Via Electra-5 (12-24V) | — | ❌ Non disponible [LACUNE] |
| **IPX800** | Automate central 8 relais | Via T600-NUC | 192.168.0.237/.238 | ✅ Propriétaire GCE |
| **Velleman PVM110N** | Conversion USB → analogique | USB (PC NUC) | — | ✅ Propriétaire Velleman |

> ⚠️ **Aucun fichier source (.ino, .cpp, .h) n'est disponible pour les 3 microcontrôleurs programmables.** La logique ci-dessous est **inférée** à partir de l'architecture documentée et doit être vérifiée sur le code réel ([Action recommandée P1.4 — extraction des firmwares]).

### 5.2 Logique de contrôle — Cimiers (inférée)

```
Chaîne de commande :
IPX800 (S4/S5/S6) → Série UART [?] → Arduino Uno → SPI → NRF24L01 TX
                                                          │ 2.4 GHz RF
Arduino Mega ← SPI ← NRF24L01 RX ←┘
    → GPIO → Relais moteurs (OG/FG/OD/FD) [A CONFIRMER : 2 ou 4 moteurs]
    → Analogique → ACS712 (courant moteur)
    → GPIO → Capteurs GH, GB, DY, DB (fins de course)
    → GPIO → Détecteur de pluie
```

**Logique inférée :**
1. **Diagnostic préalable** : tension batterie OK, relais Keyes OK, NRF24L01 OK, détecteur pluie inactif
2. **Commande** : S4 (fermeture), S5 (fermeture urgence), S6 (ouverture) via IPX800
3. **Boucle de rétroaction** : vérification courant ACS712 → cohérence fins de course → surveillance caméra
4. **Timeout** : 90 secondes (temps shutter documenté)
5. **Urgence** : S5 → arrêt immédiat → protocole de sécurité

> ⚠️ [LACUNE] Seuils ACS712, logique GH/GB/DY/DB, machine d'état timeout, protocole UART (baud rate, format trame) inconnus.

#### Cinématique des cimiers

Commande type de vérification : `SYS:IP 192.168.0.236`  
Vérification courant moteur via **ACS712** sur le **port 5482**.

### 5.3 Logique de contrôle — Rotation dôme (inférée)

```
PC (LesveDomeNet) → USB → Velleman PVM110N → Analogique → Variateur (24.0 Hz) → Moteur réducteur
                                                                                       │
Encodeur Grayhill 654321 (Gray Code, 16 trous, roue 241mm) ← Switch Home (pos. 310) ←┘
```

**Logique inférée :**
1. **Condition préalable absolue** : cimiers 100% ouverts, câble chargeur débranché
2. **Pilotage** : LesveDomeNet envoie signaux position/vitesse via USB → PVM110N
3. **Conversion** : PVM110N → signal analogique → variateur (24.0 Hz)
4. **Asservissement** : Encodeur Grayhill → retour position → LesveDomeNet
5. **Recalage** : Switch Home (position 310) → recalage zéro

> ⚠️ [LACUNE] Protocole LesveDomeNet→PVM110N non documenté. Résolution encodeur Grayhill non spécifiée.

### 5.4 Logique de contrôle — Monture (inférée)

```
PC (NINA/ASCOM) → Alcyone-5 (12V/9V) → Electra-5 (5V/3.3V, ST-4) → Maia-4 (TB67H303HC)
                                                                       → Moteurs pas-à-pas AD/DEC
                                                                       → Encodeur quadrature (boucle fermée)
```

**Points critiques :**
- ✅ Boucle fermée via encodeur quadrature (bonne base technique)
- ✅ Port ST-4 présent (autoguidage possible)
- ❌ **Absence de capteurs fin de course AD/DEC** — risque de collision destructrice
- ❌ **Autoguideur non documenté** — imagerie longue pose compromise
- ❌ Pas de détails sur PEC, backlash, compensation

### 5.5 I/O Mapping — IPX800 (Sorties relais)

| Sortie | Fonction | Documenté |
|:------:|----------|:---------:|
| S1 | Rotation Coupole | ✅ |
| S2 | Pilier 20V & Télescope 12V | ✅ |
| S3 | PC NUC T600 | ✅ |
| S4 | Fermeture Cimiers | ✅ |
| S5 | Fermeture Cimiers URGENCE | ✅ |
| S6 | Ouverture Cimiers | ✅ |
| S7 | Non spécifié | ❌ [LACUNE] |
| S8 | Non spécifié | ❌ [LACUNE] |

### 5.6 I/O Mapping inféré — Arduino Uno

| Broche | Signal | Composant |
|--------|--------|-----------|
| RX (D0) | Série UART | IPX800 (réception ordres) |
| D10 (SS) | SPI_CS | NRF24L01 |
| D11 (MOSI) | SPI_MOSI | NRF24L01 |
| D12 (MISO) | SPI_MISO | NRF24L01 |
| D13 (SCK) | SPI_SCK | NRF24L01 |
| Vin | 9V | Alcyone-5 |

> ⚠️ Mapping partiellement inféré — protocole série (baud rate, format trame) inconnu [LACUNE].

### 5.7 I/O Mapping inféré — Arduino Mega

| Broche | Signal | Composant | Rôle |
|--------|--------|-----------|------|
| D? (SPI) | SPI | NRF24L01 | Réception commandes |
| D?? | GPIO | Relais OG | Ouverture Gauche |
| D?? | GPIO | Relais FG | Fermeture Gauche |
| D?? | GPIO | Relais OD | Ouverture Droite |
| D?? | GPIO | Relais FD | Fermeture Droite |
| A? | Analogique | ACS712 | Courant moteur |
| D?? | GPIO | GH | Fin course Haut/Gauche |
| D?? | GPIO | GB | Fin course Bas/Gauche |
| D?? | GPIO | DY | Fin course ? |
| D?? | GPIO | DB | Fin course ? |

> ⚠️ Aucun pin mapping documenté — acronymes GH/GB/DY/DB non explicités [LACUNE].

### 5.8 Protocoles de communication

| Protocole | Liaison | Équipements | Rôle | État |
|-----------|---------|-------------|------|:----:|
| Série (UART) | Filaire | IPX800 → Arduino Uno | Ordres cimiers | ⚠️ Sous réserve |
| SPI | Filaire | Arduino Uno ↔ NRF24L01 | Échange radio | ✅ Inféré |
| SPI | Filaire | Arduino Mega ↔ NRF24L01 | Échange radio | ✅ Inféré |
| NRF24L01 (2.4 GHz) | Radio | Uno TX → Mega RX | Commandes cimiers | ⚠️ Sous réserve |
| OneWire | Filaire | Wemos D1 Mini ↔ DS18B20 | Température | ✅ Inféré |
| WiFi | Radio | Wemos D1 Mini → Réseau | Interface web | ⚠️ Sous réserve |
| HTTP | Ethernet/WiFi | IPX800 → PC | Interface web | ✅ Documenté |
| USB → Analogique | USB + filaire | PC → Velleman → Variateur | Rotation dôme | ⚠️ Sous réserve |
| ST-4 | Filaire (RJ) | Autoguideur → Maia-4 | Autoguidage | ❌ Non documenté |
| ASCOM | Logiciel | PC + drivers | Plateforme intégration | ✅ Documenté |
| NINA | Logiciel | PC + plugin | Acquisition/pointage | ✅ Documenté |
| AnyDesk | Réseau | PC distant → PC local | Supervision distante | ✅ Documenté |

### 5.9 Paramètres LesveDomeNet

Configuration actuelle du logiciel de pilotage de dôme :

- **Dome diameter** — À compléter
- **Park position** — À compléter
- **Home Position** — ~31°
- **Open/Close time** — 90 s
- **Watchdog** — 30s max pour 3°
- **Sensor** — Gray coder, KB059

---

## 6. Dépannage / Diagnostic

### 6.1 Codes et diagnostics

| Code / Port | Description | Statut |
|-------------|-------------|:------:|
| DIAG PORT : 5492 | Port de diagnostic (non détaillé) | ⚠️ Sous réserve |
| TELEMETRY CODE | Code télémétrique spécifique | ❌ Non défini [LACUNE] |
| SYS_IP | Identifiant système (slides) | ⚠️ Sous réserve |

### 6.2 Matrice diagnostique — Problèmes fréquents

| Symptôme | Cause probable | Action | Référence |
|----------|---------------|--------|-----------|
| IPX800 ne répond pas | Perte alimentation / réseau | Vérifier T600-NUC allumé, vérifier WiFi, redémarrer interface | §3.1 |
| Perte commutation NRF24L01 | Perte de paquets radio | Vérifier diagnostic télémétrique préalable, vérifier alimentation Arduino | §3.1 Étape 8 |
| Cimiers ne s'ouvrent/ferment pas | Batterie déchargée, relais collé, fin de course bloqué | Vérifier tension batterie, test relais Keyes, inspection caméra | §3.1 Étape 9 |
| Rotation dôme anormale | Encodeur Grayhill défaillant, variateur mal configuré | Vérifier transitions encodeur via LesveDomeNet, fréquence variateur (24.0 Hz) | §3.1 Étape 10 |
| Température anormale | Watchdog DS18B20 / ventilation Alcyone-5 | Vérifier 192.168.4.201, vérifier ventilation si tension >19V | §3.1 Étape 8 |

### 6.3 Procédure d'urgence — Cimiers

| Situation | Action |
|-----------|--------|
| Cimiers bloqués en ouverture (risque pluie) | Commande FERMETURE CIMIERS URGENCE via IPX800 S5 |
| Rotation dôme avec câble branché | **STOP IMMÉDIAT** — arrêter rotation via LesveDomeNet, débrancher câble |
| Orage imminent | Exécuter procédure d'extinction complète (Niveaux 1→4, §3.2) |
| Surchauffe Alcyone-5 (>19V sans ventilation) | Couper alimentation S2 via IPX800, vérifier ventilation |

---

## 7. Maintenance préventive

### 7.1 Calendrier de maintenance

| Périodicité | Action | Référence |
|:-----------:|--------|-----------|
| **Avant chaque session** | Diagnostic télémétrique cimiers, vérification DS18B20, test communication NRF24L01 | §3.1 Étape 8 |
| **Avant chaque session** | Vérification visuelle câbles, connecteurs, absence obstacle | §3.1 |
| **Hebdomadaire** | Contrôle batterie cimiers (tension, état chargeur) | — |
| **Mensuel** | Inspection ventilateur Alcyone-5, propreté connecteurs RJ12 et ST-4 |
| **Mensuel** | Test arrêts d'urgence et détecteur de pluie | — |
| **Trimestriel** | Vérification encodeur Grayhill (transitions, propreté roue) | — |
| **Annuel** | Relevé électrique complet, serrage connecteurs, inspection câbles | — |

### 7.2 Points de vigilance permanents

| Point | Risque | Action |
|-------|--------|--------|
| **Absence de parafoudre Type 2** | Destruction électronique par foudre | Installer Citel DS70-R ou équivalent [P1.3] |
| **Absence capteurs fin de course AD/DEC** | Collision destructrice télescope | Installer capteurs inductifs ou microswitches [P1.2] |
| **Câble charge cimiers** | Arrachement mécanique | **Toujours débrancher avant rotation** |
| **Ventilation Alcyone-5** | Surchauffe >19V | Vérifier fonctionnement si applicable |
| **Switch wifi dôme** | Point de défaillance unique | Pas de redondance réseau |

### 7.3 Maintenance PC

| PC | Rôle | Actions recommandées |
|:--:|------|---------------------|
| **T600-NUC** (1er étage) | Alimentation IPX800, entrée OCA | Mises à jour OS, nettoyage, contrôle chauffage anti-condensation |
| **T600-NUC-TELE** | Pilotage télescope | Mises à jour NINA, ASCOM, LesveDomeNet. Backup configuration. (Version Ubuntu non spécifiée [LACUNE]) |

---

## 8. Recommandations et actions prioritaires

### 🔴 P1 — Actions critiques (bloquantes)

| # | Action | Effort | Dépendances |
|---|--------|:------:|-------------|
| **P1.1** | **Relevé optique obligatoire** : mesurer focale, identifier type optique, backfocus | 1 jour | Accès télescope |
| **P1.2** | **Installer capteurs fin de course AD/DEC** sur les deux axes de la monture | 2-3 jours | Identification moteurs |
| **P1.3** | **Installer parafoudre Type 2** sur tableau alimentation dôme | ½ jour | Accès tableau |
| **P1.4** | **Extraire les firmwares** des Arduino Uno, Mega, Wemos D1 Mini | 1-2 jours | Sonde FTDI, accès physique |
| **P1.5** | **Créer une procédure de mise en station** (polar alignment) | 2 jours | Caméra polaire |

### 🟠 P2 — Actions importantes

| # | Action | Effort |
|---|--------|:------:|
| **P2.1** | Créer procédure d'alignement stellaire (plate solving NINA, ≥6 étoiles) | 1-2 jours |
| **P2.2** | Acquérir et installer un autoguideur (hors-axe recommandé) + calibrage PHD2 | 1 semaine |
| **P2.3** | Créer procédure de collimation (laser + étoile) | 1 jour |
| **P2.4** | Identifier tous les moteurs (marque, modèle, tension, couple) | 1-2 jours |
| **P2.5** | Caractériser batterie cimiers (chimie, tension, capacité) | ½ jour |
| **P2.6** | Relevé électrique et physique sur site (sections câbles, connecteurs) | 1 jour |
| **P2.7** | Vérifier/corriger paramètres synchronisation dôme NINA | 1 jour |

### 🟡 P3 — Actions souhaitables

| # | Action | Effort |
|---|--------|:------:|
| **P3.1** | Campagne mesure erreur périodique (PEC) sur ≥5 cycles | 1 nuit |
| **P3.2** | Mesurer et documenter backlash RA/DEC | 1 jour |
| **P3.3** | Produire schémas de câblage complets | 2-3 jours |
| **P3.4** | Établir BOM mécanique complète | 2 jours |
| **P3.5** | Créer fiches de calibration annuelle et nocturne | 1 jour |
| **P3.6** | Vérifier protection différentielle 30mA sur circuit dôme | ½ jour |
| **P3.7** | Centraliser documentation technique + diagramme flux optique | 1 jour |

### Dépendances entre actions

```
P1.1 (Relevé optique) ──► P2.3 (Collimation)
P1.4 (Extraction firmwares) ──► P3.1 (PEC), P3.2 (Backlash)
P2.2 (Autoguideur) ──► P3.1 (PEC), P3.2 (Backlash)
P2.6 (Relevé électrique) ──► P3.3 (Schémas câblage)
P1.5 (Mise en station) ──► P2.1 (Alignment) ──► P2.2 (Autoguideur)
```

---

## 9. Annexes

### 9.1 Glossaire

| Sigle | Signification |
|-------|---------------|
| **AD/DEC** | Ascension Droite / Déclinaison (axes monture équatoriale) |
| **GEM** | German Equatorial Mount (monture équatoriale allemande) |
| **OG/FG/OD/FD** | Ouverture Gauche / Fermeture Gauche / Ouverture Droite / Fermeture Droite (cimiers) |
| **GH/GB/DY/DB** | Capteurs fin de course cimiers (non explicités dans les sources) |
| **ST-4** | Standard d'autoguidage à 4 fils (RA+/RA-/DEC+/DEC-) |
| **ACS712** | Capteur de courant à effet Hall (5A, 20A ou 30A selon module) |
| **NRF24L01** | Module radio 2.4 GHz, jusqu'à 2 Mbps, portée ~100m LOS |
| **IPX800** | Automate Ethernet de GCE Electronics (8 relais, E/S analogiques) |
| **LesveDomeNet** | Logiciel de pilotage de dôme astronomique (ASCOM compatible) |
| **NINA** | Nighttime Imaging 'N' Astronomy — logiciel d'acquisition |
| **ASCOM** | Plateforme d'intégration pour matériel astronomique |
| **PEC** | Periodic Error Correction (correction d'erreur périodique) |
| **PHD2** | Logiciel d'autoguidage (Push Here Dummy 2) |

### 9.2 Références

| Document | Source |
|----------|--------|
| Fiche 1 — Domotisation T600.pdf | Christian Wanlin & Jean-Paul Dumoulin, 25 mai 2026 |
| Fiche 2 — Améliorations (Google Doc) | Jean-Paul Dumoulin, date non précisée |
| Fiche 3 — Opérations_T600.pptx | Jean-Paul Dumoulin & Christian Wanlin, 2026 |
| Fiche 4 — T600-Mise-en-route-20260525.pptx | Jean-Paul Dumoulin & Christian Wanlin, 26 mai 2026 |
| Fiche 5 — Domotisation-T600-20260525.pptx | Jean-Paul Dumoulin & Christian Wanlin, 25 mai 2026 |
| Analyse Astro-Optique | Bureau Gérard, 12 juin 2026 |
| Analyse Hardware | Bureau Gérard, 12 juin 2026 |
| Analyse Firmware | Bureau Gérard, 12 juin 2026 |
| Rapport de Croisement T600 | Bureau Gérard (Orchestrateur), 12 juin 2026 |

### 9.3 Identifiants et mots de passe consolidés

| Service | Identifiant | Mot de passe |
|---------|-------------|:------------:|
| IPX800 | Admin | Oc@2018 |
| AnyDesk T600-NUC-TELE | 1 041 426 244 | T600NUC2024$#@ |
| AnyDesk T600-NUC | 513 471 809 | T6002024$#@ |
| Foscam locale | foscamt600 | T6002021 |
| myfoscam.com | jean-paul.dumoulin@skynet.be | T6002021$ |
| WiFi dôme | wireless2.4G_A84620 | Admin2021$ |
| Local 1er étage | — | forets |
| Foscam Device | FI9831P-T600 | — |

### 9.4 Datasheets et documentation technique

| Composant | Type de document | Disponibilité |
|-----------|-----------------|:-------------:|
| IPX800 V4/V5 | Manuel utilisateur | GCE Electronics (en ligne) |
| TB67H303HC (Toshiba) | Datasheet fabricant | Toshiba (en ligne) |
| NRF24L01+ (Nordic) | Product Specification | Nordic Semiconductor (en ligne) |
| DS18B20 (Maxim Integrated) | Datasheet | Maxim Integrated (en ligne) |
| ACS712 (Allegro) | Datasheet | Allegro MicroSystems (en ligne) |
| Grayhill 654321 | Datasheet | Grayhill (en ligne) |
| Velleman PVM110N | Manuel utilisateur | Velleman (en ligne) |
| Foscam FI9831P | Manuel utilisateur | Foscam (en ligne) |
| Cartes Pléiades | Documentation technique | **Non disponible** [LACUNE] |

### 9.5 Traçabilité des sources

| Assertion principale | Source | Fiabilité |
|----------------------|--------|:---------:|
| Architecture IPX800 + cartes Pléiades | Fiches 1, 3, 5 | ✅ Validé (3 sources) |
| Séquence démarrage/extinction | Fiches 3, 4 | ✅ Validé |
| Chaîne cimiers NRF24L01 | Fiches 1, 3 | ✅ Validé |
| Absence autoguideur documenté | Fiche 2, toutes analyses | ✅ Validé |
| Absence fins de course AD/DEC | Fiche 2, toutes analyses | ✅ Validé |
| Absence parafoudre Type 2 | Fiche 2, HW, Cross | ✅ Validé |
| Spécifications optiques | Aucune source | ❌ LACUNE |
| Firmware Arduino/ESP8266 | Aucun fichier source | ❌ LACUNE CRITIQUE |
| Schémas de câblage détaillés | Aucune source | ❌ LACUNE |
| Modèles moteurs | Aucune source | ❌ LACUNE |
| Protocole série IPX800→Arduino | Inféré uniquement | ⚠️ Sous réserve |
| Configuration NRF24L01 | Inféré uniquement | ⚠️ Sous réserve |

---

*Document généré par le Rédacteur Technique (Bureau Gérard) — 12 juin 2026*
*Sources : FICHES_SOURCES_T600.md, ANALYSE_ASTRO_OPTIQUE.md, ANALYSE_HARDWARE.md, ANALYSE_FIRMWARE.md, CROISEMENT_T600.md*
