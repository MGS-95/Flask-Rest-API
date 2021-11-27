FROM python

WORKDIR /opt/demo/
COPY ./ .

# Install package
RUN pip install -r requirements.txt

# Set environment
ENV FLASK_ENV=production

# Deploy
# ENTRYPOINT ["python", "app.py"]
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]
