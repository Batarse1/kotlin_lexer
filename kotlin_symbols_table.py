def generate_symbols_table(lexer):
    current = ""
    i = 0
    list = []
    symbols_table = {}
    for tok in lexer:
        if current == "VAL ID ASSIGNMENT DIGIT":
            symbols_table[list[i - 2]] = "VAL"
            current = ""

        i += 1
        list.append(tok)
        current += tok.type + " "
