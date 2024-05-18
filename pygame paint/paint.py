# Muhammad Shayaan
# paint.py
# This is a paint program. It can:
'''
1. Draw using pencil, brush
2. Erase using the eraser tool
3. Draw rectangles, both filled and unfilled
4. Give descriptions when a tool is selected
5. Change the color of the tools (spray, pencil, shapes, connector, brush) using the color picker
6. Connect lines by clicking in two spots
7. drip down as you hold the mouse down when spray is selected
8. Save the work you did
9. Open the work you did
10. Undo the work you did
11. Maximize/Minimize the size of the brush using the plus and minus in the top left
12. Clear the canvas
13. stamp stickers on to the canvas using the 6 stickers at the bottom
14. Draw circles, both filled and unfilled
'''
from pygame import *
from sys import *
from random import *
from math import *
from pygame.locals import *
# TKNITER
from tkinter import *
from tkinter.colorchooser import *
from tkinter import filedialog
import os

root = Tk()
root.withdraw()

init()
screen = display.set_mode((1440, 900))
display.set_caption('SUPERHOT Paint Program')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
MAHOGANY = (66, 13, 9)
# ====== BUTTONS ======  # Here are the button's size/location in the form of Rects
pencilButton = Rect(50, 100, 80, 80)  # pencil    
eraserButton = Rect(150, 100, 80, 80)  # eraser
clearButton = Rect(250, 100, 80, 80)  # clear
canvasRect = Rect(530, 150, 850, 500)  # canvas
rectButton = Rect(50, 200, 80, 80)  # rectangles
circleButton = Rect(150, 200, 80, 80)  # circles
sprayButton = Rect(250, 200, 80, 80)  # spray paint
colorPickerButton = Rect(350, 200, 80, 80)  # color picker
brushButton = Rect(50, 300, 80, 80)
connectButton = Rect(150, 300, 80, 80)
undoRect = Rect(1120, 80, 50, 50)
redoRect = Rect(1180, 80, 50, 50)
# --- LARGEN AND SMALLEN (IDT THATS A WRD, BUT STILL)
largeButton = Rect(1330, 80, 50, 50)
smallButton = Rect(1270, 80, 50, 50)
print(font.get_fonts())
# ==== ICONS ====
# --- LOAD / SAVE STUFF ---
saveImage = image.load("save.png")                  # Icon being loaded
saveIcon = transform.scale(saveImage, (40, 40))     # Scales the icon to the proper size (e.g., 40x40)
openImage = image.load("import.png")
openIcon = transform.scale(openImage, (40,40))
openRect = Rect(600, 80, 40, 40)  # load
saveRect = Rect(650, 80, 40, 40)  # save
pencilImage = image.load("pencil.png")
pencilIcon = transform.scale(pencilImage, (80, 80))
eraserImage = image.load("erasericon.png")
eraserIcon = transform.scale(eraserImage, (80, 80))
sprayImage = image.load("spray.png")
sprayIcon = transform.scale(sprayImage, (80, 80))
clearImage = image.load("clearicon.png")
clearIcon = transform.scale(clearImage, (80, 80))
rectImage = image.load("rectangle.png")
rectIcon = transform.scale(rectImage, (80, 80))
circleImage = image.load("circle.png")
circleIcon = transform.scale(circleImage, (80, 80))
brushImage = image.load("brush.png")
brushIcon = transform.scale(brushImage, (80, 80))
connectImage = image.load("connect.png")
connectIcon = transform.scale(connectImage, (80, 80))
largeImage = image.load("large.png")
largeIcon = transform.scale(largeImage, (50, 50))
smallImage = image.load("small.png")
smallIcon = transform.scale(smallImage, (50, 50))
undoImage = image.load("undo.png")
undoIcon = transform.scale(undoImage, (50, 50))
redoImage = image.load("redo.png")
redoIcon = transform.scale(redoImage, (50, 50))
# -------------
background = image.load("background1.jpg")  # loads the background image in a variable
screen.blit(background, (0, 0))  # shows the background image
draw.rect(screen, (255, 255, 255), canvasRect)   # draws the canvas on the screen

