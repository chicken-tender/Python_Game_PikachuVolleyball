import pygame
import random
pygame.init() #초기화(반드시 필요)

# 화면 크기 설정
screen_width = 800 # 가로 크기
screen_height = 600 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) 

# 화면 타이틀 설정
pygame.display.set_caption("피카츄 배구") # 게임 이름

clock = pygame.time.Clock()

# 게임 사운드
hit_sound = pygame.mixer.Sound("C:/Python/Python_Game_PikachuVolleyball/sound/hit.mp3")
win_sound = pygame.mixer.Sound("C:/Python/Python_Game_PikachuVolleyball/sound/win.mp3")

# <images 세팅>
# 배경
background = pygame.image.load("C:/Python/Python_Game_PikachuVolleyball/images/background.jpg")
# 스테이지
stage = pygame.image.load("C:/Python/Python_Game_PikachuVolleyball/images/stage.jpg")
stage_size = stage.get_rect().size
stage_height = stage_size[1]
# 가운데 기둥
stlit = pygame.image.load("C:/Python/Python_Game_PikachuVolleyball/images/stlit.png")
stlit_size = stlit.get_rect().size
stlit_width = stlit_size[0]
stlit_height = stlit_size[1]
stlit_x_pos = screen_width / 2 - stlit_width / 2
stlit_y_pos = screen_height - stlit_height - stage_height
# 캐릭터1
character1 = pygame.image.load("C:/Python/Python_Game_PikachuVolleyball/images/character1.png")
character1_size = character1.get_rect().size
character1_width = character1_size[0]
character1_height = character1_size[1]
character1_x_pos = screen_width / 4 - (character1_width * 2) + character1_width
character1_y_pos = screen_height - character1_height - stage_height
# 캐릭터2
character2 = pygame.image.load("C:/Python/Python_Game_PikachuVolleyball/images/character2.png")
character2_size = character2.get_rect().size
character2_width = character2_size[0]
character2_height = character2_size[1]
character2_x_pos = screen_width / 2 + character2_width * 2
character2_y_pos = screen_height - character2_height - stage_height
# 공1
ball = pygame.image.load("C:/Python/Python_Game_PikachuVolleyball/images/ball.png")
ball_size = ball.get_rect().size
ball_width = ball_size[0]
ball_height = ball_size[1]
ball_pos_x = random.randint(0, screen_width / 2 - ball_width)
ball_pos_y = 0
#공2
ball2 = pygame.image.load("C:/Python/Python_Game_PikachuVolleyball/images/ball2.png")
ball2_size = ball2.get_rect().size
ball2_width = ball2_size[0]
ball2_height = ball2_size[1]
ball2_pos_x = random.randint(stlit_x_pos, screen_width - ball2_width)
ball2_pos_y = 0

# <이동할 좌표>
# 캐릭터1
character1_to_x = 0
character1_to_y = 0
# 캐릭터2
character2_to_x = 0
character2_to_y = 0
# 공
ball_to_x = 0
ball_to_y = 3
# 공2
ball2_to_x = 0
ball2_to_y = 3

# <캐릭터 이동 속도>
character1_speed = 7
character2_speed = 7
ball_speed = 1
ball2_speed = 1

# <폰트>
game_font = pygame.font.Font(None, 100)
score1 = 0
score2 = 0
game_result = ""

