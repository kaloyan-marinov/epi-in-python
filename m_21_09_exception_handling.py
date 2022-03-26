import csv
import json
import logging


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def get_value_1(filename, key):
    """
    The `finally` block is always executed,
    regardless of whether an exception was raised and/or caught.
    """
    handle = open(filename)

    try:
        file_contents = handle.read()
        json_contents = json.loads(file_contents)
        return json_contents[key]
    finally:
        # Prevent a resource leak if [the `try` block raises an exception].
        logging.info("executing the `finally` clause")
        handle.close()


def get_value_2(filename, key):
    """
    Note the duplicated code used to prevent a resource leak.
    """
    handle = open(filename)

    try:
        file_contents = handle.read()
        json_contents = json.loads(file_contents)
        handle.close()
        return (True, json_contents[key])
    except Exception:
        # Ensure that no resource leak will occur.
        handle.close()
        return (False,)


def get_value_3(filename, key):
    """
    The duplicated code in `get_value_2` can be avoided
    by using `try`-`except`-`finally`.

    It bears repeating that
    "The `finally` block is always executed,
    regardless of whether an exception was raised and/or caught."
    (which in this case might seem surprising to less-experienced programmers, because
    each of the blocks preceding the `finally` block ends with a `return` statement).
    """
    handle = open(filename)

    try:
        file_contents = handle.read()
        json_contents = json.loads(file_contents)
        value = json_contents[key]
        logging.info("returning %s", (True, value))
        return (True, value)
    except Exception as e:
        logging.info("catching an %s", e)
        return (False,)
    finally:
        # Ensure that no resource leak will occur.
        logging.info("executing the `finally` clause")
        handle.close()


class ColumnSumCsvParseException(Exception):
    def __init__(self, *args):
        Exception.__init__(self, *args)  # perhaps replace `Exception` with `super()`?
        self.line_number = args[1]


def get_col_sum(filename, col):
    # May raise `IOError` - will propagate to the caller.
    csv_file = open(filename)
    csv_reader = csv.reader(csv_file)

    line_number = 0
    running_sum = 0

    try:
        for row in csv_reader:
            if col >= len(row):
                raise IndexError("Not enough entries in row " + str(row))

            value = row[col]

            # If the value in the `col`-th column cannot be parsed to an integer,
            # skip that row & log that fact.
            try:
                running_sum += int(value)
            except ValueError:
                print("Cannot convert " + value + " to int, ignoring")

            line_number += 1
    except csv.Error:
        # Programs should raise exceptions appropriate to their level of abstraction.
        # So, we propagate the `csv.Error` as a custom-made exception to the caller.
        print("In `csv.Error` handler")
        raise ColumnSumCsvParseException(
            "Error processing csv",
            line_number,
        )
    else:
        print("Sum = " + str(running_sum))
    finally:
        # Ensure that no resource leak will occur.
        csv_file.close()
        return running_sum