#=======STICKERS & STICKER BUTTONS=======   # Stickers are stored different to the buttons for organization purposes
sticker1button = Rect(530, 720, 80, 80)
sticker2button = Rect(620, 720, 80, 80)
sticker3button = Rect(710, 720, 80, 80)
sticker4button = Rect(800, 720, 80, 80)
sticker5button = Rect(890, 720, 80, 80)
sticker6button = Rect(980, 720, 80, 80)
# ----- STICKERS START HERE -----
# sticker1
headExplode = image.load("sticker1.png")    # loads the sticker in a variable
headExplode = transform.scale(headExplode, (200, 200))    # scales it to how shown on screen (200x200)
headButton = transform.scale(headExplode, (75, 75))     # scale to how it is shown as an icon
# sticker 2
katanaHead = image.load("sticker2.png")
katanaHead = transform.scale(katanaHead, (200, 200))
katanaButton = transform.scale(katanaHead, (75, 75))
# sticker3
mainCharac = image.load("sticker3.png")
mainCharac = transform.scale(mainCharac, (200, 200))
characButton = transform.scale(mainCharac, (75, 75))
# sticker4
hacker = image.load("sticker4.webp")
hacker = transform.scale(hacker, (200, 200))
hackButton = transform.scale(hacker, (75, 75))
# sticker5
addict = image.load("sticker5.webp")
addict = transform.scale(addict, (200, 200))
addictButton = transform.scale(addict, (75, 75))
# sticker6
dog = image.load("sticker6.webp")
dog = transform.scale(dog, (200, 200))
dogButton = transform.scale(dog, (75, 75))

# ---STICKER COORDS---
stick1coo = (532, 723)   # the coordinates for the stickers for organization purposes
stick2coo = (626, 723)
stick3coo = (710, 723)
stick4coo = (801, 723)
stick5coo = (890, 723)
stick6coo = (980, 723)

# ==========SHAPES==========
rectShapes = ["placeholder", "rectF", "rectNf"]   # the list where the rectangle picker button (first one in the second row) switches between filled and unfilled
circleShapes = ["placeholder", "circleF", "circleNf"]    # same as the one above, but for circles

# --colorpicker.jpg--
colorpickerImage = image.load("colorpicker.jpg")      # the colorpicker as an image
colorpickerImage = transform.scale(colorpickerImage, (250, 125))   # scaled it
colorpickerRect = Rect(1130, 680, 250, 125)    # The colorpicker with a transparent Rect on top, so that a color can be chosen
#=======BG / CANVAS=======
tool = "None"  # what the tool is, starts as a pencil by default (first button)
running = True      # whether program is opened or not
# ----------- ELLIPSE AND RECT LISTS (DETERMINES INDEX) WITH SOME VARIABLES THAT ARE USED ELSEWHERE-----------
rectPick = 0         # index of the rectangle list
ellipsePick = 0   # index of the circle list
c = (0,0,0)    # colorpicker's color is, by default, black
start_x, start_y = None, None     # the coordinates for the start of the draggable rectangle/circle
end_x, end_y = None, None      # the coordinates for the end of the draggable rectangle/circle
sprayArea = 5     # used for the spray can, as the y drips downward

# === UNDO REDO ===
historyCanvas = []      # where the undo's images are stored
redoListed = []       # for redo's images
canvasLayer=screen.subsurface(canvasRect).copy()   # storing the canvas image as a variable
historyCanvas.append(canvasLayer)    # using the variable to store the image in the list
# ---- BRUSHTOOL ----
thickness = 3     # used to control the size of the pencil
sizePencil = 3     # for the brush (not manually controllable)
drawing = False
# --- TEXT DISPLAYED ON SCREEN ---
my_font = font.SysFont('timesnewroman', 15)
textFont = font.SysFont("Arial", 20, italic=True)    # to display the text of descriptions on the screen
def drawtext (text, font, text_col, x, y):
  img = font.render (text, True, text_col)
  screen.blit(img, (x, y))

