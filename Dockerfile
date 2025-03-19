FROM python:3.9

WORKDIR /expense_details_app

COPY . .

RUN pip install -r requirements.txt

CMD ["flask", "run"]

