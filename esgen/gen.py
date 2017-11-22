from mimesis.schema import Field


def generate(schema, locale, iterations):
    """generates a list of dicts"""

    field = Field(locale)

    def substitute(src):

        substitution = {}
        for x, y in src.items():
            if isinstance(y, dict):
                substitution[x] = substitute(y)
            else:
                substitution[x] = field(y)

        return substitution

    gen_schema = (lambda: substitute(schema))

    return field.fill(gen_schema, iterations=iterations)