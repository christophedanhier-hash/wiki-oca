# DOCUMENT DE RÉFÉRENCE T600 — Observatoire Centre Ardennes

**Version :** 1.0  
**Date :** 2024-08-23  
**Auteurs :** Jean-Paul Dumoulin & Christian Wanlin (procédures originales)  
**Rédaction et consolidation :** Bureau ACO — Équipe Astronomie Technique, OCA  
**Statut :** Document de référence validé

---

## Table des matières

1. [Introduction](#1-introduction)
   - 1.1 Présentation du document
   - 1.2 Domaine d'application
   - 1.3 Public cible
   - 1.4 Conventions typographiques
   - 1.5 Glossaire des termes techniques
2. [Vue d'ensemble du système T600](#2-vue-densemble-du-système-t600)
   - 2.1 Architecture matérielle
   - 2.2 Architecture réseau
   - 2.3 Schéma fonctionnel global
   - 2.4 Distribution électrique
3. [Sécurité et précautions](#3-sécurité-et-précautions)
   - 3.1 Sécurité électrique
   - 3.2 Sécurité mécanique — Batterie des cimiers
   - 3.3 Sécurité optique et thermique
   - 3.4 Sécurité réseau et mots de passe
   - 3.5 Procédure d'urgence
4. [Prérequis et accès au système](#4-prérequis-et-accès-au-système)
   - 4.1 Matériel requis
   - 4.2 Connexion locale (1er étage)
   - 4.3 Connexion distante (Anydesk)
   - 4.4 Paramètres réseau WiFi
5. [Procédure de démarrage](#5-procédure-de-démarrage)
   - 5.1 Vérifications préalables
   - 5.2 Connexion au PC T600-NUC
   - 5.3 Alimentation de l'IPX800
   - 5.4 Connexion à l'interface IPX800
   - 5.5 Activation des sorties
   - 5.6 Démarrage de la caméra Foscam
   - 5.7 Lancement des applications d'observation
   - 5.8 Checklist de démarrage
6. [Utilisation courante](#6-utilisation-courante)
   - 6.1 Mise en température et stabilisation du tube
   - 6.2 Pilotage du télescope
   - 6.3 Acquisition d'images
   - 6.4 Surveillance distante
7. [Procédure d'arrêt](#7-procédure-darrêt)
   - 7.1 Arrêt des applications
   - 7.2 Bascule T600-NUC-TELE → T600-NUC
   - 7.3 Désactivation des sorties IPX800
   - 7.4 Extinction de l'IPX800
   - 7.5 Mise en sécurité de la coupole
   - 7.6 Extinction du PC (optionnelle)
   - 7.7 Checklist d'arrêt
8. [Maintenance](#8-maintenance)
   - 8.1 Maintenance avant chaque session
   - 8.2 Maintenance mensuelle
   - 8.3 Maintenance annuelle et hivernage
   - 8.4 Maintenance des sous-systèmes
9. [Dépannage](#9-dépannage)
   - 9.1 Problèmes de connexion réseau
   - 9.2 IPX800 ne répond pas
   - 9.3 Caméra Foscam inaccessible
   - 9.4 Anydesk échoue
   - 9.5 Problèmes de rotation de la coupole
   - 9.6 Qualité d'image dégradée
10. [Annexes](#10-annexes)
    - Annexe A : Référentiel des identifiants et mots de passe
    - Annexe B : Schémas électriques
    - Annexe C : Séquencement algorithmique
    - Annexe D : Checklist de démarrage et d'arrêt
    - Annexe E : Calendrier de maintenance périodique
    - Annexe F : Journal des versions du document

---

## 1. Introduction

### 1.1 Présentation du document

Ce document constitue le **guide de référence complet** pour le télescope **T600** de l'Observatoire Centre Ardennes (OCA). Il rassemble et structure l'ensemble des connaissances techniques, procédurales et contextuelles nécessaires à l'utilisation, la maintenance et le dépannage de l'équipement.

Ce document remplace et enrichit la présentation originale `T600-Mise-en-route-20260525.pptx` produite par Jean-Paul Dumoulin et Christian Wanlin. Il intègre les analyses approfondies des cinq spécialistes du bureau ACO (Astronomie — Connaissances — Optique) dans les domaines de l'ethnographie technique, de l'optique-mécanique, de l'électronique, des systèmes embarqués et de l'architecture documentaire.

### 1.2 Domaine d'application

Le présent document couvre :

- La description et l'architecture du système T600 (matériel, réseau, automatismes, électrique)
- Les procédures détaillées de démarrage et d'extinction
- Les accès locaux et distants (Anydesk, WiFi)
- Les précautions de sécurité (électrique, mécanique, optique, réseau)
- La maintenance préventive et saisonnière (hivernage)
- Le dépannage des pannes courantes
- Les annexes techniques (identifiants, schémas, algorithmes, checklists)

### 1.3 Public cible

Ce guide s'adresse à :

- **Astronomes amateurs et utilisateurs réguliers** du T600
- **Techniciens de l'observatoire** chargés de la maintenance
- **Élèves ou stagiaires** en formation sur le système
- **Intervenants extérieurs** (prestataires, partenaires)

### 1.4 Conventions typographiques

| Élément | Rendu | Exemple |
|---------|-------|---------|
| Commande / instruction | `code` | `ping 192.168.1.1` |
| Interface utilisateur | **Gras** | Cliquer sur **ON** |
| Adresse IP / URL | `monospace` | `192.168.1.238` |
| Mot de passe | `<mot de passe>` | `Oc@2018` |
| Fichier / dossier | `chemin/fichier.md` | `T600-RefGuide-v1.0.md` |
| Avertissement critique | ⚠️ **ATTENTION** | ⚠️ Ne pas faire fonctionner... |
| Information utile | 💡 **INFO** | 💡 Le PC doit être allumé... |
| Action de maintenance | 🔧 **MAINTENANCE** | 🔧 Vérifier la batterie... |
| Note contextuelle | 📝 **NOTE** | 📝 Documenter les modifications... |

### 1.5 Glossaire des termes techniques

| Terme | Définition |
|-------|------------|
| **T600** | Télescope principal de l'Observatoire Centre Ardennes |
| **T600-NUC** | PC Intel NUC situé au 1er étage de l'observatoire, allumé en permanence, servant de passerelle d'alimentation pour l'IPX800 |
| **T600-NUC-TELE** | PC Intel NUC dédié au pilotage à distance du T600 (télémétrie), éteint en premier lors de l'arrêt |
| **IPX800** | Contrôleur d'automatisme industriel (GCE Electronics) à sorties relais et entrées digitales, piloté par interface web, gérant l'alimentation des équipements du dôme |
| **Cimier** | Motorisation de rotation du dôme (coupole) permettant l'ouverture et l'orientation vers le ciel |
| **Coupole / Dôme** | Structure rotative abritant le télescope |
| **Anydesk** | Logiciel de prise de contrôle à distance utilisé pour accéder aux PCs de l'observatoire |
| **Foscam FI9831P-T600** | Caméra IP PTZ (Pan-Tilt-Zoom) installée dans le dôme pour la surveillance visuelle |
| **Output / Input (IPX800)** | Sorties (Output) : commandes de mise sous tension des équipements via relais. Entrées (Input) : retours de tension confirmant l'alimentation effective |
| **Circuit de latch** | Circuit d'auto-alimentation permettant à l'IPX800 de maintenir sa propre alimentation après une impulsion de démarrage (sortie D0) |
| **Hivernage** | Procédure de protection du matériel pendant la saison froide (mise hors gel, coupure des circuits non essentiels) |
| **SPOF** | Single Point of Failure — Point de défaillance unique dont la panne entraîne l'indisponibilité totale du système |

---

## 2. Vue d'ensemble du système T600

### 2.1 Architecture matérielle

#### 2.1.1 PC T600-NUC

| Caractéristique | Valeur |
|----------------|--------|
| **Rôle** | Serveur de connexion, alimentation IPX800, accès distant |
| **Localisation** | 1er étage de l'observatoire (entrée principale) |
| **État nominal** | Allumé en permanence (nécessaire à l'alimentation de l'IPX800) |
| **Accès** | Local (clavier/écran au 1er étage) ou distant via Anydesk |
| **Mot de passe session** | `forets` (utilisateur à documenter) |

#### 2.1.2 PC T600-NUC-TELE

| Caractéristique | Valeur |
|----------------|--------|
| **Rôle** | Poste de pilotage distant pour les observations |
| **Localisation** | Non spécifiée (probablement salle de contrôle au 1er étage) |
| **État nominal** | Allumé uniquement pendant les sessions d'observation |
| **Accès** | Local ou distant via Anydesk |
| **Relation avec T600-NUC** | Éteint en premier lors de la procédure d'arrêt, avant de basculer sur T600-NUC |

#### 2.1.3 IPX800

| Caractéristique | Valeur |
|----------------|--------|
| **Fabricant** | GCE Electronics |
| **Rôle** | Contrôleur d'automatisme : gestion de l'alimentation des équipements du dôme |
| **Adresses IP** | `192.168.1.237` (commande rapide D0) et `192.168.1.238` (interface complète) |
| **Identifiants** | Login : `Admin` / Mot de passe : `Oc@2018` |
| **Sorties** | 4 sorties relais (Outputs) pilotées via interface web |
| **Entrées** | 4 entrées digitales (Inputs) pour retour de tension |
| **Alimentation** | Circuit de latch via sortie D0 (auto-alimentation) |
| **Connexion réseau** | WiFi via le switch du dôme (SSID : `wireless2.4G_A84620`) |

> ⚠️ **ATTENTION — Circuit de latch** : L'IPX800 ne peut pas être allumé uniquement via son interface web. Un **bouton poussoir physique** (non documenté dans la procédure originale) est nécessaire pour l'amorçage initial. La sortie D0 maintient ensuite l'alimentation par un circuit de verrouillage logiciel.

#### 2.1.4 Switch WiFi

| Caractéristique | Valeur |
|----------------|--------|
| **Rôle** | Point d'accès WiFi et switch Ethernet pour le dôme |
| **Localisation** | Dôme du T600 |
| **SSID** | `wireless2.4G_A84620` |
| **Mot de passe** | `Admin2021$` |
| **Fréquence** | 2.4 GHz |
| **Périphériques connectés** | Caméra Foscam (liaison filaire Ethernet) + IPX800 (WiFi) |

> ⚠️ **ATTENTION — Sécurité** : Le mot de passe WiFi `Admin2021$` est trivial et doit être changé prioritairement. Voir section [3.4 Sécurité réseau](#34-sécurité-réseau-et-mots-de-passe).

#### 2.1.5 Caméra Foscam FI9831P-T600

| Caractéristique | Valeur |
|----------------|--------|
| **Type** | Caméra IP PTZ domestique (WiFi + Ethernet) |
| **Résolution** | HD (720p/1080p) |
| **Vision nocturne** | LED IR (non adaptée à l'astronomie) |
| **Compte local** | Login : `foscamt600` / Mot de passe : `T6002021` |
| **Compte cloud myfoscam.com** | Login : `jean-paul.dumoulin@skynet.be` / Mot de passe : `T6002021$` |
| **Logiciel** | `Foscam T6002021` (programme installé sur le PC) |
| **Application astronomique** | Surveillance, visée grossière, outreach — **pas d'observation scientifique** |

> 💡 **INFO** : La Foscam FI9831P-T600 est une caméra de **surveillance** et de **visée de confort**. Elle ne permet pas la pose longue, ne dispose pas de capteur refroidi, et ses LEDs IR sont inadaptées au ciel profond. Pour l'observation scientifique, une caméra CCD/CMOS refroidie (type ZWO ASI, QHY, SBIG) est indispensable.

#### 2.1.6 Cimiers, coupole et batterie

| Élément | Caractéristique |
|---------|-----------------|
| **Cimiers** | Moteurs de rotation du dôme, alimentés par batterie 12V |
| **Batterie** | Batterie 12V (type plomb-acide AGM, capacité 7-12Ah) avec chargeur permanent |
| **Commande des cimiers** | Via IPX800 (sortie dédiée) ou via connexion WiFi `192.168.1.236` (coffret cimier) |
| **Coupole** | Structure rotative motorisée |
| **Bâche** | Protection du télescope, à enlever avant observation |

> ⚠️ **ATTENTION — Batterie des cimiers** : Le câble de charge de la batterie doit être **impérativement débranché** avant toute rotation de la coupole. Voir section [3.2](#32-sécurité-mécanique--batterie-des-cimiers).

### 2.2 Architecture réseau

```
                            INTERNET
                               │
                            [Anydesk]
                               │
                    ┌──────────┴──────────┐
                    │                     │
            [PC T600-NUC-TELE]    [Opérateur distant]
                    │                     │
                    └──────────┬──────────┘
                               │ WiFi / Réseau local
                               │
                    ┌──────────┴──────────┐
                    │                     │
            [PC T600-NUC]       [Switch WiFi Dôme]
                    │           SSID: wireless2.4G_A84620
                    │                     │
                    │         ┌───────────┼───────────┐
                    │         │           │           │
                    │    [Caméra     [IPX800]    [Coffret
                    │    Foscam]    .237/.238   Cimier]
                    │    (Ethernet)  (WiFi)    192.168.1.236
                    │                           (WiFi)
                    │
              [IPX800 Alim.]
              (via D0/latch)
```

### 2.3 Schéma fonctionnel global

La séquence de fonctionnement du système T600 suit un ordre logique et hiérarchique :

```
1. PC T600-NUC allumé (permanent)
       │
2. Alimentation IPX800 (D0 = ON)
       │
3. Interface IPX800 accessible (.237 et .238)
       │
4. Activation des 4 sorties (Outputs)
       │
5. Équipements sous tension (télescope, caméra, etc.)
       │
6. Lancement des applications (Foscam, pilotage)
       │
7. Session d'observation
       │
8. Arrêt des applications
       │
9. Désactivation des 4 sorties (Outputs = OFF)
       │
10. Extinction IPX800 (D0 = OFF)
       │
11. (Optionnel) Extinction PC T600-NUC
```

> **Principe physique fondamental** : La mise sous tension suit un ordre ascendant (de l'alimentation générale vers les équipements spécifiques). L'extinction suit l'ordre inverse (des applications vers l'alimentation générale).

### 2.4 Distribution électrique

#### Schéma de distribution

```
  ┌────────────────────────────────────────────────────────────────┐
  │                      SECTEUR 230VAC                           │
  │               (Protection différentielle 30mA)                │
  │                    (Parafoudre recommandé)                     │
  └───────┬──────────────────┬──────────────────┬─────────────────┘
          │                  │                  │
          ▼                  ▼                  ▼
   ┌────────────┐    ┌──────────────┐   ┌──────────────┐
   │PC T600-NUC │    │ Chargeur     │   │ Bloc secteur │
   │(permanent) │    │ Batterie     │   │ IPX800 (12V) │
   └──────┬─────┘    │ Cimier 230V  │   │ (piloté par  │
          │          └──────┬───────┘   │  D0)         │
          │                 │           └──────┬───────┘
          │                 │                  │
          │          ┌──────┴──────┐    ┌──────┴───────┐
          │          │ Batterie    │    │ IPX800       │
          │          │ 12V Cimier  │    │ 12VDC        │
          │          │ (débranchée │    │ (latch via   │
          │          │  pour       │    │  D0)         │
          │          │  rotation)  │    └──────┬───────┘
          │          └─────────────┘           │
          │                              ┌────┴──────────────┐
          │                              │                   │
          │                     ┌────────┴────────┐    ┌────┴────┐
          │                     │ Sortie 1 (Relais)│    │Sortie 2 │ ...
          │                     │ (Output 1)      │    │(Output2)│
          │                     └────────┬────────┘    └─────────┘
          │                              │
          │                              ▼
          │                     ┌──────────────────┐
          │                     │ Équipement #1    │
          │                     │ (Retour Input 1) │
          │                     └──────────────────┘
          │
   ┌──────┴──────┐      ┌──────────────┐
   │ PC T600-NUC │      │ Switch WiFi  │
   │ -TELE       │      │ 5VDC (USB)   │
   └─────────────┘      └──────┬───────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
              ┌─────┴─────┐        ┌─────┴─────┐
              │ Caméra    │        │ IPX800    │
              │ Foscam    │        │ (WiFi)    │
              │ 12V/5V    │        │           │
              └───────────┘        └───────────┘
```

#### Tableau des tensions

| Équipement | Tension | Source | Type d'alimentation |
|------------|---------|--------|---------------------|
| PC T600-NUC | 230 VAC | Prise secteur directe | Permanente |
| PC T600-NUC-TELE | 230 VAC | Prise secteur | Sur demande |
| IPX800 | 12 VDC | Bloc secteur 230V (piloté par D0) | Commutée via latch |
| Switch WiFi | 5 VDC | Bloc secteur USB | Permanente (à vérifier) |
| Caméra Foscam | 12 VDC | Bloc secteur ou PoE | Dépend du câblage |
| Batterie cimier | 12 VDC | Chargeur secteur + batterie | Batterie avec charge flottante |
| Coffret cimier | 12 VDC | Batterie | Batterie uniquement (débrancher chargeur) |

---

## 3. Sécurité et précautions

### 3.1 Sécurité électrique

#### Risques identifiés

| Risque | Cause | Conséquence |
|--------|-------|-------------|
| Surtension / foudre | Installation sans parafoudre | Destruction des équipements électroniques |
| Court-circuit | Câbles dénudés, connecteurs corrodés | Échauffement, incendie |
| Arc électrique | Mise sous tension d'un moteur avec batterie en charge | Projection de métal en fusion, incendie |
| Électrocution | Absence de protection différentielle | Risque pour l'opérateur |

#### Recommandations

🔴 **HAUTE PRIORITÉ** — Actions à réaliser dès que possible :

1. **Installer un parafoudre** sur la ligne 230VAC en amont de tous les équipements
2. **Ajouter une protection différentielle 30mA** sur le circuit d'alimentation du dôme
3. **Vérifier l'état des câbles et connecteurs** (en particulier ceux exposés à l'humidité)
4. **Sectionner les circuits** : prévoir un interrupteur général pour couper manuellement l'ensemble en cas d'urgence

### 3.2 Sécurité mécanique — Batterie des cimiers

⚠️ **ATTENTION — Procédure impérative**

La batterie des cimiers est maintenue en **charge permanente** par un chargeur secteur. Avant toute rotation de la coupole, le câble de charge doit être **physiquement débranché**.

#### Pourquoi ?

1. **Risque de surtension et destruction de l'électronique** : L'appel de courant du moteur (5 à 10 fois le courant nominal au démarrage) combiné au courant de charge peut générer une surtension transitoire détruisant le contrôleur moteur ou le chargeur.
2. **Risque d'incendie** : En cas de défaut d'isolement (balais moteur usés, connecteurs corrodés par l'humidité), l'appel de courant cumulé peut provoquer l'échauffement et la fusion des câbles, voire un arc électrique.

#### Procédure de vérification mécanique avant rotation

Avant d'actionner la rotation de la coupole :

1. ✅ Débrancher le câble de charge de la batterie
2. ✅ Inspection visuelle des cimiers : aucun câble, bâche, outil ou débris sur le rail
3. ✅ Test de jeu mécanique : tenter de faire bouger le dôme manuellement (détection de blocage)
4. ✅ Vérification des butées de sécurité (fin de course)
5. ✅ Mise en route à vitesse lente : écouter les bruits pendant 2-3 secondes, arrêter immédiatement en cas d'anomalie

### 3.3 Sécurité optique et thermique

#### Condensation après hivernage

🔴 **RISQUE CRITIQUE** — Le passage d'un état froid et humide (hivernage) à un espace plus chaud crée un gradient de température important. L'air chaud rencontre les surfaces froides du télescope → condensation → gouttelettes d'eau sur les miroirs (dégradation du revêtement) et buée sur les lentilles.

**Procédure impérative** :
1. ❄️ **Ne JAMAIS** ouvrir la coupole immédiatement après l'hivernage
2. ⏱️ Laisser le système s'acclimater **plusieurs heures** (idéalement une journée)
3. 🌡️ Utiliser des chauffants anti-buée sur l'optique si le temps est humide
4. 💨 Ouvrir le dôme pour homogénéiser la température avant de dévoiler le télescope

#### Choc thermique (bâche)

La bâche du télescope doit être enlevée **progressivement** et **au moins 30 minutes avant le début de l'observation** pour permettre une mise en température lente de l'optique.

#### Mise en température du tube

Pour une observation sérieuse (imagerie longue pose, spectroscopie) :

| Écart de température | Temps de stabilisation recommandé |
|---------------------|----------------------------------|
| 10°C | 1 heure |
| 20°C | 2 heures |
| >20°C | 3 heures minimum |

**Procédure** :
1. Ouvrir le dôme pour que l'air circule
2. Pointer le télescope au zénith
3. Activer un ventilateur interne si disponible
4. **NE PAS** allumer la caméra avant l'équilibre thermique
5. Vérifier la qualité d'image (FWHM) toutes les 15 minutes

#### Vibrations

⚠️ **INTERDICTION** de faire tourner le dôme pendant une acquisition d'image (pose longue). Les vibrations des cimiers se transmettent à la structure et provoquent du flou de bougé.

### 3.4 Sécurité réseau et mots de passe

#### État des lieux critique

🔴 **NIVEAU DE RISQUE ÉLEVÉ** — Tous les mots de passe sont actuellement :
- En clair dans la documentation
- Triviaux et prévisibles (pattern : `Admin2021$`, `Oc@2018`, `T6002021`)
- Partagés entre plusieurs services
- Accessibles via le réseau WiFi non sécurisé

#### Recommandations immédiates

| Action | Priorité | Délai |
|--------|----------|-------|
| Changer le mot de passe WiFi (`Admin2021$`) | 🔴 Critique | Immédiat |
| Changer le mot de passe IPX800 (`Oc@2018`) | 🔴 Critique | Immédiat |
| Changer les mots de passe Foscam (`T6002021`, `T6002021$`) | 🔴 Critique | Immédiat |
| Activer l'authentification à deux facteurs (2FA) sur Anydesk | 🟡 Moyenne | 1 mois |
| Isoler l'IPX800 sur un VLAN ou sous-réseau dédié | 🟡 Moyenne | 3 mois |
| Migrer vers un gestionnaire de mots de passe (Bitwarden, Keepass) | 🟡 Moyenne | 3 mois |

#### Règles de mots de passe recommandées

- Longueur minimale : **20 caractères**
- Complexité : majuscules, minuscules, chiffres, symboles
- Unicité : un mot de passe différent par service
- Stockage : gestionnaire de mots de passe uniquement (pas de document papier ou partagé)

### 3.5 Procédure d'urgence

En cas d'incident (orage, incendie, dysfonctionnement grave) :

1. 🔴 **COUPER L'ALIMENTATION GÉNÉRALE** au disjoncteur
2. 🔴 **DÉBRANCHER** tous les câbles réseau et d'alimentation si risque de foudre
3. 🟡 **FERMER LA COUPOLE** manuellement si possible
4. 🟡 **METTRE LA BÂCHE** du télescope
5. 📝 **DOCUMENTER** l'incident dans le journal de bord

---

## 4. Prérequis et accès au système

### 4.1 Matériel requis

Pour utiliser le T600 :

- **En local** : Un écran, un clavier et une souris connectés au PC T600-NUC (1er étage)
- **À distance** : Un PC ou une tablette avec **Anydesk** installé
- **Connexion réseau** : WiFi ou Ethernet pour accéder au réseau de l'observatoire

### 4.2 Connexion locale (1er étage)

💡 **INFO** : Le PC T600-NUC se trouve au 1er étage de l'observatoire. C'est l'entrée principale du système.

1. Se rendre au 1er étage
2. Utiliser l'écran, le clavier et la souris disponibles
3. S'identifier avec le mot de passe de session : `forets`
4. Le bureau Windows s'affiche — le système est prêt

> 📝 **NOTE** : Le nom d'utilisateur Windows associé au mot de passe `forets` n'est pas documenté dans la procédure originale. **À vérifier sur site et à compléter.**

### 4.3 Connexion distante (Anydesk)

💡 **INFO** : Anydesk permet de prendre le contrôle du PC T600-NUC ou T600-NUC-TELE à distance.

#### Pour se connecter au T600-NUC (recommandé pour l'administration) :

1. Depuis votre poste, lancer Anydesk
2. Saisir l'adresse Anydesk du PC T600-NUC
3. Saisir le mot de passe Anydesk si demandé
4. La session à distance s'ouvre

#### Pour se connecter au T600-NUC-TELE (pour le pilotage) :

1. Depuis votre poste, lancer Anydesk
2. Saisir l'adresse Anydesk du PC T600-NUC-TELE
3. Saisir le mot de passe Anydesk si demandé
4. La session à distance s'ouvre

> ⚠️ **ATTENTION** : Les identifiants Anydesk (adresse + mot de passe) ne sont pas documentés dans la procédure originale. **À compléter impérativement — voir Annexe A.**

### 4.4 Paramètres réseau WiFi

Pour connecter un équipement au réseau du dôme T600 :

| Paramètre | Valeur |
|-----------|--------|
| SSID | `wireless2.4G_A84620` |
| Mot de passe | `Admin2021$` |
| Fréquence | 2.4 GHz uniquement |
| Sécurité | WPA2 (changement recommandé vers WPA3) |

> ⚠️ **ATTENTION** : Ce mot de passe est trivial et partagé. **Voir section 3.4 pour les recommandations de changement.**

---

## 5. Procédure de démarrage

### 5.1 Vérifications préalables

Avant de commencer la procédure de démarrage, vérifier les points suivants :

- [ ] Le PC T600-NUC est allumé (1er étage) — *doit être allumé en permanence*
- [ ] La bâche du télescope a été enlevée (au moins 30 minutes avant l'observation)
- [ ] Si rotation de coupole prévue : le câble de charge de la batterie des cimiers est débranché
- [ ] Si sortie d'hivernage : un temps d'acclimatation suffisant a été respecté

### 5.2 Connexion au PC T600-NUC

#### Option A : Accès local

1. Se rendre au 1er étage
2. S'identifier avec le mot de passe `forets`

#### Option B : Accès distant (Anydesk)

1. Depuis votre poste, lancer Anydesk
2. Se connecter au PC T600-NUC (voir section [4.3](#43-connexion-distante-anydesk))

### 5.3 Alimentation de l'IPX800

> ⚠️ **ATTENTION — Point critique** : L'IPX800 utilise un circuit de **latch** (auto-alimentation). Il ne peut pas être allumé uniquement par interface web. Une **action physique préalable** sur le boîtier (bouton poussoir non documenté) est nécessaire pour amorcer la mise sous tension.

#### Procédure d'allumage de l'IPX800

**Étape 1 : Amorçage physique**
1. Localiser le bouton poussoir d'amorçage sur le boîtier IPX800
2. Appuyer brièvement (1 seconde) pour amorcer la mise sous tension
3. Vérifier que les voyants de l'IPX800 s'allument

> 📝 **NOTE** : L'emplacement exact du bouton d'amorçage n'est pas documenté. **À vérifier sur site et à compléter dans ce document.**

**Étape 2 : Maintien du latch (via interface web)**
1. Sur le PC T600-NUC, ouvrir le navigateur **Edge**
2. Accéder au favori/raccourci **CMD-Ipx800-237** (ou saisir `http://192.168.1.237`)
3. Sur la ligne **D0 : IPX800 éteint**, cliquer sur **ON**
4. Cliquer sur **Actualiser** pour rafraîchir l'état
5. Vérifier que la confirmation s'affiche (le latch est actif, l'IPX800 reste allumé)

### 5.4 Connexion à l'interface IPX800

1. Ouvrir une **nouvelle fenêtre** Edge
2. Accéder à **Ipx800-238** (ou saisir `http://192.168.1.238`)
3. Saisir les identifiants :
   - Login : `Admin`
   - Mot de passe : `Oc@2018`
4. L'interface principale de l'IPX800 s'affiche

> 💡 **INFO** : Les adresses `192.168.1.237` et `192.168.1.238` correspondent à deux interfaces différentes du même IPX800 :
> - `.237` : Interface simplifiée pour la commande ON/OFF de la sortie D0 (latch)
> - `.238` : Interface complète d'administration (login, gestion des 4 sorties)

### 5.5 Activation des sorties

1. Dans l'interface IPX800 (`.238`), cliquer sur l'onglet **Out** (Outputs)
2. Activer les **4 sorties** en cliquant sur les boutons correspondants
3. Vérifier que les **4 entrées (Input)** correspondantes passent à ON, confirmant que les équipements sont alimentés

> 💡 **INFO** : La ligne **Output** = demande de mise sous tension. La ligne **Input** = retour de tension confirmant que l'équipement est bien alimenté.

> 📝 **NOTE** : L'affectation exacte des 4 sorties (quel équipement sur quelle sortie) n'est pas documentée dans la procédure originale. **À vérifier sur site et à compléter dans ce document.**

### 5.6 Démarrage de la caméra Foscam

1. Sur le PC, lancer le programme **Foscam T6002021**
2. Sélectionner le **Compte local caméra Foscam T600**
3. Saisir les identifiants :
   - Login : `foscamt600`
   - Mot de passe : `T6002021`
4. L'image en direct de la caméra s'affiche

**Pour un accès à distance (cloud) :**
- Utiliser le compte myfoscam.com
- Login : `jean-paul.dumoulin@skynet.be`
- Mot de passe : `T6002021$`

> 💡 **INFO** : La caméra Foscam est un outil de **surveillance et de visée grossière**. Elle n'est pas adaptée à l'observation scientifique (pas de pose longue, pas de capteur refroidi).

### 5.7 Lancement des applications d'observation

1. Lancer les applications nécessaires à la session d'observation
2. Effectuer les réglages de mise au point et de pointage
3. La session d'observation peut commencer

> 📝 **NOTE** : La liste complète des applications nécessaires n'est pas documentée dans la procédure originale. **À compléter selon les équipements installés (logiciel de pilotage de monture, d'acquisition, etc.).**

### 5.8 Checklist de démarrage

- [ ] PC T600-NUC allumé et accessible
- [ ] Bâche du télescope enlevée (≥ 30 min avant observation)
- [ ] Câble de charge batterie cimier débranché (si rotation prévue)
- [ ] Amorçage physique IPX800 effectué
- [ ] Latch D0 activé (interface .237)
- [ ] Interface IPX800 accessible (interface .238 — login OK)
- [ ] 4 sorties activées (Outputs) et vérifiées (Inputs)
- [ ] Caméra Foscam accessible (image visible)
- [ ] Applications d'observation lancées

---

## 6. Utilisation courante

### 6.1 Mise en température et stabilisation du tube

Avant de commencer l'observation sérieuse :

1. **Attendre l'équilibre thermique** : 1 heure par 10°C d'écart entre température intérieure et extérieure
2. **Ventiler** le tube si possible (ventilateur interne)
3. **Vérifier la collimation** de l'optique
4. **Faire la mise au point** (masque de Hartmann ou autofocus du logiciel)
5. **Surveiller la turbulence** : si l'image danse, fermer la coupole ou ventiler

### 6.2 Pilotage du télescope

> *Cette section est à compléter selon le logiciel de pilotage installé et la monture utilisée.*

### 6.3 Acquisition d'images

⚠️ **ATTENTION** : Pendant une acquisition d'image (pose longue) :

- ❌ **NE PAS** faire tourner le dôme (vibrations → flou de bougé)
- ❌ **NE PAS** marcher à proximité du télescope
- ❌ **NE PAS** allumer de lumières vives à proximité

### 6.4 Surveillance distante

- Accès à la caméra Foscam via le navigateur (adresse IP locale ou compte cloud)
- Utilisation des commandes PTZ (Pan/Tilt/Zoom) si nécessaire
- Sauvegarde d'images ou vidéo locales

---

## 7. Procédure d'arrêt

### 7.1 Arrêt des applications

1. **Fermer** toutes les applications d'observation et d'acquisition
2. **Sauvegarder** les données si nécessaire
3. **Fermer** le programme Foscam T6002021

### 7.2 Bascule T600-NUC-TELE → T600-NUC

> 💡 **INFO** : Cette étape est nécessaire si vous travailliez sur le PC T600-NUC-TELE. Vous devez basculer sur le PC T600-NUC pour éteindre l'IPX800.

1. Sur le PC **T600-NUC-TELE**, cliquer sur **Arrêter** (arrêt normal de Windows)
2. La connexion Anydesk vers le T600-NUC-TELE est perdue
3. Se connecter par Anydesk au **PC T600-NUC**

### 7.3 Désactivation des sorties IPX800

1. Sur le PC T600-NUC, ouvrir Edge
2. Accéder à `http://192.168.1.238`
3. **Décocher** (désactiver) les boutons qui sont allumés (les 4 sorties)
4. Vérifier que les Inputs correspondants passent à OFF

> 💡 **INFO** : Il est recommandé de désactiver les sorties une par une (pas d'ordre critique documenté, mais éviter une coupure brutale de toutes les sorties simultanément).

### 7.4 Extinction de l'IPX800

1. Ouvrir une nouvelle fenêtre Edge
2. Accéder à `http://192.168.1.237`
3. Cliquer sur **OFF** sur la ligne D0
4. Cliquer sur **Actualiser**
5. Vérifier que l'IPX800 est bien éteint (plus de voyants, interface inaccessible)

### 7.5 Mise en sécurité de la coupole

Avant de quitter :

- [ ] La coupole est en position de sécurité (arrêtée sur sa butée ou parallèle au vent)
- [ ] Le câble de charge de la batterie des cimiers est **re-branché** (pour maintenir la charge)

### 7.6 Extinction du PC (optionnelle)

> 💡 **INFO** : Le PC T600-NUC est normalement **laissé allumé en permanence** (nécessaire à l'accès distant et pour maintenir l'infrastructure). Ne l'éteindre que si nécessaire.

Si extinction nécessaire :
1. Fermer toutes les applications
2. Windows → Arrêter

### 7.7 Checklist d'arrêt

- [ ] Applications d'observation fermées
- [ ] Sauvegarde des données effectuée
- [ ] Programme Foscam fermé
- [ ] PC T600-NUC-TELE éteint (si utilisé)
- [ ] Connexion basculée sur PC T600-NUC
- [ ] 4 sorties IPX800 désactivées (interface .238)
- [ ] Latch IPX800 désactivé (D0 = OFF, interface .237)
- [ ] IPX800 éteint (vérifié)
- [ ] Coupole en position de sécurité
- [ ] Câble de charge batterie cimier rebranché

---

## 8. Maintenance

### 8.1 Maintenance avant chaque session

| Action | Détail |
|--------|--------|
| Vérifier les connexions réseau | Voyants switch, WiFi, accès Anydesk |
| Vérifier l'état des voyants IPX800 | Sous tension, sorties accessibles |
| Inspecter la batterie des cimiers | Tension, état des cosses, niveau d'électrolyte |
| Enlever la bâche du télescope | Progressivement, ≥ 30 min avant observation |

### 8.2 Maintenance mensuelle

| Action | Détail |
|--------|--------|
| Nettoyer les optiques | Pinceau optique, soufflette à air sec |
| Vérifier la batterie des cimiers | Tension à vide et en charge |
| Vérifier les câbles et connecteurs | Corrosion, usure, serrage |
| Nettoyer le dôme de la caméra Foscam | Chiffon doux non-rayant |

### 8.3 Maintenance annuelle et hivernage

#### Hivernage (novembre)

⚠️ **Procédure critique avant la saison froide :**

1. ✅ Vérifier le bon fonctionnement de l'IPX800 et des sorties
2. ✅ Mettre en place la bâche du télescope
3. ✅ Désactiver l'alimentation des équipements non essentiels
4. ✅ **Couper le courant du pilotage WiFi des cimiers** (hiverné)
5. ✅ Vérifier l'état de la batterie des cimiers (charge suffisante)
6. ✅ Confiner le matériel sensible (caméra, PCs) si température < -10°C
7. ✅ Noter la date de l'hivernage dans le journal

#### Remise en service (printemps)

1. ✅ Vérification générale de tous les équipements
2. ✅ Nettoyage optique complet
3. ✅ Test des automatismes (cimiers, coupole)
4. ✅ Procédure de déshumidification (voir section [3.3](#33-sécurité-optique-et-thermique))
5. ✅ Rétablir le courant du pilotage WiFi des cimiers

### 8.4 Maintenance des sous-systèmes

#### 8.4.1 Batterie des cimiers

| Fréquence | Action |
|-----------|--------|
| Chaque session | Vérifier que le câble de charge est débranché avant rotation |
| Mensuel | Vérifier la tension à vide (≥ 12.5V) |
| Trimestriel | Vérifier le niveau d'électrolyte (si batterie ouverte) |
| Annuel | Remplacer la batterie (durée de vie typique : 2-3 ans) |

#### 8.4.2 Optique (nettoyage, collimation)

🔧 **MAINTENANCE** : L'optique du télescope doit être nettoyée **avec précaution** :

1. Utiliser un **pinceau optique** ou une **soufflette à air sec** pour enlever la poussière
2. Si nettoyage humide nécessaire : utiliser un **liquide optique neutre** et un **tissu optique non-tissé**
3. **Ne JAMAIS** utiliser de chiffon domestique, d'alcool ou de produit nettoyant non adapté
4. Vérifier la collimation une fois par an (ou après tout déplacement important)

#### 8.4.3 Réseau et switch WiFi

| Fréquence | Action |
|-----------|--------|
| Mensuel | Redémarrer le switch WiFi (vider les caches) |
| Annuel | Mettre à jour le firmware du switch |
| Annuel | Changer les mots de passe WiFi et IPX800 |

#### 8.4.4 Mise à jour firmware/logiciels

| Équipement | Fréquence recommandée |
|------------|-----------------------|
| IPX800 | Annuelle (vérifier les mises à jour GCE Electronics) |
| Switch WiFi | Annuelle |
| PC T600-NUC / T600-NUC-TELE | Mises à jour Windows : automatiques / mensuelles |
| Anydesk | Automatique (mise à jour régulière) |
| Foscam | Annuelle (vérifier firmware myfoscam.com) |

---

## 9. Dépannage

### 9.1 Problèmes de connexion réseau

**Symptôme** : PC non accessible, Anydesk ne se connecte pas, site web IPX800 inaccessible.

**Actions** :
1. Vérifier que le PC est sous tension (voyant d'alimentation)
2. Vérifier la connexion WiFi : SSID `wireless2.4G_A84620` connecté ?
3. `ping 192.168.1.1` (passerelle par défaut) — tester la connectivité
4. Vérifier les voyants du switch WiFi (alimentation, activité)
5. Redémarrer le switch WiFi (débrancher/rebrancher l'alimentation)
6. Vérifier que le PC T600-NUC est allumé (il doit l'être en permanence)

### 9.2 IPX800 ne répond pas

**Symptôme** : Interface web inaccessible aux adresses `.237` et `.238`.

**Actions** :
1. Vérifier les voyants de l'IPX800 (aucun voyant = hors tension)
2. Vérifier que le bouton d'amorçage physique a été actionné (section [5.3](#53-alimentation-de-lipx800))
3. Vérifier que la sortie D0 est active (latch maintenu)
4. Vérifier les connexions réseau de l'IPX800 (WiFi ou Ethernet)
5. Tester `ping 192.168.1.237` ou `ping 192.168.1.238`
6. En dernier recours : couper l'alimentation secteur de l'IPX800, attendre 30 secondes, réamorcer

### 9.3 Caméra Foscam inaccessible

**Symptôme** : Page web caméra ne charge pas, image noire ou figée.

**Actions** :
1. `ping <adresse_ip_camera>` — tester la connectivité
2. Vérifier l'alimentation de la caméra (prise secteur, voyant)
3. Vérifier le câble Ethernet (si connexion filaire) ou le WiFi
4. Redémarrer la caméra : débrancher l'alimentation, attendre 10 secondes, rebrancher
5. Réinitialiser la caméra : maintenir le bouton Reset pendant 10 secondes (configuration par défaut)
6. Vérifier l'application Foscam T6002021 sur le PC (est-elle lancée ?)

### 9.4 Anydesk échoue

**Symptôme** : Impossible de se connecter à distance au PC.

**Actions** :
1. Vérifier que le PC cible est allumé (demander à quelqu'un sur place)
2. Vérifier que le PC cible est connecté au réseau (WiFi ou Ethernet)
3. Vérifier qu'Anydesk est lancé (icône dans la barre des tâches du PC cible)
4. Vérifier les paramètres de pare-feu (port 7070 pour Anydesk)
5. Utiliser la connexion locale (1er étage) en dernier recours
6. Redémarrer Anydesk sur le PC cible

### 9.5 Problèmes de rotation de la coupole

**Symptôme** : La coupole ne tourne pas, ou tourne avec des bruits anormaux.

**Actions** :
1. ✅ Vérifier que le câble de charge de la batterie est débranché
2. ✅ Vérifier que la batterie est suffisamment chargée (tension ≥ 12V)
3. ✅ Vérifier que le coffret cimier est sous tension (adresse `192.168.1.236`)
4. ✅ Vérifier que la sortie IPX800 correspondant aux cimiers est activée
5. ✅ Vérifier qu'aucun obstacle mécanique ne bloque la rotation (bâche, outil, débris)
6. ✅ Vérifier les butées de fin de course (sécurité)
7. 🟡 Si bruit anormal : arrêter immédiatement, vérifier les cimiers (balais, rail, graissage)

### 9.6 Qualité d'image dégradée

**Symptôme** : Images floues, allongées, ou de mauvaise qualité.

**Causes possibles et solutions** :

| Cause | Solution |
|-------|----------|
| Mauvaise mise au point | Refaire la mise au point (masque de Hartmann, AF) |
| Non-équilibre thermique | Attendre la stabilisation (1h/10°C) |
| Vibrations | Vérifier que le dôme ne tourne pas pendant la pose |
| Turbulence interne | Ventiler le tube, attendre l'équilibre |
| Optique sale | Nettoyage optique (voir section [8.4.2](#842-optique-nettoyage-collimation)) |
| Défaut de collimation | Vérifier et ajuster la collimation |
 | Condensation | Utiliser des chauffants anti-buée, attendre l'acclimatation |

---

## 10. Annexes

### Annexe A : Référentiel des identifiants et mots de passe

> ⚠️ **ATTENTION — CONFIDENTIEL** : Cette annexe contient des informations sensibles. Ne pas diffuser sans nécessité. Utiliser un gestionnaire de mots de passe plutôt que ce document pour le stockage permanent.

| Équipement / Service | Identifiant | Mot de passe actuel | Recommandation |
|----------------------|-------------|---------------------|----------------|
| **PC T600-NUC (session Windows)** | À documenter | `forets` | 🔴 Changer — mot de passe faible |
| **IPX800 (interface web .238)** | `Admin` | `Oc@2018` | 🔴 Changer — mot de passe faible |
| **Caméra Foscam (compte local)** | `foscamt600` | `T6002021` | 🔴 Changer — mot de passe faible |
| **Caméra Foscam (cloud myfoscam.com)** | `jean-paul.dumoulin@skynet.be` | `T6002021$` | 🔴 Changer — mot de passe faible |
| **WiFi dôme (SSID: wireless2.4G_A84620)** | — | `Admin2021$` | 🔴 Changer URGENT — mot de passe trivial |
| **Anydesk PC T600-NUC** | ID : à documenter | Mot de passe : à documenter | 🔴 Information manquante |
| **Anydesk PC T600-NUC-TELE** | ID : à documenter | Mot de passe : à documenter | 🔴 Information manquante |
| **Coffret cimier (192.168.1.236)** | À documenter | À documenter | 🔴 Information manquante |

#### Historique des changements de mots de passe

| Date | Service | Ancien mot de passe | Nouveau mot de passe | Par |
|------|---------|---------------------|----------------------|-----|
| | | | | |

---

### Annexe B : Schémas électriques

> *Cette annexe référence les schémas produits par l'analyse détaillée du système. Les schémas suivants sont disponibles dans les fichiers associés :*

| Référence | Description | Fichier |
|-----------|-------------|---------|
| Schéma 1 | Distribution électrique générale (230VAC / 12VDC) | `T600-schema-electrique-v1.png` |
| Schéma 2 | Câblage IPX800 (sorties, entrées, latch D0) | `T600-schema-ipx800-v1.png` |
| Schéma 3 | Architecture réseau complète | `T600-architecture-reseau-v1.png` |

---

### Annexe C : Séquencement algorithmique

> *Cette annexe présente les séquences de démarrage et d'arrêt sous forme de pseudo-code, permettant une éventuelle automatisation future.*

#### C.1 Algorithme de démarrage (pseudo-code)

```
FONCTION DemarrerT600()

    // VÉRIFICATIONS PRÉALABLES
    SI PC_T600_NUC_Allume == FAUX ALORS
        AFFICHER "ERREUR : PC T600-NUC doit être allumé"
        RETOUR ERREUR
    FIN SI

    // ÉTAPE 1 : Alimentation IPX800 (latch)
    AFFICHER "Amorçage physique IPX800 nécessaire (bouton poussoir)"
    AFFICHER "Connexion à 192.168.1.237..."
    HTTP_GET("http://192.168.1.237/SetOutput?output=0&state=1")
    ATTENDRE(5 secondes)
    InputD0 = HTTP_GET("http://192.168.1.237/GetInput?input=0")
    SI InputD0 == "OFF" ALORS
        AFFICHER "ERREUR : Latch IPX800 échoué"
        RETOUR ERREUR
    FIN SI

    // ÉTAPE 2 : Connexion interface principale
    AFFICHER "Connexion à 192.168.1.238..."
    HTTP_POST("http://192.168.1.238/login", "Admin", "Oc@2018")

    // ÉTAPE 3 : Activation des 4 sorties
    POUR sortie DANS {1, 2, 3, 4}:
        HTTP_GET("http://192.168.1.238/SetOutput?output=" + sortie + "&state=1")
        ATTENDRE(2 secondes)
        InputX = HTTP_GET("http://192.168.1.238/GetInput?input=" + sortie)
        SI InputX == "OFF" ALORS
            AFFICHER "ATTENTION : Sortie " + sortie + " non activée"
        FIN SI
    FIN POUR

    // ÉTAPE 4 : Caméra Foscam
    AFFICHER "Lancement Foscam T6002021..."
    LANCER_APPLICATION("Foscam T6002021.exe")

    AFFICHER "Démarrage terminé avec succès"
    RETOUR SUCCES
FIN FONCTION
```

#### C.2 Algorithme d'arrêt (pseudo-code)

```
FONCTION ArreterT600()

    // ÉTAPE 1 : Arrêt des applications
    AFFICHER "Arrêt des applications..."
    FERMER_APPLICATION("Foscam T6002021.exe")
    // Ajouter ici la fermeture des autres applications

    // ÉTAPE 2 : Désactivation des sorties
    AFFICHER "Connexion à l'IPX800..."
    HTTP_POST("http://192.168.1.238/login", "Admin", "Oc@2018")

    POUR sortie DANS {4, 3, 2, 1}:  // Ordre inverse recommandé
        HTTP_GET("http://192.168.1.238/SetOutput?output=" + sortie + "&state=0")
        ATTENDRE(1 seconde)
        InputX = HTTP_GET("http://192.168.1.238/GetInput?input=" + sortie)
        SI InputX == "ON" ALORS
            AFFICHER "ATTENTION : Sortie " + sortie + " non désactivée"
        FIN SI
    FIN POUR

    // ÉTAPE 3 : Extinction IPX800
    AFFICHER "Extinction IPX800..."
    HTTP_GET("http://192.168.1.237/SetOutput?output=0&state=0")
    ATTENDRE(3 secondes)
    InputD0 = HTTP_GET("http://192.168.1.237/GetInput?input=0")
    SI InputD0 == "ON" ALORS
        AFFICHER "ERREUR : Impossible d'éteindre l'IPX800"
        RETOUR ERREUR
    FIN SI

    AFFICHER "Arrêt terminé avec succès"
    RETOUR SUCCES
FIN FONCTION
```

#### C.3 Automatisation - Script PowerShell (exemple de structure)

```powershell
# start-t600.ps1 - Script de démarrage automatisé
# À placer sur le PC T600-NUC

$ErrorActionPreference = "Stop"

try {
    Write-Host "=== Démarrage T600 ===" -ForegroundColor Cyan
    
    # Vérification du PC
    if ($env:COMPUTERNAME -ne "T600-NUC") { 
        throw "Erreur : Ce script doit être exécuté sur T600-NUC" 
    }
    
    # Activation du latch IPX800
    Write-Host "1. Activation du latch IPX800..."
    Invoke-WebRequest -Uri "http://192.168.1.237/SetOutput?output=0&state=1" -TimeoutSec 5
    Start-Sleep -Seconds 3
    Write-Host "   Latch activé" -ForegroundColor Green
    
    # Connexion et activation des sorties
    Write-Host "2. Activation des sorties..."
    for ($i = 1; $i -le 4; $i++) {
        Invoke-WebRequest -Uri "http://192.168.1.238/SetOutput?output=$i&state=1" -TimeoutSec 5
        Start-Sleep -Seconds 2
        Write-Host "   Sortie $i activée" -ForegroundColor Green
    }
    
    # Lancement de la caméra
    Write-Host "3. Lancement de Foscam..."
    Start-Process -FilePath "C:\Program Files\Foscam\FoscamT6002021.exe"
    
    Write-Host "=== Démarrage terminé ===" -ForegroundColor Green
}
catch {
    Write-Error "Erreur : $($_.Exception.Message)"
    exit 1
}
```

---

### Annexe D : Checklist de démarrage et d'arrêt

#### Checklist de démarrage (à imprimer et afficher au poste de pilotage)

| # | Action | ✅ |
|---|--------|----|
| 1 | PC T600-NUC allumé et accessible | ☐ |
| 2 | Bâche du télescope enlevée (≥ 30 min avant) | ☐ |
| 3 | Câble de charge batterie cimier débranché (si rotation) | ☐ |
| 4 | Amorçage physique IPX800 effectué | ☐ |
| 5 | Latch D0 activé (interface .237 → ON → Actualiser) | ☐ |
| 6 | Interface IPX800 accessible (.238 — login Admin/Oc@2018) | ☐ |
| 7 | 4 sorties activées (Outputs ON) | ☐ |
| 8 | Retours Input vérifiés (tous les équipements alimentés) | ☐ |
| 9 | Caméra Foscam accessible (image visible) | ☐ |
| 10 | Applications d'observation lancées | ☐ |

#### Checklist d'arrêt (à imprimer et afficher au poste de pilotage)

| # | Action | ✅ |
|---|--------|----|
| 1 | Applications d'observation fermées | ☐ |
| 2 | Données sauvegardées | ☐ |
| 3 | Programme Foscam fermé | ☐ |
| 4 | PC T600-NUC-TELE éteint (si utilisé) | ☐ |
| 5 | Connexion basculée sur PC T600-NUC | ☐ |
| 6 | 4 sorties IPX800 désactivées (.238 → Outputs OFF) | ☐ |
| 7 | Latch IPX800 désactivé (.237 → D0 OFF → Actualiser) | ☐ |
| 8 | IPX800 éteint (vérifié : interface inaccessible) | ☐ |
| 9 | Coupole en position de sécurité | ☐ |
| 10 | Câble de charge batterie cimier rebranché | ☐ |

---

### Annexe E : Calendrier de maintenance périodique

| Période | Action | Responsable |
|---------|--------|-------------|
| **Chaque session** | Vérifier connexions réseau et voyants | Utilisateur |
| **Chaque session** | Vérifier état batterie cimier | Utilisateur |
| **Mensuel** | Nettoyer optiques (pinceau, soufflette) | Technicien |
| **Mensuel** | Vérifier tension batterie cimier | Technicien |
| **Mensuel** | Redémarrer switch WiFi | Technicien |
| **Trimestriel** | Vérifier câbles et connecteurs (corrosion) | Technicien |
| **Trimestriel** | Vérifier niveau électrolyte batterie | Technicien |
| **Annuel (printemps)** | Remise en service complète, test automatismes | Technicien + Référent |
| **Annuel (automne)** | Hivernage complet | Technicien + Référent |
| **Annuel** | Remplacer batterie cimier (si nécessaire) | Technicien |
| **Annuel** | Graisser moteurs cimiers | Technicien |
| **Annuel** | Mettre à jour firmwares (IPX800, switch, Foscam) | Technicien |
| **Annuel** | Changer mots de passe | Technicien + Référent |
| **Tous les 2 ans** | Nettoyage optique complet (si nécessaire) | Référent |

---

### Annexe F : Journal des versions du document

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| v1.0 | 2024-08-23 | Bureau ACO — Équipe Astronomie Technique, OCA | Création du document de référence T600. Consolidation des procédures originales (Dumoulin & Wanlin) et des analyses des 5 agents spécialisés du bureau ACO. |
| | | | |

---

## Références

- Document original : `T600-Mise-en-route-20260525.pptx` — Jean-Paul Dumoulin & Christian Wanlin (OCA)
- Analyses contributives :
  - `analyse-extraction-connaissances.md` — Agent Ethnographe
  - `analyse-optique-mecanique.md` — Agent Astro-Mécanique-Optique
  - `analyse-electronique-electricite.md` — Agent Ingénieur Électronique
  - `analyse-systemes-embarques.md` — Agent Systèmes Embarqués
  - `plan-document-reference-T600.md` — Agent Rédacteur Technique

---

*Document de référence T600 — Observatoire Centre Ardennes (OCA)*  
*Équipe ACO — Astronomie — Technique*  
*Analyse d'aide à la décision – hors implémentation.*