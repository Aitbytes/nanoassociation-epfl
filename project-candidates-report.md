# Projets Multidisciplinaires en Microfabrication — Analyse Comparative

_Projets candidates pour une association étudiante de nanotechnologie pratique EPFL_

---

## Résumé

Cette analyse présente les **7 projets multidisciplinaires** identifiés comme réalisables en salle blanche universitaire (niveau EPFL CMi) sur un horizon de 1-2 ans, combinant plusieurs domaines : nanophotonique, MEMS, ASIC, bio-MEMS, dispositifs quantiques.

**Projet recommandé :** Biocapteur photonique intégré avec spectromètre on-chip (Lab-on-a-chip) — meilleur équilibre originalité/faisabilité/startup potential.

---

## 1. MEMS-Tunable Silicon Photonic Switch with Integrated Electronics

**Domains :** Nanophotonique + MEMS + ASIC/IC

### Concept

Interrupteur photonique 2×2 à base deactionneurs MEMS électrostatiques qui modifie l'entrefer dans un coupleur adiabatique horizontal. Latching mécanique bistable pour non-volatilité.

### Équipement Requis

| Process      | Équipement CMi                               |
| ------------ | -------------------------------------------- |
| Lithographie | DUV (193nm ou 248nm) pour guides d'ondes SOI |
| Gravure      | ICP-RIE silicium, Bosch DRIE pour release    |
| Dépôt        | LPCVD SiN, Aluminium pour électrodes         |
| Release      | HF vapor ou BOE                              |

### Timeline

- **6-8 mois** : Design + première itération
- **8-12 mois** : Caractérisation switch
- **12-18 mois** : Démonstration non-volatile <12V, μs switching

### Points Forts

- Premier switch photonique **non-volatile** (zéro consommation statique)
- Énergie de commande ~10s de fJ
- Compatible avec fonderies silicon photonics standard
- IP très défendable (brevets architecture bistable)

### Potentiel Startup

- Cible : cross-connects optiques pour datacenters/AI
- Avantage compétitif : 100mW+ consommés par les switches thermo-optiques vs. quasi-zéro ici

---

## 2. Integrated Photonic Biosensor with On-Chip Spectrometer

**Domains :** Nanophotonique + Bio-MEMS + ASIC

### Concept

Plateforme Lab-on-a-chip photonique monolithiquement intégrée sur SOI combinant :

- Microrésonateur en anneau (MRR) comme biocapteur à champ évanescent
- Spectromètre Fourier intégré (SHFTS) pour lecture sur-puce
- Canaux microfluidiques pour flow cell

### Équipement Requis

| Process                | Équipement CMi                             |
| ---------------------- | ------------------------------------------ |
| Lithographie           | E-beam ou DUV pour résonateurs sub-μm      |
| Dépôt                  | SiN pour cladding, Ge pour photodétecteurs |
| Gravure                | ICP-RIE guides d'ondes et rings            |
| Microfluidique         | DRIE canaux à travers puce, SU-8/PDMS      |
| Bio-fonctionnalisation | Chimie de surface (hors cleanroom)         |

### Données de Référence (Paper `2207.07754`)

- FSR : ~19 nm
- Sensibilité bulk : ~73 nm/RIU
- Limite de détection : 0.042 RIU

### Timeline

- **4-6 mois** : Design + fab MRR + spectromètre
- **6-9 mois** : Fonctionnalisation surface, tests analytes
- **9-12 mois** : Limite de détection, sélectivité
- **12-18 mois** : Prototype fonctionnel

### Points Forts

- **Première démonstration monolithique** MRR + spectromètre Fourier intégré
- Plateforme POCT (point-of-care testing) sur une seule puce
- Détection quantitative label-free, sensibilité SPR
- Détection multiplexée possible (multiples rings)

### Potentiel Startup

- Marché : diagnostic POCT (remplacement lateral flow tests)
- Comparables : Genalyte ($100M+ levés)
- Différenciation : chip intégré vs. système cartouche

