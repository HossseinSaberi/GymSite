FROM python:3.9
COPY . .
EXPOSE 8000
RUN pip install -r req.txt
RUN python manage.py  createsuperuser --username admin --email admin@admin.com
RUN python manage.py CreateSuperUser --username admin --password 1234@abcd
CMD python manage.py runserver 0.0.0.0:8000