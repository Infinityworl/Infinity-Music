FROM python:3.8
WORKDIR /app
COPY main.py /app/
COPY bot /app/bot/
COPY requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["python", "Nimsara/bot.py"]
