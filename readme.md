# test 

# Running enviroment
powershell
.\env\Scripts\activate
uvicorn main:app --reload
docker build -t my_fastapi_app .
docker run -d --name my_fastapi_container -p 80:80 my_fastapi_app

