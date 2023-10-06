import ply.lex as lex

from prettytable import PrettyTable

from keywords import keywords
from tokens import tokens

# Arithmetic Operators
t_MULT = r"\*"
t_DIV = r"/"
t_MOD = r"\%"
t_ADD = r"\+"
t_SUB = r"-"

# Parentheses
t_LPAREN = r"\("
t_RPAREN = r"\)"


# Braces
def t_LCURL(t):
    r"\{"
    t.lexer.level += 1
    return t


def t_RCURL(t):
    r"\}"
    t.lexer.level -= 1
    return t


# Square Brackets
t_LSQUARE = r"\["
t_RSQUARE = r"\]"

# Punctuation
t_SEMICOLON = r"\;"
t_COLON = r"\:"
t_COMMA = r"\,"
t_DOT = r"\."

# Assignment Operator
t_ASSIGNMENT = r"="

# Comparison Operators
t_LANGLE = r"\<"
t_RANGLE = r"\>"
t_LE = r"\<="
t_GE = r"\>="
t_EQEQ = r"=="
t_EXCL_EQ = r"\!="

# Logical Operators
t_CONJ = r"&&"
t_DISJ = r"\|\|"

# Other Operators
t_EXCL_NO_WS = r"\!"
t_QUEST_NO_WS = r"\?"


# Identifiers
def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = keywords.get(t.value, "IDENTIFIER")
    return t


# Literals
def t_INTEGER_LITERAL(t):
    r"-\d+ | \d+"
    t.value = int(t.value)
    return t


def t_FLOAT_LITERAL(t):
    r"-\d+\.\d+ | \d+\.\d+"
    t.value = float(t.value)
    return t


def t_BOOLEAN_LITERAL(t):
    r"true | false"
    t.value = bool(t.value)
    return t


def t_CHARACTER_LITERAL(t):
    r"\'(\\.|[^\\\'\n\r])*\'"
    t.value = str(t.value)
    return t


def t_NULL_LITERAL(t):
    r"null"
    t.value = None
    return t


# Strings
t_LINE_STR_TEXT = r"\".*\""
t_MULTI_LINE_STR_TEXT = r"\"\"\".*\"\"\""


# Comments
def t_line_comment(t):
    r"\/\/.*"
    pass


def t_delimited_comment(t):
    r"\/\*(.|\n)*\*\/"
    pass


# Newline
def t_newline(t):
    r"\r?\n"
    t.lexer.lineno += len(t.value)


# Whitespace
t_ignore = " \t"


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()
lexer.level = 0


file = open("source_code.kt", "r")

lexer.input(file.read())

ply_table = PrettyTable()
ply_table.field_names = ["Type", "Value", "Line Number", "Position", "level"]

for tok in lexer:
    ply_table.add_row([tok.type, tok.value, tok.lineno, tok.lexpos, lexer.level])

print("PLY Table")
print(ply_table)
