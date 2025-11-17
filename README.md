## 1. Objectif

Créer une simulation réaliste d’un blob (masse amorphe visco-élastique inspirée de Physarum polycephalum ou d’un organisme fictif) en Python, incluant :

- mouvements et déformations physiques réalistes,
    
- interaction avec l’environnement (nutriments, obstacles, gradients),
    
- comportements biologiques internes (oscillations, croissance),
    
- visualisation en temps réel et outils d’analyse.
    

## 2. Contraintes Générales

- Langage : Python 3.10+.
    
- Performance : compatibilité CPU et accélération (Numba/Taichi/GPU).
    
- Modularité du code en plusieurs modules (physique, biochimie, rendu…).
    

## 3. Fonctionnalités Principales

### 3.1 Moteur Physique

- Modèles possibles :
    
    - Phase-field (Allen-Cahn / Cahn-Hilliard),
        
    - Automate cellulaire,
        
    - Modèle particulaire (agent-based).
        
- Effets modélisés :
    
    - tension de surface,
        
    - viscosité interne,
        
    - forces actives (contractions),
        
    - croissance / diminution de la masse,
        
    - fusion / fragmentation.
        

### 3.2 Biochimie et Contrôle Interne

- Diffusion et dégradation de nutriments et attractants,
    
- Interactions chimiques contrôlant la mobilité,
    
- Oscillateurs internes (ex. FitzHugh-Nagumo) pour cycles contraction/déplacement.
      

### 3.3 Interaction avec l’Environnement

- [ ] Obstacles fixes ou mobiles,
    
- [ ] Sources de nutriments,
### 3.4 Visualisation & Interface

- [ ] Rendu 2D en temps réel (VisPy, PyQtGraph ou Matplotlib),
    
- [ ] Export GIF/MP4/images,
    
- [ ] Contrôle interactif des paramètres (sliders, UI),
    
- [ ] Visualisation des champs (densité du blob, gradients, vitesse).
## 4. Données d’Entrée

- [ ] Taille du domaine,
    
- [ ] Résolution de la grille,
    
- [ ] Paramètres physiques (viscosité, tension, diffusion…),
    
- [ ] Position et intensité des sources de nutriments,
    
- [ ] Configuration initiale du blob,
    
- [ ] Seed aléatoire.    

    

## 5. Architecture Logicielle Possible

- `engine.py` : moteur physique,
    
- `chemistry.py` : diffusion/réaction,
    
- `mechanics.py` : forces et mouvement,
    
- `viewer.py` : rendu et interaction,
    
- `runner.py` : gestion des expériences,
    
- `metrics/` : analyse et statistiques,
    
- `tests/` : validation.
    

## 6. Bibliothèques Recommandées

- NumPy, SciPy,
    
- Numba, Taichi, PyTorch/JAX (selon besoin GPU),
    
- VisPy / PyQtGraph / Matplotlib,
    
- ImageIO, JSON (Pour tout ce qui serait configuration initiale ect...).
    

## 7. Validation et Réalisme

- Comparaison morphologique (aire, périmètre, compacité),
    
- Analyse dynamique (fréquence oscillations, vitesse propagation),
    
- Tests qualitatifs (contournement obstacles, recherche de nutriments),
    
- Études de sensibilité.
    

## 8. Livrables

- Code source organisé et documenté,
    
    
- Guide utilisateur,
    
- Scripts d’export vidéo et d’analyse,
    
- Rapport comparatif avec références visuelles.
    

## 9. Plan de Développement (Itératif)

1. **MVP** : moteur simple, diffusion nutriment, rendu de base.
    
2. **Étape 2** : oscillateurs internes, croissance, obstacles.
    
3. **Étape 3** : accélération GPU, UI interactive.
    
4. **Étape 4** : métriques avancées, validation scientifique. 


## 10. Améliorations Futures

- Simulation 3D,
    
- Ajustement automatique des paramètres par apprentissage,
    
- Multi-blob (coopération/compétition),

- Blob online ??
