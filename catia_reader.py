import csv
from pycatia import catia

caa = catia()
document = caa.active_document
part = document.part
print(part.name)

parameters = part.parameters

def filter_parameters_by_value(parameters, keyword, max_value):
    flagged = []
    for param in parameters:
        try:
            if keyword in param.name and isinstance(param.value, (int, float)) and not isinstance(param.value, bool) and param.value < max_value:
                flagged.append((param.name, param.value))
        except:
            pass
    return flagged

result = filter_parameters_by_value(parameters, "Radius", 2.5)
print(result)
result2 = filter_parameters_by_value(parameters, "Length", 10)
print(result2)
with open("flagged_report.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Parameter", "Value"])
    for parameter in result:
        writer.writerow(parameter)
    for parameter in result2:
        writer.writerow(parameter)