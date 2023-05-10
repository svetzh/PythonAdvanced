text = tuple(sorted(x for x in input()))
elements = {}
for el in text:
    if el not in elements:
        elements[el] = 0
    elements[el] += 1

[print(f"{key}: {value} time/s") for key, value in elements.items()]

# for k, v in elements.items():
#     print(f"{k}: {v} time/s")

