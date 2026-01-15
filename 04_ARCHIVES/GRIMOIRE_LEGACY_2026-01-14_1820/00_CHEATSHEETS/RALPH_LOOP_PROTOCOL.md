# 🦅 RALPH - LE MOTEUR D'ITÉRATION (R0-R1 BRIDGE)

L'implémentation de la **Golden Stack** repose sur la capacité de Ralph à boucler de manière autonome sur les outils stratégiques.

## 🧱 LES 3 SKILLS DE MAITRISE (DANS `~/.skillz/`)

1.  `setup_bmad_automator.md` : **L'Installeur**. Capable de réparer les erreurs YAML et de naviguer dans les menus de BMad.
2.  `conductor_loop_agent.md` : **Le Chef de Chantier**. Synchronise Ralph avec les Tracks de Conductor.
3.  `bmad_loop_agent.md` : **Le Stratège**. Assure que Ralph respecte les principes agiles de BMad.

---

## ⚡ COMMANDES D'INITIATION (BOOTSTRAP)

### 1. Installation Automatisée de BMad
Si tu es bloqué dans l'install :
```bash
/ralph-loop "Utilise setup_bmad_automator pour installer BMad. Ignore les erreurs YAML, corrige-les par toi-même dans 03_RESOURCES/01_GRIMOIRE/03_BMAD_CONFIG" --max-iterations 10
```

### 2. Exécution d'une Track Conductor avec Itération Ralph
Une fois BMad et Conductor installés :
```bash
*conductor-track "Feature Solarpunk"
/ralph-loop "Implémente la spécification actuelle en utilisant bmad_loop_agent pour le style et conductor_loop_agent pour le status" --max-iterations 20
```

---

## 🛠 SYSTÈME DE DÉPANNAGE (DEBUG LOOP)
Si Ralph boucle dans le vide :
1.  Utiliser `/cancel-ralph`.
2.  Vérifier le `~/.skillz` pour voir si les fichiers `.md` sont bien formatés.
3.  Relancer avec `--max-iterations 5` pour observer le comportement court.

*Wubba Lubba Dub Dub ! Le circuit est fermé.* 🧪
