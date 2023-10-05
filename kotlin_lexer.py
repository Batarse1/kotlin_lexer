from prettytable import PrettyTable
import ply.lex as lex

from keywords import keywords
from tokens import tokens

t_RESERVED = r"\.\.\."
t_DOT = r"\."
t_COMMA = r"\,"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LSQUARE = r"\["
t_RSQUARE = r"\]"
t_LCURL = r"\{"
t_RCURL = r"\}"
t_MULT = r"\*"
t_MOD = r"\%"
t_DIV = r"/"
t_ADD = r"\+"
t_SUB = r"-"
t_INCR = r"\+\+"
t_DECR = r"--"
t_CONJ = r"&&"
t_DISJ = r"\|\|"
t_EXCL_NO_WS = r"\!"
t_COLON = r"\:"
t_SEMICOLON = r"\;"
t_ASSIGNMENT = r"="
t_ADD_ASSIGNMENT = r"\+="
t_SUB_ASSIGNMENT = r"-="
t_MULT_ASSIGNMENT = r"\*="
t_DIV_ASSIGNMENT = r"/="
t_MOD_ASSIGNMENT = r"\%="
t_ARROW = r"->"
t_DOUBLE_ARROW = r"=>"
t_RANGE = r"\.\."
t_RANGE_UNTIL = r"\.\.<"
t_COLONCOLON = r"\:\:"
t_DOUBLE_SEMICOLON = r"\;\;"
t_HASH = r"\#"
t_AT_NO_WS = r"@"
t_QUEST_NO_WS = r"\?"
t_LANGLE = r"\<"
t_RANGLE = r"\>"
t_LE = r"\<="
t_GE = r"\>="
t_EXCL_EQ = r"\!="
t_EXCL_EQEQ = r"\!=="
t_EQEQ = r"=="
t_EQEQEQ = r"==="
t_SINGLE_QUOTE = r"\'"
t_AMP = r"&"
t_CHARACTER = r"\'(\\.|[^\\\'\n\r])*\'"
t_QUOTE_OPEN = r"\".*\" "
t_TRIPLE_QUOTE_OPEN = r"\"\"\".*\"\"\""


def t_HEX(t):
    r"0[xX][0-9a-fA-F]+"
    return t


def t_FLOAT(t):
    r"-\d+\.\d+ | \d+\.\d+"
    return t


def t_DIGIT(t):
    r"-\d+ | \d+"
    return t


def t_BOOLEAN(t):
    r"true|false"
    return t


def t_NULL(t):
    r"null"
    return t


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z_0-9]*"
    t.type = keywords.get(t.value, "ID")
    return t


def t_line_comment(t):
    r"\/\/.*"
    pass


def t_delimited_comment(t):
    r"\/\*(.|\n)*\*\/"
    pass


def t_newline(t):
    r"\r?\n"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex(optimize=1)

file = open("source_code.kt", "r")

lexer.input(file.read())

ply_table = PrettyTable()
hashmap_table = PrettyTable()
ply_table.field_names = ["Type", "Value", "Line Number", "Position"]
hashmap_table.field_names = ["Key", "Value"]

hashmap = {}

for tok in lexer:
    hashmap[tok.value] = tok.type
    ply_table.add_row([tok.type, tok.value, tok.lineno, tok.lexpos])

for key, value in hashmap.items():
    hashmap_table.add_row([key, value])

print("PLY Table")
print(ply_table)
print("Hashmap Table")
print(hashmap_table)
