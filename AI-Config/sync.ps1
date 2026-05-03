# ── Paths ──────────────────────────────────────────────
$personaFile  = "C:\Users\Brian Geisler\gitSynced\main\AI-Config\persona.prompt"
$configFile   = "$HOME\.continue\config.yaml"
$backupFolder = "C:\Users\Brian Geisler\gitSynced\main\AI-Config\backup"

# ── Backup current config ───────────────────────────────
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm"
if (!(Test-Path $backupFolder)) { New-Item -ItemType Directory -Path $backupFolder }
Copy-Item $configFile "$backupFolder\config_$timestamp.yaml"
Write-Host "✅ Backup saved: config_$timestamp.yaml"

# ── Read persona ────────────────────────────────────────
$persona = Get-Content $personaFile -Raw

# ── Build new config ────────────────────────────────────
$config = @"
name: Local Config
version: 1.0.0
schema: v1
models:
  - name: Qwen2.5 Coder 14B (Chat)
    provider: ollama
    model: qwen2.5-coder:14b
    roles:
      - chat
      - edit
      - apply
    contextLength: 8192
    systemMessage: |
$(($persona -split "`n" | ForEach-Object { "      $_" }) -join "`n")

  - name: Starcoder2 7B (Autocomplete)
    provider: ollama
    model: starcoder2:7b
    roles:
      - autocomplete
    contextLength: 4096

  - name: Nomic Embed
    provider: ollama
    model: nomic-embed-text:latest
    roles:
      - embed
"@

# ── Write config ────────────────────────────────────────
$config | Out-File -FilePath $configFile -Encoding UTF8
Write-Host "✅ config.yaml updated successfully!"
Write-Host "🔄 Continue.dev will reload automatically."
