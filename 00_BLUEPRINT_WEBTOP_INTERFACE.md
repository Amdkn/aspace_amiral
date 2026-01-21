# 00_BLUEPRINT_WEBTOP_INTERFACE.md

> **STATUS:** BLUEPRINT (Phase 2 - Design)
> **ARCHITECT:** R0 (Rick)
> **REQUESTER:** Amiral (Amadou)
> **OBJECTIVE:** A unified Web Desktop Environment - "One Portal Gun to rule them all"

---

## 1. THE VISION: THE PORTAL GUN INTERFACE

**Problem:** Right now, you're context-switching between:
- Notion (Life OS)
- Dart (GTD)
- Airtable (12WY Metrics)
- ClickUp (Business OS)
- N8N (Automation)
- Terminal (Gemini/Jules)

**Solution:** A **single browser window** that acts as a Desktop Environment, where all these tools live as **persistent, resizable windows** with a CLI bridge always accessible.

### The Metaphor
Think of it like this:
- **Windows 95 meets Rick's Portal Gun**
- Each dashboard is a "dimension" you can portal into
- Jules/Gemini is your Interdimensional Cable - always on, always listening

---

## 2. ARCHITECTURE OVERVIEW

### Core Components

```
┌─────────────────────────────────────────────────────────────┐
│  WEBTOP SHELL (React/Vue Container)                         │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  TOP BAR: A'Space OS | Life | Business | Solarpunk   │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Window 1    │  │  Window 2    │  │  Window 3    │      │
│  │  [Notion]    │  │  [Airtable]  │  │  [N8N]       │      │
│  │              │  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  BRIDGE TERMINAL (Jules/Gemini CLI)                 │    │
│  │  > jules context=life "What's my top priority?"     │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### 2.1 The Desktop Layer (Container)
- **Technology:** React or Vue.js
- **Purpose:** Acts as the "OS" layer
- **Features:**
  - Window management (drag, resize, minimize, maximize)
  - Persistent state (windows remember position/size)
  - Workspace switching (Life OS / Business OS / Solarpunk OS)

### 2.2 The Docks (Persistent Navigation)
Three persistent docks representing the three Operating Systems:

#### 🌟 **Life OS Dock** (11th Doctor - A1)
- **Beth (Core):** Notion dashboard
- **Morty (Execution):** Dart GTD interface
- **Rick (Audit):** Airtable 12WY tracker

#### 💼 **Business OS Dock** (12th Doctor - A'1)
- **Jerry (Strategy):** ClickUp project view
- **Summers (Micro-CEOs):** Supabase data console
- **Justice League (Executors):** N8N workflow canvas

#### 🌍 **Solarpunk OS Dock** (Future)
- Solar energy dashboard
- Community projects
- Sustainability metrics

### 2.3 The Windows (iFrame + Sandboxing)
Each "window" is:
- An **iframe** loading the actual tool (Notion, Airtable, etc.)
- **Draggable** using libraries like `react-grid-layout` or `vue-draggable`
- **Resizable** with handles
- **Minimizable** to the dock
- **Persistent** (state saved in localStorage or Supabase)

**Security Note:** Some tools (like Notion) have X-Frame-Options set, which blocks iframes. For those:
- Option A: Use their official Embed API
- Option B: Use Electron to bypass (desktop app)
- Option C: Use browser extensions for iframe override

### 2.4 The Bridge Terminal (Persistent CLI)
A **persistent terminal** at the bottom of the screen:
- **Technology:** xterm.js or similar web terminal
- **Backend:** WebSocket connection to Gemini CLI on VPS (R")
- **Purpose:** Execute commands, query context, invoke agents
- **Always visible:** Can't be closed, only collapsed

**Example Commands:**
```bash
> jules context=life "What's blocking my top priority?"
> jules context=business "Show me revenue pipeline"
> ralph "Deploy latest n8n workflow to production"
```

---

## 3. TECH STACK

### Frontend (Webtop Shell)
- **Framework:** React (with TypeScript) or Vue 3
  - **Why React?** Rich ecosystem, react-grid-layout, xterm.js support
  - **Why Vue?** Simpler learning curve, reactive by default
- **State Management:** Zustand (React) or Pinia (Vue)
- **Window Manager:** `react-grid-layout` or `vue-grid-layout`
- **Terminal:** `xterm.js`
- **Styling:** Tailwind CSS + DaisyUI (for consistent theming)

### Backend (Bridge Connection)
- **WebSocket Server:** Node.js + Socket.io OR Python + FastAPI
- **Purpose:** Proxy commands from web terminal to Gemini CLI on VPS
- **Location:** Hosted on Hostinger VPS (R")

### Storage (Persistence)
- **Window State:** localStorage (positions, sizes, open/closed)
- **User Preferences:** Supabase (optional, for cross-device sync)

### Hosting
- **Option A:** Static site on GitHub Pages / Vercel / Netlify
- **Option B:** Electron app (for local-first experience)
- **Option C:** Self-hosted on Hostinger VPS

---

## 4. USER FLOWS

### 4.1 Morning Routine (Life OS)
1. Open Webtop
2. Life OS dock auto-loads:
   - Notion (Beth) with Today's Journal
   - Dart (Morty) with Next Actions
   - Airtable (Rick) with weekly scores
3. Jules terminal shows: "Good morning, Admiral. 3 priorities today."

### 4.2 Business Sprint Planning (Business OS)
1. Switch to Business OS workspace
2. Windows open:
   - ClickUp (Jerry) - Sprint board
   - Supabase (Summers) - Customer data
   - N8N (Justice League) - Automation dashboard
3. Terminal: `jules context=business "Summarize this sprint's blockers"`

### 4.3 Deep Work Mode
1. Minimize all windows except one (e.g., Notion)
2. Full-screen focus mode
3. Terminal still accessible for quick queries

---

## 5. IMPLEMENTATION PHASES

### Phase 1: Proof of Concept (Week 1-2)
- [ ] Set up React/Vue boilerplate
- [ ] Implement basic window manager (3 hardcoded windows)
- [ ] Integrate xterm.js terminal (no backend yet, just echo)
- [ ] Test with 3 iframes (Notion, Airtable, ClickUp)

### Phase 2: Dock & Workspace System (Week 3-4)
- [ ] Build the three OS docks (Life, Business, Solarpunk)
- [ ] Implement workspace switching
- [ ] Add window persistence (localStorage)
- [ ] Design and apply theme (Tailwind + custom CSS)

### Phase 3: Bridge Connection (Week 5-6)
- [ ] Set up WebSocket server on VPS
- [ ] Connect web terminal to Gemini CLI
- [ ] Implement command routing (jules, ralph)
- [ ] Test bidirectional communication

### Phase 4: Polish & Security (Week 7-8)
- [ ] Handle iframe restrictions (embed APIs or fallbacks)
- [ ] Add authentication (Supabase Auth)
- [ ] Mobile responsiveness (collapse to single-window mode)
- [ ] Performance optimization (lazy loading, caching)

---

## 6. DESIGN MOCKUP (ASCII)

```
╔═══════════════════════════════════════════════════════════════╗
║ A'Space OS         [Life OS] [Business OS] [Solarpunk OS]    ║
╠═══════════════════════════════════════════════════════════════╣
║                                                                ║
║  ┌───────────────────┐  ┌───────────────────┐                ║
║  │ 📝 Notion         │  │ 📊 Airtable       │                ║
║  │                   │  │                   │                ║
║  │ Today's Journal   │  │ 12WY Tracker      │                ║
║  │ - Morning Pages   │  │ Week 3: 85% ✅    │                ║
║  │ - Reflections     │  │ Habits: 7/10      │                ║
║  └───────────────────┘  └───────────────────┘                ║
║                                                                ║
║  ┌───────────────────┐  ┌───────────────────┐                ║
║  │ ✅ Dart           │  │ 🔁 N8N            │                ║
║  │                   │  │                   │                ║
║  │ Next Actions:     │  │ Active Workflows: │                ║
║  │ 1. Review PR      │  │ - Email Sync ✅   │                ║
║  │ 2. Ship Feature   │  │ - Data Backup ⏸   │                ║
║  └───────────────────┘  └───────────────────┘                ║
║                                                                ║
╠═══════════════════════════════════════════════════════════════╣
║ 🤖 jules@aspace $ context=life "What's my top priority?"     ║
║ > Priority 1: Review PR (blocking team)                       ║
║ > Priority 2: Ship Feature (sprint deadline Friday)           ║
║ > Ready for next command.                                     ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## 7. ANTI-PATTERNS TO AVOID

