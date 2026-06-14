# RAPPORT D'ANALYSE DES RISQUES — T600
## OBSERVATOIRE CENTRE ARDENNES (OCA) — Équipe ACO

**Document :** OCA-T600-LIVRABLE-FINAL-20250527  
**Version :** 2.0  
**Pilote :** Jean-Paul Dumoulin & Christian Wanlin  
**Rédaction :** Orchestrateur OCA — Bureau ACO (Astronomie, Technique, Connaissances)

---

## 1. SYNTHÈSE EXÉCUTIVE

**Objet :** Analyse de trois risques critiques identifiés sur le télescope T600 automatisé de l'Observatoire Centre Ardennes, suite à la revue des documents de conception (Domotisation-T600-20260525.pptx, T600-Mise-en-route-20260525.pptx, Opérations_T600.pptx).

**Correction préalable — Topologie réseau confirmée :**
- **PC NUC-T600** (1er étage) → alimente l'IPX800, sert de point d'entrée principal
- **PC NUC-T600-TELE** → alimenté par l'IPX800, pilote le télescope et exécute NINA

### Classement des risques par criticité

| # | Risque | Criticité (P×I) | Urgence | Coût solution | Priorité |
|---|--------|:---------------:|:-------:|:-------------:|:--------:|
| **R1** | Absence capteurs fin de course AD/DEC | **25/25 — CRITIQUE** | **Immédiate** | ~125 € | **1** |
| **R3** | Absence parafoudre type 2 | **20/25 — CRITIQUE** | **Avant orages** | ~800 € | **2** |
| **R2** | Autoguideur non documenté | **12/25 — ÉLEVÉ** | **1 mois** | ~50 € | **3** |

**Message clé :** Pour un investissement total estimé à **~1 425 €**, les trois risques peuvent être traités, protégeant ainsi un instrument dont la seule instrumentation vulnérable est estimée entre **15 000 € et 40 000 €**.

---

## 2. CONTEXTE ET PÉRIMÈTRE

### 2.1 Le T600 en bref

| Caractéristique | Valeur |
|-----------------|--------|
| Diamètre | 600 mm |
| Masse estimée (tube + instrumentation) | 150 - 250 kg |
| Monture | Allemande (probable) |
| Logiciel de pilotage | NINA (astrophotographie) |
| Contrôle moteurs | Cartes Alcyone-5, MAIA-4, ELECTRA-5 |
| Domotique | IPX800 (contrôleur relais) |
| Supervision | AnyDesk + Caméra Foscam FI9831P-T600 |
| Réseau wifi dôme | SSID wireless2.4G_A84620 / Psw Admin2021$ |

### 2.2 Architecture de distribution électrique

```
[PC NUC-T600] — 1er étage
     │
     ├── Alimente l'IPX800 (via connexion internet)
     │
[IPX800] — 192.168.1.237 / 238 — Contrôleur relais
     │
     ├── [PC NUC-T600-TELE] — Pilote le télescope
     ├── [Cartes Alcyone-5] — Moteur AD
     ├── [Cartes MAIA-4] — Moteur DEC
     ├── [Cartes ELECTRA-5] — Auxiliaire
     ├── [Cartes cimiers] — Ouverture/fermeture (sur batterie)
     ├── [Variateur fréquence + Encodeur] — Rotation dôme
     └── [Switch wifi] — Caméra Foscam, réseau local
```

### 2.3 Équipe d'analyse mobilisée

| Agent | Compétence | Risques traités |
|-------|-----------|-----------------|
| **Astronome-physicien** | Mécanique, optique, physique instrumentale | R1 (mécanique) + R3 (instrumentation) |
| **Ingénieur électricien** | Électronique, câblage, protection électrique | R1 (câblage) + R3 (protection foudre) |
| **Firmware expert** | Microcontrôleurs, ASCOM, protocoles série | R1 (firmware) + R2 (autoguideur) |
| **Ethnographe** | Extraction connaissances, lacunes documentaires | R2 (lacunes) + transversal |
| **Rédacteur technique** | Coordination, structuration, mise en page | Synthèse et livrable final |

---

## 3. ANALYSE DÉTAILLÉE — RISQUE 1 : ABSENCE DE CAPTEURS DE FIN DE COURSE AD/DEC

### 3.1 Analyse mécanique (Agent : Astronome-physicien)

**Constat :** Aucun capteur de fin de course mécanique, optique ou magnétique n'est documenté sur les axes AD (Ascension Droite) et DEC (Déclinaison). Sans butées physiques ni détection électronique, la collision est une question de temps.

#### Scénarios de collision identifiés

| # | Scénario | Cause probable | Conséquence immédiate | Dommage estimé |
|---|----------|---------------|----------------------|:--------------:|
| 1 | **Meridian Flip raté** | Échec du changement de côté de la monture allemande | Tube percute le pilier → miroir primaire (30-50 kg) délogé, collimation perdue, tube tordu | **30 000 - 50 000 €** |
| 2 | **Rotation AD excessive** | Erreur logicielle ou blocage NINA | Câbles alimentation/USB3/Ethernet tendus puis arrachés → court-circuit, connecteurs caméra détruits | **5 000 - 15 000 €** |
| 3 | **Rotation DEC excessive** | Dépassement de l'ouverture du dôme | Caméra CCD/CMOS principale détruite en premier impact contre la structure du dôme | **10 000 - 30 000 €** |
| 4 | **Dépassement de butée mécanique** | Saturation du moteur sans arrêt | Courroies d'entraînement sautées, dents cassées, perte de pas | **500 - 2 000 €** |

#### Physique de l'impact

| Paramètre | Valeur | Interprétation |
|-----------|--------|----------------|
| Masse totale | 200 kg | Tube + instrumentation |
| Vitesse de pointage | 2°/s (0,035 rad/s) | Vitesse standard de déplacement |
| Vitesse de slew rapide | 5°/s (0,087 rad/s) | Vitesse maximale |
| Énergie cinétique (pointage) | **E = ½ × 200 × (0,035)² = 0,12 J** | Faible mais concentrée |
| Énergie cinétique (slew) | **E = ½ × 200 × (0,087)² = 0,76 J** | Suffisant pour endommager un axe |

> **Note :** L'énergie semble faible, mais elle est concentrée sur les roulements et paliers qui ne sont pas dimensionnés pour des arrêts brutaux. Une collision même à faible vitesse peut déformer des axes ou casser des supports.

#### Préconisations mécaniques

