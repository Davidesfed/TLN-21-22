import csv

path = 'c:\\Users\\amministratore\\Desktop\\Scuola\Magistrale\\TLN\\03\ Di\ Caro\\Esercitazioni\\FCA\\concepts.csv'
concepts = []
with open(path, 'r', encoding='utf8') as f:
    data = csv.reader(f)
    features = next(data)[1:]
    for i, row in enumerate(data):
        animal_name = row[0]
        res = [animal_name,]
        print(f"Animal: {animal_name}")
        for feature in features:
            r = input(f'Is this animal {feature}? (0/1)\n')
            if r == '1':
                res.append('X')
            elif r == '0':
                res.append('')
        concepts.append(res)
        print(f'Caratteristiche di {res[0]}: ' + str([features[i] for i, el in enumerate(res) if el == 'X']))