import ply.yacc as yacc

from kotlin_lexer import tokens

# parsing rules for kotlin
precedence = (
    ("left", "DISJ"),  # Disjunction ||
    ("left", "CONJ"),  # Conjunction &&
    ("left", "EQEQ", "EXCL_EQ"),  # Equality ==, Inequality !=
    ("nonassoc", "LANGLE", "RANGLE", "LE", "GE"),  # Comparison operators <, >, <=, >=
    ("left", "ADD", "SUB"),  # Addition +, Subtraction -
    ("left", "MULT", "DIV", "MOD"),  # Multiplication *, Division /, Modulo %
    ("right", "EXCL_NO_WS"),  # Exclamation mark !
)


def p_espression_disj(p):
    "expression : expression DISJ expression"
    p[0] = p[1] or p[3]


def p_expression_conj(p):
    "expression : expression CONJ expression"
    p[0] = p[1] and p[3]


def p_expression_eqeq(p):
    "expression : expression EQEQ expression"
    p[0] = p[1] == p[3]


def p_expression_excl_eq(p):
    "expression : expression EXCL_EQ expression"
    p[0] = p[1] != p[3]


def p_expression_langle(p):
    "expression : expression LANGLE expression"
    p[0] = p[1] < p[3]


def p_expression_rangle(p):
    "expression : expression RANGLE expression"
    p[0] = p[1] > p[3]


def p_expression_le(p):
    "expression : expression LE expression"
    p[0] = p[1] <= p[3]


def p_expression_ge(p):
    "expression : expression GE expression"
    p[0] = p[1] >= p[3]


def p_expression_add(p):
    "expression : expression ADD term"
    p[0] = p[1] + p[3]


def p_expression_sub(p):
    "expression : expression SUB term"
    p[0] = p[1] - p[3]


def p_expression_term(p):
    "expression : term"
    p[0] = p[1]


def p_term_mult(p):
    "term : term MULT factor"
    p[0] = p[1] * p[3]


def p_term_div(p):
    "term : term DIV factor"
    p[0] = p[1] / p[3]


def p_term_mod(p):
    "term : term MOD factor"
    p[0] = p[1] % p[3]


def p_term_factor(p):
    "term : factor"
    p[0] = p[1]


def p_factor_num(p):
    "factor : INTEGER_LITERAL"
    p[0] = p[1]


def p_factor_expr(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()

while True:
    try:
        s = input("calc > ")
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
