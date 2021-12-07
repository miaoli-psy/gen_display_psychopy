import pandas as pd
from psychopy import monitors, visual

from src.common.process_basic_data_structure import get_position_list, select_random_half, get_diff_between_2_lists

if __name__ == '__main__':
    # TODO
    fix_fillcolor = "#FF9797"
    fix_linecolor = "#FF9797"
    background_color = '#B6B6B6'
    fixation_size = (10, 10)

    disc_color_black = "black"
    disc_color_white = "white"

    # read file
    path = "../displays/"
    filename = "displays.xlsx"
    displays_xls = pd.ExcelFile(path + filename, engine = "openpyxl")

    # list excel sheets
    sheet_list = displays_xls.sheet_names
    # TODO
    # sheet_name = "ref"
    # sheet_name = "stim"
    sheet_name = "subtitizing"

    # read displays info into df
    displays_df_list = [pd.read_excel(displays_xls, sheet_name) for sheet_name in sheet_list]
    indx = sheet_list.index(sheet_name)
    display = displays_df_list[indx]

    # central discs
    all_posis = get_position_list(display, "allposis")
    if sheet_name == "stim":
        central_posis = get_position_list(display, "centralposis")
        extra_posis = get_position_list(display, "extraposis")

    disk_radius = 4.57  # TODO
    color = disc_color_white

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
    trgt_disk = visual.Circle(win, radius = disk_radius, lineColor = "black", fillColor = "black")
    trgt_disk_b = visual.Circle(win, radius = disk_radius, lineColor = "black", fillColor = "black")
    trgt_disk_w = visual.Circle(win, radius = disk_radius, lineColor = "white", fillColor = "white")

    # contrast ref displays
    black_posis = [select_random_half(posis) for posis in all_posis]
    white_posis = list()
    for i, posis in enumerate(all_posis):
        white = get_diff_between_2_lists(posis, black_posis[i])
        white_posis.append(white)

    # uniform display
    for index, dp in enumerate(all_posis):
        for i in range(len(dp)):

            if color == 'black':
                trgt_disk_b.setPos(dp[i])
                trgt_disk_b.draw()
            elif color == 'white':
                trgt_disk_w.setPos(dp[i])
                trgt_disk_w.draw()
        # fixation
        # fixation = visual.TextStim(win, text= '+', bold = True, color= '#FF9797')
        fixation = visual.ShapeStim(win, vertices = "cross", units = "pix", size = (10, 10), fillColor = "#FF9797",
                                    lineColor = "#FF9797")
        fixation.setPos([0, 0])
        fixation.draw()

        # filp: see all that have been drawn
        win.flip()

        win.getMovieFrame()
        win.saveMovieFrames('../output/%ssub%s.png' % (color, index + 1))
    win.close()