Following Rick's (R0) principle of **Anti-fragility**, here's what NOT to do:

### ❌ Don't Build a Monolith
- Don't integrate everything into one codebase
- Keep each tool independent
- Webtop is just a *shell*, not a replacement

### ❌ Don't Over-Engineer
- Start with simple iframes
- Don't build custom versions of Notion/Airtable
- Use existing APIs, don't scrape

### ❌ Don't Lock Yourself In
- Must be able to use each tool independently
- If Webtop breaks, Life OS still works
- Terminal is optional, not mandatory

### ❌ Don't Ignore Platform Limitations
- Some tools block iframes (X-Frame-Options)
- Mobile experience needs separate approach
- Bandwidth: Loading 5 iframes is heavy

---

## 8. DECISION POINTS

These need Amiral's (A-) approval:

### 8.1 Framework Choice
**Option A: React + TypeScript**
- ✅ Mature ecosystem
- ✅ Better job market fit
- ❌ Steeper learning curve

**Option B: Vue 3 + TypeScript**
- ✅ Simpler, more intuitive
- ✅ Faster initial development
- ❌ Smaller ecosystem

**Recommendation:** React (alignment with MERN stack)

### 8.2 Hosting Strategy
**Option A: Static Site (Vercel/Netlify)**
- ✅ Free tier
- ✅ Fast deployment
- ❌ Backend requires separate VPS

