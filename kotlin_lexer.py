from prettytable import PrettyTable
import ply.lex as lex

keywords = {
    "fun": "FUN",
}

tokens = [
    "STRING",
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "LCURL",
    "RCURL",
    "COLON",
    "SEMICOLON",
    "LANGLE",
    "RANGLE",
] + list(keywords.values())

t_STRING = r"\".*\" "
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LCURL = r"\{"
t_RCURL = r"\}"
t_COLON = r"\:"
t_SEMICOLON = r"\;"
t_LANGLE = r"\<"
t_RANGLE = r"\>"


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = keywords.get(t.value, "ID")
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_line_comment(t):
    r"\/\/.*"
    pass


def t_delimited_comment(t):
    r"\/\*(.|\n)*\*\/"
    pass


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

data = """
// Hello World Program

fun("hello world"){

}
"""

lexer.input(data)

table = PrettyTable()
table.field_names = ["Type", "Value", "Line Number", "Position"]

for tok in lexer:
    table.add_row([tok.type, tok.value, tok.lineno, tok.lexpos])

print(table)
