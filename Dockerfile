FROM python:3.9
COPY . .
EXPOSE 8000
RUN pip install -r req.txt
# RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '1234@abcd')" | ./manage.py shell
CMD python manage.py runserver 0.0.0.0:8000