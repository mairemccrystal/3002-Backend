import csv
import cv2


with open('garments.csv') as csvfile:
    reader = csv.DictReader(csvfile)

 # Creating the menu
    print('---- MENU -----')
    print('--PRESS 1 FOR TOP LAYER --')
    print('--PRESS 2 FOR BOTTOM LAYER --')
    print('--PRESS 3 FOR SHOES --')
    print('--PRESS 4 TO CLOSE THE PROGRAM --')


    menu_action = input('')

    if menu_action == '1':
        countTop = 0
        for column in reader:
                if column['Garment Layer'] == 'Top':
                    topID = column['ID']
                    print(topID)
                    countTop = countTop+1
        print(countTop)

    elif menu_action == '2':
            countBottom = 0
            for column in reader:
                if column['Garment Layer'] == 'Bottom':
                    bottomID = column['ID']
                    print(bottomID)
                    countBottom = countBottom + 1
            print(countBottom)

    elif menu_action == '3':
            countShoes = 0
            for column in reader:
                if column['Garment Layer'] == 'Shoe':
                    shoeID = column['ID']
                    print(shoeID)
                    countShoes = countShoes + 1
            print(countShoes)

