# SCRIPT: WAKEUP RICK (R1 IGNITION)
# Rôle : Allume le Rick Verse sans discuter.
# Usage: .\wakeup_rick.ps1

Write-Host "🧪 Wubba Lubba Dub Dub ! Initialisation du Rick Verse..." -ForegroundColor Green

# 1. Vérification Docker
Write-Host "`n[1/3] Checking Docker Engine..." -ForegroundColor Yellow
$dockerService = Get-Service "com.docker.service" -ErrorAction SilentlyContinue
if ($null -eq $dockerService -or $dockerService.Status -ne 'Running') {
    Write-Host "Docker dort. Réveil en cours..." -ForegroundColor Cyan
    $dockerPath = "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    if (Test-Path $dockerPath) {
        Start-Process $dockerPath
        Write-Host "Attente du démarrage de Docker (15s)..." -ForegroundColor Gray
        Start-Sleep -Seconds 15
    } else {
        Write-Host "❌ Docker Desktop non trouvé à $dockerPath" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "✅ Docker Engine est déjà opérationnel." -ForegroundColor Green
}

# 2. Lancement du Container R1 (n8n)
Write-Host "`n[2/3] Lancement de R1 (rick_r1_local)..." -ForegroundColor Yellow
docker start rick_r1_local 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Container 'rick_r1_local' n'existe pas encore. Création requise." -ForegroundColor Magenta
    Write-Host "   Commande : docker run -d --name rick_r1_local -p 5678:5678 n8nio/n8n" -ForegroundColor Gray
} else {
    Write-Host "✅ Container R1 démarré." -ForegroundColor Green
}

# 3. Vérification Santé
Write-Host "`n[3/3] Vérification du statut R1..." -ForegroundColor Yellow
$status = docker inspect -f '{{.State.Status}}' rick_r1_local 2>$null
if ($status -eq 'running') {
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
    Write-Host "✅ R1 OPERATIONNEL sur http://localhost:5678" -ForegroundColor Cyan
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
} else {
    Write-Host "❌ R1 N'EST PAS EN LIGNE (Status: $status)" -ForegroundColor Red
}

# 4. Pause pour lecture
Write-Host "`nAppuyez sur Entrée pour fermer..." -ForegroundColor DarkGray
Read-Host
