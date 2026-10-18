@echo off
set "PATH=C:\Program Files\Git\cmd;%PATH%"

echo [1/3] Adding changes and committing...
git add .
git commit -m "ci: add GitHub Pages auto deploy workflow" 2>nul

echo [2/3] Remote configured:
git remote -v

echo [3/3] Pushing to main branch...
git push -u origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================
    echo SUCCESS: Pushed to GitHub successfully!
    echo ========================================
) else (
    echo.
    echo ========================================
    echo Push failed. Please check error above.
    echo ========================================
)
