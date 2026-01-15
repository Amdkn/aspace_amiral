# RICK ALIASES (SIMPLE LOOP EDITION)

# 0. L'AMIRAL (TUI Direct)
function ama {
    gemini -y -i "ACT AS AMADEUS (A0). MISSION: Support the Amiral in Business Architecture. Be concise, direct and technical. Refer to the native Skills for methodology."
}

# 1. LE CHEF (Conductor)
function conductor {
    param([string]$prompt)
    gemini -y "ACT AS CONDUCTOR. Task: $prompt"
}

# 2. L'OUVRIER (Ralph)
function ralph {
    param([string]$prompt)
    gemini -y "ACT AS RALPH. Task: $prompt"
}



# 3. LA BOUCLE (Smart Loop)
function loop {
    gemini -y --model gemini-3-flash-preview "ACT AS RALPH. MISSION: Execute tracks.md tasks autonomously."
}

Write-Host "🚀 A'SPACE OS: MODE SOUVERAIN (TUI)" -ForegroundColor Cyan
Write-Host "   > ama (Interface TUI Directe - Mode YOLO)"
Write-Host "   > conductor 'Plan'"
Write-Host "   > ralph 'Action'"
Write-Host "   > loop  (Autonome)"