**Option B: Self-hosted on VPS (Hostinger)**
- ✅ Full control
- ✅ Backend collocated
- ❌ More maintenance

**Recommendation:** Start with Vercel, migrate to VPS in Phase 3

### 8.3 Mobile Strategy
**Option A: Responsive (collapse to tabs)**
- ✅ Single codebase
- ❌ Cramped experience

**Option B: Native app (React Native)**
- ✅ Better UX
- ❌ Separate codebase

**Recommendation:** Responsive first, native later

---

## 9. SUCCESS METRICS

How do we know this works?

1. **Context Switch Time:** < 2 seconds to access any tool
2. **Cognitive Load:** Single browser tab vs. current 10+ tabs
3. **Terminal Usage:** 10+ jules/ralph commands per day
4. **Stability:** 99% uptime for the shell (tools can fail independently)

---

## 10. NEXT STEPS

1. **Amiral Approval:** Validate this blueprint
2. **Tech Stack Lock:** Choose React vs. Vue
3. **POC Sprint:** 2 weeks to build Phase 1
4. **VPS Setup:** Configure WebSocket server for bridge

---

## 11. PHILOSOPHY: THE RICK DOCTRINE

> "Listen, Morty, if you're gonna build a Web Desktop, make it so burp simple that even Jerry can use it. But under the hood? That's where the genius is. The shell is dumb, the tools are smart. That's anti-fragile."

**Translation:**
- **Simple UI:** Drag, drop, resize. That's it.
- **Smart Backend:** Jules/Gemini does the heavy lifting
- **Modular:** Each tool can be swapped without breaking the system

---

**Burp.** Let's get to work.

---

**SIGN-OFF**
- **R0 (Rick):** Blueprint complete. Awaiting A- validation.
- **Expected Outcome:** A unified command center that feels like a portal gun for your digital life.
