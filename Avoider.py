import pygame
import random
import os
pygame.init()
pygame.display.set_caption("Avoider")
pygame.mouse.set_visible(False)

#Extract txt info
if os.path.isfile('AvoiderData/data.txt'):
    with open('AvoiderData/data.txt', 'r') as data:
        data_list = data.readlines()
    #Window
    if int(data_list[1]) == 0 or int(data_list[3]) == 0:
        screen_info = pygame.display.Info()
        window_width = screen_info.current_w
        change_window_width = screen_info.current_w
        window_height = screen_info.current_h
        change_window_height = screen_info.current_h
        autowindow = True
        autowindow2 = True
    else:
        window_width = int(data_list[1])
        change_window_width = int(data_list[1])
        window_height = int(data_list[3])
        change_window_height = int(data_list[3])
        autowindow = False
        autowindow2 = False
    if int(data_list[5]) == 1: 
        window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
        DoFullscreen = 1
    else: 
        window = pygame.display.set_mode((window_width, window_height))
        DoFullscreen = 0
    if window_width == 1280 and window_height == 720: custom_resolution = False
    elif window_width == 1920 and window_height == 1080: custom_resolution = False
    elif autowindow: custom_resolution = False
    else: custom_resolution = True
    custom_resolution2 = custom_resolution
    #Game
    highscore = int(data_list[7])
    gamesplayed = int(data_list[9])
    #Volume
    volume_music = float(data_list[11])
    volume_sfx = float(data_list[13])
    #Intro
    if int(data_list[15]) == 1: intro = True
    else: intro = False
else:
    #Window
    screen_info = pygame.display.Info()
    window_width = screen_info.current_w
    change_window_width = 0
    window_height = screen_info.current_h
    change_window_height = 0
    window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
    DoFullscreen = 1
    autowindow = True
    autowindow2 = False
    custom_resolution = False
    custom_resolution2 = False
    #Game
    highscore = 0
    gamesplayed = 0
    #Volume
    volume_music = 1.0
    volume_sfx = 1.0
    #Intro
    intro = True

#Insert pictures
smileF = pygame.image.load('AvoiderData/smile.png')
deadPF = pygame.image.load('AvoiderData/dead.png')
verisedF = pygame.image.load('AvoiderData/verised.png')
wowF = pygame.image.load('AvoiderData/wow.png')
yongershiF = pygame.image.load('AvoiderData/yongershi.png')
cursor = pygame.image.load('AvoiderData/cursor.png')
desintresseF = pygame.image.load('AvoiderData/desintresse.png')
nothingF = pygame.image.load('AvoiderData/nothing.png')
warningF = pygame.image.load('AvoiderData/warning.png')
creditsF = pygame.image.load('AvoiderData/credits.png')
arrow1F = pygame.image.load('AvoiderData/arrow1.png')
arrow2F = pygame.image.load('AvoiderData/arrow2.png')
pygameF = pygame.image.load('AvoiderData/pygame_powered.png')
keydevF = pygame.image.load('AvoiderData/keydev.png')
aliveP = smileF
deadP = deadPF

#Insert sfx
click_sfx = pygame.mixer.Sound("AvoiderData/click.wav")
pressplay_sfx = pygame.mixer.Sound("AvoiderData/pressplay.wav")
safespotactive_sfx = pygame.mixer.Sound("AvoiderData/safespotactive.wav")
safespotpreparing_sfx = pygame.mixer.Sound("AvoiderData/safespotpreparing.wav")
death_sfx = pygame.mixer.Sound("AvoiderData/death.wav")
explosion_sfx = pygame.mixer.Sound("AvoiderData/explosion.wav")
explosionarrive_sfx = pygame.mixer.Sound("AvoiderData/explosionarrive.wav")
lasergrid_sfx = pygame.mixer.Sound("AvoiderData/lasergrid.wav")
lasershoot_sfx = pygame.mixer.Sound("AvoiderData/lasershoot.wav")
preparelaser_sfx = pygame.mixer.Sound("AvoiderData/preparelaser.wav")
back_sfx = pygame.mixer.Sound("AvoiderData/back.wav")

soundeffects = [click_sfx, pressplay_sfx, safespotactive_sfx, safespotpreparing_sfx, death_sfx, explosion_sfx, explosionarrive_sfx, lasergrid_sfx, lasershoot_sfx, preparelaser_sfx, back_sfx]

# Set colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
DRED = (100, 0, 0)
LRED = (255, 155, 155)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (100, 100, 100)

# Player variables
player_height = window_height // 15
player_width = window_height // 15

# Game variables
clock = pygame.time.Clock()
running = True
play = False
time = 0
time_b_v = 0
action_time = 300
time_action_v = 0
dead = False
dead_v = 0
game_over = False
score = 0
action = True
missile = False
menu = True
pause = False
menu_v = 1
play_v = 1
play_v2 = 1
back_press = False
chaos_mode = False

#Settings variables
settings = False
fullscreenselect = False
applyselect = False
waitconfirm = False
keepchangesselect = False
resolutionselect = True
resolution_v = 0
introselect = False

# Menu variables
selectm9 = False
selectm8 = False
selectm7 = False
selectm6 = False
selectm5 = False
selectm4 = False
selectm2 = False
selectm3 = False
menu_time = 0
credits_page = False
backselect = False
selectgo_t = False

#Character editor variables
dead_character_edit = False
alive_character_edit = False
selectCE1 = False
selectCE2 = False
selectCE3 = False
selectCE4 = False
selectCE5 = False
selectCE6 = False
selectCE7 = False

# Bomb variables
bomb_radius = window_height // 15
bomb_p_radius = bomb_radius // 1.5
bomb_speed = bomb_radius // 2
bomb = False
bomb_v = 0
boom = False

# Trail variables
mouse_x_list = []
mouse_y_list = []
trail_lenght = 7
trail_v = [0, 1, 2, 3, 4, 5, 6]

# Red edge
edge_height = window_height
edge_width = window_width
in_edge_height = edge_height - 20
in_edge_width = edge_width - 20
edge_x = 0
edge_y = 0
in_edge_x = 10
in_edge_y = 10

#Missile variables
missile_x = window_width // 2
missile_radius = player_height // 3
missile_y = 0
missile_speed = 0.025
missile_time = 0

#Laser variables
laser = False
time_laser = 0
laser_height = 0
laser_shoot = False
laser_v = False
laser_width_v = 0
laser_shoot_v = False

#Laser grid variables
laser_grid_height = window_height / 20
laser_grid_width_v = window_height / 20
laser_grid = False
time_laser_grid = 0
laser_grid_width = 0
laser_grid_active = False
laser_grid_v = False
laser_grid_height_v = 0
laser_grid_active = False

#Safe spot variables
safe_spot = False
safe_spot_time = 0
safe_spot_active = False

#Corner kill variables
corner_kill = False
corner_kill_time = 0
corner_kill_warning = False

#Volume
for sfx in soundeffects:
    pygame.mixer.Sound.set_volume(sfx, volume_sfx)
pygame.mixer.music.set_volume(volume_music)

