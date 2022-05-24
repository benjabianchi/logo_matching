 FROM python:3.7

 WORKDIR /app

 COPY requirements.txt tm_functions.py /app

 RUN pip install -r requirements.txt

 WORKDIR /app/uploads

 WORKDIR /app

 RUN apt-get update
 RUN apt-get install ffmpeg libsm6 libxext6  -y
 RUN apt install libxcb-xinerama0 

 CMD ["python3" , "app.py"]
