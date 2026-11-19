<#
  Windows 개발 환경 설정 스크립트 (VSCode 확장, Git 설정, 버전 확인)

  사용법 (PowerShell):
    .\scripts\setup-windows.ps1 -Name "GitHub사용자명" -Email "GitHub에 등록한 이메일"

  이 스크립트가 하지 않는 것: VSCode의 GitHub 로그인은 브라우저 인증이 필요해서
  직접 해야 합니다. (아래 안내 참고)
#>
param(
    [Parameter(Mandatory = $true)][string]$Name,
    [Parameter(Mandatory = $true)][string]$Email
)

Write-Host "=== 1. 버전 확인 ===" -ForegroundColor Cyan
python --version
git --version

Write-Host "`n=== 2. Git 사용자 정보와 기본 브랜치 설정 ===" -ForegroundColor Cyan
git config --global user.name $Name
git config --global user.email $Email
git config --global init.defaultBranch main
git config --global --get user.name
git config --global --get user.email
git config --global --get init.defaultBranch

Write-Host "`n=== 3. VSCode 확장 설치 ===" -ForegroundColor Cyan
code --install-extension ms-python.python
code --install-extension MS-CEINTL.vscode-language-pack-ko
code --list-extensions | Select-String -Pattern "ms-python.python|language-pack-ko"

Write-Host "`n=== 4. Hello 실행 확인 ===" -ForegroundColor Cyan
python -c "print('Hello')"

Write-Host "`n=== 남은 수동 단계 ===" -ForegroundColor Yellow
Write-Host "1) VSCode 왼쪽 아래 계정 아이콘 > 'GitHub로 로그인' > 브라우저에서 승인"
Write-Host "2) 계정 아이콘에 GitHub 사용자명이 보이면 연동 성공 (이 화면을 캡처)"
