import pandas as pd
import os
from psychopy import core, monitors, visual
import ast


def str_to_list(string: str) -> list:
    return ast.literal_eval(string)


if __name__ == '__main__':
    path = 'displays/'
    filename = 'exp2_displays.xlsx'
    displays = pd.read_excel(path + filename, engine = 'openpyxl')

    disk_radius = 3.82
    # monsize = [1024, 768]
    monsize = [1920, 1080]
    fullscrn = False
    scr = 0
    mondist = 57
    monwidth = 41
    Agui = False
    monitorsetting = monitors.Monitor('Monitor',
                                      width = monwidth,
                                      distance = mondist)
    monitorsetting.setSizePix(monsize)

    # creat new window
    win = visual.Window(monitor = monitorsetting,
                        size = monsize,
                        screen = scr,
                        units = 'pix',
                        fullscr = fullscrn,
                        allowGUI = Agui,
                        color = [0, 0, 0])

    # target disk
    trgt_disk = visual.Circle(win, radius = disk_radius, lineColor = "black", fillColor = "black")

    allposis = displays["all posis"]
    allposis_list = list()
    for i in range(0, 600):
        posi = str_to_list(allposis[i])
        allposis_list.append(posi)

    for i, display in enumerate(allposis_list):
        for posi in display:
            trgt_disk.setPos(posi)
            trgt_disk.draw()

        fixation = visual.TextStim(win, text = '+', bold = True, color = (-1.0, -1.0, -1.0))
        fixation.setPos([0, 0])
        fixation.draw()

        win.flip()
        win.getMovieFrame()
        win.saveMovieFrames("d%s.png" % (i + 1))

    win.close()
