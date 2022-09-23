cd ..\


@echo off
set /p title_project="Enter project name: "

cd %title_project%

@echo off
set /p title_venv="Enter venv name: "
call ../%title_venv%/Scripts/activate.bat



python manage.py startapp main