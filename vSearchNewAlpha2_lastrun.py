#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 21, 2020, at 15:55
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'vSearchNewAlpha2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'taskVer': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\Documents\\Work\\Projects\\vSearchNewAlpha2\\vSearchNewAlpha2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1088, 614], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()

# Initialize components for Routine "instr"
instrClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text=None,
    font='Arial',
    pos=[0,0.1], height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instrResp = keyboard.Keyboard()
l1ex = visual.ImageStim(
    win=win,
    name='l1ex', 
    image='L1.png', mask=None,
    ori=0, pos=(-0.3, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
l2ex = visual.ImageStim(
    win=win,
    name='l2ex', 
    image='L2.png', mask=None,
    ori=0, pos=(-0.1, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
t1ex = visual.ImageStim(
    win=win,
    name='t1ex', 
    image='T1.png', mask=None,
    ori=0, pos=(0.1, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
tTex = visual.ImageStim(
    win=win,
    name='tTex', 
    image='TT.png', mask=None,
    ori=0, pos=(0.3, -0.3), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialFix = visual.TextStim(win=win, name='trialFix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trialL11 = visual.ImageStim(
    win=win,
    name='trialL11', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
trialL12 = visual.ImageStim(
    win=win,
    name='trialL12', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
trialL21 = visual.ImageStim(
    win=win,
    name='trialL21', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
trialL22 = visual.ImageStim(
    win=win,
    name='trialL22', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
trialT11 = visual.ImageStim(
    win=win,
    name='trialT11', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
trialT12 = visual.ImageStim(
    win=win,
    name='trialT12', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
trialL13 = visual.ImageStim(
    win=win,
    name='trialL13', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
trialL14 = visual.ImageStim(
    win=win,
    name='trialL14', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
trialL23 = visual.ImageStim(
    win=win,
    name='trialL23', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
trialL24 = visual.ImageStim(
    win=win,
    name='trialL24', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
trialT13 = visual.ImageStim(
    win=win,
    name='trialT13', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
trialT14 = visual.ImageStim(
    win=win,
    name='trialT14', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
trialL15 = visual.ImageStim(
    win=win,
    name='trialL15', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
trialL16 = visual.ImageStim(
    win=win,
    name='trialL16', 
    image='L1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
trialL25 = visual.ImageStim(
    win=win,
    name='trialL25', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
trialL26 = visual.ImageStim(
    win=win,
    name='trialL26', 
    image='L2.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
trialT15 = visual.ImageStim(
    win=win,
    name='trialT15', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
trialT16 = visual.ImageStim(
    win=win,
    name='trialT16', 
    image='T1.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-18.0)
trialTT = visual.ImageStim(
    win=win,
    name='trialTT', 
    image='TT.png', mask=None,
    ori=0, pos=[0,0], size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-19.0)
trialResp = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='This is the end of the experiment. Thank you for your time. Please remember to return to the questionnaire to carry on with the study. Press ‘space’ to exit.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endResp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
taskLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('taskCond.xlsx'),
    seed=None, name='taskLoop')
thisExp.addLoop(taskLoop)  # add the loop to the experiment
thisTaskLoop = taskLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTaskLoop.rgb)
if thisTaskLoop != None:
    for paramName in thisTaskLoop:
        exec('{} = thisTaskLoop[paramName]'.format(paramName))

for thisTaskLoop in taskLoop:
    currentLoop = taskLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTaskLoop.rgb)
    if thisTaskLoop != None:
        for paramName in thisTaskLoop:
            exec('{} = thisTaskLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    if condsFile == "vSearch1Cond.xlsx":
        instrText.text = "In this task you will see sets of shapes made of four different shapes as outlined below. Only press the ‘s’ key if you see the upright “T” shape, which is the last shape. Otherwise, press the ‘k’ key. There will be 6, 12, or 18 shapes to observe in each trial. Press ‘space’ to continue."
    elif condsFile == "vSearch2Cond.xlsx":
        instrText.text = "A quick break before the next set of trials. Remember, only press the ‘s’ key if you see the upright “T” shape, which is the last shape below. Otherwise, press the ‘k’ key. There will be 6, 12, or 18 shapes to observe in each trial. Press ‘space’ to continue."
    elif condsFile == "vSearchCond.xlsx":
        instrText.text = "A quick break before the next set of trials. Remember, only press the ‘s’ key if you see the upright “T” shape, which is the last shape below. Otherwise, press the ‘k’ key. There will be 6, 12, or 18 shapes to observe in each trial. Press ‘space’ to continue."
    else: 
        instrText.text = "A quick break before the next set of trials. Remember, only press the ‘s’ key if you see the upright “T” shape, which is the last shape below. Otherwise, press the ‘k’ key. There will be 6, 12, or 18 shapes to observe in each trial. Press ‘space’ to continue."
    instrResp.keys = []
    instrResp.rt = []
    _instrResp_allKeys = []
    # keep track of which components have finished
    instrComponents = [instrText, instrResp, l1ex, l2ex, t1ex, tTex]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrText* updates
        if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrText.frameNStart = frameN  # exact frame index
            instrText.tStart = t  # local t and not account for scr refresh
            instrText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
            instrText.setAutoDraw(True)
        
        # *instrResp* updates
        waitOnFlip = False
        if instrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrResp.frameNStart = frameN  # exact frame index
            instrResp.tStart = t  # local t and not account for scr refresh
            instrResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrResp, 'tStartRefresh')  # time at next scr refresh
            instrResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instrResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instrResp.status == STARTED and not waitOnFlip:
            theseKeys = instrResp.getKeys(keyList=['space'], waitRelease=False)
            _instrResp_allKeys.extend(theseKeys)
            if len(_instrResp_allKeys):
                instrResp.keys = _instrResp_allKeys[-1].name  # just the last key pressed
                instrResp.rt = _instrResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *l1ex* updates
        if l1ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l1ex.frameNStart = frameN  # exact frame index
            l1ex.tStart = t  # local t and not account for scr refresh
            l1ex.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l1ex, 'tStartRefresh')  # time at next scr refresh
            l1ex.setAutoDraw(True)
        
        # *l2ex* updates
        if l2ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l2ex.frameNStart = frameN  # exact frame index
            l2ex.tStart = t  # local t and not account for scr refresh
            l2ex.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l2ex, 'tStartRefresh')  # time at next scr refresh
            l2ex.setAutoDraw(True)
        
        # *t1ex* updates
        if t1ex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            t1ex.frameNStart = frameN  # exact frame index
            t1ex.tStart = t  # local t and not account for scr refresh
            t1ex.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(t1ex, 'tStartRefresh')  # time at next scr refresh
            t1ex.setAutoDraw(True)
        
        # *tTex* updates
        if tTex.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tTex.frameNStart = frameN  # exact frame index
            tTex.tStart = t  # local t and not account for scr refresh
            tTex.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tTex, 'tStartRefresh')  # time at next scr refresh
            tTex.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    taskLoop.addData('instrText.started', instrText.tStartRefresh)
    taskLoop.addData('instrText.stopped', instrText.tStopRefresh)
    taskLoop.addData('l1ex.started', l1ex.tStartRefresh)
    taskLoop.addData('l1ex.stopped', l1ex.tStopRefresh)
    taskLoop.addData('l2ex.started', l2ex.tStartRefresh)
    taskLoop.addData('l2ex.stopped', l2ex.tStopRefresh)
    taskLoop.addData('t1ex.started', t1ex.tStartRefresh)
    taskLoop.addData('t1ex.stopped', t1ex.tStopRefresh)
    taskLoop.addData('tTex.started', tTex.tStartRefresh)
    taskLoop.addData('tTex.stopped', tTex.tStopRefresh)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condsFile),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        trialL11.setPos([loc1,loc2])
        trialL12.setPos([loc3,loc4])
        trialL21.setPos([loc5,loc6])
        trialL22.setPos([loc7,loc8])
        trialT11.setPos([loc9,loc10])
        trialT12.setPos([loc11,loc12])
        trialL13.setPos((loc13, loc14))
        trialL14.setPos((loc15, loc16))
        trialL23.setPos((loc17, loc18))
        trialL24.setPos((loc19, loc20))
        trialT13.setPos((loc21, loc22))
        trialT14.setPos((loc23, loc24))
        trialL15.setPos((loc25, loc26))
        trialL16.setPos((loc27, loc28))
        trialL25.setPos((loc29, loc30))
        trialL26.setPos((loc31, loc32))
        trialT15.setPos((loc33, loc34))
        trialT16.setPos((loc35, loc36))
        trialTT.setPos([loc37,loc38])
        trialResp.keys = []
        trialResp.rt = []
        _trialResp_allKeys = []
        # keep track of which components have finished
        trialComponents = [trialFix, trialL11, trialL12, trialL21, trialL22, trialT11, trialT12, trialL13, trialL14, trialL23, trialL24, trialT13, trialT14, trialL15, trialL16, trialL25, trialL26, trialT15, trialT16, trialTT, trialResp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trialFix* updates
            if trialFix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialFix.frameNStart = frameN  # exact frame index
                trialFix.tStart = t  # local t and not account for scr refresh
                trialFix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialFix, 'tStartRefresh')  # time at next scr refresh
                trialFix.setAutoDraw(True)
            if trialFix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trialFix.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    trialFix.tStop = t  # not accounting for scr refresh
                    trialFix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trialFix, 'tStopRefresh')  # time at next scr refresh
                    trialFix.setAutoDraw(False)
            
            # *trialL11* updates
            if trialL11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL11.frameNStart = frameN  # exact frame index
                trialL11.tStart = t  # local t and not account for scr refresh
                trialL11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL11, 'tStartRefresh')  # time at next scr refresh
                trialL11.setAutoDraw(True)
            
            # *trialL12* updates
            if trialL12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL12.frameNStart = frameN  # exact frame index
                trialL12.tStart = t  # local t and not account for scr refresh
                trialL12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL12, 'tStartRefresh')  # time at next scr refresh
                trialL12.setAutoDraw(True)
            
            # *trialL21* updates
            if trialL21.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL21.frameNStart = frameN  # exact frame index
                trialL21.tStart = t  # local t and not account for scr refresh
                trialL21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL21, 'tStartRefresh')  # time at next scr refresh
                trialL21.setAutoDraw(True)
            
            # *trialL22* updates
            if trialL22.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL22.frameNStart = frameN  # exact frame index
                trialL22.tStart = t  # local t and not account for scr refresh
                trialL22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL22, 'tStartRefresh')  # time at next scr refresh
                trialL22.setAutoDraw(True)
            
            # *trialT11* updates
            if trialT11.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialT11.frameNStart = frameN  # exact frame index
                trialT11.tStart = t  # local t and not account for scr refresh
                trialT11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialT11, 'tStartRefresh')  # time at next scr refresh
                trialT11.setAutoDraw(True)
            
            # *trialT12* updates
            if trialT12.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialT12.frameNStart = frameN  # exact frame index
                trialT12.tStart = t  # local t and not account for scr refresh
                trialT12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialT12, 'tStartRefresh')  # time at next scr refresh
                trialT12.setAutoDraw(True)
            
            # *trialL13* updates
            if trialL13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL13.frameNStart = frameN  # exact frame index
                trialL13.tStart = t  # local t and not account for scr refresh
                trialL13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL13, 'tStartRefresh')  # time at next scr refresh
                trialL13.setAutoDraw(True)
            
            # *trialL14* updates
            if trialL14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL14.frameNStart = frameN  # exact frame index
                trialL14.tStart = t  # local t and not account for scr refresh
                trialL14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL14, 'tStartRefresh')  # time at next scr refresh
                trialL14.setAutoDraw(True)
            
            # *trialL23* updates
            if trialL23.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL23.frameNStart = frameN  # exact frame index
                trialL23.tStart = t  # local t and not account for scr refresh
                trialL23.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL23, 'tStartRefresh')  # time at next scr refresh
                trialL23.setAutoDraw(True)
            
            # *trialL24* updates
            if trialL24.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL24.frameNStart = frameN  # exact frame index
                trialL24.tStart = t  # local t and not account for scr refresh
                trialL24.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL24, 'tStartRefresh')  # time at next scr refresh
                trialL24.setAutoDraw(True)
            
            # *trialT13* updates
            if trialT13.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialT13.frameNStart = frameN  # exact frame index
                trialT13.tStart = t  # local t and not account for scr refresh
                trialT13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialT13, 'tStartRefresh')  # time at next scr refresh
                trialT13.setAutoDraw(True)
            
            # *trialT14* updates
            if trialT14.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialT14.frameNStart = frameN  # exact frame index
                trialT14.tStart = t  # local t and not account for scr refresh
                trialT14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialT14, 'tStartRefresh')  # time at next scr refresh
                trialT14.setAutoDraw(True)
            
            # *trialL15* updates
            if trialL15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL15.frameNStart = frameN  # exact frame index
                trialL15.tStart = t  # local t and not account for scr refresh
                trialL15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL15, 'tStartRefresh')  # time at next scr refresh
                trialL15.setAutoDraw(True)
            
            # *trialL16* updates
            if trialL16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL16.frameNStart = frameN  # exact frame index
                trialL16.tStart = t  # local t and not account for scr refresh
                trialL16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL16, 'tStartRefresh')  # time at next scr refresh
                trialL16.setAutoDraw(True)
            
            # *trialL25* updates
            if trialL25.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL25.frameNStart = frameN  # exact frame index
                trialL25.tStart = t  # local t and not account for scr refresh
                trialL25.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL25, 'tStartRefresh')  # time at next scr refresh
                trialL25.setAutoDraw(True)
            
            # *trialL26* updates
            if trialL26.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialL26.frameNStart = frameN  # exact frame index
                trialL26.tStart = t  # local t and not account for scr refresh
                trialL26.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialL26, 'tStartRefresh')  # time at next scr refresh
                trialL26.setAutoDraw(True)
            
            # *trialT15* updates
            if trialT15.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialT15.frameNStart = frameN  # exact frame index
                trialT15.tStart = t  # local t and not account for scr refresh
                trialT15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialT15, 'tStartRefresh')  # time at next scr refresh
                trialT15.setAutoDraw(True)
            
            # *trialT16* updates
            if trialT16.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialT16.frameNStart = frameN  # exact frame index
                trialT16.tStart = t  # local t and not account for scr refresh
                trialT16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialT16, 'tStartRefresh')  # time at next scr refresh
                trialT16.setAutoDraw(True)
            
            # *trialTT* updates
            if trialTT.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialTT.frameNStart = frameN  # exact frame index
                trialTT.tStart = t  # local t and not account for scr refresh
                trialTT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTT, 'tStartRefresh')  # time at next scr refresh
                trialTT.setAutoDraw(True)
            
            # *trialResp* updates
            waitOnFlip = False
            if trialResp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                trialResp.frameNStart = frameN  # exact frame index
                trialResp.tStart = t  # local t and not account for scr refresh
                trialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
                trialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trialResp.status == STARTED and not waitOnFlip:
                theseKeys = trialResp.getKeys(keyList=['s', 'k', 'w', 'e', 'a', 'd', 'z', 'x', 'i', 'o', 'j', 'm', ',', 'l'], waitRelease=False)
                _trialResp_allKeys.extend(theseKeys)
                if len(_trialResp_allKeys):
                    trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                    trialResp.rt = _trialResp_allKeys[-1].rt
                    # was this correct?
                    if (trialResp.keys == str(corrAns)) or (trialResp.keys == corrAns):
                        trialResp.corr = 1
                    else:
                        trialResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('trialFix.started', trialFix.tStartRefresh)
        trials.addData('trialFix.stopped', trialFix.tStopRefresh)
        trials.addData('trialL11.started', trialL11.tStartRefresh)
        trials.addData('trialL11.stopped', trialL11.tStopRefresh)
        trials.addData('trialL12.started', trialL12.tStartRefresh)
        trials.addData('trialL12.stopped', trialL12.tStopRefresh)
        trials.addData('trialL21.started', trialL21.tStartRefresh)
        trials.addData('trialL21.stopped', trialL21.tStopRefresh)
        trials.addData('trialL22.started', trialL22.tStartRefresh)
        trials.addData('trialL22.stopped', trialL22.tStopRefresh)
        trials.addData('trialT11.started', trialT11.tStartRefresh)
        trials.addData('trialT11.stopped', trialT11.tStopRefresh)
        trials.addData('trialT12.started', trialT12.tStartRefresh)
        trials.addData('trialT12.stopped', trialT12.tStopRefresh)
        trials.addData('trialL13.started', trialL13.tStartRefresh)
        trials.addData('trialL13.stopped', trialL13.tStopRefresh)
        trials.addData('trialL14.started', trialL14.tStartRefresh)
        trials.addData('trialL14.stopped', trialL14.tStopRefresh)
        trials.addData('trialL23.started', trialL23.tStartRefresh)
        trials.addData('trialL23.stopped', trialL23.tStopRefresh)
        trials.addData('trialL24.started', trialL24.tStartRefresh)
        trials.addData('trialL24.stopped', trialL24.tStopRefresh)
        trials.addData('trialT13.started', trialT13.tStartRefresh)
        trials.addData('trialT13.stopped', trialT13.tStopRefresh)
        trials.addData('trialT14.started', trialT14.tStartRefresh)
        trials.addData('trialT14.stopped', trialT14.tStopRefresh)
        trials.addData('trialL15.started', trialL15.tStartRefresh)
        trials.addData('trialL15.stopped', trialL15.tStopRefresh)
        trials.addData('trialL16.started', trialL16.tStartRefresh)
        trials.addData('trialL16.stopped', trialL16.tStopRefresh)
        trials.addData('trialL25.started', trialL25.tStartRefresh)
        trials.addData('trialL25.stopped', trialL25.tStopRefresh)
        trials.addData('trialL26.started', trialL26.tStartRefresh)
        trials.addData('trialL26.stopped', trialL26.tStopRefresh)
        trials.addData('trialT15.started', trialT15.tStartRefresh)
        trials.addData('trialT15.stopped', trialT15.tStopRefresh)
        trials.addData('trialT16.started', trialT16.tStartRefresh)
        trials.addData('trialT16.stopped', trialT16.tStopRefresh)
        trials.addData('trialTT.started', trialTT.tStartRefresh)
        trials.addData('trialTT.stopped', trialTT.tStopRefresh)
        # check responses
        if trialResp.keys in ['', [], None]:  # No response was made
            trialResp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               trialResp.corr = 1;  # correct non-response
            else:
               trialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('trialResp.keys',trialResp.keys)
        trials.addData('trialResp.corr', trialResp.corr)
        if trialResp.keys != None:  # we had a response
            trials.addData('trialResp.rt', trialResp.rt)
        trials.addData('trialResp.started', trialResp.tStartRefresh)
        trials.addData('trialResp.stopped', trialResp.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'taskLoop'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
endResp.keys = []
endResp.rt = []
_endResp_allKeys = []
# keep track of which components have finished
endComponents = [endText, endResp]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    
    # *endResp* updates
    waitOnFlip = False
    if endResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endResp.frameNStart = frameN  # exact frame index
        endResp.tStart = t  # local t and not account for scr refresh
        endResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endResp, 'tStartRefresh')  # time at next scr refresh
        endResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endResp.status == STARTED and not waitOnFlip:
        theseKeys = endResp.getKeys(keyList=['space'], waitRelease=False)
        _endResp_allKeys.extend(theseKeys)
        if len(_endResp_allKeys):
            endResp.keys = _endResp_allKeys[-1].name  # just the last key pressed
            endResp.rt = _endResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('endText.started', endText.tStartRefresh)
thisExp.addData('endText.stopped', endText.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
