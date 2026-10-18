Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " [Detail Slice Compressor] Git Repository Setup Script " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

# 1. PATH 자동 갱신 및 Git 실행 파일 자동 탐색
$possibleGitPaths = @(
    "C:\Program Files\Git\cmd",
    "C:\Program Files\Git\bin",
    "C:\Program Files (x86)\Git\cmd",
    "$env:LOCALAPPDATA\Programs\Git\cmd"
)

foreach ($p in $possibleGitPaths) {
    if (Test-Path $p) {
        if ($env:Path -notlike "*$p*") {
            $env:Path = "$p;$env:Path"
        }
    }
}

# 2. Git 설치 확인
$gitCmd = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitCmd) {
    Write-Host "[ERROR] Git executable not found in default paths." -ForegroundColor Red
    Write-Host "Please ensure Git is installed at C:\Program Files\Git" -ForegroundColor Yellow
    Write-Host ""
    return
}

$gitVer = git --version
Write-Host "[OK] Git detected: $gitVer" -ForegroundColor Green
Write-Host ""

# 3. Git init & branch
Write-Host "[1/4] Initializing Git repository & setting main branch..." -ForegroundColor Green
git init
git branch -M main

# 4. Git staging
Write-Host "[2/4] Staging project files..." -ForegroundColor Green
git add .

# 5. Git config user identity check
$userName = git config user.name
if (-not $userName) {
    git config user.name "Seller-Kim"
    git config user.email "seller@market.local"
}

# 6. Git commit
Write-Host "[3/4] Creating initial commit..." -ForegroundColor Green
git commit -m "feat: detail page slice and webp compressor SPA"

# 6. GitHub CLI (gh) Check
Write-Host "[4/4] Checking GitHub CLI (gh)..." -ForegroundColor Green
$possibleGhPaths = @(
    "C:\Program Files\GitHub CLI",
    "$env:LOCALAPPDATA\Programs\GitHub CLI"
)
foreach ($gp in $possibleGhPaths) {
    if (Test-Path $gp) {
        if ($env:Path -notlike "*$gp*") {
            $env:Path = "$gp;$env:Path"
        }
    }
}

$ghCmd = Get-Command gh -ErrorAction SilentlyContinue
if ($ghCmd) {
    $reply = Read-Host "GitHub CLI (gh) detected! Create remote repo on GitHub now? (y/n)"
    if ($reply -eq 'y' -or $reply -eq 'Y') {
        gh repo create detail-slice-compressor --public --source=. --remote=origin --push
    } else {
        Write-Host "Skipped remote repository creation." -ForegroundColor Gray
    }
} else {
    Write-Host "GitHub CLI (gh) not detected." -ForegroundColor Yellow
    Write-Host "To link and push to your remote GitHub repository manually:" -ForegroundColor Gray
    Write-Host "  1. Create a repository on https://github.com/new" -ForegroundColor Gray
    Write-Host "  2. Run the following commands:" -ForegroundColor Gray
    Write-Host "     git remote add origin https://github.com/<YOUR_ID>/detail-slice-compressor.git" -ForegroundColor White
    Write-Host "     git push -u origin main" -ForegroundColor White
}

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Done! Git repository and initial commit are ready! " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