| Priorité | Action | Détail |
|:--------:|--------|--------|
| **1** | Butée mécanique physique (hardstop) | Caoutchouc dur ou acier recouvert de néoprène sur AD et DEC |
| **2** | Capteurs magnétiques à effet Hall | Honeywell SS49E — sécurité primaire sans contact |
| **3** | Micro-switch IP67 | Sécurité secondaire redondante (Honeywell V15W2-EZ200) |

---

### 3.2 Analyse électronique et câblage (Agent : Ingénieur électricien)

#### Cartes disponibles et entrées exploitables

| Carte | Rôle | Entrées libres | Type | Adapté pour |
|-------|------|:--------------:|------|-------------|
| **Alcyone-5** | Contrôle moteur AD | 4 entrées (EN1-EN4) | Opto-isolées, protection galvanique | ✅ **Idéal** capteurs extérieurs |
| **MAIA-4** | Contrôle moteur DEC | 4 entrées (ET1-ET4) | TOR contact sec | ✅ OK avec pull-up externe |
| **ELECTRA-5** | Auxiliaire/focuser | 2 numériques + 2 analogiques | Mixte | ⚠ Analogique pour mesure continue |

#### Architecture de câblage préconisée (boucle fail-safe)

```
+24VDC ALIM                         ALIM 0V
   │                                    │
   ├──[BP URGENCE NC]───[Capteur AD+ NC]───[Capteur AD- NC]─── ...
   │                                        │
   └──[R pull-up 10kΩ]─────────────────────┼──── EN1 (Alcyone-5)
                                           │
                                    [Diode TVS P6KE24A]
                                           │
                                          0V
```

**Logique de sécurité fail-safe :**

| État | Contact NC | Entrée Alcyone | Action |
|------|:----------:|:--------------:|--------|
| Normal | Fermé | 0V (actif LOW) | Mouvement autorisé |
| Fin de course déclenché | **Ouvert** | **24V (HIGH)** | **Arrêt immédiat moteur** |
| Câble coupé ou arraché | **Ouvert** | **24V (HIGH)** | **Sécurité intrinsèque** |

#### Protection des entrées (par canal)

```
[Capteur NC] ──[R série 470Ω 1/2W]──┬──[Diode TVS P6KE24A]── 0V
                                     │
                                     ├──[Condensateur 100nF]── 0V
                                     │
                                     └── EN1 (Alcyone-5)
```

#### Intégration IPX800

| Niveau | Action | Délai |
|:------:|--------|:-----:|
| 1 | Alcyone-5 détecte le signal → OUT1 bascule | < 1 ms |
| 2 | IPX800 reçoit le signal → coupe alim moteurs + envoie notification | < 100 ms |
| 3 | BP urgence câblé en amont → coupure physique manuelle | Instantané |

#### Spécifications des capteurs recommandés

| Référence | Type | Indice protection | Plage température | Courant max | Prix unitaire |
|-----------|------|:-----------------:|:-----------------:|:-----------:|:-------------:|
| **Honeywell V15W2-EZ200** | Micro-switch | IP67 | -40°C à +85°C | 10 A | ~15 € |
| Omron D2HW-211G | Micro-switch | IP67 | -40°C à +85°C | 2 A | ~10 € |
| Honeywell SS49E | Effet Hall | — | -40°C à +150°C | 10 mA | ~3 € |

---

### 3.3 Analyse firmware et logicielle (Agent : Firmware expert)

#### Microcontrôleur probable des cartes

| Carte | µC probable | Driver moteur | Capacité multitâche |
|-------|:-----------:|:-------------:|:-------------------:|
| Alcyone-5 | **ESP32** (2 cœurs, WiFi natif) | TMC2209 (StealthChop2 + StallGuard) | ✅ Excellente |
| MAIA-4 | **ESP32** | DRV8825 ou A4988 | ✅ Bonne |
| ELECTRA-5 | **STM32** | TMC2209 | ✅ Très bonne |
| **⚠ Risque** | **Si Arduino 8-bit (Uno/Mega)** | — | **❌ Migration nécessaire** |

#### Implémentation par interruption matérielle (ISR) — Code de référence

```cpp
// Fichier : limit_switches.h
// Logique : capteurs NC (Normalement Fermés) → FALLING = déclenchement

const int PIN_LIMIT_AD = 12;
const int PIN_LIMIT_DEC = 13;
const int PIN_ENABLE_AD = 14;
const int PIN_ENABLE_DEC = 27;

volatile bool limitAD_Triggered = false;
volatile bool limitDEC_Triggered = false;

// ISR — Interruption Service Routine (exécution PRIORITAIRE)
void IRAM_ATTR limitAD_ISR() {
    digitalWrite(PIN_ENABLE_AD, LOW);   // Arrêt moteur immédiat
    limitAD_Triggered = true;
}

void IRAM_ATTR limitDEC_ISR() {
    digitalWrite(PIN_ENABLE_DEC, LOW);  // Arrêt moteur immédiat
    limitDEC_Triggered = true;
}

void setup() {
    pinMode(PIN_LIMIT_AD, INPUT_PULLUP);
    pinMode(PIN_LIMIT_DEC, INPUT_PULLUP);
    pinMode(PIN_ENABLE_AD, OUTPUT);
    pinMode(PIN_ENABLE_DEC, OUTPUT);
    
    digitalWrite(PIN_ENABLE_AD, HIGH);  // Moteurs désactivés au démarrage
    digitalWrite(PIN_ENABLE_DEC, HIGH);
    
    // FALLING = contact NC qui s'ouvre (HIGH→LOW)
    attachInterrupt(digitalPinToInterrupt(PIN_LIMIT_AD), limitAD_ISR, FALLING);
    attachInterrupt(digitalPinToInterrupt(PIN_LIMIT_DEC), limitDEC_ISR, FALLING);
}

void loop() {
    if (limitAD_Triggered || limitDEC_Triggered) {
        handleLimitEvent();
        return;  // Priorité : ne pas traiter d'autres commandes
    }
    
    // Réception et traitement des commandes NINA
    if (Serial.available()) {
        processCommand(Serial.readStringUntil('#'));
    }
    
    // Logique de mouvement normale
    updateMotorControl();
}
```

#### Protocole de communication série avec NINA/ASCOM

| Commande | Fonction | Paramètre | Réponse |
|:--------:|----------|:---------:|:-------:|
| `:Gm#` | Get limit status | — | `:Gm0#` = OK / `:Gm1#` = AD / `:Gm2#` = DEC / `:Gm3#` = les deux |
| `:Rh#` | Reset homing | — | `:Rh0#` = succès / `:Rh1#` = échec |
| `:Msdddd#` | Move steps | dddd = nombre de pas | `:Ms0#` = OK / `:Ms1#` = refusé (limite active) |

