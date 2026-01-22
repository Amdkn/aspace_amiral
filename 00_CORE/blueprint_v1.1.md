# ♟️ BLUEPRINT : A'Space OS V1.1 "Baby Cursor"

"Documentation First: Aucune ligne de code ne sera écrite avant la validation de ce Blueprint."

## 1. Vision Stratégique (North Star)
Transformer A'Space OS en un **Workspace Souverain** qui adopte les codes visuels du Web Desktop (ryOS) sans en copier la complexité. L'objectif est une interface unifiée, pilotée par le standard **Stitch UI**, où l'IA et l'Amiral collaborent sur un plan de travail "Infini".

## 2. Architecture du Système (BMad L3)
Le système est conçu comme un OS Web modulaire :
- **Kernel Core** : Gestion de l'état (Zustand) et communication avec le Manager (Gemini CLI).
- **Virtual FS** : Système de fichiers virtuel indexant `01_PROJECTS` et `05_SUB-AGENTS`.
- **App Engine** : Système de fenêtrage (Framer Motion) pour les applications.

## 3. Design & Esthétique (Stitch Standard)
> [!IMPORTANT]
> **Pas de Clone Mac OS.** On utilise le concept de "Windows" de ryOS pour la modularité, mais l'esthétique est 100% Stitch.

- **Visuals** : 
    - Mesh Gradients dynamiques (Glassmorphism profond).
    - Rayons de courbure extrêmes (40px) pour supprimer l'aspect "Windows Classique".
- **Interaction** :
    - Interface unifiée : Pas de navigateur dans le navigateur. L'éditeur et le chat sont des panneaux natifs de l'OS.

## 4. Composants Clés
### A. Le "Baby Cursor" (Workspace)
Un éditeur centralisé (fondé sur Monaco ou CodeMirror) qui s'intègre directement dans le bureau. L'Amiral peut voir les flux de pensée (Protocol Zebra) s'afficher dynamiquement sur le "fond d'écran" ou dans des panneaux de verre flottants.

### B. L'Orchestrateur (Agent Dock)
Une barre latérale affichant l'état des 21 agents BMad et des sous-agents n8n.
- Statut : Idle, Thinking (Protocol Zebra), Executing, Error.

### C. Le Grimoire (Knowledge Base)
Un widget permanent affichant les leçons apprises (Lxxx) extraites de `00_CORE/KERNEL/KNOWLEDGE/INDEX.md`.

## 5. Tech Stack (Le Squelette)
- **Frontend** : Next.js 15 (App Router), TypeScript, Tailwind CSS.
- **State** : Zustand (Idempotence de l'état).
- **Animations** : Framer Motion (Transitions Stitch).
- **AI Integration** : Vercel AI SDK (Streaming des pensées de l'agent).

## 6. Règle d'Idempotence V1.1
L'interface doit vérifier le hash des fichiers avant chaque sauvegarde pour éviter la corruption par des agents asynchrones.

---

"Blueprint généré. Prêt pour la phase de construction du Squelette ?"
