imperialname = ["ounce", "cup", "pint", "quart", "gallon"]
metrictable = [28.41307, 284.1307, 0.56826, 1136.523, 4.54609]
metricname= ["milliliter","milliliter","liter","milliliter","liter"]

layout = "1 {} is equal to {:6.2f}{}"
index =0
while (index != len(metrictable)):
    print(layout.format (imperialname[index],
                         metrictable[index],
                         metricname[index]))
    index = index +1
print("goodbye")
