import pandas as pd
from psychopy import monitors, visual

from src.common.process_basic_data_structure import get_position_list

if __name__ == '__main__':
    fixation_color = "black"
    # background_color = "#B6B6B6"
    background_color = "white"
    # fixation_size = (10, 10)

    disc_color = "black"

    disc_radius = 5

    # read file
    path = "../displays/"
    numerosity = 32
    filename = "n1000_%s.csv" %(numerosity)

    displays_df = pd.read_csv(path + filename)

    # positions
    all_posis = get_position_list(displays_df, "allposis")

    # monitor specifications
    monsize = [500, 500]
    fullscrn = False
    scr = 0
    mondist = 57
    monwidth = 53.5
    Agui = True
    monitorsetting = monitors.Monitor('Monitor',
                                      width = monwidth,
                                      distance = mondist)
    monitorsetting.setSizePix(monsize)

    # creat new window
    win = visual.Window(monitor=monitorsetting,
                        size=monsize,
                        screen=scr,
                        units='pix',
                        fullscr=fullscrn,
                        allowGUI=Agui,
                        color=background_color)

    # target disk
    trgt_disk = visual.Circle(win, radius=disc_radius, lineColor="black", fillColor="black")

    # draw displays
    for index, dp in enumerate(all_posis):
        for i in range(len(dp)):
            trgt_disk.setPos(dp[i])
            trgt_disk.draw()

        # # fixation
        # fixation = visual.ShapeStim(win,
        #                             vertices="cross",
        #                             units="pix",
        #                             size=fixation_size,
        #                             fillColor=fixation_color,
        #                             lineColor=fixation_color)
        # fixation.setPos([0, 0])
        # fixation.draw()


        win.flip()

        win.getMovieFrame()
        win.saveMovieFrames('../output/%s/%s.png' % (numerosity, index + 1))
    win.close()




