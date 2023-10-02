FROM python

WORKDIR /app

RUN pip install ply
RUN pip install prettytable

COPY kotlin_lexer.py /app

CMD [ "python", "kotlin_lexer.py" ]