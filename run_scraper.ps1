# MSB Scraper Manuel Tetikleme - PowerShell Script
# UTF-8 encoding ile çalıştırın

Write-Host ""
Write-Host "🚀 MSB Scraper Manuel Tetikleme" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# GitHub CLI kontrol
Write-Host "📋 GitHub CLI kontrol ediliyor..." -ForegroundColor Yellow
try {
    $ghVersion = gh --version 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ GitHub CLI kurulu" -ForegroundColor Green
        Write-Host "   $ghVersion" -ForegroundColor Gray
    } else {
        throw "GitHub CLI bulunamadı"
    }
} catch {
    Write-Host "❌ GitHub CLI kurulu değil!" -ForegroundColor Red
    Write-Host ""
    Write-Host "📥 Kurulum için: https://cli.github.com/" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Devam etmek için Enter'a basın"
    exit 1
}

Write-Host ""

# Kimlik doğrulama kontrol
Write-Host "🔐 Kimlik doğrulama kontrol ediliyor..." -ForegroundColor Yellow
try {
    $authStatus = gh auth status 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ GitHub'a giriş yapılmış" -ForegroundColor Green
        Write-Host "   $authStatus" -ForegroundColor Gray
    } else {
        throw "Kimlik doğrulama hatası"
    }
} catch {
    Write-Host "⚠️  GitHub'a giriş yapılmamış" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "🔑 Giriş yapmak için: gh auth login" -ForegroundColor Cyan
    Write-Host ""
    Read-Host "Devam etmek için Enter'a basın"
    exit 1
}

Write-Host ""

# Workflow başlat
Write-Host "🚀 MSB Scraper workflow'u başlatılıyor..." -ForegroundColor Yellow
try {
    $result = gh workflow run "MSB Günlük Veri Çekme" 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✅ Workflow başarıyla başlatıldı!" -ForegroundColor Green
        Write-Host ""
        Write-Host "📊 Durumu kontrol etmek için:" -ForegroundColor Cyan
        Write-Host "   gh run list --workflow=`"MSB Günlük Veri Çekme`"" -ForegroundColor White
        Write-Host ""
        Write-Host "👀 Canlı logları izlemek için:" -ForegroundColor Cyan
        Write-Host "   gh run watch --workflow=`"MSB Günlük Veri Çekme`"" -ForegroundColor White
        Write-Host ""
        Write-Host "🌐 GitHub Actions'da görüntülemek için:" -ForegroundColor Cyan
        Write-Host "   https://github.com/veliozcan0/pertem/actions" -ForegroundColor White
    } else {
        throw "Workflow başlatılamadı"
    }
} catch {
    Write-Host ""
    Write-Host "❌ Workflow başlatılamadı!" -ForegroundColor Red
    Write-Host ""
    Write-Host "🔍 Hata detayları:" -ForegroundColor Yellow
    Write-Host "$result" -ForegroundColor Red
    Write-Host ""
    Write-Host "💡 Çözüm önerileri:" -ForegroundColor Cyan
    Write-Host "   1. Repository ayarlarını kontrol edin" -ForegroundColor White
    Write-Host "   2. Workflow dosyasının doğru olduğundan emin olun" -ForegroundColor White
    Write-Host "   3. GitHub token'ınızı yenileyin: gh auth logout && gh auth login" -ForegroundColor White
}

Write-Host ""
Read-Host "Çıkmak için Enter'a basın"
