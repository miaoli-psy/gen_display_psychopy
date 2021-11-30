import pandas as pd
import ast
import random
from psychopy import monitors, visual


def get_position_list(df, col_name):
    '''
    df: dataframe that that contains col of positions
    col_name: str
    '''
    # get list like str
    list_like_str = df[col_name].tolist()
    # return list of positions
    return [ast.literal_eval(i) for i in list_like_str]


def select_random_half(posilist):
    n = int(len(posilist) / 2)
    return random.sample(posilist, n)


def get_diff_between_2_lists(list1, list2):
    li_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return li_dif


# read file
path = "../../displays/"
filename = "displays_ms2_exp2.xlsx"  # TODO
displays_xls = pd.ExcelFile(path + filename, engine = "openpyxl")

# list excel sheets
sheet_list = displays_xls.sheet_names

# read displays info into df
displays_df_list = [pd.read_excel(displays_xls, sheet_name) for sheet_name in sheet_list]
display = displays_df_list[1]  # TODO

# central discs
all_posis = get_position_list(display, "allposis")
# central_posis = get_position_list(display, "centralposis")
# extra_posis = get_position_list(display, "extraposis")

disk_radius = 4.57  # TODO
contrast = False
color = "white"

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
if not contrast:
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
        win.saveMovieFrames('output/%sref%s.png' % (color, index + 1))
    win.close()

# include contrast polarity
else:
    for index, central_posi in enumerate(central_posis):
        for j in range(len(central_posi)):
            trgt_disk_b.setPos(central_posi[j])
            trgt_disk_b.draw()
            trgt_disk_w.setPos(extra_posis[index][j])
            trgt_disk_w.draw()

        # fixation 
        fixation = visual.TextStim(win, text = '+', bold = True, color = '#FF9797')
        fixation.setPos([0, 0])
        fixation.draw()

        win.flip()
        win.getMovieFrame()
        win.saveMovieFrames('output/d%s_contrast.png' % (index + 1))
    win.close()

# single fixation
fixation = visual.ShapeStim(win, vertices = "cross", units = "pix", size = (10, 10), fillColor = "#FF9797",
                            lineColor = "#FF9797")
fixation.setPos([0, 0])
fixation.draw()

win.flip()
win.getMovieFrame()
win.saveMovieFrames("output/fixation.png")
win.close()