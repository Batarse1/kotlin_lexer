from keywords import keywords

tokens = [
    # Arithmetic Operators
    "MULT",  # Multiplication *
    "DIV",  # Division /
    "MOD",  # Modulo %
    "ADD",  # Addition +
    "SUB",  # Subtraction -
    # Parentheses
    "LPAREN",  # Left parenthesis (
    "RPAREN",  # Right parenthesis )
    # Braces
    "LCURL",  # Left curly brace {
    "RCURL",  # Right curly brace }
    # Square Brackets:
    "LSQUARE",  # Left square bracket [
    "RSQUARE",  # Right square bracket ]
    # Punctuation
    "SEMICOLON",  # Semicolon ;
    "COLON",  # Colon :
    "COMMA",  # Comma ,
    "DOT",  # Dot .
    # Assignment Operator
    "ASSIGNMENT",  # Assignment =
    # Comparison Operators
    "LANGLE",  # Less than <
    "RANGLE",  # Greater than >
    "LE",  # Less than or equal to <=
    "GE",  # Greater than or equal to >=
    "EQEQ",  # Equality ==
    "EXCL_EQ",  # Inequality !=
    # Logical Operators
    "CONJ",  # Conjunction &&
    "DISJ",  # Disjunction ||
    # Other Operators
    "EXCL_NO_WS",  # Exclamation mark !
    "QUEST_NO_WS",  # Question mark ?
    # Identifiers
    "IDENTIFIER",  # Identifier (e.g. main)
    # Literals
    "INTEGER_LITERAL",  # Integer literal (e.g. 42)
    "FLOAT_LITERAL",  # Float literal (e.g. 3.14)
    "BOOLEAN_LITERAL",  # Boolean literal (e.g. true)
    "CHARACTER_LITERAL",  # Character literal (e.g. 'a')
    "NULL_LITERAL",  # Null literal (e.g. null)
    # Strings
    "LINE_STR_TEXT",  # Line string text (e.g. Hello)
    "MULTI_LINE_STR_TEXT",  # Multi-line string text (e.g. Hello)
    # Keywords
] + list(keywords.values())
