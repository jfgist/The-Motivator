import sys
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
import time

pygame.init()
pygame.display.set_caption("Sound Board II")
screen = pygame.display.set_mode((640, 480), 0, 32)

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LED's
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.output(9,True)
GPIO.output(10,True)
GPIO.output(17,True)
GPIO.output(27,True)


time_stamp = time.time()

bTime = 300

sound0 = pygame.mixer.Sound("nope.wav")
sound1 = pygame.mixer.Sound("worksmarter.wav")
sound2 = pygame.mixer.Sound("CastleThunder.wav")
sound3 = pygame.mixer.Sound("donottellme.wav")
sound4 = pygame.mixer.Sound("justmakeitwork.wav")
sound5 = pygame.mixer.Sound("shipit.wav")
sound6 = pygame.mixer.Sound("WilhelmScream.wav")
sound7 = pygame.mixer.Sound("applause.wav")

def PlaySound(channel):
  print "Entering PlaySound"

  global time_stamp
  time_now = time.time()

  print "Time Stamp"
#  print time_stamp
#  print "Time Now:" 
#  print time_now
#  print "Difference" 
#  print (time_now - time_stamp)
  
  if (time_now - time_stamp) >= .3:
    print channel
    if channel == 14:
      sound0.play()
    if channel == 15:
      sound1.play()
    if channel == 18:
      sound2.play()
    if channel == 23:
      sound3.play()
    if channel == 24:
      sound4.play()
    if channel == 25:
      sound5.play()
    if channel == 8:
      sound6.play()
    if channel == 7:
      sound7.play()
  time_stamp = time.time()
  
GPIO.add_event_detect(14, GPIO.RISING, callback=PlaySound, bouncetime=bTime)
GPIO.add_event_detect(15, GPIO.RISING, callback=PlaySound, bouncetime=bTime)
GPIO.add_event_detect(18, GPIO.RISING, callback=PlaySound, bouncetime=bTime)
GPIO.add_event_detect(23, GPIO.RISING, callback=PlaySound, bouncetime=bTime)
GPIO.add_event_detect(24, GPIO.RISING, callback=PlaySound, bouncetime=bTime)
GPIO.add_event_detect(25, GPIO.RISING, callback=PlaySound, bouncetime=bTime)
GPIO.add_event_detect(8, GPIO.RISING, callback=PlaySound, bouncetime=bTime)
GPIO.add_event_detect(7, GPIO.RISING, callback=PlaySound, bouncetime=bTime)


while True:

  for event in pygame.event.get():
    if event.type == KEYDOWN:
      print 'KeyDown'
      print event.key
      if event.key == K_w:
        sound0.play()
      if event.key == K_e:
        sound7.play()
      if event.key == K_c:
        quit()