#Game Intro
if intro:
    #Keydev
    #IN
    for x in range(0,51):
        window.fill(BLACK)
        keydevF.set_alpha(5*x)
        window.blit(keydevF, (window_width // 2 - 400, window_height // 2 - 300))
        pygame.display.update()
        clock.tick(60)
    #WAIT
    for x in range(0,48):
        pygame.display.update()
        clock.tick(60)
    #OUT
    for x in range(0,51):
        window.fill(BLACK)
        keydevF.set_alpha(255 - 5*x)
        window.blit(keydevF, (window_width // 2 - 400, window_height // 2 - 300))
        pygame.display.update()
        clock.tick(60)
    #WAIT
    for x in range(0,30):
        pygame.display.update()
        clock.tick(60)
    #Pygame
    #IN
    for x in range(0,51):
        window.fill(BLACK)
        pygameF.set_alpha(5*x)
        window.blit(pygameF, (window_width // 2 - 400, window_height // 2 - 160))
        pygame.display.update()
        clock.tick(60)
    #WAIT
    for x in range(0,48):
        pygame.display.update()
        clock.tick(60)
    #OUT
    for x in range(0,51):
        window.fill(BLACK)
        pygameF.set_alpha(255 - 5*x)
        window.blit(pygameF, (window_width // 2 - 400, window_height // 2 - 160))
        pygame.display.update()
        clock.tick(60)
    #WAIT
    for x in range(0,30):
        pygame.display.update()
        clock.tick(60)

    #Make sure esc doesn't instantly quit if you press it before the menu :)
    for event in pygame.event.get():
        pass

# Game loop
pygame.mouse.set_pos(window_width // 2, window_height // 2)
while running:
    #Get mouse pos
    mouse = pygame.mouse.get_pos()
    mouse_x = mouse[0]
    mouse_y = mouse[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if play:
                    pause = True
                    pygame.mixer.music.pause()
                    pygame.mixer.pause()
                elif game_over:
                    menu = True
                    menu_v = 1
                    game_over = False
                elif alive_character_edit:
                    alive_character_edit = False
                    menu = True
                    menu_v = 0
                elif dead_character_edit:
                    dead_character_edit = False
                    menu = True
                    menu_v = 0
                elif credits_page:
                    credits_page = False
                    menu = True
                    menu_v = 0
                elif settings:
                    settings = False
                    menu = True
                    menu_v = 1
                    autowindow = autowindow2
                else: running = False
            if event.key == pygame.K_t:
                if game_over or menu:
                    pygame.mouse.set_pos(window_width // 2, window_height // 2)
                    score = 0
                    menu = False
                    game_over = False
                    play = True
                    play_v = 1
                    time = 0
                    time_action_v = 0
                    action_time = 300
                    gamesplayed += 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backselect:
                back_press = True
            if menu:
                if selectm2:
                    pressplay_sfx.play()
                    pygame.mouse.set_pos(window_width // 2, window_height // 2)
                    score = 0
                    menu = False
                    game_over = False
                    play = True
                    play_v = 1
                    time = 0
                    time_action_v = 0
                    action_time = 300
                    gamesplayed += 1
                if selectm3: 
                    click_sfx.play()
                    settings = True
                    menu = False
                    settings_one = True
                if selectm4:
                    click_sfx.play()
                    credits_page = True
                    menu = False
                if selectm5: 
                    running = False
                if selectm6:
                    menu = False
                    alive_character_edit = True
                    click_sfx.play()
                if selectm7:
                    menu = False
                    dead_character_edit = True
                    click_sfx.play()
                if selectm8: chaos_mode = False
                if selectm9: chaos_mode = True
            if alive_character_edit:
                if selectCE1: 
                    click_sfx.play()
                    aliveP = nothingF
                if selectCE2: 
                    click_sfx.play()
                    aliveP = deadPF
                if selectCE3: 
                    click_sfx.play()
                    aliveP = verisedF
                if selectCE4: 
                    click_sfx.play()
                    aliveP = yongershiF
                if selectCE5: 
                    click_sfx.play()
                    aliveP = wowF
                if selectCE6:
                    click_sfx.play()
                    aliveP = desintresseF
                if selectCE7:
                    click_sfx.play()
                    aliveP = smileF
            if dead_character_edit:
                if selectCE1: 
                    click_sfx.play()
                    deadP = nothingF
                if selectCE2: 
                    click_sfx.play()
                    deadP = deadPF
                if selectCE3: 
                    click_sfx.play()
                    deadP = verisedF
                if selectCE4: 
                    click_sfx.play()
                    deadP = yongershiF
                if selectCE5: 
                    click_sfx.play()
                    deadP = wowF
                if selectCE6:
                    click_sfx.play()
                    deadP = desintresseF
                if selectCE7:
                    click_sfx.play()
                    deadP = smileF
            if selectgo_t and game_over:
                pygame.mouse.set_pos(window_width // 2, window_height // 2)
                score = 0
                menu = False
                game_over = False
                play = True
                play_v = 1
                time = 0
                time_action_v = 0
                action_time = 300
                gamesplayed += 1
            if settings:
                if fullscreenselect and not waitconfirm:
                    if change_fullscreen == 0: change_fullscreen = 1
                    else: change_fullscreen = 0
                if applyselect and not waitconfirm:
                    waitconfirm = True
                    wait_time = 0
                    DoFullscreen = change_fullscreen
                    window_width = change_window_width
                    window_height = change_window_height
                    autowindow2 = autowindow
                    if DoFullscreen == 1: 
                        window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
                    else: 
                        window = pygame.display.set_mode((window_width, window_height))
                    player_height = window_height // 15
                    player_width = window_height // 15
                    bomb_radius = window_height // 15
                    bomb_p_radius = bomb_radius // 1.5
                    bomb_speed = bomb_radius // 2
                    edge_height = window_height
                    edge_width = window_width
                    in_edge_height = edge_height - 20
                    in_edge_width = edge_width - 20
                    missile_x = window_width // 2
                    missile_radius = player_height // 3
                    laser_grid_height = window_height / 20
                    laser_grid_width_v = window_height / 20
                if keepchangesselect:
                    waitconfirm = False
                    current_window_width = window_width
                    current_window_height = window_height
                    current_fullscreen_status = DoFullscreen
                    keepchangesselect = False
                if resolutionselect and not waitconfirm:
                    custom_resolution2 = False
                    if resolution_v == 1:
                        resolution_v = 0
                        change_window_width = 1280
                        change_window_height = 720
                        autowindow = False
                    elif resolution_v == 2:
                        resolution_v = 1
                        screen_info = pygame.display.Info()
                        change_window_width = screen_info.current_w
                        change_window_height = screen_info.current_h
                        autowindow = True
                    elif resolution_v == 3:
                        resolution_v = 2
                        change_window_width = 1920
                        change_window_height = 1080
                        autowindow = False
                    if resolution_v == 0: resolution_v = 3
                if introselect:
                    if intro: intro = False
                    else: intro = True
        else: back_press = False
    if back_press:
        back_sfx.play()
        if alive_character_edit:
            alive_character_edit = False
            menu = True
            menu_v = 0
        if dead_character_edit:
            dead_character_edit = False
            menu = True
            menu_v = 0
        if credits_page:
            credits_page = False
            menu = True
            menu_v = 0
        if game_over:
            menu = True
            menu_v = 1
            game_over = False
        if settings:
            menu = True
            settings = False
            menu_v = 1
            waitconfirm = False
            autowindow = autowindow2
        back_press = False
        backselect = False

    if menu:
        #menu time
        if menu_time >= 20: menu_time = 0
        else: menu_time += 1
        wait_confirm = False

        if menu_v == 1:
            #Reset actions
            #Bomb
            time_action_v = 0
            action_time = random.randint(60, 300)
            bomb = False
            boom = False
            #Missile
            missile_time = 600
            action = True
            dead = False
            play = False
            #Laser
            laser = False
            time_laser = 0
            laser_shoot = False
            laser_v = False
            laser_shoot_v = False
            #Laser grid
            laser_grid = False
            time_laser_grid = 0
            laser_grid_active = False
            laser_grid_v = False
            laser_grid_active_v = False
            #Safe spot
            safe_spot_active = False
            safe_spot = False
            #Corner kill
            in_edge_height = edge_height - 20
            in_edge_width = edge_width - 20
            in_edge_x = 10
            in_edge_y = 10
            corner_kill = False
            corner_kill_time = 0

            #Random player pos
            player_x = window_width // 6 - player_width / 2
            player_y = window_height // 3 - player_height / 2
            player_x2 = window_width // 6 * 5 - player_width / 2

            #Preset text
            m1font = pygame.font.Font(None, int(window_height / 4))
            m2font = pygame.font.Font(None, int(window_height / 8))
            m3font = pygame.font.Font(None, int(window_height / 12))
            m4font = pygame.font.Font(None, int(window_height // 15))
            mtext = m1font.render("AVOIDER", True, WHITE)
            m2text = m2font.render("Play", True, WHITE)
            m3text = m2font.render("Settings", True, WHITE)
            m4text = m2font.render("Credits", True, WHITE)
            m5text = m2font.render("Quit", True, WHITE)
            m6text = m3font.render("Highscore: " + str(highscore), True, WHITE)
            m7text = m3font.render("Games played: " + str(gamesplayed), True, WHITE)
            m8text = m4font.render("NORMAL", True, WHITE)
            m9text = m4font.render("CHAOS", True, WHITE)
            m10text = m4font.render("-", True, WHITE)
            mtext_rec = mtext.get_rect(center=(window_width // 2, window_height // 8))
            m2text_rec = m2text.get_rect(center=(window_width // 2, window_height // 8 + mtext.get_height()))
            m3text_rec = m3text.get_rect(center=(window_width // 2, window_height // 8 + mtext.get_height() + 1.5 * m2text.get_height()))
            m4text_rec = m4text.get_rect(center=(window_width // 2, window_height // 8 + mtext.get_height() + 3 * m2text.get_height()))
            m5text_rec = m5text.get_rect(center=(window_width // 2, window_height // 8 + mtext.get_height() + 4.5 * m2text.get_height()))
            m6text_rec = m6text.get_rect(center=(window_width // 6 * 5, window_height // 3*2))
            m7text_rec = m7text.get_rect(center=(window_width // 6, window_height // 3*2))
            m8text_rec = m8text.get_rect(center=(window_width // 2 - 2 * m10text.get_width() - m8text.get_width() // 2, window_height // 20 * 19))
            m9text_rec = m9text.get_rect(center=(window_width // 2 + 2 * m10text.get_width() + m9text.get_width() // 2, window_height // 20 * 19))
            m10text_rec = m10text.get_rect(center=(window_width // 2, window_height // 20 * 19))

            #Load music
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("AvoiderData/BeautyFlow.mp3")
            pygame.mixer.music.play(-1, 0.0, 2000)
            play_v = 1

            menu_v = 0

        #Update window
        window.fill(BLACK)

        if not selectm6 or menu_time > 10:
            pygame.draw.rect(window, WHITE, (player_x, player_y, player_width, player_height))
        window.blit(aliveP, (player_x + player_width / 2 - 20, player_y + player_height / 2 - 20))
        if not selectm7 or menu_time > 10:
            pygame.draw.rect(window, RED, (player_x2, player_y, player_width, player_height))
        window.blit(deadP, (player_x2 + player_width / 2 - 20, player_y + player_height / 2 - 20))
        m1font = pygame.font.Font(None, int(window_height / 4))
        m2font = pygame.font.Font(None, int(window_height // 6))
        m3font = pygame.font.Font(None, int(window_height / 12))

        if  window_height // 8 + mtext.get_height() - m2text.get_height() // 2 <= mouse_y <= window_height // 8 + mtext.get_height() + m2text.get_height() // 2 and window_width // 2 - m2text.get_width() // 2 <= mouse_x <= window_width // 2 + m2text.get_width() // 2:
            m2text = m2font.render("Play", True, GREEN)
            selectm2 = True
        else: 
            m2text = m2font.render("Play", True, WHITE)
            selectm2 = False
        if  window_height // 8 + mtext.get_height() + 1.5 * m2text.get_height() - m2text.get_height() // 2 <= mouse_y <= window_height // 8 + mtext.get_height() + 1.5 * m2text.get_height() + m2text.get_height() // 2 and window_width // 2 - m3text.get_width() // 2 <= mouse_x <= window_width // 2 + m3text.get_width() // 2:
            m3text = m2font.render("Settings", True, BLUE)
            selectm3 = True
        else: 
            m3text = m2font.render("Settings", True, WHITE)
            selectm3 = False
        if  window_height // 8 + mtext.get_height() + 3 * m2text.get_height() - m2text.get_height() // 2 <= mouse_y <= window_height // 8 + mtext.get_height() + 3 * m2text.get_height() + m2text.get_height() // 2 and window_width // 2 - m4text.get_width() // 2 <= mouse_x <= window_width // 2 + m4text.get_width() // 2:
            m4text = m2font.render("Credits", True, BLUE)
            selectm4 = True
        else: 
            m4text = m2font.render("Credits", True, WHITE)
            selectm4 = False
        if  window_height // 8 + mtext.get_height() + 4.5 * m2text.get_height() - m2text.get_height() // 2 <= mouse_y <= window_height // 8 + mtext.get_height() + 4.5 * m2text.get_height() + m2text.get_height() // 2 and window_width // 2 - m5text.get_width() // 2 <= mouse_x <= window_width // 2 + m5text.get_width() // 2:
            m5text = m2font.render("Quit", True, RED)
            selectm5 = True
        else: 
            m5text = m2font.render("Quit", True, WHITE)
            selectm5 = False
        if player_x <= mouse_x <= player_x + player_width and player_y <= mouse_y <= player_y + player_height: selectm6 = True
        else: selectm6 = False
        if player_x2 <= mouse_x <= player_x2 + player_width and player_y <= mouse_y <= player_y + player_height: selectm7 = True
        else: selectm7 = False
        if m8text_rec[0] <= mouse_x <= m8text_rec[0] + m8text.get_width() and m8text_rec[1] <= mouse_y <= m8text_rec[1] + m8text.get_height(): 
            selectm8 = True
            pygame.draw.rect(window, GREY, (m8text_rec[0], m8text_rec[1], m8text.get_width(), m8text.get_height()))
        else: selectm8 = False
        if m9text_rec[0] <= mouse_x <= m9text_rec[0] + m9text.get_width() and m9text_rec[1] <= mouse_y <= m9text_rec[1] + m9text.get_height(): 
            selectm9 = True
            pygame.draw.rect(window, GREY, (m9text_rec[0], m9text_rec[1], m9text.get_width(), m9text.get_height()))
        else: selectm9 = False

        #Mode select
        if chaos_mode:
            m8text = m4font.render("NORMAL", True, WHITE)
            m9text = m4font.render("CHAOS", True, BLACK)
            pygame.draw.rect(window, WHITE, (m9text_rec[0], m9text_rec[1], m9text.get_width(), m9text.get_height()))
        else:
            pygame.draw.rect(window, WHITE, (m8text_rec[0], m8text_rec[1], m8text.get_width(), m8text.get_height()))
            m9text = m4font.render("CHAOS", True, WHITE)
            m8text = m4font.render("NORMAL", True, BLACK)
        
        m10text = m4font.render("-", True, WHITE)
        mtext_rec = mtext.get_rect(center=(window_width // 2, window_height // 8))
        m2text_rec = m2text.get_rect(center=(window_width // 2, window_height // 8 + mtext.get_height()))
        m3text_rec = m3text.get_rect(center=(window_width // 2, window_height // 8 + mtext.get_height() + 1.5 * m2text.get_height()))
        m4text_rec = m4text.get_rect(center=(window_width // 2, window_height // 8 + mtext.get_height() + 3 * m2text.get_height()))
        m5text_rec = m5text.get_rect(center=(window_width // 2, window_height // 8 + mtext.get_height() + 4.5 * m2text.get_height()))
        m8text_rec = m8text.get_rect(center=(window_width // 2 - 2 * m10text.get_width() - m8text.get_width() // 2, window_height // 20 * 19))
        m9text_rec = m9text.get_rect(center=(window_width // 2 + 2 * m10text.get_width() + m9text.get_width() // 2, window_height // 20 * 19))
        m10text_rec = m10text.get_rect(center=(window_width // 2, window_height // 20 * 19))
        window.blit(mtext, mtext_rec)
        window.blit(m2text, m2text_rec)
        window.blit(m3text, m3text_rec)
        window.blit(m4text, m4text_rec)
        window.blit(m5text, m5text_rec)
        window.blit(m6text, m6text_rec)
        window.blit(m7text, m7text_rec)
        window.blit(m10text, m10text_rec)
        window.blit(m8text, m8text_rec)
        window.blit(m9text, m9text_rec)
        window.blit(cursor, (mouse_x, mouse_y))

    elif play:
        if play_v == 1:
            mouse = pygame.mouse.get_pos()
            mouse_x = mouse[0]
            mouse_y = mouse[1]
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("AvoiderData/Rhinoceros.mp3")
            pygame.mixer.music.play(-1, 0.0, 4000)   
            play_v = 0
            in_edge_height = edge_height - 20
            in_edge_width = edge_width - 20
            in_edge_x = 10
            in_edge_y = 10
        
        #Pause
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = True
                        pause = False
                        play = False
                        menu_v = 1
                    if event.key == pygame.K_r:
                        pause = False
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
            pfont = pygame.font.Font(None, int(window_height / 10))
            p2font = pygame.font.Font(None, int(window_height / 20))
            ptext = pfont.render("PAUSE", True, WHITE)
            p2text = p2font.render("[R] Continue game", True, WHITE)
            p3text = p2font.render("[Esc] Back to menu", True, WHITE)
            ptext_rec = ptext.get_rect(center=(window_width // 2, window_height // 2))
            p2text_rec = p2text.get_rect(center=(window_width // 2, window_height - 2 * p2text.get_height()))
            p3text_rec = p3text.get_rect(center=(window_width // 2, window_height - p2text.get_height()))
            window.blit(ptext, ptext_rec)
            window.blit(p2text, p2text_rec)
            window.blit(p3text, p3text_rec)
            pygame.mouse.set_pos(mouse_x, mouse_y)
            pygame.display.update()
            clock.tick(20)

        # Update action time
        if time_action_v < action_time and not dead:
            time_action_v += 1 + score / 20

        #Update action
        if time_action_v >= action_time or chaos_mode:
            time_action_v = 0
            if action:
                action_v_r = random.randint(1,11)
                if action_v_r == 1:
                    time_b_v = 0
                    bomb_v = 0
                    bomb = True
                    action = False
                if action_v_r == 2:
                    if not missile:
                        missile = True
                        missile_time = 0
                if action_v_r == 3:
                    time_laser = 0
                    laser_height = 0
                    laser = True
                    action = False
                    laser_shoot = False
                if action_v_r == 4:
                    time_laser = 0
                    laser_width_v = 0
                    laser_v = True
                    action = False
                    laser_shoot_v = False
                if action_v_r == 5:
                    time_laser = 0
                    laser_width_v = 0
                    laser_v = True
                    action = False
                    laser_shoot_v = False
                    laser_height = 0
                    laser = True
                    laser_shoot = False   
                if action_v_r == 6:
                    laser_grid = True
                    time_laser_grid = 0
                    laser_grid_width = 0
                    laser_grid_active = False
                    action = False
                if action_v_r == 7:
                    laser_grid_v = True
                    time_laser_grid = 0
                    laser_grid_height_v = 0
                    laser_grid_active_v = False
                    action = False
                if action_v_r == 8:
                    missile_time = 600
                    laser_grid = True
                    laser_grid_width = 0
                    laser_grid_active = False
                    laser_grid_v = True
                    time_laser_grid = 0
                    laser_grid_height_v = 0
                    laser_grid_active_v = False
                    action = False
                if action_v_r == 9:
                    #Chaos :)  
                    missile_time = 600                  
                    time_laser = 0
                    laser_width_v = 0
                    laser_v = True
                    laser_shoot_v = False
                    laser_height = 0
                    laser = True
                    laser_shoot = False
                    laser_grid = True
                    laser_grid_width = 0
                    laser_grid_active = False
                    laser_grid_v = True
                    time_laser_grid = 0
                    laser_grid_height_v = 0
                    laser_grid_active_v = False
                    action = False
                if action_v_r == 10:
                    missile_time = 600
                    safe_spot = True
                    safe_spot_time = 0
                    safe_spot_active = False
                    action = False
                    safe_spot_x = random.randint(player_width, window_width - 3*player_width)
                    safe_spot_y = random.randint(player_height, window_height - 3*player_height)
                if action_v_r == 11:
                    corner_kill = True
                    corner_kill_time = 0
                    action = False

        #Bomb time
        time_b_v += 1
        if time_b_v >= 60:
            time_b_v = 0
        
        # Trail
        if True:
            mouse_x_list.append(mouse_x - player_width // 2)
            mouse_y_list.append(mouse_y - player_height // 2)
        if len(mouse_x_list) > trail_lenght:
            mouse_x_list.pop(0)
            mouse_y_list.pop(0)

        # Player pos
        if not dead:
            player_x = mouse_x - player_width // 2
            player_y = mouse_y - player_height // 2

        #Check if dead:
        #Wall
        if player_y <= in_edge_y or player_y + player_height >= edge_height - in_edge_y or player_x <= in_edge_x or player_x + player_width >= edge_width - in_edge_x:
            dead = True
        #Bomb
        if boom:
            if bomb_p2_y - bomb_p_radius - player_width <= player_y <= bomb_p2_y + bomb_p_radius and bomb_x - bomb_p_radius - player_width <= player_x <= bomb_x + bomb_p_radius:
                dead = True
            elif bomb_p2_y - bomb_p_radius - player_width <= player_y <= bomb_p2_y + bomb_p_radius and bomb_p_x - bomb_p_radius - player_width <= player_x <= bomb_p_x + bomb_p_radius:
                dead = True
            elif bomb_y - bomb_p_radius - player_width <= player_y <= bomb_y + bomb_p_radius and bomb_p_x - bomb_p_radius - player_width <= player_x <= bomb_p_x + bomb_p_radius:
                dead = True
            elif bomb_p_y - bomb_p_radius - player_width <= player_y <= bomb_p_y + bomb_p_radius and bomb_p_x - bomb_p_radius - player_width <= player_x <= bomb_p_x + bomb_p_radius:
                dead = True
            elif bomb_p_y - bomb_p_radius - player_width <= player_y <= bomb_p_y + bomb_p_radius and bomb_x - bomb_p_radius - player_width <= player_x <= bomb_x + bomb_p_radius:
                dead = True
            elif bomb_p_y - bomb_p_radius - player_width <= player_y <= bomb_p_y + bomb_p_radius and bomb_p2_x - bomb_p_radius - player_width <= player_x <= bomb_p2_x + bomb_p_radius:
                dead = True
            elif bomb_y - bomb_p_radius - player_width <= player_y <= bomb_y + bomb_p_radius and bomb_p2_x - bomb_p_radius - player_width <= player_x <= bomb_p2_x + bomb_p_radius:
                dead = True
            elif bomb_p2_y - bomb_p_radius - player_width <= player_y <= bomb_p2_y + bomb_p_radius and bomb_p2_x - bomb_p_radius - player_width <= player_x <= bomb_p2_x + bomb_p_radius:
                dead = True
        #Missile
        if missile:
            if missile_y - missile_radius - player_width <= player_y <= missile_y + missile_radius and missile_x - missile_radius - player_width <= player_x <= missile_x + missile_radius:
                dead = True
                missile_time = 600
                explosion_sfx.play()
        #Laser
        if laser_shoot:
            if laser_y + laser_height + player_height / 2 >= mouse_y >= laser_y - player_height / 2:
                dead = True
        if laser_shoot_v:
            if laser_x + laser_width_v + player_width / 2 >= mouse_x >= laser_x - player_height / 2:
                dead = True
        #Laser grid
        if laser_grid_active:
            if laser_grid_y1 + laser_grid_height + player_height / 2 >= mouse_y >= laser_grid_y1 - player_height / 2:
                dead = True
            if laser_grid_y2 + laser_grid_height + player_height / 2 >= mouse_y >= laser_grid_y2 - player_height / 2:
                dead = True
            if laser_grid_y3 + laser_grid_height + player_height / 2 >= mouse_y >= laser_grid_y3 - player_height / 2:
                dead = True
        if laser_grid_active_v:
            if laser_grid_x1 + laser_grid_width_v + player_width / 2 >= mouse_x >= laser_grid_x1 - player_width / 2:
                dead = True
            if laser_grid_x2 + laser_grid_width_v + player_width / 2 >= mouse_x >= laser_grid_x2 - player_width / 2:
                dead = True
            if laser_grid_x3 + laser_grid_width_v + player_width / 2 >= mouse_x >= laser_grid_x3 - player_width / 2:
                dead = True
        #Safe spot
        if safe_spot_active:
            if not (safe_spot_x <= player_x <= safe_spot_x + player_width and safe_spot_y <= player_y <= safe_spot_y + player_height):
                dead = True

        # Update score
        if time >= 60 and not dead:
            score += 1
            time = 0
        else:
            time += 1

        # Bomb
        if not bomb:
            bomb_x = random.randint(0, window_width)
            bomb_y = random.randint(0, window_height)
            bomb_p_y = bomb_y 
            bomb_p2_y = bomb_y
            bomb_p_x = bomb_x 
            bomb_p2_x = bomb_x

        # Update screen
        window.fill(BLACK)

        #Edge
        pygame.draw.rect(window, RED, (edge_x, edge_y, edge_width, edge_height))
        pygame.draw.rect(window, BLACK, (in_edge_x, in_edge_y, in_edge_width, in_edge_height))

        #Safe spot
        if safe_spot:
            safe_spot_time += 1
            if safe_spot_time > 120:
                safe_spot_active = False
                safe_spot = False
                action = True
                action_time = random.randint(60, 300)
            elif safe_spot_time > 60:
                if safe_spot_time == 61: safespotactive_sfx.play()
                safe_spot_active = True
                window.fill(RED)
                pygame.draw.rect(window, BLACK, (safe_spot_x, safe_spot_y, 2*player_width, 2*player_height))
            else:
                if safe_spot_time == 1: safespotpreparing_sfx.play()
                pygame.draw.rect(window, LRED, (in_edge_x, in_edge_y, in_edge_width, in_edge_height))
                pygame.draw.rect(window, BLACK, (safe_spot_x, safe_spot_y, 2*player_width, 2*player_height))

        #Trail
        if len(mouse_x_list) == trail_lenght and not dead:
            for v in trail_v:
               pygame.draw.rect(window, (5 + v * 25, 5 + v * 25, 5 + v * 25), (mouse_x_list[v], mouse_y_list[v], player_width, player_height))

        if dead:
            dead_v += 0.5
            if dead_v == 0.5:
                pygame.mixer.music.stop() 
                death_sfx.play()
                play_v = 0
                if score > highscore: highscore = score
        if dead and dead_v > 60:
            dead_v2 = dead_v - 60 + 1
            pygame.draw.rect(window, DRED, (player_x, player_y, player_width // dead_v2, player_height // dead_v2))
            if dead_v > 90:
                #Reset actions
                #Bomb
                time_action_v = 0
                action_time = random.randint(60, 300)
                bomb = False
                boom = False
                #Missile
                missile_time = 600
                action = True
                dead = False
                play = False
                #Laser
                laser = False
                time_laser = 0
                laser_shoot = False
                laser_v = False
                laser_shoot_v = False
                #Laser grid
                laser_grid = False
                time_laser_grid = 0
                laser_grid_active = False
                laser_grid_v = False
                laser_grid_active_v = False
                #Safe spot
                safe_spot_active = False
                safe_spot = False
                #Corner kill
                in_edge_height = edge_height - 20
                in_edge_width = edge_width - 20
                in_edge_x = 10
                in_edge_y = 10
                corner_kill = False
                corner_kill_time = 0

                game_over = True
        elif dead:
            pygame.draw.rect(window, RED, (player_x, player_y, player_width, player_height))
            window.blit(deadP, (player_x + player_width / 2 - 20, player_y + player_height / 2 - 20))
        elif not dead:
            dead_v = 0
            pygame.draw.rect(window, WHITE, (player_x, player_y, player_width, player_height))
            window.blit(aliveP, (mouse_x - 20, mouse_y - 20))

        if bomb:
            if time_b_v == 30:
                bomb_v += 1
            if bomb_v >=1:
                if bomb_v >= 3:
                    time_action_v = 0
                    action_time = random.randint(60, 300)
                    bomb = False
                    boom = False
                    action = True
                else:
                    boom = True
                if bomb_v == 1: 
                    pygame.draw.circle(window, RED, (bomb_x, bomb_y), bomb_radius)
                bomb_p_x += bomb_speed
                bomb_p_y += bomb_speed
                bomb_p2_x -= bomb_speed
                bomb_p2_y -= bomb_speed

                pygame.draw.circle(window, RED, (bomb_x, bomb_p2_y), bomb_p_radius)
                pygame.draw.circle(window, RED, (bomb_p_x, bomb_p2_y), bomb_p_radius)
                pygame.draw.circle(window, RED, (bomb_p_x, bomb_y), bomb_p_radius)
                pygame.draw.circle(window, RED, (bomb_p_x, bomb_p_y), bomb_p_radius)
                pygame.draw.circle(window, RED, (bomb_x, bomb_p_y), bomb_p_radius)
                pygame.draw.circle(window, RED, (bomb_p2_x, bomb_p_y), bomb_p_radius)
                pygame.draw.circle(window, RED, (bomb_p2_x, bomb_y), bomb_p_radius)
                pygame.draw.circle(window, RED, (bomb_p2_x, bomb_p2_y), bomb_p_radius)
            else:
                if time_b_v == 1: explosionarrive_sfx.play()
                if time_b_v == 29: explosion_sfx.play()
                pygame.draw.circle(window, LRED, (bomb_x, bomb_y), bomb_radius)

        #Laser
        if laser:
            time_laser += 1
            if time_laser > 210:
                laser_shoot = False
                time_action_v = 0
                action = True
                action_time = random.randint(60, 300)
                laser = False
            elif time_laser > 150:
                if time_laser == 151: lasershoot_sfx.play()
                pygame.draw.rect(window, RED, (0, laser_y, window_width, laser_height))
                laser_shoot = True
            elif time_laser > 120:
                LLRED = (255, 75, 75)
                pygame.draw.rect(window, LLRED, (0, laser_y, window_width, laser_height))
            else:
                if time_laser == 1: preparelaser_sfx.play()
                laser_height = window_height/1200*time_laser
                laser_y = mouse_y - 0.5*laser_height
                pygame.draw.rect(window, LRED, (0, laser_y, window_width, laser_height))
        if laser_v:
            if not laser: time_laser += 1
            if time_laser > 210:
                laser_shoot_v = False
                time_action_v = 0
                action = True
                action_time = random.randint(60, 300)
                laser_v = False
            elif time_laser > 150:
                if time_laser == 151 and not laser: lasershoot_sfx.play()
                pygame.draw.rect(window, RED, (laser_x, 0, laser_width_v, window_height))
                laser_shoot_v = True
            elif time_laser > 120:
                LLRED = (255, 75, 75)
                pygame.draw.rect(window, LLRED, (laser_x, 0, laser_width_v, window_height))
            else:
                if time_laser == 1 and not laser: preparelaser_sfx.play()
                laser_width_v = window_height/1200*time_laser
                laser_x = mouse_x - 0.5*laser_width_v
                pygame.draw.rect(window, LRED, (laser_x, 0, laser_width_v, window_height))

        #Laser grid
        if laser_grid:
            time_laser_grid += 1
            if time_laser_grid > 90:
                action_time = random.randint(60, 300)
                time_action_v = 0
                laser_grid = False
                if not laser_grid_v: time_laser_grid = 0
                laser_grid_active = False
                if not laser: action = True
            elif time_laser_grid > 30:
                pygame.draw.rect(window, RED, (0, laser_grid_y1, laser_grid_width, laser_grid_height))
                pygame.draw.rect(window, RED, (0, laser_grid_y2, laser_grid_width, laser_grid_height))
                pygame.draw.rect(window, RED, (0, laser_grid_y3, laser_grid_width, laser_grid_height))
                laser_grid_active = True
            else:
                if time_laser_grid == 1: lasergrid_sfx.play()
                laser_grid_width = window_width / 30 * time_laser_grid
                laser_grid_y1 = window_height / 2 - 0.5 * laser_grid_height
                laser_grid_y2 = window_height / 4 - 0.5 * laser_grid_height
                laser_grid_y3 = window_height / 4 * 3 - 0.5 * laser_grid_height
                pygame.draw.rect(window, LRED, (window_width - laser_grid_width, laser_grid_y1, laser_grid_width, laser_grid_height))
                pygame.draw.rect(window, LRED, (0, laser_grid_y2, laser_grid_width, laser_grid_height))
                pygame.draw.rect(window, LRED, (0, laser_grid_y3, laser_grid_width, laser_grid_height))
        if laser_grid_v:
            if not laser_grid: 
                time_laser_grid += 1
            if time_laser_grid > 90:
                action_time = random.randint(60, 300)
                time_action_v = 0
                laser_grid_v = False
                time_laser_grid = 0
                laser_grid_active_v = False
                if not laser: action = True
            elif time_laser_grid > 30:
                pygame.draw.rect(window, RED, (laser_grid_x1, window_height - laser_grid_height_v, laser_grid_width_v, laser_grid_height_v))
                pygame.draw.rect(window, RED, (laser_grid_x2, 0, laser_grid_width_v, laser_grid_height_v))
                pygame.draw.rect(window, RED, (laser_grid_x3, 0, laser_grid_width_v, laser_grid_height_v))
                laser_grid_active_v = True
            else:
                if time_laser_grid == 1 and not laser_grid: lasergrid_sfx.play()
                laser_grid_height_v = window_height / 30 * time_laser_grid
                laser_grid_x1 = window_width / 2 - 0.5 * laser_grid_width_v
                laser_grid_x2 = window_width / 4 - 0.5 * laser_grid_width_v
                laser_grid_x3 = window_width / 4 * 3 - 0.5 * laser_grid_width_v
                pygame.draw.rect(window, LRED, (laser_grid_x1, window_height - laser_grid_height_v, laser_grid_width_v, laser_grid_height_v))
                pygame.draw.rect(window, LRED, (laser_grid_x2, 0, laser_grid_width_v, laser_grid_height_v))
                pygame.draw.rect(window, LRED, (laser_grid_x3, 0, laser_grid_width_v, laser_grid_height_v))

        #Homing missile
        if missile and missile_time < 600:
            missile_time += 1
            if missile_time == 1: explosion_sfx.play()
            missile_d_x = mouse_x - missile_x
            missile_d_y = mouse_y - missile_y
            missile_x += missile_d_x * missile_speed
            missile_y += missile_d_y * missile_speed
            pygame.draw.circle(window, RED, (missile_x, missile_y), missile_radius)
        elif missile:
            missile_time = 0
            missile_x = window_width // 2
            missile_y = 0
            missile = False

        #Corner kill
        if corner_kill: 
            corner_kill_time += 1
            if corner_kill_time > 120:
                in_edge_height = edge_height - 20
                in_edge_width = edge_width - 20
                in_edge_x = 10
                in_edge_y = 10
                corner_kill = False
                corner_kill_time = 0
                action = True
                action_time = random.randint(60, 300)
            elif corner_kill_time > 30:
                if corner_kill_time == 31: lasershoot_sfx.play()
                in_edge_height = edge_height - (edge_height // 3)
                in_edge_width = edge_width - (edge_height // 3)
                in_edge_x = edge_height // 6
                in_edge_y = edge_height // 6
            else:
                if corner_kill_time == 1: explosionarrive_sfx.play()
                window.blit(warningF, (window_width // 2 - 50, window_height // 2 - 50))

        font = pygame.font.Font(None, int(window_height / 600 * 25))
        text = font.render("Score: " + str(score), True, RED)
        text_rec = text.get_rect(center=(window_width // 2, window_height / 600 * 25))
        window.blit(text, text_rec)

    if game_over:
        window.fill(DRED)
        if mouse_x < 80 and mouse_y < 40:
            window.blit(arrow2F, (0,0))
            backselect = True
        else: 
            window.blit(arrow1F, (0,0))
            backselect = False
        font = pygame.font.Font(None, int(window_height / 4))
        font2 = pygame.font.Font(None, int(window_height / 10))
        font3 = pygame.font.Font(None, int(window_height / 6))
        text = font.render("Game Over", True, RED)
        text2 = font2.render("Try Again", True, BLACK)
        text3 = font3.render("Score: " + str(score), True, BLUE)
        text_rec = text.get_rect(center=(window_width // 2, window_height // 2 - text.get_height()))
        text_rec2 = text2.get_rect(center=(window_width // 2, window_height // 2 + text3.get_height()))
        text_rec3 = text3.get_rect(center=(window_width // 2, window_height // 2))

        if text_rec2[0] <= mouse_x <= text_rec2[0] + text2.get_width() and text_rec2[1] <= mouse_y <= text_rec2[1] + text2.get_height():
            text2 = font2.render("Try Again", True, WHITE)
            selectgo_t = True
        else: selectgo_t = False

        window.blit(text, text_rec)
        window.blit(text2, text_rec2)
        window.blit(text3, text_rec3)
        window.blit(cursor, (mouse_x, mouse_y))

    if alive_character_edit:
        window.fill(BLACK)
        if mouse_x < 80 and mouse_y < 40:
            window.blit(arrow2F, (0,0))
            backselect = True
        else: 
            window.blit(arrow1F, (0,0))
            backselect = False
        pygame.draw.rect(window, WHITE, (window_width // 2 - player_width // 2, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, WHITE, (window_width // 2 - player_width // 2 + 2 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, WHITE, (window_width // 2 - player_width // 2 - 2 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, WHITE, (window_width // 2 - player_width // 2 + 4 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, WHITE, (window_width // 2 - player_width // 2 - 4 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, WHITE, (window_width // 2 - player_width // 2 + 6 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, WHITE, (window_width // 2 - player_width // 2 - 6 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        window.blit(nothingF, (window_width // 2 - 20, window_height // 3 * 2 - 20))
        window.blit(deadPF, (window_width // 2 + 2 * player_width - 20, window_height // 3 * 2 - 20))
        window.blit(verisedF, (window_width // 2 - 2 * player_width - 20, window_height // 3 * 2 - 20))
        window.blit(yongershiF, (window_width // 2 + 4 * player_width - 20, window_height // 3 * 2 - 20))
        window.blit(wowF, (window_width // 2 - 4 * player_width - 20, window_height // 3 * 2 - 20))
        window.blit(desintresseF, (window_width // 2 + 6 * player_width - 20, window_height // 3 * 2 - 20))
        window.blit(smileF, (window_width // 2 - 6 * player_width - 20, window_height // 3 * 2 - 20))
        pygame.draw.rect(window, WHITE, (window_width // 2 - player_width // 2, window_height // 3 - player_height // 2, player_width, player_height))
        window.blit(aliveP, (window_width // 2 - 20, window_height // 3 - 20))
        window.blit(cursor, (mouse_x, mouse_y))

        if window_width // 2 - player_width // 2 <= mouse_x <= window_width // 2 + player_width // 2 and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE1 = True
        else: selectCE1 = False
        if window_width // 2 - player_width // 2 + 2 * player_width <= mouse_x <= window_width // 2 + player_width // 2 + 2 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE2 = True
        else: selectCE2 = False
        if window_width // 2 - player_width // 2 - 2 * player_width <= mouse_x <= window_width // 2 + player_width // 2 - 2 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE3 = True
        else: selectCE3 = False
        if window_width // 2 - player_width // 2 + 4 * player_width <= mouse_x <= window_width // 2 + player_width // 2 + 4 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE4 = True
        else: selectCE4 = False
        if window_width // 2 - player_width // 2 - 4 * player_width <= mouse_x <= window_width // 2 + player_width // 2 - 4 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE5 = True
        else: selectCE5 = False
        if window_width // 2 - player_width // 2 + 6 * player_width <= mouse_x <= window_width // 2 + player_width // 2 + 6 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE6 = True
        else: selectCE6 = False
        if window_width // 2 - player_width // 2 - 6 * player_width <= mouse_x <= window_width // 2 + player_width // 2 - 6 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE7 = True
        else: selectCE7 = False

    if dead_character_edit:
        window.fill(BLACK)
        if mouse_x < 80 and mouse_y < 40:
            window.blit(arrow2F, (0,0))
            backselect = True
        else: 
            window.blit(arrow1F, (0,0))
            backselect = False
        pygame.draw.rect(window, RED, (window_width // 2 - player_width // 2, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, RED, (window_width // 2 - player_width // 2 + 2 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, RED, (window_width // 2 - player_width // 2 - 2 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, RED, (window_width // 2 - player_width // 2 + 4 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, RED, (window_width // 2 - player_width // 2 - 4 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, RED, (window_width // 2 - player_width // 2 + 6 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        pygame.draw.rect(window, RED, (window_width // 2 - player_width // 2 - 6 * player_width, window_height // 3 * 2 - player_height // 2, player_width, player_height))
        window.blit(nothingF, (window_width // 2 - 20, window_height // 3 * 2 - 20))
        window.blit(deadPF, (window_width // 2 + 2 * player_width - 20, window_height // 3 * 2 - 20))
        window.blit(verisedF, (window_width // 2 - 2 * player_width - 20, window_height // 3 * 2 - 20))
        window.blit(yongershiF, (window_width // 2 + 4 * player_width - 20, window_height // 3 * 2 - 20))
        window.blit(wowF, (window_width // 2 - 4 * player_width - 20, window_height // 3 * 2 - 20))
        window.blit(desintresseF, (window_width // 2 + 6 * player_width - 20, window_height // 3 * 2 - 20))
        window.blit(smileF, (window_width // 2 - 6 * player_width - 20, window_height // 3 * 2 - 20))
        pygame.draw.rect(window, RED, (window_width // 2 - player_width // 2, window_height // 3 - player_height // 2, player_width, player_height))
        window.blit(deadP, (window_width // 2 - 20, window_height // 3 - 20))
        window.blit(cursor, (mouse_x, mouse_y))

        if window_width // 2 - player_width // 2 <= mouse_x <= window_width // 2 + player_width // 2 and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE1 = True
        else: selectCE1 = False
        if window_width // 2 - player_width // 2 + 2 * player_width <= mouse_x <= window_width // 2 + player_width // 2 + 2 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE2 = True
        else: selectCE2 = False
        if window_width // 2 - player_width // 2 - 2 * player_width <= mouse_x <= window_width // 2 + player_width // 2 - 2 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE3 = True
        else: selectCE3 = False
        if window_width // 2 - player_width // 2 + 4 * player_width <= mouse_x <= window_width // 2 + player_width // 2 + 4 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE4 = True
        else: selectCE4 = False
        if window_width // 2 - player_width // 2 - 4 * player_width <= mouse_x <= window_width // 2 + player_width // 2 - 4 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE5 = True
        else: selectCE5 = False
        if window_width // 2 - player_width // 2 + 6 * player_width <= mouse_x <= window_width // 2 + player_width // 2 + 6 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE6 = True
        else: selectCE6 = False
        if window_width // 2 - player_width // 2 - 6 * player_width <= mouse_x <= window_width // 2 + player_width // 2 - 6 * player_width and window_height // 3 * 2 - player_height // 2 <= mouse_y <= window_height // 3 * 2 + player_height // 2:
            selectCE7 = True
        else: selectCE7 = False

    if credits_page:
        window.fill(BLACK)
        if mouse_x < 80 and mouse_y < 40:
            window.blit(arrow2F, (0,0))
            backselect = True
        else: 
            window.blit(arrow1F, (0,0))
            backselect = False
        window.blit(creditsF, (window_width // 2 - 400, window_height // 2 - 300))
        window.blit(cursor, (mouse_x, mouse_y))
    
    if settings:
        if settings_one:
            change_window_width = window_width
            change_window_height = window_height
            current_window_width = window_width
            current_window_height = window_height
            change_fullscreen = DoFullscreen
            current_fullscreen_status = DoFullscreen
            resolution_v = 0
            custom_resolution2 = custom_resolution
            settings_one = False
            wait_time = 0
        window.fill(BLACK)
        if mouse_x < 80 and mouse_y < 40:
            window.blit(arrow2F, (0,0))
            backselect = True
        else: 
            window.blit(arrow1F, (0,0))
            backselect = False

        font = pygame.font.Font(None, int(window_height / 5))
        font2 = pygame.font.Font(None, int(window_height / 8))
        font3 = pygame.font.Font(None, int(window_height / 16))
        text = font.render("SETTINGS", True, WHITE)
        text2 = font2.render("VIDEO:", True, WHITE)
        text3 = font2.render("SOUND:", True, WHITE)
        text4 = font3.render("Music: " + str(int(volume_music * 100)), True, BLACK)
        text5 = font3.render("Soundeffects: " + str(int(volume_sfx * 100)), True, BLACK)
        text6 = font3.render("Fulscreen:", True, WHITE)
        text7 = font3.render("APPLY", True, WHITE)
        text8 = font2.render("KEEP CHANGES - " + str((300 - wait_time) // 60), True, WHITE)
        text9 = font3.render("Resolution: " + str(change_window_width) + "x" + str(change_window_height) + " ", True, WHITE)
        text10 = font3.render("*You may have to restart the game after applying", True, RED)
        text11 = font3.render("Intro:", True, WHITE)
        text_rec = text.get_rect(center=(window_width // 2, window_height // 10))
        text_rec2 = text2.get_rect(center=(window_width // 4, window_height // 4))
        text_rec3 = text3.get_rect(center=(window_width // 4 * 3, window_height // 4))
        text_rec4 = text4.get_rect(center=(window_width // 4 * 3, window_height // 3 + window_height / 30))
        text_rec5 = text5.get_rect(center=(window_width // 4 * 3, window_height // 2 + window_height / 30))
        text_rec6 = text6.get_rect(center=(window_width // 4 - text6.get_height() // 4 * 3, window_height // 3))
        text_rec7 = text7.get_rect(center=(window_width // 4, window_height // 10 * 8))
        text_rec8 = text8.get_rect(center=(window_width // 2, window_height // 2))
        text_rec9 = text9.get_rect(center=(window_width // 4, window_height // 2.5))
        text_rec10 = text10.get_rect(center=(window_width // 2, window_height // 10 * 9))
        text_rec11 = text11.get_rect(center=(window_width // 4 - text11.get_height() // 4 * 3, window_height / 2))
        window.blit(text, text_rec)
        window.blit(text2, text_rec2)
        window.blit(text3, text_rec3)
        window.blit(text10, text_rec10)

        #Window
        #Fulscreen
        window.blit(text6, text_rec6)
        pygame.draw.rect(window, WHITE, (text_rec6[0] + text6.get_width() + text6.get_height() // 2, text_rec6[1], text6.get_height(), text6.get_height()))
        if change_fullscreen: pygame.draw.rect(window, RED, (text_rec6[0] + text6.get_width() + text6.get_height() // 2 + window_height // 200, text_rec6[1] + window_height // 200, text6.get_height() - window_height // 100, text6.get_height() - window_height // 100))
        else: pygame.draw.rect(window, BLACK, (text_rec6[0] + text6.get_width() + text6.get_height() // 2 + window_height // 200, text_rec6[1] + window_height // 200, text6.get_height() - window_height // 100, text6.get_height() - window_height // 100))
        if text_rec6[0] + text6.get_width() + text6.get_height() // 2 <= mouse_x <= text_rec6[0] + text6.get_width() + text6.get_height() // 2 + text6.get_height() and text_rec6[1] <= mouse_y <= text_rec6[1] + text6.get_height(): fullscreenselect = True
        else: fullscreenselect = False

        #Resolution
        if autowindow:
            text9 = font3.render("Resolution: " + str(change_window_width) + "x" + str(change_window_height) + " (AUTO) ", True, WHITE)
            text_rec9 = text9.get_rect(center=(window_width // 4, window_height // 2.5))
        elif custom_resolution2:
            text9 = font3.render("Resolution: " + str(change_window_width) + "x" + str(change_window_height) + " (CUSTOM) ", True, WHITE)
            text_rec9 = text9.get_rect(center=(window_width // 4, window_height // 2.5))
        window.blit(text9, text_rec9)
        pygame.draw.rect(window, WHITE, (text_rec9[0] + text9.get_width(), text_rec9[1], text9.get_height(), text9.get_height()))
        if text_rec9[0] + text9.get_width() <= mouse_x <= text_rec9[0] + text9.get_width() + text9.get_height() and text_rec9[1] <= mouse_y <= text_rec9[1] + text9.get_height() and not waitconfirm:
            pygame.draw.rect(window, BLUE, (text_rec9[0] + text9.get_width(), text_rec9[1], text9.get_height(), text9.get_height()))
            resolutionselect = True
        else: resolutionselect = False

        #Fulscreen
        window.blit(text11, text_rec11)
        pygame.draw.rect(window, WHITE, (text_rec11[0] + text11.get_width() + text11.get_height() // 2, text_rec11[1], text11.get_height(), text11.get_height()))
        if intro: pygame.draw.rect(window, GREEN, (text_rec11[0] + text11.get_width() + text11.get_height() // 2 + window_height // 200, text_rec11[1] + window_height // 200, text11.get_height() - window_height // 100, text11.get_height() - window_height // 100))
        else: pygame.draw.rect(window, BLACK, (text_rec11[0] + text11.get_width() + text11.get_height() // 2 + window_height // 200, text_rec11[1] + window_height // 200, text11.get_height() - window_height // 100, text11.get_height() - window_height // 100))
        if text_rec11[0] + text11.get_width() + text11.get_height() // 2 <= mouse_x <= text_rec11[0] + text11.get_width() + text11.get_height() // 2 + text11.get_height() and text_rec11[1] <= mouse_y <= text_rec11[1] + text11.get_height(): introselect = True
        else: introselect = False
        
        #Volume slider
        #Mouse pos
        if pygame.mouse.get_pressed()[0]:
            for sfx in soundeffects:
                pygame.mixer.Sound.set_volume(sfx, volume_sfx)
            pygame.mixer.music.set_volume(volume_music)
            if window_width / 4 * 3 - window_width / 8 <= mouse_x <= window_width / 4 * 3 - window_width / 8 - window_width / 160 + window_width / 4 + window_width / 160:
                if window_height // 3 <= mouse_y <= window_height // 3 + window_height / 15:
                    volume_music = int(mouse_x - (window_width / 4 * 3 - window_width / 8)) / (window_width / 4)
                if window_height // 2 <= mouse_y <= window_height //2 + window_height / 15:
                    volume_sfx = int(mouse_x - (window_width / 4 * 3 - window_width / 8)) / (window_width / 4)
            elif window_width / 4 * 3 - window_width / 8 - window_width / 80 <= mouse_x <= window_width / 4 * 3 - window_width / 8:
                if window_height // 3 <= mouse_y <= window_height // 3 + window_height / 15:
                    volume_music = 0
                if window_height // 2 <= mouse_y <= window_height //2 + window_height / 15:
                    volume_sfx = 0
            elif window_width / 4 * 3 - window_width / 8 - window_width / 160 + window_width / 4 + window_width / 160 <= mouse_x <= window_width / 4 * 3 - window_width / 8 - window_width / 160 + window_width / 4 + window_width / 160 + window_width / 80:
                if window_height // 3 <= mouse_y <= window_height // 3 + window_height / 15:
                    volume_music = 1.0
                if window_height // 2 <= mouse_y <= window_height //2 + window_height / 15:
                    volume_sfx = 1.0

        #Music
        pygame.draw.rect(window, GREY, (window_width / 4 * 3 - window_width / 8 - window_width / 160, window_height // 3, window_width / 4 + window_width / 80, window_height / 15))
        pygame.draw.rect(window, RED, (window_width / 4 * 3 - window_width / 8 + volume_music * window_width / 4 - window_width / 160, window_height // 3, window_width / 80, window_height / 15))
        window.blit(text4, text_rec4)
        #Soundeffects
        pygame.draw.rect(window, GREY, (window_width / 4 * 3 - window_width / 8 - window_width / 160, window_height // 2, window_width / 4 + window_width / 80, window_height / 15))
        pygame.draw.rect(window, BLUE, (window_width / 4 * 3 - window_width / 8 + volume_sfx * window_width / 4 - window_width / 160, window_height // 2, window_width / 80, window_height / 15))
        window.blit(text5, text_rec5)

        #Apply
        if text_rec7[0] <= mouse_x <= text_rec7[0] + text7.get_width() and text_rec7[1] <= mouse_y <= text_rec7[1] + text7.get_height():
            text7 = font3.render("APPLY", True, BLUE)
            applyselect = True
        else: applyselect = False
        window.blit(text7, text_rec7)

        if waitconfirm:
            wait_time += 1
            if text_rec8[0] <= mouse_x <= text_rec8[0] + text8.get_width() and text_rec8[1] <= mouse_y <= text_rec8[1] + text8.get_height():
                text8 = font2.render("KEEP CHANGES - " + str((300 - wait_time) // 60), True, RED)
                keepchangesselect = True
            else:
                keepchangesselect = False
            if wait_time > 10:
                pygame.draw.rect(window, BLACK, (text_rec8[0], text_rec8[1], text8.get_width(), text8.get_height()))
                window.blit(text8, text_rec8)
            if wait_time >= 300:
                window_width = current_window_width
                window_height = current_window_height
                DoFullscreen = current_fullscreen_status
                change_fullscreen = DoFullscreen
                if DoFullscreen == 1: 
                    window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
                else: 
                    window = pygame.display.set_mode((window_width, window_height))
                waitconfirm = False

        window.blit(cursor, (mouse_x, mouse_y))

    pygame.display.update()
    clock.tick(60)

autowindow = autowindow2
if autowindow:
    change_window_width = 0
    change_window_height = 0
if DoFullscreen: dfs = 1
else: dfs = 0
if os.path.isfile('AvoiderData/data.txt'):
    if autowindow:
        data_list[1] = "0" + "\n"
        data_list[3] = "0" + "\n"
    else:
        data_list[1] = str(change_window_width) + "\n"
        data_list[3] = str(change_window_height) + "\n"
    data_list[5] = str(dfs) + "\n"
    data_list[7] = str(highscore) + "\n"
    data_list[9] = str(gamesplayed) + "\n"
    data_list[11] = str(volume_music) + "\n"
    data_list[13] = str(volume_sfx) + "\n"
    if intro: 
        data_list[15] = "1" + "\n"
    else:
        data_list[15] = "0" + "\n"
    with open('AvoiderData/data.txt', 'w',) as file:
        file.writelines(data_list)
else:
    if intro: isintro = 1
    else: isintro = 0
    write = ["Window width:", str(change_window_width), "Window height:", str(change_window_height), "Fullscreen (1/0):", str(dfs), "Highscore", str(highscore), "Games Played:", str(gamesplayed), "Music Volume (0-1):", str(volume_music), "Sound Effects Volume (0-1):", str(volume_sfx),"Intro (1/0):", str(isintro), "", "If either the window width or height is 0, the program will automatically set it. (RECOMMENDED)", "IMPORTANT: Don't change anything if you don't know what it will do!"]
    f = open("AvoiderData/data.txt", "w")
    f.write("\n".join(write))
    f.close