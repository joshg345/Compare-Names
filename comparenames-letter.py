import time
import csv

lines = list()
with open('/Users/Grant/Desktop/Territory/91387/91387-LetterTerritory.csv', mode='r', encoding='utf-8-sig') as csv_file:
    with open('/Users/Grant/Desktop/Territory/91387/91387-LetterTerritory-SpanishOnly.csv', mode='a') as output_file:
        fieldnames = ['Name','Address']
        wr = csv.DictWriter(output_file, fieldnames = fieldnames)
        wr.writeheader()
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        firstname = f'{row["First Name"]}'
        lastname = f'{row["Last Name"]}'
        fulladdress = f'{row["Full Address"]}'
        phonenumber = f'{row["Phone Number"]}'
        city = f'{row["City"]}'
        streetname = f'{row["Street Name"]}'
        streetnumber = f'{row["Street Number"]}'
        with open('/Users/Grant/Desktop/Territory/91387/spanishnames.csv', mode='r') as csv_file2:
            csv_reader2 = csv.DictReader(csv_file2)
            line_count2 = 0
            for row2 in csv_reader2:
                spanishname = f'{row2["Spanish Name"]}'
                #print("Comparing '" + lastname + "' with '" + spanishname.capitalize() + "'")
                if spanishname.capitalize() == lastname:
                    print("Spanish name found: " + lastname)
                    with open('/Users/Grant/Desktop/Territory/91387/91387-LetterTerritory-SpanishOnly.csv', mode='a') as output_file1:
                        fieldnames = ['Name','Address']
                        wr2 = csv.DictWriter(output_file1, fieldnames = fieldnames)
                        wr2.writerow({'Name': firstname + " " + lastname, 'Address': streetnumber + " " + streetname + ", " + city})
                    break
                elif "-" + spanishname.capitalize() in lastname:
                    print("Spanish name found: " + lastname)
                    with open('/Users/Grant/Desktop/Territory/91387/91387-LetterTerritory-SpanishOnly.csv', mode='a') as output_file1:
                        fieldnames = ['Name','Address']
                        wr2 = csv.DictWriter(output_file1, fieldnames = fieldnames)
                        wr2.writerow({'Name': firstname + " " + lastname, 'Address': streetnumber + " " + streetname + ", " + city})
                    break
                elif spanishname.capitalize() + "-" in lastname:
                    print("Spanish name found: " + lastname)
                    with open('/Users/Grant/Desktop/Territory/91387/91387-LetterTerritory-SpanishOnly.csv', mode='a') as output_file1:
                        fieldnames = ['Name','Address']
                        wr2 = csv.DictWriter(output_file1, fieldnames = fieldnames)
                        wr2.writerow({'Name': firstname + " " + lastname, 'Address': streetnumber + " " + streetname + ", " + city})
                    break
                line_count2 += 1
    line_count += 1
