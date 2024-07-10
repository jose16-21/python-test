# test 

# Running enviroment
- `powershell` .\env\Scripts\activate
- `rum` uvicorn app.main:app --reload
- `build image docker` docker build -t my_fastapi_app .
- `rum docker` docker run -d --name my_fastapi_container -p 80:80 my_fastapi_app

