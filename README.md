@echo off


call %~dp0telegram_bot\venv\Scripts\activate


cd %~dp0telegram_bot

set TOKEN=5423124439:AAGAhucWLfXPwu6wHB3Wqiq1grKmVaHy6t8

python bot_telegram.py
pause

HOSTNAME = btuxctyhgz