
def _input(*prompt):

    try:
        input(prompt)
    except NameError as error:
        row_intput(prompt)