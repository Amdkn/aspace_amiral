# RICK ALIASES - Raccourcis PowerShell pour le Rick Verse
# 
# INSTALLATION:
# 1. Ouvre ton profil PowerShell : notepad $PROFILE
# 2. Colle le contenu de ce fichier à la fin.
# 3. Sauvegarde et relance PowerShell.
# 4. Tape 'rick "Hello"' pour tester.

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# ALIAS RICK : Architecte / Génération de Code
# Usage: rick "Génère un workflow n8n pour X"
function rick {
    param([string]$prompt)
    gemini run --context "Rick Verse" --skill "Rick_Build" --prompt $prompt
}

# ALIAS DOC : 13th Doctor / Opérations Infra
# Usage: doc "Vérifie le statut de R1"
function doc {
    param([string]$prompt)
    gemini run --context "Core OS" --skill "Conductor" --prompt $prompt
}

# ALIAS RALPH : Lance le TUI Custom
# Usage: ralph
function ralph {
    gemini tui --config "$env:ASPACE_ROOT\.gemini\ralph_config.json"
}

# ALIAS WAKEUP : Démarre le Rick Verse (Docker + n8n)
# Usage: wakeup
function wakeup {
    & "$env:ASPACE_ROOT\03_RESOURCES\01_GRIMOIRE\02_SCRIPTS\wakeup_rick.ps1"
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# VARIABLE D'ENVIRONNEMENT (À définir une fois)
# Décommente et ajuste si nécessaire :
# $env:ASPACE_ROOT = "C:\Users\amado\Documents\A'Space OS\00_Amiral"

Write-Host "🧪 Rick Aliases chargés. Commandes disponibles: rick, doc, ralph, wakeup" -ForegroundColor Green
