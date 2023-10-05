FROM python

WORKDIR /app

RUN pip install ply
RUN pip install prettytable

COPY . /app

CMD [ "python", "kotlin_lexer.py" ]