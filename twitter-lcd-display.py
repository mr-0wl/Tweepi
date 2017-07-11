import twitter
from RPLCD import CharLCD
import time
import HTMLParser

lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12])

# Insert your API and access keys here
api=twitter.Api(consumer_key='',
	consumer_secret='',
	access_token_key='',
	access_token_secret='')

htmlParser = HTMLParser.HTMLParser()

framebuffer = [
    '',
    '',
]

def write_to_lcd(lcd, framebuffer, num_cols):
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')

from RPLCD import CharLCD

write_to_lcd(lcd, framebuffer, 16)


def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.5): #DELAY= CONTROLS THE SPEED OF SCROLL
    padding = ' ' * num_cols
    s = padding + string + padding
    for i in range(len(s) - num_cols + 1):
        framebuffer[row] = s[i:i+num_cols]
        write_to_lcd(lcd, framebuffer, num_cols)
        time.sleep(delay)

while True:
    homeTimeline=api.GetHomeTimeline(count=1)
    tweetUser = homeTimeline[0].user.screen_name
    tweetText = homeTimeline[0].text
    tweetText = htmlParser.unescape(tweetText)
    tweetText = tweetText.replace('\n',' ')
    tweetText1 = tweetUser+ ": "+tweetText
    long_string = tweetText1

	#looping 4 times to prevent excessive api calls
    loop_string(long_string, lcd, framebuffer, 1, 16)
    time.sleep(10)
	loop_string(long_string, lcd, framebuffer, 1, 16)
    time.sleep(10)
	loop_string(long_string, lcd, framebuffer, 1, 16)
    time.sleep(10)
	loop_string(long_string, lcd, framebuffer, 1, 16)
    time.sleep(10)
	loop_string(long_string, lcd, framebuffer, 1, 16)
    time.sleep(10)
