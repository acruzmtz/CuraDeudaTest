from models.query import create_new_state, create_new_township, create_new_suburb
import xlrd


sheets = [
    "Aguascalientes",
    "Baja_California",
    "Baja_California_Sur",
    "Campeche",
    "Coahuila_de_Zaragoza",
    "Colima",
    "Chiapas",
    "Chihuahua",
    "Distrito_Federal",
    "Durango",
    "Guanajuato",
    "Guerrero",
    "Hidalgo",
    "Jalisco",
    "México",
    "Michoacán_de_Ocampo",
    "Morelos",
    "Nayarit",
    "Nuevo_León",
    "Oaxaca",
    "Puebla",
    "Querétaro",
    "Quintana_Roo",
    "San_Luis_Potosí",
    "Sinaloa",
    "Sonora",
    "Tabasco",
    "Tamaulipas",
    "Tlaxcala",
    "Veracruz_de_Ignacio_de_la_Llave",
    "Yucatán",
    "Zacatecas"
]


def run():
    file_name = 'CPdescarga2.xls'
    openFile = xlrd.open_workbook(file_name)
    number_of_sheets = len(sheets)
    counter = 0

    while counter < number_of_sheets:
        sheet = openFile.sheet_by_name(sheets[counter])

        # code, description
        if create_new_state(int(sheet.cell_value(1, 7)), sheet.cell_value(1, 4)):
            print(f'{sheets[counter]} agregado correctamente')

        for element in range(1, sheet.nrows):
            #print("code: " + sheet.cell_value(element, 11) + " -desc: " + sheet.cell_value(element, 3) + " -state_code: " + sheet.cell_value(element, 7))
            create_new_township(int(sheet.cell_value(element, 11)), sheet.cell_value(element, 3), int(sheet.cell_value(element, 7)))

            #print("code: " + sheet.cell_value(element, 0) + " - desc: " + sheet.cell_value(element, 1) + " - township_code: " + sheet.cell_value(element, 11))
            create_new_suburb(int(sheet.cell_value(element, 0)), sheet.cell_value(element, 1), int(sheet.cell_value(element, 11)))


        print(f"Carga de el estado de {sheets[counter]} exitosamente!")
        counter += 1


if __name__ == '__main__':
    run()
