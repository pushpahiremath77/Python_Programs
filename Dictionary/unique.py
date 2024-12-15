sample_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
               {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

unique_values = set()

for dictionary in sample_data:
    for value in dictionary.values():
        unique_values.add(value)
print("Unique Values:", unique_values)
