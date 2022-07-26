from psutil import sensors_battery
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw, ImageFont
from time import sleep
from config import *

chck_interval = True

def get_battery_info() -> dict:
    battery_info = sensors_battery()
    return dict(
        percentage = battery_info[0],
        is_pluged = battery_info[2]
        )

def set_status_color(battery_perc: int,is_pluged: bool) -> tuple:
    if battery_perc == 100:
        return STATUS_COLORS['full']
    if is_pluged == True:
        return STATUS_COLORS['charging']
    if battery_perc <= BATTERY_CRITICAL_LEVEL:
        return STATUS_COLORS['critical']
    return STATUS_COLORS['normal']

def create_icon(battery_perc: int,is_pluged: bool) -> Image:
    if USE_STATUS_COLORS == True:
        status_color = set_status_color(battery_perc,is_pluged)
    else:
        status_color = DEFAULT_COLOR

    image = Image.new('RGBA', ICON_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT, FONT_SIZE)
    text_off_x = (ICON_SIZE[0] - draw.textlength(str(battery_perc),font=font))/2
    text_off_y = TEXT_Y_OFFSET
    draw.text(
        (text_off_x,text_off_y),
        str(battery_perc),
        font=font,
        fill=status_color
        )
    return image

def update_icon(icon: Icon, battery_data: dict) -> None:
    icon.icon = create_icon(battery_data['percentage'],battery_data['is_pluged'])

def quit(icon) -> None:
    global chck_interval
    chck_interval = False #Turn off data checking while loop 
    icon.stop()           #Turn off tray icon
    

def main():
    battery_data = get_battery_info()
    icon = Icon('Battery Percentage')
    menu = Menu(MenuItem("Quit",quit))
    icon.menu = menu
    icon.icon = create_icon(battery_data['percentage'],battery_data['is_pluged'])
    def setup(icon):
        icon.visible = True
    icon.run_detached(setup)

    global chck_interval
    while chck_interval:
        sleep(BATTERY_CHECK_INTERVAL)
        new_battery_data = get_battery_info()
        if (new_battery_data['percentage'] != battery_data['percentage']) or (new_battery_data['is_pluged'] != battery_data['is_pluged']):
            update_icon(icon,new_battery_data)
            battery_data = new_battery_data

if __name__ == "__main__":
    main()