#### Procédure de Homing après déclenchement

```
[Fin de course détecté par ISR]
        │
        v
[Arrêt moteur immédiat (coupure ENABLE)]
        │
        v
[Attente commande :Rh# de NINA]
        │
        v
[Commande :Rh# reçue ?]
   ├── OUI → Sortie douce de butée (500ms sens inverse)
   │         ├── Validation : capteur revenu à l'état non déclenché
   │         ├── Déplacement vers position de sécurité (+1000 pas)
   │         └── Réponse :Rh0# (succès)
   │
   └── NON → Télescope immobilisé, alerte maintenue
             → Réponse :Gm1#/2# à chaque interrogation
```

#### Intégration NINA

| Propriété ASCOM | Valeur | Effet |
|----------------|:------:|-------|
| `HasLimits` | `True` | Active la gestion des limites |
| Rapport d'état | via `CommandString(":Gm#")` | NINA interroge périodiquement |
| Réaction à l'erreur | Interruption séquence | Arrêt de la pose, fermeture caméra |
| Réarmement | Manuel uniquement | L'utilisateur doit acquitter dans NINA |

> **Configuration NINA :** Equipment > Telescope > Settings > Limits → Permet de définir les angles limites. Aucun plugin spécifique requis.

---

### 3.4 Préconisations intégrées — Risque 1

| # | Action | Pilote | Échéance | Coût |
|---|--------|--------|:--------:|:----:|
| 1 | Acheter 4× micro-switch Honeywell V15W2-EZ200 IP67 | Pilote | J+1 | 60 € |
| 2 | Câbler boucle de sécurité NC sur Alcyone-5 (EN1 + EN2) | Hardware | J+3 | 40 € |
| 3 | Ajouter bouton poussoir arrêt d'urgence rouge (contact NC en série) | Hardware | J+3 | 25 € |
| 4 | Mettre à jour firmware : ISR + Homing + commandes `:Gm`/`:Rh` | Firmware | J+7 | 0 € |
| 5 | Configurer NINA : `HasLimits = True`, angles limites | Firmware | J+7 | 0 € |
| 6 | Test de validation (collision simulée, meridian flip test) | Équipe ACO | J+10 | 0 € |
| | **Total** | | | **~125 €** |

---

## 4. ANALYSE DÉTAILLÉE — RISQUE 2 : AUTOGUIDEUR NON DOCUMENTÉ

### 4.1 Analyse des lacunes documentaires (Agent : Ethnographe)

**Constat :** Aucune information relative à l'autoguideur n'apparaît dans les trois présentations fournies (Domotisation, Mise en route, Opérations). Ce vide documentaire compromet la maintenance et l'exploitation en imagerie longue pose.

#### Questions à poser aux concepteurs

| # | Question | Priorité | Pourquoi c'est critique |
|---|----------|:--------:|-------------------------|
| **1** | Quel système d'autoguidage est utilisé ? (Guide scope séparé ? Optique hors-axe OAG ?) | 🔴 Critique | Détermine toute l'architecture optique |
| **2** | Quelle caméra de guidage ? (marque, modèle, capteur) | 🔴 Critique | Compatibilité logicielle et drivers |
| **3** | Quel logiciel de guidage ? (PHD2 ? Guidage interne NINA ? Autre ?) | 🔴 Critique | Architecture logicielle, protocole |
| **4** | Comment communique l'autoguideur avec la monture ? (ST4 direct ? ASCOM PulseGuiding ?) | 🔴 Critique | Protocole à implémenter dans le firmware |
| **5** | L'autoguideur partage-t-il le PC NUC-T600-TELE avec NINA ? | 🟡 Haute | Conflits USB, CPU, bruit |
| **6** | Existe-t-il une procédure de calibration documentée ? (fichier .txt, paramètres PHD2) | 🟡 Haute | Fichier de configuration essentiel |
| **7** | Quel est l'angle de l'autoguideur par rapport à la caméra principale ? | 🟡 Haute | Aligné (0°) ou roté ? Critique calibration |
| **8** | Y a-t-il un focuser motorisé pour l'autoguideur ? | ⚪ Moyenne | Mise au point manuelle ou motorisée ? |
| **9** | Des photos de la configuration optique existent-elles ? | ⚪ Moyenne | Permet de décoder sans démonter |

### 4.2 Analyse logicielle et protocole (Agent : Firmware expert)

#### Architecture typique d'autoguidage avec NINA

```
┌─────────┐    socket TCP:4400    ┌──────────┐
│  NINA   │◄─────────────────────►│   PHD2   │
│ (Driver │                        │ (Guidage)│
│  ASCOM) │                        └────┬─────┘
└────┬────┘                              │
     │ ASCOM PulseGuide                   │ ST4 (TTL)
     │ ou CommandString                   │
     ▼                                   ▼
┌────────────────────────────────────────────┐
│         Monture T600 (Cartes Alcyone/...)   │
└────────────────────────────────────────────┘
```

#### Comparaison des protocoles

| Critère | ST4 (TTL Pulse Guide) | ASCOM PulseGuiding |
|---------|:---------------------:|:------------------:|
| Câblage | 4 broches dédiées (RA+/RA-/DEC+/DEC-) | Aucun — même port série |
| Complexité matérielle | Carte guideur séparée nécessaire | Intégré au driver ASCOM |
| Latence | Excellente (signal direct) | Dépend du driver |
| Maintenance | Câble supplémentaire à gérer | Mise à jour logicielle uniquement |
| Documentation | Plus complexe | Standard de l'industrie |
| **Recommandation** | ❌ Déconseillé | **✅ Recommandé** |

#### Implémentation firmware du pulse guide

