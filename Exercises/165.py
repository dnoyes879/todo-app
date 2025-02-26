import FreeSimpleGUI as sg

sg.theme('Black')

feet_label = sg.Text('Enter feet:')
inches_label = sg.Text('Enter inches:')

feet_input = sg.InputText(tooltip='Enter a feet value', key = 'feet')
inches_input = sg.InputText(tooltip= 'Enter an inch value', key = 'inches')

convert_button = sg.Button('Convert')
exit_button = sg.Button('Exit')

result_text = sg.Text(key='result')

window = sg.Window('Convertor', layout = [[feet_label, feet_input],
                                          [inches_label, inches_input],
                                          [convert_button, exit_button,result_text]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Convert':
            metres = .3048*float(values['feet']) + 0.0254*float(values['inches'])
            window['result'].update(value=metres, text_color= 'white')
            print(metres)

        case sg.WIN_CLOSED:
            break

        case 'Exit':
            break





window.close()