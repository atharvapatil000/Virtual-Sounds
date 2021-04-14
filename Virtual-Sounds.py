import cv2
import numpy as np
import imutils
import pygame
import time

pygame.mixer.init()
pygame.init()

from tkinter import *
import tkinter.messagebox
from tkinter import ttk

root = Tk()
root.geometry('900x700')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
root.title('VIRTUAL AIR DRUM')
frame.config(background='light blue')
label = Label(frame, text="VIRTUAL AIR DRUM", bg='light blue', font=('Times 35 bold'))
label.pack(side=TOP)

background_label = Label(frame)
background_label.pack(side=TOP)

menu = Menu(root)
root.config(menu=menu)

def contri():
    tkinter.messagebox.showinfo("Contributors", "\n 1. Rakshitha Krishnan \n 2. Atharva Patil \n 3. Aditya Kadam \n 4. Kartiki Pande")

def helpp():
    help(cv2)

def prj():
    tkinter.messagebox.showinfo("Our Project", "Welcome ! \n Is this your first time using our drum set or are you stuck somewhere? \n Don't worry, we are here to help you \n \n Select drum stick 1:- \n \n Select the colour of your own preference which will be detected by our program(the colours offered are red, blue , green and yellow) \n \n  Select drumstick2:- \n \n Select the colour of your own preference which will be detected by our program(the colours offered are red, blue , green and yellow) \n \n Play drums:- \n \n In this option you will be able to play the drums without recording your video while playing it \n \n  Play drums while recording:- \n \n If you want to record yourself while playing the drums, this is the option for you. \n We wish you a fun and good user experience!")

subm1 = Menu(menu)
menu.add_cascade(label="Tools", menu=subm1)
subm1.add_command(label="Help", command = helpp)

subm2 = Menu(menu)
menu.add_cascade(label="About", menu=subm2)
subm2.add_command(label="Our Project", command = prj)
subm2.add_command(label="Contributors", command = contri)



