FROM python:3.9.1

WORKDIR /leetcode

COPY requirements.txt /leetcode/requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/leetcode/exercises"

