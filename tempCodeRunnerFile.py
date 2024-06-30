
# # Initialize the degree dictionary
# degree = {
#     "A": "",
#     "B": "",
#     "C": "",
#     "D": "",
#     "E": "",
#     "F": "",
#     "G": "",
#     "H": "",
#     "I": "",
#     "J": ""
# }

# # Populate the degree dictionary
# for entry in rulebook:
#     rule, y_final = entry
#     rule_part = rule.split('=')[0]  # Extract the part before the '=' sign
#     degree[y_final] += rule_part + ", "  # Concatenate with a comma

# # Add "max(" and ")" and remove trailing comma
# for key, value in degree.items():
#     degree[key] = "max(" + value[:-2] + ")"

# # Print the degree dictionary
# for key, value in degree.items():
#     print(f"{key}= {value}")



