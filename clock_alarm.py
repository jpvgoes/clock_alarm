try:
    import pygame
    import datetime
    import time
except ImportError as error:
    print(f'\033[0;31m{error}\033[m. Try to install the modules required')
    raise SystemExit # or: exit()


def check_time_format(given_time) -> bool:
    """"
    checks if the given time format is correct

    """
    try:
        datetime.datetime.strptime(given_time, "%H:%M:%S")  # Try converting to HH:MM:SS
        return False
    except ValueError:
        return True

def alarm_clock(clock_time):

    print(f'Your alarm is set to {clock_time}')
    is_running = True

    while is_running:

        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        clock_sound = 'HINO DO FLAMENGO.mp3'
        print(current_time)

        if current_time == clock_time:
            print("WAKE UP")
            pygame.mixer.init()
            pygame.mixer.music.load(clock_sound)
            pygame.mixer.music.play()
            is_running = False
            while pygame.mixer.music.get_busy():
                time.sleep(1)

        time.sleep(1)




if __name__ == '__main__':

    ans = str(input('Choose your alarm clock(ex: 00:00:00): '))
    while check_time_format(ans):
        ans = str(input('Choose your alarm clock(ex: 00:00:00): '))

    alarm_clock(ans)

