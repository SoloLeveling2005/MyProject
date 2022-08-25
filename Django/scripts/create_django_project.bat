cd ..\

@echo off
set /p title_venv="Enter venv name: "
call %title_venv%/Scripts/activate.bat

pip install django

@echo off
set /p title_project="Enter project name: "
django-admin startproject %title_project%

cmd