---

## 3. FMCW LiDAR Photonic Integrated Circuit with Electronic Driver

**Domains :** Nanophotonique + ASIC + MEMS

### Concept

Moteur LiDAR cohérent intégré photonique-électronique combinant :

- Générateur de forme d'onde haute tension
- Circuit photonique hybride avec laser Vernier accordable + actionneurs piézoélectriques
- Amplificateur à guide d'onde dopé Erbium
- Intégration BiCMOS 130nm

### Équipement Requis

| Process                | Équipement CMi                                |
| ---------------------- | --------------------------------------------- |
| Lithographie           | DUV SiN PIC, couches épi III-V                |
| Dépôt                  | SiN LPCVD, silice dopée Erbium, bonding III-V |
| Gravure                | ICP-RIE SiN, mesa etching III-V               |
| Intégration hétérogène | Die-to-wafer bonding                          |
| ASIC                   | Accès post-processing BiCMOS                  |

### Timeline

- **12-18 mois** : Réaliste compte tenu de la complexité d'intégration hétérogène

### Points Forts

- Intégration **wafer-scale**-III-V + SiN + BiCMOS sur même wafer
- Source FMCW **turnkey, linearization-free**
- Première démonstration de **toute l'intégration** pour LiDAR cohérent
- Solution drop-in pour systèmes LiDAR FMCW

### Potentiel Startup

- Marché : robotique, véhicules autonomes, automation industrielle
- Concurrent : Voyant Photonics (Columbia Lipson, $15.4M)
- Différenciation : intégration III-V + SiN plus serrée, coût réduit

---

## 4. AlN Piezoelectric MEMS with Integrated ASIC Readout

**Domains :** MEMS + ASIC + Energy Harvesting

### Concept

Films minces de nitrure d'aluminium (AlN) de haute qualité sur substrat SOI pour :

- Transducteurs ultrasonores micromachinés (PMUTs)
- Capteurs AFM à auto-détection
- Récupération d'énergie piézoélectrique

### Équipement Requis

| Process      | Équipement CMi                                                            |
| ------------ | ------------------------------------------------------------------------- |
| Dépôt        | Sputtering AlN avec orientation c-axis contrôlée, Pt bottom electrode PVD |
| Lithographie | DUV pour couche structurale                                               |
| Gravure      | DRIE (Bosch) pour etching through-wafer                                   |
| CMP          | planarisation wafer-level si nécessaire                                   |
| Assembly     | Wire bonding vers PCB                                                     |

### Timeline

- **6-9 mois** : Optimisation dépôt AlN, fab PMUT
- **9-12 mois** : Caractérisation coefficients piézoélectriques, LDV
- **12-15 mois** : Intégration ASIC readout chip
- **15-20 mois** : Démonstration système complet

### Points Forts

- **CMOS-compatible** AlN piezoelectric MEMS
- **6× plus faible bruit de force** que cantilevers SiN conventionnels (Fantner group EPFL)
- Plateforme dual-use : sensing + energy harvesting
- Expertise directement applicable aux biocapteurs

### Potentiel Startup

- Marché 1 : Capteurs NEMS pour AFM, sensing massique, biosensing
- Marché 2 : Energy harvesting pour capteurs IoT auto-alimentés
- Fort potentiel brevets sur processus AlN-on-SOI

---

## 5. Integrated Optomechanical Gyroscope / Vibratory MEMS

**Domains :** MEMS + Nanophotonique + ASIC

### Concept

Résonateurs MEMS intégrés avec lecture photonique — utilisant le couplage optomécanique pour un sensing ultra-haut-Q. Combiné avec circuits photoniques intégrés pour interrogation optique sur-puce.

### Équipement Requis

| Process      | Équipement CMi                                                 |
| ------------ | -------------------------------------------------------------- |
| Lithographie | E-beam + DUV pour structures nanomécaniques haute précision    |
| Dépôt        | SiN low-stress ou silicium amorphe                             |
| Gravure      | ICP-RIE pour poutres nanomécaniques suspendues                 |
| Release      | Critical point dryer pour release microdisques                 |
| Intégration  | Guides d'ondes SiN couplés évanescentiellement aux résonateurs |

