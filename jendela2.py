import PySimpleGUI as sg
sg.theme("DarkBlue10")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("Nama     : RISKY ALFARIT")],
                           [sg.Text("NPM      : 22100104")],
                           [sg.Text("Kelas    : 5A TI Nonreg BJM")],
                           [sg.Text("Matkul : Visual 3")],
                           [sg.Text("UNISKA BANJARMASIN")],
                         ],
                    size=(500,200))
                  
window()
window.close()