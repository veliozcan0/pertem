@echo off
chcp 65001 >nul
echo.
echo 🚀 MSB Scraper Manuel Tetikleme
echo ================================
echo.

echo 📋 GitHub CLI kontrol ediliyor...
gh --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ GitHub CLI kurulu değil!
    echo.
    echo 📥 Kurulum için: https://cli.github.com/
    echo.
    pause
    exit /b 1
)

echo ✅ GitHub CLI kurulu
echo.

echo 🔐 Kimlik doğrulama kontrol ediliyor...
gh auth status >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  GitHub'a giriş yapılmamış
    echo.
    echo 🔑 Giriş yapmak için: gh auth login
    echo.
    pause
    exit /b 1
)

echo ✅ GitHub'a giriş yapılmış
echo.

echo 🚀 MSB Scraper workflow'u başlatılıyor...
gh workflow run "MSB Günlük Veri Çekme"

if %errorlevel% equ 0 (
    echo.
    echo ✅ Workflow başarıyla başlatıldı!
    echo.
    echo 📊 Durumu kontrol etmek için:
    echo    gh run list --workflow="MSB Günlük Veri Çekme"
    echo.
    echo 👀 Canlı logları izlemek için:
    echo    gh run watch --workflow="MSB Günlük Veri Çekme"
) else (
    echo.
    echo ❌ Workflow başlatılamadı!
    echo.
    echo 🔍 Hata detayları için logları kontrol edin
)

echo.
pause