### Timeline

- **9-12 mois** : Design + première fab
- **12-18 mois** : Caractérisation optique, mesure facteur Q
- **18-24 mois** : Démonstration gyroscope optomécanique complet

### Points Forts

- **Couplage optomécanique** = lecture backaction-free — physique fondamentale
- **Gyroscope optique chip-scale** — remplace gyro fibre optique volumineux
- Expertise couvre deux domaines hot (MEMS + photonique)
- Potentiel pour sensing déplacement limite quantique

### Potentiel Startup

- Marché : gyroscopes navigation-grade (drones, AR/VR, véhicules autonomes)
- Concurrents : Aera (Honeywell), GyroTru (Qualcomm) — tous volumineux ou chers
- Différenciation : fabrication wafer-scale + intégration photonique = réduction coût 10×

---

## 6. Hybrid Superconducting / Nanophotonic Quantum Chip

**Domains :** Nanophotonique + Dispositifs Quantiques + ASIC

### Concept

Plateforme photonique quantique hétérogène combinant :

- Source de photons uniques quantum dot (III-V semi-conducteur)
- Circuit photonique intégré SiN basse perte
- Démonstration de lois de suppression bosonique et génération d'intrication photonique

### Équipement Requis

| Process      | Équipement CMi                                         |
| ------------ | ------------------------------------------------------ |
| Lithographie | E-beam pour patterning quantum dot, DUV pour SiN PIC   |
| Épitaxie     | Croissance quantum dot MOVPE — source externe probable |
| Bonding      | Transfer printing ou wafer bonding                     |
| Cryogénie    | Station de test cryogénique                            |
| Électronique | Contrôle quantique FPGA (hors cleanroom)               |

### Timeline

- **12-18 mois** : Plateforme intégration hétérogène, source photons + PIC
- **18-24 mois** : Démonstrations intrication multi-photons

### ⚠️ Complexité Très Élevée

- Requiert expertise quantique profonde
- Collaboration externe probablement nécessaire
- Timeline ambitieuse pour 2 ans

### Points Forts

- Première **source photonique déterministe** interfacée avec PIC SiN programmable
- Démonstration **scalable** vers calcul quantique photonique
- Potentiel publication Nature/Science
- Fort intérêt dePsiQuantum, Xanadu (quantum computing)

### Potentiel Startup

- **Très élevé** — quantum computing photonique lourd funded ($450M PsiQuantum, $250M Xanadu)
- Chemin : IP université → acquisition/licensing par quantum computing company
- Risque : requiert 3+ ans pour chemin commercial viable

---

## 7. Microfluidic-Photonic Integrated Biosensor Platform

**Domains :** Bio-MEMS + Nanophotonique

### Concept

Circuits de biocapteurs photoniques topologiquement intégrés utilisant des états de bord photoniques topologiques comme guides d'ondes robustes — résolvant le problème de robustesse contre les variations de fabrication dans les réseaux de biocapteurs intégrés.

### Données de Référence (Paper `2408.04945`)

- Biocapteur QCM avec résonateur quartz 125 MHz intégré dans microchannel
- Limite de détection : 1 ng/mL IgG (supérieur au standard SPR or)

### Équipement Requis

| Process                | Équipement CMi                                                 |
| ---------------------- | -------------------------------------------------------------- |
| Lithographie           | DUV pour structuration cristal photonique                      |
| Gravure                | ICP-RIE trous crystal photonique + canaux microfluidiques      |
| Microfluidique         | DRIE canaux à travers puce, SU-8 ou PDMS pour soft lithography |
| Bio-fonctionnalisation | Chimie EDC/NHS standard (hors cleanroom)                       |

### Timeline

