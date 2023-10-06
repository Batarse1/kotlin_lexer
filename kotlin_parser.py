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


# parenthesized expression


# def p_parenthesizedExpression(p):
#     "parenthesizedExpression : LPAREN expression RPAREN"
#     p[0] = p[2]


def p_elvis(p):
    "elvis : QUEST_NO_WS COLON"
    p[0] = p[1]


def postfixUnaryExpression(p):
    """
    postfixUnaryExpression : primaryExpression postfixUnarySuffix
    """
    p[0] = p[1]
    if len(p) > 2:
        for suffix in p[2:]:
            p[0] += suffix


def postfixUnarySuffix(p):
    """postfixUnarySuffix : postfixUnaryOperator"""
    p[0] = p[1]


def p_primaryExpression(p):
    """primaryExpression : literalConstant
    | stringLiteral"""
    p[0] = p[1]


def p_literalConstant(p):
    """literalConstant : INTEGER_LITERAL
    | FLOAT_LITERAL
    | BOOLEAN_LITERAL
    | CHARACTER_LITERAL
    | NULL_LITERAL"""
    p[0] = p[1]


def p_stringLiteral(p):
    """stringLiteral : lineStringLiteral
    | multiLineStringLiteral"""
    p[0] = p[1]


def p_lineStringLiteral(p):
    "lineStringLiteral : LINE_STR_TEXT"
    p[0] = p[1]


def p_multiLineStringLiteral(p):
    "multiLineStringLiteral : MULTI_LINE_STR_TEXT"
    p[0] = p[1]


def p_jumpExpression(p):
    """jumpExpression : CONTINUE
    | BREAK"""
    p[0] = p[1]


def p_equalityOperator(p):
    """equalityOperator : EXCL_EQ
    | EQEQ"""
    p[0] = p[1]


def p_comparisonOperator(p):
    """comparisonOperator : LANGLE
    | RANGLE
    | LE
    | GE"""
    p[0] = p[1]


def p_inOperator(p):
    "inOperator : IN"
    p[0] = p[1]


def p_isOperator(p):
    "isOperator : IS"
    p[0] = p[1]


def p_additiveOperator(p):
    """additiveOperator : ADD
    | SUB"""
    p[0] = p[1]


def p_multiplicativeOperator(p):
    """multiplicativeOperator : MULT
    | DIV
    | MOD"""
    p[0] = p[1]


def p_asOperator(p):
    "asOperator : AS"
    p[0] = p[1]


def prefixUnaryOperator(p):
    """prefixUnaryOperator : ADD
    | SUB
    | excl"""

    p[0] = p[1]


def postfixUnaryOperator(p):
    """postfixUnaryOperator : EXCL_NO_WS excl"""
    p[0] = p[1]


def p_excl(p):
    "excl : EXCL_NO_WS"
    p[0] = p[1]


def p_memberAccessOperator(p):
    """memberAccessOperator : DOT
    | safeNav"""
    p[0] = p[1]


def p_safeNav(p):
    "safeNav : QUEST_NO_WS DOT"
    p[0] = p[1]


# SECTION: identifiers


def simpleIdentifier(p):
    "simpleIdentifier : IDENTIFIER"
    p[0] = p[1]


def identifier(p):
    """
    identifier : simpleIdentifier
               | identifier DOT simpleIdentifier
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + "." + p[3]


def p_error(p):
    print("Syntax error in input!", p)


parser = yacc.yacc()


file = open("source_code.kt", "r")

result = parser.parse(file.read())

print(result)
