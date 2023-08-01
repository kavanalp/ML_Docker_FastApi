FROM tiangolo/uvicorn-gunicorn:python3.9

WORKDIR /Users/kavanalipanahi/Downloads/docker/app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]