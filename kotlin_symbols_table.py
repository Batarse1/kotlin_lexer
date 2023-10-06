from prettytable import PrettyTable

symbols_table = PrettyTable()
symbols_table.field_names = ["Type", "Value", "ID", "level"]

variables = ["VAL", "VAR"]
types = ["TYPE_INT", "TYPE_STRING", "TYPE_DOUBLE", "TYPE_FLOAT", "TYPE_BOOLEAN"]


def error():
    print("TODO ERROR")


def generate_symbols_table(lexer_tokens):
    i = 0
    j = 0
    while i < len(lexer_tokens):
        if lexer_tokens[i]["type"] in variables:
            if lexer_tokens[i + 1]["type"] == "ID":
                if lexer_tokens[i + 2]["type"] == "ASSIGNMENT":
                    a_type = type(lexer_tokens[i + 3]["value"])
                    value = lexer_tokens[i + 3]["value"]
                    id = lexer_tokens[i + 1]["value"]
                    level = lexer_tokens[i]["level"]

                    i += 4

                    symbols_table.add_row([a_type, value, id, level])

                    continue
                elif lexer_tokens[i + 2]["type"] == "COLON":
                    if lexer_tokens[i + 3]["type"] in types:
                        if lexer_tokens[i + 4]["type"] == "ASSIGNMENT":
                            print(
                                [
                                    type(lexer_tokens[i + 5]["value"]),
                                    lexer_tokens[i + 5]["value"],
                                    lexer_tokens[i + 1]["value"],
                                    lexer_tokens[i]["level"],
                                ]
                            )
                            i += 4
                            continue
                        else:
                            error()
                    else:
                        error()
                else:
                    error()
            else:
                error()

        i += 1


def print_table():
    print("Symbols Table")
    print(symbols_table)
