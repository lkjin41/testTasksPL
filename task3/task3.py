import json

values_path = input()
tests_path = input()
report_path = input()


def find_value(values, id):
    for value in values:
        if value["id"] == id:
            return value["value"]
    return None


def fill_values(tests, values):
    for test in tests:
        test["value"] = find_value(values, test["id"])
        if "values" in test:
            fill_values(test["values"], values)


with open(values_path, "r") as file:
    values_data = json.load(file)["values"]

with open(tests_path) as file:
    tests_data = json.load(file)

fill_values(tests_data["tests"], values_data)

with open(report_path, "w") as file:
    json.dump(tests_data, file, indent=4)
