# test 

# Running enviroment
- `enviroment virtual` python -m venv env
- `powershell` .\env\Scripts\activate
- `rum` uvicorn config.main:app --reload
- `build image docker` docker build -t my_fastapi_app .
- `rum docker` docker run -d --name my_fastapi_container -p 80:80 my_fastapi_app
- `identify process powershell` Get-Process | Where-Object { $_.ProcessName -like "*python*" }
- `kill process` kill 456789

