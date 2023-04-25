FROM apache/airflow:2.5.3

ENV AIRFLOW_HOME=/opt/airflow

USER airflow

WORKDIR $AIRFLOW_HOME

COPY . .

RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r requirements.txt