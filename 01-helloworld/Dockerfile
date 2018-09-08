FROM python:3.7

COPY Pipfile /
COPY Pipfile.lock /

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

COPY app.py /
COPY swagger.yaml /
RUN chmod +x app.py

WORKDIR /data
CMD /app.py