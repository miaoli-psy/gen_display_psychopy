from psychopy import monitors, visual

if __name__ == '__main__':
    # TODO
    fillcolor = "#FF9797"
    linecolor = "#FF9797"
    background_color = '#B6B6B6'
    fixation_size = (10, 10)

    # monitor specifications
    monsize = [1920, 1080]
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
    win = visual.Window(monitor = monitorsetting,
                        size = monsize,
                        screen = scr,
                        units = 'pix',
                        fullscr = fullscrn,
                        allowGUI = Agui,
                        color = background_color)

    # single fixation
    fixation = visual.ShapeStim(win, vertices = "cross", units = "pix", size = fixation_size, fillColor = fillcolor,
                                lineColor = linecolor)
    fixation.setPos([0, 0])
    fixation.draw()

    win.flip()
    win.getMovieFrame()
    win.saveMovieFrames("../output/fixation.png")
    win.close()
