#ICON
ICON_SIZE = (256,256)
BACKGROUND_COLOR = (0,0,0,0)    #RGBA transparent

#ICON'S TEXT and FONT
FONT_SIZE = 154                 #This one fits idkw
TEXT_Y_OFFSET = 32              #Higher value -> text will render lower
FONT = 'fonts/Segoe_UI.ttf'     #Standard Win10 font
USE_STATUS_COLORS = True        #If False percentage icon text will only use DEFAULT_COLOR
                                #Otherwise it will change colors based on battery status (charging, critical level, normal, fully charged)
STATUS_COLORS = dict(
    normal = (255,255,255),
    charging = (0,128,255),
    critical = (254,32,32),
    full = (76,187,23)
)
DEFAULT_COLOR = (255,255,255)   #Color that is used when USE_STATUS_COLOR = False

#OTHER SETTINGS
BATTERY_CHECK_INTERVAL = 5  #Battery data refresh interval
BATTERY_CRITICAL_LEVEL = 20 #Standrad battery level when Win10 battery saver kicks in