# 이벤트 루프
running = True # 게임 진행중
while running:
    dt = clock.tick(60)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생하였는가?
            running = False # 게임이 진행중이 아님
        # 키보드 이벤트(눌렀을때)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                character1_to_x -= character1_speed
            elif event.key == pygame.K_d:
                character1_to_x += character1_speed
            elif event.key == pygame.K_SPACE:
                character1_to_x += 20
            
            if event.key == pygame.K_LEFT:
                character2_to_x -= character2_speed
            elif event.key == pygame.K_RIGHT:
                character2_to_x += character2_speed
            elif event.key == pygame.K_RETURN:
                character2_to_x += 20
        # 키보드 이벤트(떼었을때)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                character1_to_x = 0
            elif event.key == pygame.K_SPACE:
                character1_to_x = 0
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character2_to_x = 0
            elif event.key == pygame.K_RETURN:
                character2_to_x = 0

    character1_x_pos += character1_to_x
    character1_y_pos += character1_to_y
    character2_x_pos += character2_to_x
    character2_y_pos += character2_to_y
    ball_pos_y += ball_speed
    ball2_pos_y += ball2_speed
    
    # 가로 경계값
    if character1_x_pos < 0:
        character1_x_pos = 0
    elif character1_x_pos > (screen_width / 2) - (stlit_width / 2) - character1_width:
        character1_x_pos = (screen_width / 2) - (stlit_width / 2) - character1_width
    
    if character2_x_pos > screen_width - character2_width:
        character2_x_pos = screen_width - character2_width
    elif character2_x_pos < screen_width / 2 + stlit_width / 2:
        character2_x_pos = screen_width / 2 + stlit_width / 2
    # 세로 경계값
    if character1_y_pos < 0:
        character1_y_pos = 0
    elif character1_y_pos > screen_height - character1_height - stage_height:
        character1_y_pos = screen_height - character1_height - stage_height

    if character2_y_pos < 0:
        character2_y_pos = 0
    elif character2_y_pos > screen_height - character2_height - stage_height:
        character2_y_pos = screen_height - character2_height - stage_height

    if ball_pos_y > screen_height - ball_height - stage_height and ball_pos_x < screen_width / 2 - stlit_width / 2 :
        ball_pos_y = screen_height - ball_height - stage_height
        pygame.time.delay(2000)
        score2 += 1
        ball_pos_y = 0
        ball_pos_x = screen_width / 4 - (character1_width * 2) + character1_width
        ball_to_x = random.randint(0, 3)
    elif ball_pos_y > screen_height - ball_height - stage_height and ball_pos_x > screen_width / 2 - stlit_width / 2 :
        ball_pos_y = screen_height - ball_height - stage_height
        pygame.time.delay(2000)
        score1 += 1
        ball_pos_y = 0
        ball_pos_x = screen_width / 2 + character2_width * 2
        ball_to_x = random.randint(0, 3)

    if ball_pos_y < 0:
        ball_pos_y = 0
        ball_to_y = 5
    
    if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width or ball_pos_x > stlit_x_pos - stlit_width / 2:
        ball_to_x = ball_to_x * -1
    ball_pos_x += ball_to_x

    if ball2_pos_x < 0 or ball2_pos_x > screen_width - ball2_width or ball2_pos_x < stlit_x_pos + stlit_width / 2:
        ball2_to_x = ball2_to_x * -1
    ball2_pos_x += ball2_to_x
    
    if ball2_pos_y > screen_height - ball2_height - stage_height and ball2_pos_x < screen_width / 2 - stlit_width / 2 :
        ball2_pos_y = screen_height - ball2_height - stage_height
        pygame.time.delay(2000)
        score2 += 1
        ball2_pos_y = 0
        ball2_pos_x = random.randint(0, screen_width - ball2_width)
        ball2_to_x = random.randint(0, 3)
    elif ball2_pos_y > screen_height - ball2_height - stage_height and ball2_pos_x > screen_width / 2 - stlit_width / 2 :
        ball2_pos_y = screen_height - ball2_height - stage_height
        pygame.time.delay(2000)
        score1 += 1
        ball2_pos_y = 0
        ball2_pos_x = random.randint(0, screen_width - ball2_width)
        ball2_to_x = random.randint(-3, 0)

    if ball2_pos_y < 0:
        ball2_pos_y = 0
        ball2_to_y = 5

    if score1 == 5:
        game_result = "Player1 WIN"
        win_sound.play()
        running = False
    elif score2 == 5:
        game_result = "Player2 WIN"
        win_sound.play()
        running = False


    # 충돌 처리
    character1_rect = character1.get_rect()
    character1_rect.left = character1_x_pos
    character1_rect.top = character1_y_pos

    character2_rect = character2.get_rect()
    character2_rect.left = character2_x_pos
    character2_rect.top = character2_y_pos

    ball_rect = ball.get_rect()
    ball_rect.left = ball_pos_x
    ball_rect.top = ball_pos_y

    ball2_rect = ball2.get_rect()
    ball2_rect.left = ball2_pos_x
    ball2_rect.top = ball2_pos_y

    if ball_rect.colliderect(character1_rect):
        hit_sound.play()
        ball_to_y = -18
        ball_to_x = 6
    
    if ball_rect.colliderect(character2_rect):
        hit_sound.play()
        ball_to_y = -18
        ball_to_x = -6

    if ball2_rect.colliderect(character1_rect):
        hit_sound.play()
        ball2_to_y = -25
        ball2_to_x = 6
    
    if ball2_rect.colliderect(character2_rect):
        hit_sound.play()
        ball2_to_y = -25
        ball2_to_x = -6
    
    ball_pos_x += ball_to_x
    ball_pos_y += ball_to_y

    ball2_pos_x += ball2_to_x
    ball2_pos_y += ball2_to_y

    game_score1 = game_font.render(str(score1), True, (0,0,255))
    game_score2 = game_font.render(str(score2), True, (0,0,255))
    
    screen.blit(background, (0, 0))
    screen.blit(game_score1, (80,40))
    screen.blit(game_score2, (700,40))
    screen.blit(stlit, (stlit_x_pos, stlit_y_pos))
    screen.blit(stage, (0,screen_height - stage_height))
    screen.blit(character1, (character1_x_pos,character1_y_pos))
    screen.blit(character2, (character2_x_pos,character2_y_pos))
    screen.blit(ball, (ball_pos_x,ball_pos_y))
    screen.blit(ball2, (ball2_pos_x,ball2_pos_y))

    msg = game_font.render(game_result, True, (255,0,0))
    msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
    screen.blit(msg, msg_rect)
    pygame.display.update()

pygame.time.delay(3000)
# pygame 종료
pygame.quit()