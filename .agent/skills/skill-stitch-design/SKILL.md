---
name: stitch-design
description: Protocole de design "Stitch" de Google Labs pour A'Space OS. Maximise l'esthétique AI via Mesh Gradients, Glassmorphism 3.0 et arrondis extrêmes (40px+).
---

# 🧶 Skill: Stitch Design Architect

Ce Skill permet de transformer n'importe quel composant React ou page web en une interface "Premium AI" suivant les standards de **Google Stitch (I/O 2025)**.

## 🎨 Core Visual Language

| Élément | Standard Stitch (Solarpunk Light) | Implémentation CSS/Tailwind |
| :--- | :--- | :--- |
| **Bords** | Arrondis Maximaux | `rounded-[40px]` ou `rounded-[48px]` |
| **Profondeur** | Luminous Glass 3.5 | `backdrop-blur-3xl`, `bg-white/40`, `border-white/60` |
| **Fonds** | Solar Mesh (Luminous) | `bg-amber-50/20` + Mesh Gradients (Emerald, Gold, Sky) |
| **Layout** | Floating Nature Cards | `shadow-[0_40px_100px_rgba(0,0,0,0.05)]`, `border-white` |
| **Couleurs** | Palette Bio-Vibration | Gold (#F59E0B), Emerald (#10B981), Sky (#0EA5E9) |

## 🛠️ Composition Patterns

### 1. The Stitch Container
```jsx
const StitchPanel = ({ children }) => (
  <div className="bg-slate-900/40 backdrop-blur-3xl border border-white/10 rounded-[40px] p-8 shadow-2xl transition-all hover:border-white/20">
    {children}
  </div>
);
```

### 2. The Mesh Nebula Effect
Toujours utiliser au moins 3 sources lumineuses (`blur-[120px]`) pour les fonds d'écran.
```jsx
<div className="absolute top-0 left-0 w-full h-full -z-10 overflow-hidden bg-slate-950">
    <div className="absolute top-[-10%] left-[-10%] w-[50%] h-[50%] bg-purple-600/20 blur-[120px] rounded-full" />
    <div className="absolute bottom-[-10%] right-[-10%] w-[50%] h-[50%] bg-blue-500/10 blur-[120px] rounded-full" />
</div>
```

## 🚀 Workflows Relatés
- `/stitch-ui` : Transforme une section entière au standard Stitch.
- `/stitch-component [nom]` : Crée un composant UI unitaire "Stitch-ified".

---
*Aligné avec Phase 4: Regeneration (BMad).*
