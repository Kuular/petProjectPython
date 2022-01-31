FROM python:3.10

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r reqierements.txt


ENTRYPOINT ["pytest", ]
CMD ["pytest", "test_pet_store.py"]