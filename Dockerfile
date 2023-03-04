# Daniela Sanchez, dls4848
# Dockerfile for iss_tracker project

FROM python:3.8.10

RUN pip install Flask==2.2.2
RUN pip install requests==2.2.0
RUN pip install xmltodict==0.13.0

COPY iss_tracker.py /iss_tracker.py

CMD ["python", "iss_tracker.py"]
