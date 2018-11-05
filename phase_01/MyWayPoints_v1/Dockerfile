FROM python:3.6.4-slim
COPY ./MyWayPoints /MyWayPoints
RUN pip install -r /MyWayPoints/requirements.txt
ENTRYPOINT ["python", "/MyWayPoints/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
EXPOSE 8000