- **6-9 mois** : Design + fab intégration photonique + microfluidique
- **9-15 mois** : Fonctionnalisation surface + détection biomarqueurs
- **15-18 mois** : Démonstration multiplexage multi-biomarqueurs

### Points Forts

- **Photonique topologique** appliquée au biosensing — physique Novelle + application pratique
- **Robustesse aux désordres** — résout le vrai problème de variation de fabrication
- Capacité **multiplexage** (multiples biomarqueurs simultanément)
- Limite de détection cliniquement pertinente

### Potentiel Startup

- Marché : détection biomarqueurs cancer, screening maladies infectieuses
- Comparables : Theranos (discrédité) mais avec vraie photonique intégrée
- Différenciation : robustesse topologique = meilleur yield manufacturing = coût réduit

---

## Tableau Comparatif

| Projet                                | Domains                 | Complexité | Timeline | Startup       | Publication   |
| ------------------------------------- | ----------------------- | ---------- | -------- | ------------- | ------------- |
| **MEMS-Photonic Switch**              | Photonics+MEMS+ASIC     | Medium     | 12-18 mo | High          | High          |
| **Integrated Biosensor+Spectrometer** | Photonics+Bio-MEMS+ASIC | Medium     | 12-18 mo | **Very High** | **Very High** |
| **FMCW LiDAR PIC**                    | Photonics+MEMS+ASIC     | High       | 12-18 mo | **Very High** | **Very High** |
| **AlN PiezoMEMS+ASIC**                | MEMS+ASIC+Energy        | Medium     | 15-20 mo | High          | High          |
| **Optomechanical Gyroscope**          | MEMS+Photonics+ASIC     | High       | 18-24 mo | Med-High      | **Very High** |
| **Quantum Photonic Chip**             | Photonics+Quantum+ASIC  | Very High  | 18-24 mo | **Very High** | **Very High** |
| **Microfluidic-Photonic Biosensor**   | Bio-MEMS+Photonics      | Medium     | 12-18 mo | **Very High** | High          |

---

## Recommandations

### Pour maximiser le succès en 18 mois

→ **Projet 2 : Integrated Biosensor with On-Chip Spectrometer**

### Pour maximiser l'impact publication (Nature/Science)

→ **Projet 6 : Quantum Photonic Platform** ou **Projet 3 : FMCW LiDAR**

### Pour le risque le plus sûr (littérature la plus établie)

→ **Projet 4 : AlN PiezoMEMS + ASIC Readout**

### Pour maximiser l'utilisation des équipements CMi

→ **Projet 3 : FMCW LiDAR** — utilise DUV, ICP, ALD, III-V bonding, BiCMOS

### Pour un projet hybride optimal

**Design du projet #1 (MEMS-Photonic Switch)** comme projet principal + ajout d'éléments du projet #2 (biosensor) comme second track — 70% du même process flow SOI, efficacité maximale.

---

## Références Principales

- `2407.00070` — Daoxin Dai group (2024) : Nonvolatile Silicon Photonic MEMS Switch
- `2207.07754` — Yoo / Ray T. Chen group (2022) : Lab-on-a-Chip Optical Biosensor Platform
- `2306.07990` — Lukashchuk / Kippenberg group EPFL (2023) : Photonic-electronic integrated circuit-based coherent LiDAR engine
- `2307.03366` — Jadhav & Pratap (2023) : Fabrication and Characterization of AlN-based, CMOS compatible Piezo-MEMS Devices
- `2307.01122` — Weis / Stobbe group DTU (2023) : Design, fabrication, and characterization of electrostatic comb-drive actuators
- `2302.06282` — Wang / Paesani/Lodahl group (2023) : Deterministic photon source interfaced with programmable silicon-nitride integrated circuit
- `2408.04945` — Kong et al. (2024) : Topologically integrated photonic biosensor circuits

---

_Rapport généré à partir de la recherche "Projets multidisciplinaires faisables en cleanroom universitaire" — sources : arXiv, startup databases, documentation EPFL CMi._
