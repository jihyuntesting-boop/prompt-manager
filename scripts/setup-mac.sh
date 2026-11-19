#!/usr/bin/env bash
# macOS 개발 환경 설정 (Git 설정, VSCode 확장, 버전 확인)
#
# 사용법 (터미널):
#   bash scripts/setup-mac.sh "GitHub사용자명" "GitHub에 등록한 이메일"
#
# 하지 않는 것: VSCode의 GitHub 로그인은 브라우저 인증이 필요해서 직접 해야 합니다.

set -u

if [ $# -ne 2 ]; then
  echo '사용법: bash scripts/setup-mac.sh "GitHub사용자명" "이메일"'
  exit 1
fi
NAME="$1"
EMAIL="$2"

echo "=== 1. 버전 확인 ==="
python3 --version || echo "python3가 없습니다. https://www.python.org/downloads/ 에서 3.10 이상을 설치하세요."
git --version || echo "git이 없습니다. 터미널에서 'xcode-select --install'을 실행하세요."

echo
echo "=== 2. Git 사용자 정보와 기본 브랜치 설정 ==="
git config --global user.name "$NAME"
git config --global user.email "$EMAIL"
git config --global init.defaultBranch main
echo "user.name          = $(git config --global --get user.name)"
echo "user.email         = $(git config --global --get user.email)"
echo "init.defaultBranch = $(git config --global --get init.defaultBranch)"

echo
echo "=== 3. VSCode 확장 설치 ==="
if command -v code >/dev/null 2>&1; then
  code --install-extension ms-python.python
  code --install-extension MS-CEINTL.vscode-language-pack-ko
  code --list-extensions | grep -E "ms-python.python|language-pack-ko"
else
  echo "'code' 명령을 찾을 수 없습니다."
  echo "VSCode에서 Cmd+Shift+P > 'Shell Command: Install code command in PATH' 실행 후 이 스크립트를 다시 실행하세요."
fi

echo
echo "=== 4. Hello 실행 확인 ==="
python3 -c "print('Hello')"

echo
echo "=== 남은 수동 단계 ==="
echo "1) VSCode 왼쪽 아래 계정 아이콘 > 'GitHub로 로그인' > 브라우저에서 승인"
echo "2) 계정 아이콘에 GitHub 사용자명이 보이면 연동 성공 (이 화면을 캡처)"
