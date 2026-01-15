<#
.SYNOPSIS
    GOLDEN STACK INSTALLER - RICK VERSE ENGINE
.DESCRIPTION
    Installe BMad, Conductor, Ralph (Kranthik) et Skillz (Intellectronica).
    Prépare le dossier ~/.skillz pour les compétences custom.
.AUTHOR
    Rick A"1 pour Amadeus (A0)
#>

Write-Host "🧪 INITIALISATION DE LA GOLDEN STACK..." -ForegroundColor Cyan

# 1. INSTALLATION DU CERVEAU (BMad)
Write-Host "[1/4] Installation du Cerveau (BMad Method)..."
try {
    # On utilise npx pour installer BMad dans le dossier courant
    cmd /c "npx bmad-method@alpha install"
    Write-Host "   >>> BMad Matrix Active." -ForegroundColor Green
}
catch {
    Write-Host "   >>> Erreur BMad. Vérifiez Node.js." -ForegroundColor Red
}

# 2. INSTALLATION DE L'ORCHESTRATEUR (Conductor)
Write-Host "[2/4] Recrutement du Chef de Chantier (Conductor)..."
try {
    # Installation de Conductor via Gemini CLI
    gemini extensions install https://github.com/gemini-cli-extensions/conductor --auto-update --consent
    Write-Host "   >>> Conductor Foreman On-Site." -ForegroundColor Green
}
catch {
    Write-Host "   >>> Erreur Conductor. Assurez-vous que Gemini CLI est installé." -ForegroundColor Red
}

# 3. INSTALLATION DU MOTEUR ITÉRATIF (Ralph - Kranthik)
Write-Host "[3/4] Démarrage du Moteur Ralph (Kranthik123)..."
try {
    # Installation de Ralph via Gemini CLI
    gemini extensions install https://github.com/kranthik123/Gemini-Ralph-Loop --auto-update --consent
    Write-Host "   >>> Ralph Engine Ignited." -ForegroundColor Green
}
catch {
    Write-Host "   >>> Erreur Ralph." -ForegroundColor Red
}

# 4. INSTALLATION DU SYSTÈME NERVEUX (Skillz) - DÉSACTIVÉ (Natif)
# Write-Host "[4/4] Greffe des Compétences (Intellectronica)..."
# native agent skills used instead
Write-Host "[4/4] Skillz: Utilisation des Agent Skills natifs." -ForegroundColor Green

$skillzDir = Join-Path $HOME ".skillz"

if (-not (Test-Path $skillzDir)) {
    New-Item -Path $skillzDir -ItemType Directory -Force | Out-Null
    Write-Host "   >>> Dossier C:\Users\Amiral\.skillz CRÉÉ." -ForegroundColor Green
    
    # Création d'un skill exemple 'Hello_Rick.md'
    $exampleSkill = @"
---
name: hello_rick
description: Salutation protocolaire du Rick Verse
---
Dites simplement 'Wubba Lubba Dub Dub' à l'utilisateur.
"@
    Set-Content -Path (Join-Path $skillzDir "hello_rick.md") -Value $exampleSkill
}
else {
    Write-Host "   >>> Dossier .skillz déjà présent." -ForegroundColor Cyan
}

Write-Host "`n✅ GOLDEN STACK PRÊTE." -ForegroundColor Green -BackgroundColor Black
Write-Host "Rappel Workflow : *workflow-init -> *conductor-track -> /ralph-loop"
Read-Host "Appuyez sur Entrée..."
