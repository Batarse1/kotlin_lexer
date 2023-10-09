from ply.lex import lex
from prettytable import PrettyTable

symbols_table = PrettyTable()
symbols_table.field_names = ["Type", "Value", "ID", "level"]

variables = ["VAL", "VAR"]
values = [
    "LINE_STR_TEXT",
    "CHARACTER_LITERAL",
    "INTEGER_LITERAL",
    "FLOAT_LITERAL",
    "MULT",
    "DIV",
    "ADD",
    "SUB",
    "BOOLEAN_LITERAL",
]
types = [
    "Int",
    "Float",
    "Boolean",
    "Char",
    "String",
]
typeMap = {
    int: "Int",
    float: "Float",
    bool: "Boolean",
    str: "String",
}

typeMap[None.__class__] = "Null"

errors = 0

symbols_map = {}


def concatenate_values(lexer_tokens, i, remaining):
    j = 0
    value = []
    row_type = ""
    row_id = lexer_tokens[i + 1]["value"]

    while lexer_tokens[i + remaining + j]["type"] in values:
        if len(row_type) == 0:
            row_type = typeMap[type(lexer_tokens[i + remaining + j]["value"])]

        value.append(lexer_tokens[i + remaining + j]["value"])
        if (i + remaining + j + 1) >= len(lexer_tokens):
            break

        j += 1

    if row_type == "String" and len(lexer_tokens[i + remaining + j]["value"]) == 3:
        row_type = "Char"

    row_value = " ".join(map(str, value))
    row_level = lexer_tokens[i]["level"]

    symbols_map[row_id] = {
        "value": row_value,
        "level": row_level,
        "type": row_type,
    }

    return j


def generate_symbols_table(lexer_tokens):
    i = 0
    global errors
    while i < len(lexer_tokens):
        if lexer_tokens[i]["type"] in variables:
            if lexer_tokens[i + 1]["type"] == "IDENTIFIER":
                if lexer_tokens[i + 2]["type"] == "ASSIGNMENT":
                    j = concatenate_values(lexer_tokens, i, 3)
                    i += 3 + j

                    continue
                elif lexer_tokens[i + 2]["type"] == "COLON":
                    if lexer_tokens[i + 3]["value"] in types:
                        if lexer_tokens[i + 4]["type"] == "ASSIGNMENT":
                            j = concatenate_values(lexer_tokens, i, 5)
                            i += 5 + j

                            continue
                        else:
                            i += 5
                            errors += 1
                            continue
                    else:
                        i += 4
                        errors += 1
                        continue
                else:
                    i += 3
                    errors += 1
                    continue
            else:
                i += 2
                errors += 1
                continue

        i += 1


def print_errors():
    if errors == 1:
        print("There is 1 syntax error in symbols")
    elif errors > 1:
        print("There are", errors, "syntax errors in symbols")


def print_table():
    for key, value in symbols_map.items():
        symbols_table.add_row([value["type"], value["value"], key, value["level"]])
    print("Symbols Table")
    print(symbols_table)
    print_errors()
