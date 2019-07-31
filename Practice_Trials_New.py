#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.1),
    on Wed Aug  1 14:12:02 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Practice_Trials_Touchscreen'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "trial"
trialClock = core.Clock()
RT_Clock = core.Clock()
first_image = visual.ImageStim(
    win=win, name='first_image',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
second_image = visual.ImageStim(
    win=win, name='second_image',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=(0.3, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-2.0);

mouse = event.Mouse(win=win)
x, y = [None, None]
Top_Left = visual.Rect(
    win=win, name='Top_Left',units='norm', 
    width=(0.3, 0.4)[0], height=(0.3, 0.4)[1],
    ori=0, pos=[0,0],
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
Top_Middle = visual.Rect(
    win=win, name='Top_Middle',units='norm', 
    width=(0.3, 0.4)[0], height=(0.3, 0.4)[1],
    ori=0, pos=[0,0],
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
Top_Right = visual.Rect(
    win=win, name='Top_Right',units='norm', 
    width=(0.3, 0.4)[0], height=(0.3, 0.4)[1],
    ori=0, pos=[0,0],
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
Right_Middle = visual.Rect(
    win=win, name='Right_Middle',units='norm', 
    width=(0.3, 0.4)[0], height=(0.3, 0.4)[1],
    ori=0, pos=[0,0],
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
Bottom_Right = visual.Rect(
    win=win, name='Bottom_Right',units='norm', 
    width=(0.3, 0.4)[0], height=(0.3, 0.4)[1],
    ori=0, pos=[0,0],
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
Bottom_Middle = visual.Rect(
    win=win, name='Bottom_Middle',units='norm', 
    width=(0.3, 0.4)[0], height=(0.3, 0.4)[1],
    ori=0, pos=[0,0],
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
Bottom_Left = visual.Rect(
    win=win, name='Bottom_Left',units='norm', 
    width=(0.3, 0.4)[0], height=(0.3, 0.4)[1],
    ori=0, pos=[0,0],
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
Left_Middle = visual.Rect(
    win=win, name='Left_Middle',units='norm', 
    width=(0.3, 0.4)[0], height=(0.3, 0.4)[1],
    ori=0, pos=[0,0],
    lineWidth=4, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
invisible_clickable = visual.Rect(
    win=win, name='invisible_clickable',units='norm', 
    width=(0.3, 0.4)[0], height=(0.3, 0.4)[1],
    ori=0, pos=[0,0],
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=-13.0, interpolate=True)
green_check = visual.ImageStim(
    win=win, name='green_check',units='norm', 
    image='checkmark.png', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice_trials_new.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    stopLogging = False # Flag to exit 'if' statement after logging one timestamp

    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    first_RT = 0
    trialClock.reset()  # clock
    RT_Clock.reset()
    frameN = -1
    continueRoutine = True
    pause_now = False
    # update component parameters for each repeat
    first_image.setPos(placement1)
    first_image.setImage(stimImg_1)
    second_image.setPos(placement3)
    second_image.setImage(stimImg_1)
    second_image.opacity=0.0
    green_check.opacity = 0.0
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    Top_Left.setPos(TopLeft)
    Top_Middle.setPos(TopMiddle)
    Top_Right.setPos(TopRight)
    Right_Middle.setPos(RightMiddle)
    Bottom_Right.setPos(BottomRight)
    Bottom_Middle.setPos(BottomMiddle)
    Bottom_Left.setPos(BottomLeft)
    Left_Middle.setPos(LeftMiddle)
    invisible_clickable.setPos(placement3)
    green_check.setPos([0,0])
    # keep track of which components have finished
    trialComponents = [first_image, second_image, text, mouse, Top_Left, Top_Middle, Top_Right, Right_Middle, Bottom_Right, Bottom_Middle, Bottom_Left, Left_Middle, invisible_clickable, green_check]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        first_RT = RT_Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *first_image* updates
        if t >= 2.0 and first_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            first_image.tStart = t
            first_image.frameNStart = frameN  # exact frame index
            first_image.setAutoDraw(True)
            thisExp.addData('First Image Onset',first_image.tStart)
        frameRemains = 2.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if first_image.status == STARTED and t >= frameRemains:
            first_image.setAutoDraw(False)
        
        
        # *second_image* updates
        if t >= 2.0 and second_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            second_image.tStart = t
            second_image.frameNStart = frameN  # exact frame index
            second_image.setAutoDraw(True)
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        pauseKey = event.getKeys()
        txt = visual.TextStim(win,text='paused, press R to resume')
        
        if second_image.opacity == 0.0:
            thisExp.addData('Second Image Onset', 'NONE')
            
        if t >= 4:
            second_image.opacity=1.0
            
        if second_image.opacity==1.0 and stopLogging == False:
            thisExp.addData('Second Image Onset',t)
            stopLogging = True 
        
            
        if 'p' in pauseKey:
          td = win._toDraw
          win._toDraw = []  # hides whatever was being auto-drawn
          while not event.getKeys(keyList=['r']):
            txt.draw()
            win.flip()
          win._toDraw = td  # restore auto-draw
          pauseKey = NOT_STARTED
          pauseKey = []  
        
        if 'escape' in pauseKey:
            core.quit()
            
        if second_image.contains(mouse):
            pause_now = True
            green_check.opacity = 1.0
            thisExp.addData('Correct Click Time',t)
            start_time = trialClock.getTime()
            mouse.setPos(newPos=(0,0))

        if pause_now == True and  trialClock.getTime() - start_time > 1.0:
            continueRoutine = False
            
        if Top_Left.contains(mouse) and second_image.opacity == 0.0:
            mouse.setPos(newPos=(0,0))
            thisExp.addData('First Click','Top_Left')
            thisExp.addData('Incorrect Click Time',t)
            
        if Top_Middle.contains(mouse) and second_image.opacity == 0.0:
            mouse.setPos(newPos=(0,0))
            thisExp.addData('First Click','Top_Middle')
            thisExp.addData('Incorrect Click Time',t)
            
        if Top_Right.contains(mouse) and second_image.opacity == 0.0:
            mouse.setPos(newPos=(0,0))
            thisExp.addData('First Click','Top_Right')
            thisExp.addData('Incorrect Click Time',t)
            
        if Right_Middle.contains(mouse) and second_image.opacity == 0.0:
            mouse.setPos(newPos=(0,0))
            thisExp.addData('First Click','Right_Middle')
            thisExp.addData('Incorrect Click Time',t)
            
        if Bottom_Right.contains(mouse) and second_image.opacity == 0.0:
            mouse.setPos(newPos=(0,0))
            thisExp.addData('First Click','Bottom_Right')
            thisExp.addData('Incorrect Click Time',t)
            
        if Bottom_Middle.contains(mouse) and second_image.opacity == 0.0:
            mouse.setPos(newPos=(0,0))
            thisExp.addData('First Click','Bottom_Middle')
            thisExp.addData('Incorrect Click Time',t)
            
        if Bottom_Left.contains(mouse) and second_image.opacity == 0.0:
            mouse.setPos(newPos=(0,0))
            thisExp.addData('First Click','Bottom_Left')
            thisExp.addData('Incorrect Click Time',t)
            
        if Left_Middle.contains(mouse) and second_image.opacity == 0.0:
            mouse.setPos(newPos=(0,0))
            thisExp.addData('First Click','Left_Middle')
            thisExp.addData('Incorrect Click Time',t)
            
        

        # *mouse* updates
        if t >= 0.0 and mouse.status == NOT_STARTED:
            # keep track of start time/frame for later
            mouse.tStart = t
            mouse.frameNStart = frameN  # exact frame index
            mouse.status = STARTED
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not stopped!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    x, y = mouse.getPos()
                   # mouse.x.append(x)
                    #mouse.y.append(y)
                    #mouse.leftButton.append(buttons[0])
                    #mouse.midButton.append(buttons[1])
                    #mouse.rightButton.append(buttons[2])
                    #mouse.time.append(trialClock.getTime())
                    # check if the mouse was inside our 'clickable' objects
                    for obj in [second_image]:
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *Top_Left* updates
        if t >= 0.0 and Top_Left.status == NOT_STARTED:
            # keep track of start time/frame for later
            Top_Left.tStart = t
            Top_Left.frameNStart = frameN  # exact frame index
            Top_Left.setAutoDraw(True)
        if np.all([Top_Left.status == STARTED,second_image.opacity>0.0,bool(Updated=='Top_Left')]):
        #if np.all([Top_Left.status == STARTED,second_image.opacity>0.0]):
            Top_Left.setPos([-1.2,1])
            #Top_Left.size = .00001
            #Top_Left.setAutoDraw(False)
        
        # *Top_Middle* updates
        if t >= 0.0 and Top_Middle.status == NOT_STARTED:
            # keep track of start time/frame for later
            Top_Middle.tStart = t
            Top_Middle.frameNStart = frameN  # exact frame index
            Top_Middle.setAutoDraw(True)
        if np.all([Top_Middle.status == STARTED,second_image.opacity>0.0,bool(Updated=='Top_Middle')]):
            Top_Middle.setPos([-1.2,1])
            #Top_Middle.size = .00001
            Top_Middle.setAutoDraw(False)
            
        # *Top_Right* updates
        if t >= 0.0 and Top_Right.status == NOT_STARTED:
            # keep track of start time/frame for later
            Top_Right.tStart = t
            Top_Right.frameNStart = frameN  # exact frame index
            Top_Right.setAutoDraw(True)
        if np.all([Top_Right.status == STARTED,second_image.opacity>0.0,bool(Updated=='Top_Right')]):
            Top_Right.setPos([-1.2,1])
            #Top_Right.size = .00001
            Top_Right.setAutoDraw(False)
            
        # *Right_Middle* updates
        if t >= 0.0 and Right_Middle.status == NOT_STARTED:
            # keep track of start time/frame for later
            Right_Middle.tStart = t
            Right_Middle.frameNStart = frameN  # exact frame index
            Right_Middle.setAutoDraw(True)
        if np.all([Right_Middle.status == STARTED,second_image.opacity>0.0,bool(Updated=='Right_Middle')]):
            Right_Middle.setPos([-1.2,1])
            #Right_Middle.size = .00001
            Right_Middle.setAutoDraw(False)
            
        # *Bottom_Right* updates
        if t >= 0.0 and Bottom_Right.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bottom_Right.tStart = t
            Bottom_Right.frameNStart = frameN  # exact frame index
            Bottom_Right.setAutoDraw(True)
        if np.all([Bottom_Right.status == STARTED,second_image.opacity>0.0,bool(Updated=='Bottom_Right')]):
            Bottom_Right.setPos([-1.2,1])
            #Bottom_Right.size = .00001
            Bottom_Right.setAutoDraw(False)
            
        # *Bottom_Middle* updates
        if t >= 0.0 and Bottom_Middle.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bottom_Middle.tStart = t
            Bottom_Middle.frameNStart = frameN  # exact frame index
            Bottom_Middle.setAutoDraw(True)
        if np.all([Bottom_Middle.status == STARTED,second_image.opacity>0.0,bool(Updated=='Bottom_Middle')]):
            Bottom_Middle.setPos([-1.2,1])
            #Bottom_Middle.size = .00001
            Bottom_Middle.setAutoDraw(False)
            
        # *Bottom_Left* updates
        if t >= 0.0 and Bottom_Left.status == NOT_STARTED:
            # keep track of start time/frame for later
            Bottom_Left.tStart = t
            Bottom_Left.frameNStart = frameN  # exact frame index
            Bottom_Left.setAutoDraw(True)
        if np.all([Bottom_Left.status == STARTED,second_image.opacity>0.0,bool(Updated=='Bottom_Left')]):
            Bottom_Left.setPos([-1.2,1])
            #Bottom_Left.size = .00001
            Bottom_Left.setAutoDraw(False)
            
        # *Left_Middle* updates
        if t >= 0.0 and Left_Middle.status == NOT_STARTED:
            # keep track of start time/frame for later
            Left_Middle.tStart = t
            Left_Middle.frameNStart = frameN  # exact frame index
            Left_Middle.setAutoDraw(True)
        if np.all([Left_Middle.status == STARTED,second_image.opacity>0.0,bool(Updated=='Left_Middle')]):
            Left_Middle.setPos([-1.2,1])
            #Left_Middle.size = .00001
            Left_Middle.setAutoDraw(False)
            
        # *invisible_clickable* updates
        if t >= 0.0 and invisible_clickable.status == NOT_STARTED:
            # keep track of start time/frame for later
            invisible_clickable.tStart = t
            invisible_clickable.frameNStart = frameN  # exact frame index
            invisible_clickable.setAutoDraw(True)
        frameRemains = 0.0 + 0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if invisible_clickable.status == STARTED and t >= frameRemains:
            invisible_clickable.setAutoDraw(False)
        
        # *green_check* updates
        if t >= 0.0 and green_check.status == NOT_STARTED:
            # keep track of start time/frame for later
            green_check.tStart = t
            green_check.frameNStart = frameN  # exact frame index
            green_check.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # store data for trials_2 (TrialHandler)
    if len(mouse.x): trials_2.addData('mouse.x', mouse.x[0])
    if len(mouse.y): trials_2.addData('mouse.y', mouse.y[0])
    if len(mouse.leftButton): trials_2.addData('mouse.leftButton', mouse.leftButton[0])
    if len(mouse.midButton): trials_2.addData('mouse.midButton', mouse.midButton[0])
    if len(mouse.rightButton): trials_2.addData('mouse.rightButton', mouse.rightButton[0])
    if len(mouse.time): trials_2.addData('mouse.time', mouse.time[0])
    if len(mouse.clicked_name): trials_2.addData('mouse.clicked_name', mouse.clicked_name[0])
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