```cpp
void processCommand(String cmd) {
    if (cmd.startsWith(":Mg")) {           // Pulse Guide
        char direction = cmd.charAt(3);    // 'n', 's', 'e', 'w'
        int duration = cmd.substring(4).toInt();  // durée en millisecondes
        
        // ⚠ CRITIQUE : Utiliser TIMER HARDWARE, JAMAIS delay()
        executePulseGuide(direction, duration);
        Serial.print(":Mg#");              // Acquittement
    }
}

void executePulseGuide(char dir, uint16_t duration_ms) {
    // Activer la correction sur l'axe approprié
    switch(dir) {
        case 'n': startGuideTimer(DEC_PLUS, duration_ms); break;
        case 's': startGuideTimer(DEC_MINUS, duration_ms); break;
        case 'e': startGuideTimer(RA_PLUS, duration_ms); break;
        case 'w': startGuideTimer(RA_MINUS, duration_ms); break;
    }
    // Retour immédiat — PAS de blocage
}

// Timer hardware configuré pour se désactiver après duration_ms
void startGuideTimer(AxisDirection dir, uint16_t ms) {
    // Exemple avec ESP32 Timer
    timerAttachInterrupt(guideTimer, &onGuideTimeout, true);
    timerAlarmWrite(guideTimer, ms * 1000, false);  // µs
    timerAlarmEnable(guideTimer);
    
    // Appliquer la correction au driver moteur
    applyGuidePulse(dir, true);
}

void IRAM_ATTR onGuideTimeout() {
    // Désactiver la correction
    applyGuidePulse(currentGuideDir, false);
    timerDetachInterrupt(guideTimer);
}
```

#### Règles de sécurité pour l'autoguidage

| Règle | Implémentation |
|-------|---------------|
| **Timeout** | Si pulse non terminé → arrêt + erreur signalée |
| **Non-bloquant** | Zéro `delay()` dans le code de guidage |
| **Limites** | Le guidage ne peut pas dépasser les fins de course |
| **Priorité** | Mouvement de guidage prioritaire sur le suivi sidéral |

#### Risque identifié — Capacité du microcontrôleur

| Microcontrôleur | Suivi sidéral + Pulse guide + Série simultané | Action requise |
|:---------------:|:----------------------------------------------:|:--------------:|
| **ESP32** (2 cœurs) | ✅ Facile — un cœur pour communication, un pour moteurs | Aucune |
| **STM32** | ✅ Possible — timers hardware performants | Aucune |
| **Arduino Uno/Mega 8-bit** | ❌ Difficile — capacité insuffisante | **Migration ESP32** |

---

### 4.3 Préconisations intégrées — Risque 2

| # | Action | Pilote | Échéance |
|---|--------|--------|:--------:|
| 1 | Interviewer les concepteurs (9 questions clés ci-dessus) | Pilote | J+1 |
| 2 | Identifier physiquement le microcontrôleur des cartes | Firmware | J+3 |
| 3 | Choisir le protocole d'autoguidage (ASCOM PulseGuiding recommandé) | Équipe | J+5 |
| 4 | Ajouter les commandes `:Mg` au firmware si manquantes | Firmware | J+14 |
| 5 | Documenter la procédure de calibration de l'autoguideur | Équipe | J+7 |
| 6 | Tester en simulation (script Python envoyant `:Mgn0100#`) puis ciel réel | Équipe | J+21 |

---

## 5. ANALYSE DÉTAILLÉE — RISQUE 3 : ABSENCE DE PARAFOUDRE TYPE 2

### 5.1 Analyse électrique et protection (Agent : Ingénieur électricien)

