import PySimpleGUI as sg
sg.theme("DarkBlue10")
sg.theme_text_color("#C1CDCD")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DIKELAS",
                          font=("Arial",25,"italic","bold","underline"))],      
                       [sg.Text("Nama     : RISKY ALFARIT")],
                           [sg.Text("NPM      : 22100104")],
                           [sg.Text("Kelas    : 5A TI Nonreg BJM")],
                           [sg.Text("Matkul : Visual 3")],
                           [sg.Text("UNISKA BANJARMASIN")],
                         ],
                    size=(500,200),
                    font=("Times",18))
window()
window.close()