import board
import digitalio
import time
import alarm

BEEP_SHORT = 0.05
BEEP_LONG = 0.1
CYCLE_TIME = 10

buzzer = digitalio.DigitalInOut(board.D0)
buzzer.direction = digitalio.Direction.OUTPUT

button_alarm = alarm.pin.PinAlarm(pin=board.BUTTON, value=False, pull=True)

if (isinstance(alarm.wake_alarm, alarm.time.TimeAlarm)):
	# Beep
	buzzer.value = True
	time.sleep(BEEP_LONG)
	buzzer.value = False
	
	time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + CYCLE_TIME)
	alarm.exit_and_deep_sleep_until_alarms(time_alarm, button_alarm)
elif (isinstance(alarm.wake_alarm, alarm.time.PinAlarm) and alarm.sleep_memory[0] == False):
	# "ON" chirp
	buzzer.value = True
	time.sleep(BEEP_SHORT)
	buzzer.value = False
	time.sleep(BEEP_SHORT)
	buzzer.value = True
	time.sleep(BEEP_SHORT)
	buzzer.value = False
	
	alarm.sleep_memory[0] = True
	time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + CYCLE_TIME)
	alarm.exit_and_deep_sleep_until_alarms(time_alarm, button_alarm)
elif (isinstance(alarm.wake_alarm, alarm.time.PinAlarm) and alarm.sleep_memory[0] == True):
	# "OFF" chirp
	buzzer.value = True
	time.sleep(BEEP_SHORT)
	buzzer.value = False
	time.sleep(BEEP_SHORT)
	buzzer.value = True
	time.sleep(BEEP_SHORT)
	buzzer.value = False
	time.sleep(BEEP_SHORT)
	buzzer.value = True
	time.sleep(BEEP_SHORT)
	buzzer.value = False
	
	alarm.sleep_memory[0] = False
	alarm.exit_and_deep_sleep_until_alarms(button_alarm)