import pandas as pd
from psychopy import monitors, visual

from src.common.process_basic_data_structure import get_position_list

if __name__ == '__main__':
    fix_color = "black"
    background_color = "#B6B6B6"
    fixation_size = (10, 10)

    disc_color = "black"
    disc_radius = 4.57 # TODO

    # read file
    path = "../displays/"
    filename = "ms1_displays.xlsx"
    displays_xls = pd.ExcelFile(path + filename, engine = "openpyxl")
    displays_df = pd.read_excel(displays_xls)

    # positions
    all_posis = get_position_list(displays_df, "positions")

    # monitor specifications
    monsize = [1920, 1080]
    fullscrn = True
    scr = 0
    mondist = 57
    monwidth = 53.5
    Agui = True
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
                        color = '#B6B6B6')

    # target disk
    trgt_disk = visual.Circle(win, radius = disc_radius, lineColor = "black", fillColor = "black")

    # uniform display
    for index, dp in enumerate(all_posis):
        for i in range(len(dp)):
            trgt_disk.setPos(dp[i])
            trgt_disk.draw()

        # fixation
        fixation = visual.ShapeStim(win,
                                    vertices = "cross",
                                    units = "pix",
                                    size = fixation_size,
                                    fillColor = fix_color,
                                    lineColor = fix_color)
        fixation.setPos([0, 0])
        fixation.draw()

        # filp: see all that have been drawn
        win.flip()

        win.getMovieFrame()
        win.saveMovieFrames('../output/%s.png' % (index + 1))
    win.close()