while running:
  draw.rect(screen, (0, 0, 0), openRect, 2)   # draws the button to open image on the screen
  screen.blit(openIcon, (600, 80))     # draws the icon
  draw.rect(screen, (0, 0, 0), saveRect)    # draws the save button
  screen.blit(saveIcon, (650, 80)) 
  click = False    # sets the click variable for usage later
  for evt in event.get():
    if evt.type == MOUSEBUTTONDOWN:   # checks if mb down, but not held
      positx, posity = evt.pos     # used for the connector tool 
      click = True    # mb down, not held
      back = screen.copy()    # copy the screen in a variable
      if canvasRect.collidepoint(mx, my):     # if the canvas is collided with the cursor
        surf = Surface((1440, 900))     # sets a variable called surf containing the dimensions of the screen
        surf.blit(screen, (0, 0))  # blits it, not on the screen, but in the list
        historyCanvas.append(surf)   # appends wutever was blitted to the list
      if evt.button == 1:
        start_x, start_y = evt.pos   # starting position for the rect and circle tool
        end_x, end_y = evt.pos    # ending position for the rect and circle tool
        drawing = True     # if mb held, drawing is set as true
    if evt.type == MOUSEMOTION:     # checks if the mouse is moving
      back78 = screen.copy()     # back, but used elsewhere
      sprayArea = 5   # resets the spray if moved
      if drawing:
        end_x, end_y = evt.pos    # the end of the shape is determined by the mouse being let go. 
    if evt.type == MOUSEBUTTONUP:
      drawing = False    # if mb is up, dont draw
    if evt.type == QUIT:
      running = False      # quits, doesnt crash, if X is clicked
  #----------------------------
  mx, my = mouse.get_pos()    # gets position of mouse
  mb = mouse.get_pressed()       # if mouse is held down
  # === CURSOR ===
  if canvasRect.collidepoint(mx, my):
    mouse.set_cursor(SYSTEM_CURSOR_CROSSHAIR)  # changes the cursor if interacting with canvas vs not interacting
  else:
    mouse.set_cursor(SYSTEM_CURSOR_ARROW)
  # === BRUSH TOOL ===
  if brushButton.collidepoint(mx, my):
    if mb[0]:   # if mb is held
      draw.rect(screen, BLUE, brushButton)     # draw BLUE button if clicked
      screen.blit(brushIcon, (50, 300))   # display icon on top
      tool = "brush"   # set the tool to the brush
    else:
      draw.rect(screen, MAHOGANY, brushButton)  # if hovered button is mahogany
      screen.blit(brushIcon, (50, 300))
  else:
    draw.rect(screen, RED, brushButton)   # by default, button is red
    screen.blit(brushIcon, (50, 300))
  # === MAXIMUS OU MINIMUS
  draw.rect(screen, GREEN, largeButton)
  screen.blit(largeIcon, (1330, 80))
  if largeButton.collidepoint(mx, my):
    draw.rect(screen, GRAY, largeButton)
    screen.blit(largeIcon, (1330, 80))
    if mb[0]:
      draw.rect(screen, BLUE, largeButton)
      screen.blit(largeIcon, (1330, 80))
  if click:
    if largeButton.collidepoint(mx, my):
      sizePencil += 3    # if mb is clicked, enlarge the brush
  draw.rect(screen, GREEN, smallButton)
  screen.blit(smallIcon, (1270, 80))
  if smallButton.collidepoint(mx, my):
    draw.rect(screen, GRAY, smallButton)
    screen.blit(smallIcon, (1270, 80))
    if mb[0]:
      draw.rect(screen, BLUE, smallButton)
      screen.blit(smallIcon, (1270, 80))
  if click:
    if smallButton.collidepoint(mx, my):
      sizePencil -= 3    # make brush smaller
  # === LOAD ===
  if click:
    back3 = screen.copy()
    if openRect.collidepoint(mx, my):
      result = filedialog.askopenfilename(filetypes=[("Picture files",
                                                      "*.png;*.jpg")])   # opens the dialogue box to ask user which image to open
      userImage = os.path.abspath(result)   # gets the path selected
      imageSeen = image.load(userImage)         # loads the image into a var
      screen.blit(imageSeen, (530, 150))   # loads image on screen
  # === SAVE ===
    elif saveRect.collidepoint(mx, my):   
      bakk = screen.subsurface(canvasRect)      # stores canvas into a var
      result = filedialog.asksaveasfilename()      # box to save
      image.save(bakk, result + ".png")    # saves the image in selected path, adds .png so that the canvas is viewable
  # === CONNECT DOTS ===
  if connectButton.collidepoint(mx, my):
    if mb[0]:
      draw.rect(screen, BLUE, connectButton)
      screen.blit(connectIcon, (150, 300))
      tool = "connect"
    else:
      draw.rect(screen, MAHOGANY, connectButton)
      screen.blit(connectIcon, (150, 300))
  else:
    draw.rect(screen, RED, connectButton)
    screen.blit(connectIcon, (150, 300))
  # === UNDO ===
  if undoRect.collidepoint(mx, my):
    if click:
      if len (historyCanvas) > 1:     
        redoListed.append(Surface((1440, 900)))     # appends a surface that has the screen size
        redoListed[-1].blit(screen, (0, 0))         # blits the entire screen into a list
        screen.blit(historyCanvas.pop(), (0, 0))    # blits on the screen what is removed from the list
      draw.rect(screen, BLUE, undoRect)
      screen.blit(undoIcon, (1120, 80))
    else:
      draw.rect(screen, MAHOGANY, undoRect)
      screen.blit(undoIcon, (1120, 80))
  else:
    draw.rect(screen, RED, undoRect)
    screen.blit(undoIcon, (1120, 80))
  # == REDO ==
  if redoRect.collidepoint(mx, my):
    if click:
      draw.rect(screen, BLUE, redoRect)
      screen.blit(redoIcon, (1180, 80))
      if len (redoListed) > 0:
        historyCanvas.append(Surface((1440, 900)))    # appends a surface that has the screen size
        historyCanvas[-1].blit(screen, (0, 0))        # blits the entire screen into a list
        screen.blit(redoListed.pop(), (0, 0))         # blits on the screen what is removed from the list
    else:
      draw.rect(screen, MAHOGANY, redoRect)
      screen.blit(redoIcon, (1180, 80))
  else:
    draw.rect(screen, RED, redoRect)
    screen.blit(redoIcon, (1180, 80))
  #=======PENCIL=======
  if pencilButton.collidepoint(mx, my):
    if mb[0]:
      draw.rect(screen, BLUE, pencilButton)
      screen.blit(pencilIcon, (50, 100))
      tool = "pencil"
    else:
      draw.rect(screen, MAHOGANY, pencilButton)
      screen.blit(pencilIcon, (50, 100))
  else:
    draw.rect(screen, RED, pencilButton)
    screen.blit(pencilIcon, (50, 100))
  # =========COLORPICKER=========
  draw.rect(screen, (0, 0, 0, 0), colorpickerRect)
  screen.blit(colorpickerImage, (1130, 680))
  if colorpickerRect.collidepoint(mx, my):
    if mb[0]:
      c = screen.get_at((mx, my))    # gets the color into a variable
      draw.rect(screen, c, (1130, 805, 250, 50))     # draws the selected color into a rectangle (lets user know wut color is picked)
  # =======ERASER=======
  if eraserButton.collidepoint(mx, my):
    if mb[0]:
      draw.rect(screen, BLUE, eraserButton)
      screen.blit(eraserIcon, (150, 100))
      tool = "eraser"
    else:
      draw.rect(screen, MAHOGANY, eraserButton)
      screen.blit(eraserIcon, (150, 100))
  else:
    draw.rect(screen, RED, eraserButton)
    screen.blit(eraserIcon, (150, 100))
  #======= SPRAYPAINT =======
  if sprayButton.collidepoint(mx, my):
    if mb[0]:
      draw.rect(screen, BLUE, sprayButton)
      screen.blit(sprayIcon, (250, 200))
      tool = "spray"
    else:
      draw.rect(screen, MAHOGANY, sprayButton)
      screen.blit(sprayIcon, (250, 200))
  else:
    draw.rect(screen, RED, sprayButton)
    screen.blit(sprayIcon, (250, 200))
  # ======== SHAPES =========
  # ---- RECT ----
  if rectButton.collidepoint(mx, my):
    if mb[0]:
      if click:
        rectPick += 1     # switches from filled to unfilled rect
      if rectPick > 2:
        rectPick = 1    # switches from unfilled to filled rect
      draw.rect(screen, BLUE, rectButton)
      screen.blit(rectIcon, (50, 200))
      tool = rectShapes[rectPick]       # switches between rectangle types
    else:
      draw.rect(screen, MAHOGANY, rectButton)
      screen.blit(rectIcon, (50, 200))
  else:
    draw.rect(screen, RED, rectButton)
    screen.blit(rectIcon, (50, 200))
  # ---- ELLIPSE ----
  if circleButton.collidepoint(mx, my):
    if mb[0]:
      if click:
        ellipsePick += 1   # switches from filled to unfilled circle
      if ellipsePick > 2:
        ellipsePick = 1    # switches from unfilled to filled circle
      draw.rect(screen, BLUE, circleButton)
      screen.blit(circleIcon, (150, 200))
      tool = circleShapes[ellipsePick]   # switches between circle types
    else:
      draw.rect(screen, MAHOGANY, circleButton)
      screen.blit(circleIcon, (150, 200))
  else:
    draw.rect(screen, RED, circleButton)
    screen.blit(circleIcon, (150, 200))
  #=======CLEAR CANVAS=======
  if clearButton.collidepoint(mx, my):
    if mb[0]:
      draw.rect(screen, BLUE, clearButton)
      screen.blit(clearIcon, (250, 100))
      tool = "clear"
    else:
      draw.rect(screen, MAHOGANY, clearButton)
      screen.blit(clearIcon, (250, 100))
  else:
    draw.rect(screen, RED, clearButton)
    screen.blit(clearIcon, (250, 100))
  #=======STICKERS=======
  # sticker1
  if sticker1button.collidepoint(mx, my):
    if mb[0]:
      draw.rect(screen, CYAN, sticker1button)
      screen.blit(headButton, stick1coo)
      tool = "sticker1"
    else:
      draw.rect(screen, BLUE, sticker1button)
      screen.blit(headButton, stick1coo)
  else:
    draw.rect(screen, WHITE, sticker1button)
    screen.blit(headButton, stick1coo)
    # sticker2
  if sticker2button.collidepoint(mx, my):
    if mb[0]:
      draw.rect(screen, CYAN, sticker2button)
      screen.blit(katanaButton, stick2coo)
      tool = "sticker2"
    else:
      draw.rect(screen, BLUE, sticker2button)
      screen.blit(katanaButton, stick2coo)
  else:
    draw.rect(screen, WHITE, sticker2button)
    screen.blit(katanaButton, stick2coo)
    # sticker3
    if sticker3button.collidepoint(mx, my):
      if mb[0]:
        draw.rect(screen, CYAN, sticker3button)
        screen.blit(characButton, stick3coo)
        tool = "sticker3"
      else:
        draw.rect(screen, BLUE, sticker3button)
        screen.blit(characButton, stick3coo)
    else:
      draw.rect(screen, WHITE, sticker3button)
      screen.blit(characButton, stick3coo)
    # sticker4
    if sticker4button.collidepoint(mx, my):
      if mb[0]:
        draw.rect(screen, CYAN, sticker4button)
        screen.blit(hackButton, stick4coo)
        tool = "sticker4"
      else:
        draw.rect(screen, BLUE, sticker4button)
        screen.blit(hackButton, stick4coo)
    else:
      draw.rect(screen, WHITE, sticker4button)
      screen.blit(hackButton, stick4coo)
  # sticker5
  if sticker5button.collidepoint(mx, my):
    if mb[0]:
      draw.rect(screen, CYAN, sticker5button)
      screen.blit(addictButton, stick5coo)
      tool = "sticker5"
    else:
      draw.rect(screen, BLUE, sticker5button)
      screen.blit(addictButton, stick5coo)
  else:
    draw.rect(screen, WHITE, sticker5button)
    screen.blit(addictButton, stick5coo)
  # sticker6
  if sticker6button.collidepoint(mx, my):
    if mb[0]:
      draw.rect(screen, CYAN, sticker6button)
      screen.blit(dogButton, stick6coo)
      tool = "sticker6"
    else:
      draw.rect(screen, BLUE, sticker6button)
      screen.blit(dogButton, stick6coo)
  else:
    draw.rect(screen, WHITE, sticker6button)
    screen.blit(dogButton, stick6coo)
    #=======WHICH TOOL DOES WHAT=======
    randomSpray = (randint(int(mx - 10), int(mx + 10)),
                   randint(int(my + sprayArea - 2), int(my + sprayArea)))   # randomizes the x and y for the spraypaint tool
    if mb[0] and canvasRect.collidepoint(mx, my):
      screen.set_clip(canvasRect)
      if tool == "connect":
        draw.line(screen, c, (positx, posity), (oposx, oposy), sizePencil)     # sets the x and y when mb down, oposx and y being one loop behind to give the connected feeling
      if tool == "brush":
        thickness += 1     # only if the coords are held in one spot, increase brush size
        if thickness > 10:
          thickness = 10         #makes sure it doesnt go out of a specified limit
        if thickness <= 1:
          thickness = 3     #makes sure it doesnt go less than a specified limit
        draw.line(screen, c, (omx, omy), (mx, my), int(thickness))
        if ((omx, omy) != (mx, my)):
          thickness -= 4
      if tool == "pencil":
        drawtext("HEWWo", textFont, (0, 0, 255), 220, 150)
        draw.line(screen, c, (omx, omy), (mx, my), sizePencil)
      if tool == "eraser":
        draw.circle(screen, (255, 255, 255), (mx, my), 10)
      if tool == "spray":
        sprayArea += 5   # increases the sprayArea to give the dripping effect
        draw.circle(screen, c, (randomSpray), 5)

      # ======= SHAPES =======
      # RECTANGLE -----------
      if tool == "rectF":
        if start_x is not None and end_x is not None:  # chacks if mb[0] is held
          screen.blit(back, (0, 0))
          rect_x = min(start_x, end_x)    # gets the minimum between the two xs
          rect_y = min(start_y, end_y)    # gets the minimum between the two ys
          rect_width = abs(end_x - start_x)      # find the absolute value (bc it needs to be drawn)
          rect_height = abs(end_y - start_y)
          draw.rect(screen, c,
                    (rect_x, rect_y, rect_width, rect_height))        # minimum as the starting x and y, width and height determined by the subtraction of both values
      if tool == "rectNf":
        if start_x is not None and end_x is not None:
          screen.blit(back, (0, 0))
          rect_x = min(start_x, end_x)
          rect_y = min(start_y, end_y)
          rect_width = abs(end_x - start_x)
          rect_height = abs(end_y - start_y)
          draw.rect(screen, c,
                    (rect_x, rect_y, rect_width, rect_height), 2)
      # CIRCLE -----------
      if tool == "circleF":
        if start_x is not None and end_x is not None:
          screen.blit(back, (0, 0))
          ellipse_x = min(start_x, end_x)
          ellipse_y = min(start_y, end_y)
          ellipse_width = abs(end_x - start_x)
          ellipse_height = abs(end_y - start_y)
          draw.ellipse(screen, c,
                       (ellipse_x, ellipse_y, ellipse_width, ellipse_height))
      if tool == "circleNf":
        if start_x is not None and end_x is not None:
          screen.blit(back, (0, 0))
          ellipse_x = min(start_x, end_x)
          ellipse_y = min(start_y, end_y)
          ellipse_width = abs(end_x - start_x)
          ellipse_height = abs(end_y - start_y)
          draw.ellipse(screen, c,
                       (ellipse_x, ellipse_y, ellipse_width, ellipse_height),
                       2)
      # ---STICKERS---
      if tool == "sticker1":
        screen.blit(back, (0, 0))
        screen.blit(headExplode, (mx - 100, my - 100))
      if tool == "sticker2":
        screen.blit(back, (0, 0))
        screen.blit(katanaHead, (mx - 100, my - 100))
      if tool == "sticker3":
        screen.blit(back, (0, 0))
        screen.blit(mainCharac, (mx - 100, my - 100))
      if tool == "sticker4":
        screen.blit(back, (0, 0))
        screen.blit(hacker, (mx - 100, my - 100))
      if tool == "sticker5":
        screen.blit(back, (0, 0))
        screen.blit(addict, (mx - 100, my - 100))
      if tool == "sticker6":
        screen.blit(back, (0, 0))
        screen.blit(dog, (mx - 100, my - 100))
    if not mb[0]:
      sprayArea = 5

    screen.set_clip(None)
  if tool == "clear":
    draw.rect(screen, WHITE, canvasRect)
  #-------------------
  pencilSentence = ["Pencil – Using the cursor",
                    "(and clicking on canvas), you can do ",
                    "freehand drawing."]
  eraserSentence = ["Eraser - Erase work done on",
                    "screen, whether it be shapes, images,",
                    "or anything else."]
  brushSentence = ["Brush - Similar to the pencil,",
                   "but thickens and thins continuously.",
                   "  "]
  clearSentence = ["Clear Canvas - removes whatever",
                   "is on the canvas, making it a",
                   "clean slate."
                   ]
  rectSentence = ["Rectangle - Draws a rectangle ",
                  "on the screen. Click the",
                  "rectangle button to get different type."
                  ]
  circleSentence = ["Circle - Draws a circle",
                  "on the screen. Click the",
                  "circle button to get different type."]
  spraySentence = ["Spray - Draws mini-circles on the screen.",
                   "As you hold the mouse, the circles fall.",
                   "If you move the cursor, it resets."]
  connectSentence = ["Conector - Draws a line between",
                     "two points. Those two points are",
                     "determined by where you click."
                     ]
  stickerSentence = ["Stickers - Predetermined images",
                     "that you can drag and click",
                     "onto the canvas."]
  noneSentence = ["Pick a tool to get started!",
                  "   ",
                  "   "]
  largeSentence = ["Enlarge the size of the brush tool",
                  "   ",
                  "   "]
  smallSentence = ["Reduce the size of the brush tool",
                  "   ",
                  "   "]
  omx, omy = mx, my
  if click:
    oposx, oposy = positx, posity
  draw.rect(screen, WHITE, (50, 720, 400, 80), 0, 10)
  for i in range(len(pencilSentence)):
    if tool == "None":
      drawtext(noneSentence[i], textFont, (0, 0, 255), 60, i*23+720)
    if tool == "pencil":
      drawtext(pencilSentence[i], textFont, (0, 0, 255), 60, i*23+720)
      draw.rect(screen, BLUE, pencilButton)
      screen.blit(pencilIcon, (50, 100))
    if tool == "eraser":
      drawtext(eraserSentence[i], textFont, (0, 0, 255), 60, i*23+720)
      draw.rect(screen, BLUE, eraserButton)
      screen.blit(eraserIcon, (150, 100))
    if tool == "brush":
      drawtext(brushSentence[i], textFont, (0, 0, 255), 60, i*23+720)
      draw.rect(screen, BLUE, brushButton)
      screen.blit(brushIcon, (50, 300))
    if tool == "clear":
      drawtext(clearSentence[i], textFont, (0, 0, 255), 60, i*23+720)
    if "rect" in tool:
      drawtext(rectSentence[i], textFont, (0, 0, 255), 60, i*23+720)
      draw.rect(screen, BLUE, rectButton)
      screen.blit(rectIcon, (50, 200))
    if "circle" in tool:
      drawtext(circleSentence[i], textFont, (0, 0, 255), 60, i*23+720)
      draw.rect(screen, BLUE, circleButton)
      screen.blit(circleIcon, (150, 200))
    if tool == "spray":
      drawtext(spraySentence[i], textFont, (0, 0, 255), 60, i*23+720)
      draw.rect(screen, BLUE, sprayButton)
      screen.blit(sprayIcon, (250, 200))
    if "sticker" in tool:
      drawtext(stickerSentence[i], textFont, (0, 0, 255), 60, i*23+720)
    if tool == "connect":
      drawtext(connectSentence[i], textFont, (0, 0, 255), 60, i*23+720)
      draw.rect(screen, BLUE, connectButton)
      screen.blit(connectIcon, (150, 300))
  coordinates = (mx, my)
  if canvasRect.collidepoint(mx, my):
    draw.rect(screen, GRAY, (530, 660, 200, 25), 0, 5)
    text_surface = my_font.render(f"Coordinates: {coordinates}", False, (255, 255, 255))
    screen.blit(text_surface, (550,663))
  display.flip()

quit()
# End of File