**Constat :** Aucun parafoudre de type 2 (protection contre les surtensions d'origine atmosphérique) n'est documenté dans l'installation. L'OCA est situé en Ardennes, zone rurale sujette aux orages, avec une coupole métallique faisant office de capteur de foudre potentiel.

#### Analyse de vulnérabilité slide par slide

| Slide (source) | Équipement | Longueur câble | Vulnérabilité | Action corrective |
|:--------------:|------------|:--------------:|:-------------:|-------------------|
| Domotisation 4 | IPX800 + NUC | — | Aucune protection secteur, pas d'onduleur | Parafoudre Type 2 + onduleur |
| Domotisation 7-11 | Cartes cimiers émettrice/réceptrice | 10-20 m extérieur | Couplage inductif, foudre indirecte | Parafoudre ligne 24VDC |
| Domotisation 21-31 | Alcyone-5, MAIA-4, ELECTRA-5 | — | Alimentation directe non protégée | Vérifier/ajouter TVS |
| Domotisation 34 | Variateur fréquence + Encodeur dôme | Long (dôme) | Induction sur câbles moteur et signal | Filtre Schaffner + parafoudre RJ45 |
| Mise en route 1 | Caméra Foscam FI9831P-T600 (PoE) | Extérieur | Extérieur, non protégée | Parafoudre PoE |
| Mise en route 3 | Batterie cimiers (en charge permanente) | — | Charge permanente non protégée | Parafoudre batterie |

#### Schéma de protection global préconisé

```
                     RÉSEAU EDF 230V AC
                            │
              ┌─────────────────────────────┐
              │  PARAFOUDRE TYPE 2          │
              │  In ≥ 20kA  —  Up ≤ 1.5kV   │
              │  Legrand 04633 / Citel LED20 │
              └─────────────┬───────────────┘
                            │
              ┌─────────────────────────────┐
              │  DISJONCTEUR GÉNÉRAL 20A    │
              └─────────────┬───────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                  │
   ┌──────┴──────┐  ┌──────┴──────┐   ┌───────┴───────┐
   │ PRISE TYPE 3│  │ PRISE TYPE 3│   │ PRISE TYPE 3  │
   │ + ONDULEUR  │  │ + ONDULEUR  │   │   IPX800      │
   │ 1000VA      │  │ 1000VA      │   │               │
   │ PC NUC-T600 │  │PC NUC-T600- │   │               │
   │             │  │   TELE      │   │               │
   └─────────────┘  └─────────────┘   └───────┬───────┘
                                              │
                     ┌────────────────────────┼────────────┐
                     │                        │             │
              ┌──────┴──────┐          ┌──────┴──────┐  ┌──┴──────────┐
              │ PARAFOUDRE  │          │ PARAFOUDRE  │  │  FILTRE +   │
              │ LIGNE 24VDC │          │   RJ45 +    │  │  PARAFOUDRE │
              │ Citel PD-24 │          │ PoE Citel   │  │  Schaffner  │
              │ Cartes      │          │ Switch wifi │  │  Variateur  │
              │ Alcyone/... │          │ + Caméra    │  │  fréquence  │
              └─────────────┘          └─────────────┘  └─────────────┘
                                              │
                                     ┌────────┴────────┐
                                     │ CÂBLES CIMIERS  │
                                     │ PARAFOUDRE 24V  │
                                     └─────────────────┘
                     
                TOUTES LES TERRES → [PRISE DE TERRE < 10 Ω]
```

#### Spécifications techniques des équipements de protection

| Équipement | Caractéristique | Valeur requise |
|------------|----------------|:--------------:|
| **Parafoudre Type 2** | Courant nominal de décharge (In) | ≥ 20 kA (8/20 µs) |
| | Courant maximal (Imax) | ≥ 40 kA |
| | Tension de protection (Up) | ≤ 1,5 kV |
| | Tension max continue (Uc) | ≥ 275 V AC |
| | Norme | NF EN 61643-11 |
| **Prise de terre** | Résistance | **< 10 Ω** |
| **Onduleur** | Type | Ligne interactive |
| | Puissance | ≥ 1000 VA |
| | Autonomie | ≥ 5 min (fermeture propre) |

#### Références composants — Protection foudre

| Référence | Usage | Prix unitaire | Fournisseur |
|-----------|-------|:-------------:|-------------|
| **Citel LED20-20** | Parafoudre Type 2 — 20 kA, Up=1,5 kV | ~150 € | Sonelec, Rexel |
| **Legrand 046 33** | Parafoudre Type 2 — 20 kA, Up=1,5 kV | ~120 € | Legrand, Rexel |
| **APC BX1000M** | Onduleur 1000 VA ligne interactive | ~150 € | LDLC, Amazon |
| **Citel HSC-RJ45-1** | Parafoudre RJ45 — In=10 kA, Up=20 V | ~40 € | Sonelec |
| **Citel HSC-RJ45-PoE** | Parafoudre PoE — 48 V DC | ~50 € | Sonelec |
| **Citel PD-24** | Parafoudre ligne 24 V DC | ~30 € | Sonelec |
| **Citel BR-24** | Parafoudre batterie 24 V | ~35 € | Sonelec |
| **Schaffner FN258-7-07** | Filtre + parafoudre variateur 2,5 kW | ~100 € | RS Components |

---

### 5.2 Impact sur l'instrumentation (Agent : Astronome-physicien)

#### Équipements vulnérables

| Équipement | Fonction | Coût de remplacement | Risque spécifique de surtension |
|------------|----------|:--------------------:|--------------------------------|
| **Caméra principale CCD/CMOS** | Acquisition images scientifiques | **10 000 - 30 000 €** | Destruction capteur, pixels chauds permanents, circuit Peltier grillé |
| **Roue à filtres motorisée** | Changement filtres LRGB/Ha/OIII | **2 000 - 5 000 €** | Moteur grillé, perte index de position |
| **Focuser motorisé** | Mise au point automatique | **1 000 - 3 000 €** | Blocage en position → impossibilité de mise au point |
| **Autoguideur** | Guidage longue pose | **600 - 2 000 €** | Destruction totale du capteur |
| **Contrôleur de dôme** | Rotation et ouverture/fermeture | **500 - 2 000 €** | Perte de contrôle → dôme bloqué |
| **Caméra Foscam** | Supervision à distance | **100 - 500 €** | Perte de la supervision visuelle |
| **PC NUC (×2)** | Pilotage télescope et domotique | **1 500 - 3 000 €** | Perte de données, disque dur endommagé |
| | **Total instrumentation vulnérable** | **15 000 - 40 000 €** | |

#### Risques indirects (les plus dangereux)

| Risque | Scénario | Conséquence |
|--------|----------|-------------|
| **Blocage dôme ouvert** | Surtension grille le circuit de commande du dôme → impossible de fermer | Télescope exposé à la pluie, neige, condensation pendant des heures ou jours |
| **Blocage pointage haut** | Télescope bloqué à 80-90° de hauteur (près du zénith) | Accumulation de condensation sur le correcteur de champ → trace de calcaire, biofilm, dégradation optique |
| **Condensation capteur CCD** | Caméra reste allumée (refroidissement Peltier) alors que l'ambiance est humide | Microfissures dans la couche antireflet, court-circuit du Peltier par l'eau |
| **Perte de mise au point** | Focuser bloqué + variation thermique brutale (orage) | Déformation du tube (dilatation/contraction), contraintes mécaniques anormales |

---

### 5.3 Préconisations intégrées — Risque 3

| # | Action | Priorité | Coût estimé |
|---|--------|:--------:|:-----------:|
| 1 | Mesurer la résistance de la prise de terre actuelle (méthode 3 pôles) | J+1 | 0 € |
| 2 | Si R > 10 Ω : ajouter des piquets de terre (×2 1,5 m) ou conducteur cuivre nu 25 mm² | J+3 | 80-150 € |
| 3 | Installer parafoudre Type 2 au tableau général divisionnaire (Legrand 04633) | J+7 | 150-300 € |
| 4 | Ajouter prises parasurtenseurs Type 3 pour les 3 équipements critiques | J+7 | 60-150 € |
| 5 | Installer onduleurs 1000 VA (×2) pour PC NUC-T600 et NUC-T600-TELE | J+7 | 200-400 € |
| 6 | Protéger lignes réseau : parafoudre RJ45 (switch) + PoE (caméra Foscam) | J+14 | 90 € |
| 7 | Protéger câbles cimiers longue distance : parafoudre ligne 24 V DC (×2) | J+14 | 60 € |
| 8 | Ajouter filtre + parafoudre sur variateur de fréquence du dôme | J+21 | 100 € |
| | **Total** | | **~610 - 1 200 €** |

---

## 6. MATRICE DE PRIORISATION DES RISQUES

### Grille de criticité

| Score | Niveau | Action requise |
|:----:|:------:|----------------|
| 1-6 | Faible | Surveillance |
| 7-12 | Moyen | Planifier |
| 13-18 | Élevé | Action rapide |
| **19-25** | **Critique** | **Action immédiate** |

### Matrice détaillée

| Critère | Poids | **R1 : Fin de course AD/DEC** | **R2 : Autoguideur** | **R3 : Parafoudre Type 2** |
|---------|:----:|:----------------------------:|:--------------------:|:--------------------------:|
| **Probabilité** | /5 | **5** — Sans capteurs, collision inévitable à terme (meridian flip, erreur logicielle, perte de pas) | **3** — Système utilisé à chaque session, documentation absente → tout dépannage impossible | **4** — Observatoire en Ardennes, zone orageuse, coupole métallique, câbles longs extérieurs |
| **Impact** | /5 | **5** — Destruction miroir (30-50k€), caméra (10-30k€), monture | **4** — Images longue pose inexploitables (étoiles filées), nuits perdues | **5** — Destruction instrumentation (15-40k€) + risques indirects (dôme bloqué, condensation) |
| **Criticité (P×I)** | /25 | **25 — CRITIQUE** | **12 — MOYEN** | **20 — CRITIQUE** |
| **Coût correction** | /5 | **1** (~125 €) | **1** (~50 €) | **2** (~800 €) |
| **Délai de mise en œuvre** | | J+10 | J+21 | J+14 |
| **Rapport coût/bénéfice** | | **Exceptionnel** (125 € pour protéger 50 000 €) | **Bon** (50 € pour sécuriser le travail scientifique) | **Excellent** (800 € pour protéger 40 000 €) |
| **Priorité finale** | | **1** | **3** | **2** |

---

## 7. PLAN D'ACTION RECOMMANDÉ

### Phase 1 — URGENTE (avant la prochaine session d'observation)

| # | Action | Pilote | Échéance | Coût | Dépendance |
|---|--------|--------|:--------:|:----:|:----------:|
| **1.1** | 🛒 Acheter 4× micro-switch Honeywell V15W2-EZ200 IP67 | Pilote | J+1 | 60 € | — |
| **1.2** | 🔧 Câbler boucle de sécurité NC sur Alcyone-5 (EN1 + EN2) + BP urgence | Hardware | J+3 | 65 € | 1.1 |
| **1.3** | 💻 Mettre à jour firmware : ISR, Homing, commandes `:Gm`/`:Rh`, `HasLimits=True` | Firmware | J+7 | 0 € | — |
| **1.4** | 📏 Mesurer résistance de la prise de terre (multimètre méthode 3 pôles) | Hardware | J+1 | 0 € | — |
| **1.5** | ⚡ Installer parafoudre Type 2 au tableau général (Legrand 04633 ou Citel LED20) | Hardware | J+7 | 150-300 € | 1.4 |
| **1.6** | 🔌 Installer onduleurs 1000 VA (×2) pour PC NUC-T600 et NUC-T600-TELE | Hardware | J+7 | 200-400 € | — |

### Phase 2 — COURT TERME (1 mois)

| # | Action | Pilote | Échéance | Coût |
|---|--------|--------|:--------:|:----:|
| **2.1** | 💬 Interviewer les concepteurs (Christian Wanlin, Jean-Paul Dumoulin) — 13 questions clés | Pilote | J+1 | 0 € |
| **2.2** | 🔍 Identifier physiquement le microcontrôleur des cartes (ESP32 vs Arduino 8-bit vs STM32) | Firmware | J+3 | 0 € |
| **2.3** | 💻 Ajouter commandes `:Mg` (pulse guide) au firmware — protocole ASCOM PulseGuiding | Firmware | J+14 | 0 € |
| **2.4** | 🛡️ Protéger lignes réseau : parafoudre RJ45 (switch) + parafoudre PoE (caméra Foscam) | Hardware | J+14 | 90 € |
| **2.5** | 🛡️ Protéger câbles cimiers : parafoudre ligne 24 V DC (×2, aux deux extrémités) | Hardware | J+14 | 60 € |
| **2.6** | 📝 Documenter la procédure de calibration de l'autoguideur (paramètres, fichier, étapes) | Équipe | J+21 | 0 € |

### Phase 3 — MOYEN TERME (3 mois)

| # | Action | Pilote | Échéance | Coût |
|---|--------|--------|:--------:|:----:|
| **3.1** | 🛡️ Ajouter filtre Schaffner + parafoudre sur variateur de fréquence du dôme | Hardware | J+21 | 100 € |
| **3.2** | 📄 Rédiger le manuel d'utilisation complet du T600 automatisé | Rédacteur | J+60 | 50 € |
| **3.3** | 📐 Créer le schéma électrique global et le plan de câblage des cartes | Hardware | J+60 | 0 € |
| **3.4** | 🧪 Tests complets de validation : simulation collision, meridian flip, guidage, ciel réel | Équipe ACO | J+90 | 0 € |
| **3.5** | 📋 Mettre en place un registre de logs d'incidents (cahier ou fichier) | Équipe ACO | J+30 | 10 € |

### Budget consolidé

| Phase | Poste | Coût min | Coût max |
|:-----:|-------|:--------:|:--------:|
| **1** | Capteurs fin de course + câblage | 125 € | 125 € |
| **1** | Parafoudre Type 2 + installation | 150 € | 300 € |
| **1** | Onduleurs (×2) | 200 € | 400 € |
| **2** | Protection réseau RJ45 + PoE | 90 € | 90 € |
| **2** | Protection câbles cimiers 24 V DC | 60 € | 60 € |
| **3** | Filtre variateur fréquence dôme | 100 € | 100 € |
| **3** | Documentation + fournitures | 60 € | 60 € |
| | **Total** | **~785 €** | **~1 135 €** |

> **Soit un investissement de 785 € à 1 135 € pour protéger un parc instrumental de 15 000 € à 40 000 €.**

---

## 8. QUESTIONS AUX CONCEPTEURS

### Questions critiques — À traiter avant toute modification matérielle ou logicielle

#### Risque 1 : Capteurs de fin de course

| # | Question | Pourquoi c'est critique |
|---|----------|------------------------|
| **Q1** | Y a-t-il des butées mécaniques physiques sur les axes AD et DEC ? | Détermine l'urgence : si des butées existent, la collision n'est pas imminente |
| **Q2** | Quelle est l'amplitude de rotation exacte des axes AD et DEC (angles limites) ? | Permet de positionner les capteurs et de configurer NINA |
| **Q3** | Y a-t-il déjà eu des incidents de collision ? Si oui, lesquels et quels dégâts ? | Évalue la probabilité réelle |
| **Q4** | Les cartes Alcyone-5/MAIA-4/ELECTRA-5 ont-elles des entrées digitales libres (et combien) ? | Conditionne la faisabilité sans changement de carte |
| **Q5** | Que détectent exactement les diodes d'arrêt d'urgence visibles slide 19 ? | Peut indiquer une logique existante à exploiter ou étendre |
| **Q6** | Le système coupe-t-il automatiquement les moteurs si NINA se bloque ou plante ? | Watchdog présent ou non — sécurité critique |

#### Risque 2 : Autoguideur

| # | Question | Pourquoi c'est critique |
|---|----------|------------------------|
| **Q7** | Quel système d'autoguidage est installé ? (Guide scope séparé ? Optique hors-axe OAG ?) | Détermine toute l'architecture optique |
| **Q8** | Quelle est la marque et le modèle exact de la caméra de guidage ? | Compatibilité logicielle, drivers |
| **Q9** | Quel logiciel de guidage est utilisé et comment communique-t-il avec la monture ? (PHD2 via ST4 ? ASCOM PulseGuiding ?) | Protocole à implémenter ou documenter |
| **Q10** | Où est stocké le fichier de calibration de l'autoguideur (paramètres PHD2) ? | Sans ce fichier, la calibration est à refaire intégralement |

#### Risque 3 : Parafoudre

| # | Question | Pourquoi c'est critique |
|---|----------|------------------------|
| **Q11** | Y a-t-il un paratonnerre sur le bâtiment de l'observatoire ? Date de la dernière vérification ? | Protection directe foudre |
| **Q12** | Quelle est la résistance de la prise de terre (en ohms) — a-t-elle déjà été mesurée ? | < 10 Ω nécessaire pour l'efficacité du parafoudre |
| **Q13** | A-t-on déjà constaté des dommages liés à la foudre ou aux orages sur le T600 ou ses équipements ? | Évalue la probabilité réelle et le vécu du site |

---

## 9. SYNTHÈSE DES CONVERGENCES ET POINTS D'ATTENTION

### Convergences entre les 5 agents

| Point de convergence | Agents concernés | Conclusion commune |
|---------------------|-----------------|-------------------|
| **Gravité du risque R1** | Astronome + Hardware + Firmware | **Critique unanime** — priorité absolue, risque de destruction majeure |
| **Logique fail-safe** | Hardware + Firmware | Capteurs NC → coupure de fil = sécurité intrinsèque (même conclusion technique) |
| **Protocole autoguideur** | Firmware + Ethnographe | Nécessité d'identifier le protocole actuel avant toute modification |
| **Protection contre la foudre** | Hardware + Astronome | **Complémentarité** : hardware préconise l'installation, astronome justifie par la valeur de l'instrumentation |
| **Besoin de documentation** | Ethnographe + Rédacteur | **Urgence documentaire** : schémas, manuel, logs sont absents |

### Points d'attention / réserves

| Point | Agent source | Réserve | Impact si non résolu |
|-------|-------------|---------|:--------------------:|
| **Architecture exacte des cartes** | Astronome + Firmware | Les cartes Alcyone-5/MAIA-4/ELECTRA-5 sont **hypothétiques** — besoin de confirmation visuelle | Solutions à adapter après identification |
| **Microcontrôleur des cartes** | Firmware | Si Arduino 8-bit au lieu d'ESP32 → capacité multitâche insuffisante | **Migration ESP32 nécessaire** (coût supplémentaire ~50 €/carte) |
| **Protection des entrées existante** | Hardware | « Vérifier TVS » — nécessite inspection visuelle des cartes | Composants à ajouter si absents |
| **Résistance de terre** | Hardware | Donnée **inconnue** — mesure obligatoire avant installation du parafoudre | Parafoudre inefficace si terre > 10 Ω |
| **Calibration autoguideur** | Ethnographe | Aucune donnée — besoin d'interviewer impérativement | Sans calibration, l'autoguidage est inutilisable |
| **Butées mécaniques existantes** | Astronome | Si des butées existent déjà, la criticité de R1 peut être réduite | Probabilité de 5/5 → 4/5 |

---

## 10. ANNEXES

### Annexe A : Logigramme de sécurité — Fin de course

```
                     ┌───────────────────┐
                     │  DÉMARRAGE        │
                     │  FIRMWARE         │
                     └────────┬──────────┘
                              │
                              ▼
                     ┌───────────────────┐
                     │  INITIALISATION   │
                     │  µC + ISRs        │
                     │  Moteurs OFF      │
                     └────────┬──────────┘
                              │
                              ▼
                     ┌───────────────────┐
                     │  ATTENTE          │
                     │  COMMANDES NINA   │
                     │  (série ASCOM)    │
                     └────────┬──────────┘
                              │
              ┌───────────────┴───────────────┐
              │                               │
              ▼                               ▼
    ┌───────────────────┐         ┌─────────────────────┐
    │ COMMANDE          │         │ INTERRUPTION        │
    │ MOUVEMENT REÇUE   │         │ FIN DE COURSE (ISR) │
    └────────┬──────────┘         └──────────┬──────────┘
             │                               │
             ▼                               ▼
    ┌───────────────────┐         ┌─────────────────────┐
    │ FIN DE COURSE     │         │ DÉSACTIVER ENABLE   │
    │ ACTIF ?           │         │ MOTEUR (arrêt imméd.)│
    └──┬───────┬────────┘         └──────────┬──────────┘
       │       │                            │
     OUI      NON                           ▼
       │       │                  ┌─────────────────────┐
       ▼       ▼                  │ MARQUER ÉTAT        │
    ┌─────┐ ┌───────┐             │ LIMIT_ACTIVE        │
    │REFUS │ │EXÉCU-│             └──────────┬──────────┘
    │MVT + │ │TER   │                       │
    │ERREUR│ │MVT   │                       ▼
    │NINA  │ │      │             ┌─────────────────────┐
    └──┬───┘ └───────┘             │ ATTENDRE COMMANDE  │
       │                          │ HOMING (`:Rh#`)    │
       ▼                          └──────────┬──────────┘
    ┌───────────────────┐                    │
    │ ATTENDRE          │        ┌───────────┴───────────┐
    │ COMMANDE HOMING   │        │                       │
    └───────────────────┘        ▼                       ▼
                          ┌──────────────┐     ┌──────────────────┐
                          │ HOMING REÇU  │     │ PAS DE HOMING   │
                          │ RECULER DOUCE│     │ TÉLESCOPE       │
                          │ → POSITION 0 │     │ IMMOBILISÉ      │
                          │ → RÉARMER OK │     │ ALERTE MAINTENUE│
                          └──────────────┘     └──────────────────┘
```

### Annexe B : Architecture des cartes électroniques (synthèse)

| Carte | Rôle | µC probable | Entrées libres | Driver moteur | Connectique |
|-------|------|:-----------:|:--------------:|:-------------:|:----------:|
| **Alcyone-5** | Contrôle moteur AD | ESP32 | 4 opto-isolées (EN1-EN4) | TMC2209 | Bornier vis |
| **MAIA-4** | Contrôle moteur DEC | ESP32 | 4 TOR (ET1-ET4) | DRV8825/A4988 | Bornier vis |
| **ELECTRA-5** | Auxiliaire/focuser | STM32 | 2 numériques + 2 analogiques | TMC2209 | Bornier vis |

### Annexe C : Liste des composants recommandés

| # | Référence | Usage | Prix unitaire | Qté | Total | Fournisseur |
|:-:|-----------|-------|:-------------:|:---:|:----:|-------------|
| 1 | Honeywell V15W2-EZ200 | Capteur fin de course IP67 | ~15 € | 4 | 60 € | RS Components, Mouser |
| 2 | Bouton poussoir XB4-BV | Arrêt d'urgence rouge | ~25 € | 1 | 25 € | Schneider, Rexel |
| 3 | Câble blindé 2×0,5mm² | Câblage capteurs | ~2 €/m | 20 m | 40 € | Rexel, Distrelec |
| 4 | Diode TVS P6KE24A | Protection ESD entrées | ~1 € | 10 | 10 € | Mouser, Farnell |
| 5 | Citel LED20-20 | Parafoudre Type 2 20 kA | ~150 € | 1 | 150 € | Sonelec, Rexel |
| 6 | Legrand 046 33 | Parafoudre Type 2 20 kA | ~120 € | 1 | 120 € | Legrand, Rexel |
| 7 | APC BX1000M | Onduleur 1000 VA | ~150 € | 2 | 300 € | LDLC, Amazon |
| 8 | Citel HSC-RJ45-1 | Parafoudre RJ45 | ~40 € | 1 | 40 € | Sonelec |
| 9 | Citel HSC-RJ45-PoE | Parafoudre PoE | ~50 € | 1 | 50 € | Sonelec |
| 10 | Citel PD-24 | Parafoudre ligne 24 V DC | ~30 € | 2 | 60 € | Sonelec |
| 11 | Schaffner FN258-7-07 | Filtre variateur fréquence | ~100 € | 1 | 100 € | RS Components |

### Annexe D : Tableau de bord — Suivi des actions

| Action | Statut | Pilote | Date butoir | Date réalisation | Commentaire |
|--------|:-----:|--------|:-----------:|:----------------:|-------------|
| 1.1 Achat capteurs | 🔴 À faire | Pilote | J+1 | — | |
| 1.2 Câblage boucle NC | 🔴 À faire | Hardware | J+3 | — | |
| 1.3 Màj firmware ISR | 🔴 À faire | Firmware | J+7 | — | |
| 1.4 Mesure terre | 🔴 À faire | Hardware | J+1 | — | |
| 1.5 Parafoudre Type 2 | 🔴 À faire | Hardware | J+7 | — | |
| 1.6 Onduleurs | 🔴 À faire | Hardware | J+7 | — | |
| 2.1 Interview concepteurs | 🔴 À faire | Pilote | J+1 | — | |
| 2.2 Identifier µC cartes | 🔴 À faire | Firmware | J+3 | — | |
| 2.3 Commandes `:Mg` firmware | 🔴 À faire | Firmware | J+14 | — | |
| 2.4 Protection RJ45/PoE | 🔴 À faire | Hardware | J+14 | — | |
| 2.5 Protection cimiers 24V | 🔴 À faire | Hardware | J+14 | — | |
| 2.6 Documentation autoguideur | 🔴 À faire | Équipe | J+21 | — | |
| 3.1 Filtre variateur dôme | 🔴 À faire | Hardware | J+21 | — | |
| 3.2 Manuel utilisateur T600 | 🔴 À faire | Rédacteur | J+60 | — | |
| 3.3 Schéma électrique global | 🔴 À faire | Hardware | J+60 | — | |
| 3.4 Tests validation | 🔴 À faire | Équipe | J+90 | — | |

### Annexe E : Glossaire

| Terme | Définition |
|-------|-----------|
| **AD** | Ascension Droite — axe de rotation est-ouest de la monture |
| **DEC** | Déclinaison — axe de rotation nord-sud de la monture |
| **ASCOM** | Standard de communication pour l'astronomie amateur/professionnelle |
| **NINA** | Nighttime Imaging 'N' Astronomy — logiciel d'acquisition et pilotage |
| **PHD2** | Push Here Dummy 2 — logiciel d'autoguidage open source |
| **IPX800** | Contrôleur de relais Ethernet programmable (domotique) |
| **Monture allemande** | Type de monture équatoriale avec contrepoids |
| **Meridian Flip** | Changement de côté de la monture lors du passage au méridien |
| **ISR** | Interruption Service Routine — routine prioritaire du µC |
| **Fail-safe** | Mode de défaillance sécurisé — l'équipement se met en sécurité |
| **NC** | Normalement Fermé — contact fermé au repos |
| **Homing** | Procédure de recherche de la position de référence |
| **Gray code** | Code binaire réfléchi pour encodeur de position |
| **PulseGuiding** | Technique de correction du suivi par impulsions courtes |
| **OAG** | Off-Axis Guider — autoguideur hors-axe |
| **PoE** | Power over Ethernet — alimentation sur câble réseau |
| **TVS** | Transient Voltage Suppressor — diode de protection contre les surtensions |
| **µC** | Microcontrôleur |

---

## 11. PROCHAINES ÉTAPES

```
┌─────────────────────────────────────────────────────────────────┐
│                    PLAN D'ACTION — PROCHAINES ÉTAPES            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  🔴 ÉTAPE 1 — VALIDATION (J+0)                                  │
│  ├── Valider ce rapport avec Christian Wanlin & Jean-Paul Dumoulin│
│  └── Obtenir les réponses aux 13 questions clés (Section 8)      │
│                                                                  │
│  🟡 ÉTAPE 2 — PHASE URGENTE (J+1 à J+10)                        │
│  ├── Acheter et câbler les capteurs de fin de course            │
│  ├── Mettre à jour le firmware (ISR + Homing)                   │
│  ├── Mesurer la résistance de terre et installer le parafoudre  │
│  └── Installer les onduleurs                                     │
│                                                                  │
│  🟢 ÉTAPE 3 — PHASE COURT TERME (J+10 à J+30)                   │
│  ├── Interviewer les concepteurs pour documenter l'autoguideur  │
│  ├── Ajouter le pulse guide au firmware                         │
│  ├── Protéger les lignes réseau et les câbles cimiers           │
│  └── Documenter la calibration de l'autoguideur                 │
│                                                                  │
│  🔵 ÉTAPE 4 — PHASE MOYEN TERME (J+30 à J+90)                   │
│  ├── Ajouter le filtre sur le variateur de fréquence du dôme    │
│  ├── Rédiger le manuel utilisateur complet du T600              │
│  ├── Créer le schéma électrique global                          │
│  └── Tests complets de validation                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

*Analyse d'aide à la décision — hors implémentation.*

**Document produit par le Bureau ACO — Observatoire Centre Ardennes**
**Équipe :** Astronome-physicien | Ingénieur électricien | Firmware expert | Ethnographe | Rédacteur technique
**Contact :** Orchestrateur OCA — Pour tout approfondissement technique (schémas détaillés, code complet, devis fournisseurs)