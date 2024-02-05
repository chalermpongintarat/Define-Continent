with open("define_country.txt", "r") as file: 
    lines = file.read().split("\n")

    f = open("continent.txt", "w")

    australia = ["Australia"]
    asia = ["Bhutan", "Cambodia", "China", "Hong Kong", "India", "Japan", "Korea", "Laos", 
                "Malaysia", "Myanmar", "Nepal", "Philippines", "Singapore", "South Korea", 
                "Taiwan", "Thailand", "Viet Nam"]
    europe = ["Albania", "Austria", "Belarus", "Belgium", "Bulgaria", "Croatia", 
                "Czech Republic", "Denmark", "France", "Germany", "Hungary", "Ireland", 
                "Israel", "Italy", "Latvia", "Lithuania", "Netherlands", "Poland", "Portugal",
                "Romania", "Russia", "Serbia", "Slovakia", "Slovenia", "Spain", "Switzerland",
                "Turkey", "Ukraine", "United Kingdom"]
    none = ["None"]
    north_america = ["Canada", "Costa Rica", "Mexico", "USA"]
    south_america = ["Chile", "Colombia", "Peru", "Uruguay"]

    for line in lines:
        if line in australia:
            f.write("Australia" + "\n")
        elif line in asia:
            f.write("Asia" + "\n")
        elif line in europe:
            f.write("Europe" + "\n")
        elif line in none:
            f.write("None" + "\n")
        elif line in north_america:
            f.write("North America" + "\n")
        elif line in south_america:
            f.write("South America" + "\n")
        else:
            f.write("Can not define" + "\n")

    f.close()