def rec():
    drop1txt = combo1.get()
    drop2txt = combo2.get()
    print(drop1txt)
    print(drop2txt)
    cap = cv2.VideoCapture(0);
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    op = cv2.VideoWriter('Download.avi', fourcc, 11.0, (640, 480))


    def hover1(snd):
        if snd == 'hit_hat_close':
            cv2.rectangle(frame, (860, 550), (1200, 700), (255, 255, 255), 3)
            return

        elif snd == 'snare':
            cv2.rectangle(frame, (0, 300), (320, 450), (255, 255,255), 3)
            return

        elif snd == 'snare_rim':
            cv2.rectangle(frame, (860, 300), (1200, 450), (255, 255, 255), 3)
            return

        elif snd == 'hit_hat':
            cv2.rectangle(frame, (0, 550), (320, 700), (255, 255, 255), 3)
            return

        elif snd == 'hit_hat_open':
            cv2.rectangle(frame, (420, 550), (740, 700), (255, 255, 255), 3)
            return

        elif snd == 'tom_hi':
            cv2.rectangle(frame, (0, 0), (320, 200), (255, 255, 255), 3)
            return

        elif snd == 'tom_mid':
            cv2.rectangle(frame, (420, 0), (740, 200), (255, 255, 255), 3)
            return

        elif snd == 'tom_low':
            cv2.rectangle(frame, (860, 0), (1200, 200), (255, 255, 255), 3)


    def hover2(sond):
        if sond == 'hit_hat_close':
            cv2.rectangle(frame, (860, 550), (1200, 700), (0, 0, 0), 3)
            return

        elif sond == 'snare':
            cv2.rectangle(frame, (0, 300), (320, 450), (0, 0, 0), 3)
            return

        elif sond == 'snare_rim':
            cv2.rectangle(frame, (860, 300), (1200, 450),(0, 0, 0), 3)
            return

        elif sond == 'hit_hat':
            cv2.rectangle(frame, (0, 550), (320, 700),(0, 0, 0), 3)
            return

        elif sond == 'hit_hat_open':
            cv2.rectangle(frame, (420, 550), (740, 700),(0, 0, 0), 3)
            return

        elif sond == 'tom_hi':
            cv2.rectangle(frame, (0, 0), (320, 200),(0, 0, 0), 3)
            return

        elif sond == 'tom_mid':
            cv2.rectangle(frame, (420, 0), (740, 200),(0, 0, 0), 3)
            return

        elif sond == 'tom_low':
            cv2.rectangle(frame, (860, 0), (1200, 200),(0, 0, 0), 3)
            return

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = imutils.resize(frame, height=1200, width=1200)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lowred = np.array([131, 90, 106])
        highred = np.array([255, 255, 255])

        lowgreen = np.array([40, 40, 45])
        highgreen = np.array([70, 255, 255])

        lowblue = np.array([40, 150, 116])
        highblue = np.array([255, 255, 255])

        lowyellow = np.array([20, 100, 100])
        highyellow = np.array([30, 255, 255])

        red_mask = cv2.inRange(hsv, lowred, highred)
        blue_mask = cv2.inRange(hsv, lowblue, highblue)
        green_mask = cv2.inRange(hsv, lowgreen, highgreen)
        yellow_mask = cv2.inRange(hsv, lowyellow, highyellow)

        # image/frame, start_point, end_point, color, thickness
        cv2.rectangle(frame, (0, 0), (320, 200), (255, 0, 0), 3)
        cv2.putText(frame, 'TOM HIGH', (40, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (420, 0), (740, 200), (255, 0, 0), 3)
        cv2.putText(frame, 'TOM MID', (460, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (860, 0), (1200, 200), (255, 0, 0), 3)
        cv2.putText(frame, 'TOM LOW', (900, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)

        cv2.rectangle(frame, (0, 300), (320, 450), (255, 0, 0), 3)
        cv2.putText(frame, 'SNARE', (40, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (860, 300), (1200, 450), (255, 0, 0), 3)
        cv2.putText(frame, 'SNARE RIM', (920, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (0, 550), (320, 700), (255, 0, 0), 3)
        cv2.putText(frame, 'HIT HAT', (40, 590), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (420, 550), (740, 700), (255, 0, 0), 3)
        cv2.putText(frame, 'HIT HAT OPEN', (460, 590), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (860, 550), (1200, 700), (255, 0, 0), 3)
        cv2.putText(frame, 'HITHAT CLOSE', (900, 590), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)

        if drop1txt == 'red':
            # for the red Object
            contours, hierachy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            # startpoint, endpoint, color, thickness
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                

                if x > 860 and y > 550 and x < 1200 and y < 700:
                      # HIT HAT CLOSE
                    hover1('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break
                

                if x > 0 and y > 300 and x < 320 and y < 450:
                     # SNARE
                    hover1('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                     # SNARE RIM
                    hover1('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover1('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                     # HIT HAT OPEN
                    hover1('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break


                if x > 0 and y > 0 and x < 320 and y < 200:
                      # TOM HI
                    hover1('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break


                if x > 420 and y > 0 and x < 740 and y < 200:
                      # TOM MID
                    hover1('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                      # TOM LOW
                    hover1('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)


                    break


                break

        if drop1txt == 'blue':
            # for the blue Object
            contours, hierachy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            # startpoint, endpoint, color, thickness
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover1('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover1('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover1('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover1('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover1('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover1('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover1('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover1('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break
        if drop1txt == 'green':
            contours, hierachy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            #
            # for green object
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover1('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover1('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover1('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover1('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover1('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover1('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover1('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover1('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if drop1txt == 'yellow':
            # for yellow object
            contours, hierachy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover1('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover1('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover1('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover1('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover1('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover1('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover1('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover1('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if drop2txt == 'red':
            # for the red Object
            contours, hierachy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover2('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover2('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover2('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover2('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover2('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover2('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover2('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover2('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if drop2txt == 'blue':
            contours, hierachy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            #
            # for the blue Object
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover2('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover2('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover2('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover2('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover2('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover2('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover2('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover2('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if drop2txt == 'green':
            # for green object
            contours, hierachy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            #
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover2('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover2('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover2('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover2('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover2('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover2('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover2('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover2('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if drop2txt == 'yellow':
            # for yellow object
            contours, hierachy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover2('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover2('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover2('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover2('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover2('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover2('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover2('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover2('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        cv2.imshow("frame", frame)

        op.write(frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    op.release()
    cap.release()
    cv2.destroyAllWindows()


def wrec():
    combo1txt = combo1.get()
    combo2txt = combo2.get()
    print(combo1txt)
    print(combo2txt)
    cap = cv2.VideoCapture(0);

    def hover1(snd):
        if snd == 'hit_hat_close':
            cv2.rectangle(frame, (860, 550), (1200, 700), (255, 255, 255), 3)
            return

        elif snd == 'snare':
            cv2.rectangle(frame, (0, 300), (320, 450), (255, 255, 255), 3)
            return

        elif snd == 'snare_rim':
            cv2.rectangle(frame, (860, 300), (1200, 450), (255, 255, 255), 3)
            return

        elif snd == 'hit_hat':
            cv2.rectangle(frame, (0, 550), (320, 700), (255, 255, 255), 3)
            return

        elif snd == 'hit_hat_open':
            cv2.rectangle(frame, (420, 550), (740, 700), (255, 255, 255), 3)
            return

        elif snd == 'tom_hi':
            cv2.rectangle(frame, (0, 0), (320, 200), (255, 255, 255), 3)
            return

        elif snd == 'tom_mid':
            cv2.rectangle(frame, (420, 0), (740, 200), (255, 255, 255), 3)
            return

        elif snd == 'tom_low':
            cv2.rectangle(frame, (860, 0), (1200, 200), (255, 255, 255), 3)

    def hover2(sond):
        if sond == 'hit_hat_close':
            cv2.rectangle(frame, (860, 550), (1200, 700), (0, 0, 0), 3)
            return

        elif sond == 'snare':
            cv2.rectangle(frame, (0, 300), (320, 450), (0, 0, 0), 3)
            return

        elif sond == 'snare_rim':
            cv2.rectangle(frame, (860, 300), (1200, 450), (0, 0, 0), 3)
            return

        elif sond == 'hit_hat':
            cv2.rectangle(frame, (0, 550), (320, 700), (0, 0, 0), 3)
            return

        elif sond == 'hit_hat_open':
            cv2.rectangle(frame, (420, 550), (740, 700), (0, 0, 0), 3)
            return

        elif sond == 'tom_hi':
            cv2.rectangle(frame, (0, 0), (320, 200), (0, 0, 0), 3)
            return

        elif sond == 'tom_mid':
            cv2.rectangle(frame, (420, 0), (740, 200), (0, 0, 0), 3)
            return

        elif sond == 'tom_low':
            cv2.rectangle(frame, (860, 0), (1200, 200), (0, 0, 0), 3)
            return

    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = imutils.resize(frame, height=1200, width=1200)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lowred = np.array([131, 90, 106])
        highred = np.array([255, 255, 255])

        lowgreen = np.array([40, 40, 45])
        highgreen = np.array([70, 255, 255])

        lowblue = np.array([40, 150, 116])
        highblue = np.array([255, 255, 255])

        lowyellow = np.array([20, 100, 100])
        highyellow = np.array([30, 255, 255])

        red_mask = cv2.inRange(hsv, lowred, highred)
        blue_mask = cv2.inRange(hsv, lowblue, highblue)
        green_mask = cv2.inRange(hsv, lowgreen, highgreen)
        yellow_mask = cv2.inRange(hsv, lowyellow, highyellow)

        # image/frame, start_point, end_point, color, thickness
        cv2.rectangle(frame, (0, 0), (320, 200), (255, 0, 0), 3)
        cv2.putText(frame, 'TOM HIGH', (40, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (420, 0), (740, 200), (255, 0, 0), 3)
        cv2.putText(frame, 'TOM MID', (460, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (860, 0), (1200, 200), (255, 0, 0), 3)
        cv2.putText(frame, 'TOM LOW', (900, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)

        cv2.rectangle(frame, (0, 300), (320, 450), (255, 0, 0), 3)
        cv2.putText(frame, 'SNARE', (40, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (860, 300), (1200, 450), (255, 0, 0), 3)
        cv2.putText(frame, 'SNARE RIM', (920, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (0, 550), (320, 700), (255, 0, 0), 3)
        cv2.putText(frame, 'HIT HAT', (40, 590), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (420, 550), (740, 700), (255, 0, 0), 3)
        cv2.putText(frame, 'HIT HAT OPEN', (460, 590), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.rectangle(frame, (860, 550), (1200, 700), (255, 0, 0), 3)
        cv2.putText(frame, 'HITHAT CLOSE', (900, 590), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)

        if combo1txt == 'red':
            # for the red Object
            contours, hierachy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            # startpoint, endpoint, color, thickness
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover1('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover1('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover1('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover1('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover1('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover1('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover1('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover1('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if combo1txt == 'blue':
            # for the blue Object
            contours, hierachy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            # startpoint, endpoint, color, thickness
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover1('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover1('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover1('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover1('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover1('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover1('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover1('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover1('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break
        if combo1txt == 'green':
            contours, hierachy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            #
            # for green object
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover1('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover1('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover1('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover1('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover1('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover1('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover1('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover1('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if combo1txt == 'yellow':
            # for yellow object
            contours, hierachy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover1('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover1('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover1('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover1('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover1('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover1('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover1('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover1('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if combo2txt == 'red':
            # for the red Object
            contours, hierachy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover2('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover2('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover2('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover2('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover2('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover2('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover2('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover2('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if combo2txt == 'blue':
            contours, hierachy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            #
            # for the blue Object
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover2('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover2('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover2('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover2('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover2('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover2('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover2('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover2('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if combo2txt == 'green':
            # for green object
            contours, hierachy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
            #
            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover2('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover2('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover2('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover2('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover2('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover2('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover2('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:
                    # TOM LOW
                    hover2('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                break

        if combo2txt == 'yellow':
            # for yellow object
            contours, hierachy = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if x > 860 and y > 550 and x < 1200 and y < 700:
                    # HIT HAT CLOSE
                    hover2('hit_hat_close')
                    pygame.mixer.music.load('hihat_closed.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 0 and y > 300 and x < 320 and y < 450:
                    # SNARE
                    hover2('snare')
                    pygame.mixer.music.load('snare.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 300 and x < 1200 and y < 450:
                    # SNARE RIM
                    hover2('snare_rim')
                    pygame.mixer.music.load('bass.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 550 and x < 320 and y < 700:
                    # HIT HAT
                    hover2('hit_hat')
                    pygame.mixer.music.load('cymbal.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break
                    time.sleep(0.16)

                if x > 450 and y > 550 and x < 740 and y < 700:
                    # HIT HAT OPEN
                    hover2('hit_hat_open')
                    pygame.mixer.music.load('ride.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 0 and y > 0 and x < 320 and y < 200:
                    # TOM HI
                    hover2('tom_hi')
                    pygame.mixer.music.load('crash.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)
                    break

                if x > 420 and y > 0 and x < 740 and y < 200:
                    # TOM MID
                    hover2('tom_mid')
                    pygame.mixer.music.load('tom.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break

                if x > 860 and y > 0 and x < 1200 and y < 200:

                    # TOM LOW
                    hover2('tom_low')
                    pygame.mixer.music.load('tom_low.wav')
                    pygame.mixer.music.play()
                    time.sleep(0.16)

                    break
                break
        cv2.imshow("frame", frame)


        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


l1 = Label(frame, text='choose first drum', padx=5, pady=5, width=39, bg='white', fg='black', relief=GROOVE,
           font=('helvetica 15 bold'))
l1.place(x=5, y=130)
combo1 = ttk.Combobox(frame, width=76)
combo1['values'] = ('red', 'blue', 'green', 'yellow')
combo1.place(x=5, y=165)
combo1.current(0)

l2 = Label(frame, text='choose second drum', padx=5, pady=5, width=39, bg='white', fg='black', relief=GROOVE, font=('helvetica 15 bold'))
l2.place(x=5, y=210)
combo2 = ttk.Combobox(frame, width=76)
combo2['values'] = ('red', 'blue', 'green', 'yellow')
combo2.place(x=5, y=244)
combo2.current(0)

but1 = Button(frame, padx=5, pady=5, width=39, bg='white', fg='black', relief=GROOVE, text='Play Drums',
              font=('helvetica 15 bold'), command=wrec)
but1.place(x=5, y=296)

but2 = Button(frame, padx=5, pady=5, width=39, bg='white', fg='black', relief=GROOVE, text='Play Drums and record',
              font=('helvetica 15 bold'), command=rec)
but2.place(x=5, y=390)

root.mainloop()
