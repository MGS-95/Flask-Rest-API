FROM python

WORKDIR /opt/demo/
COPY ./ .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]