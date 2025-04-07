def Expression_Evaluation(evalexp):
    def parse(tokens):
        def parse_expression():
            node = parse_term()
            while tokens and tokens[0] in ('+', '-'):
                op = tokens.pop(0)
                right = parse_term()
                if op == '+':
                    node += right
                else:
                    node -= right
            return node

        def parse_term():
            node = parse_factor()
            while tokens and tokens[0] in ('', '/'):
                op = tokens.pop(0)
                right = parse_factor()
                if op == '':
                    node = right
                else:
                    node /= right
            return node

        def parse_factor():
            token = tokens.pop(0)
            if token == '(':
                node = parse_expression()
                tokens.pop(0)  # remove ')'
                return node
            else:
                return float(token)

        return parse_expression()

    def tokenize(expr):
        tokens = []
        number = ''
        for char in expr:
            if char.isdigit() or char == '.':
                number += char
            elif char in '+-/()':
                if number:
                    tokens.append(number)
                    number = ''
                tokens.append(char)
            elif char.isspace():
                if number:
                    tokens.append(number)
                    number = ''
        if number:
            tokens.append(number)
        return tokens

    tokens = tokenize(evalexp)
    return parse(tokens)
print(Expression_Evaluation("2 + 7 * (78 - 1)"))