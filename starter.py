from pico2d import *
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running, x1, y1, click_list,x,y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x1, y1 = event.x, TUK_HEIGHT - 1 - event.y
            click_list.append((x1, y1))
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
x,y = TUK_WIDTH//2, TUK_HEIGHT//2
x1, y1 = 0, 0
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
click_list = []
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.clip_draw(0,0,50,50,x,y)



    if click_list:
        target = click_list[0]
        dx = target[0] - character_x
        dy = target[1] - character_y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:
            speed = 0.5
            character_x += (dx / distance) * speed
            character_y += (dy / distance) * speed


        for i in range(0, len(click_list)):
            hand_arrow.clip_draw(0,0,50,50,click_list[i][0],click_list[i][1])

        #hand_arrow.clip_draw(0, 0, 50, 50, target[0], target[1])

        if distance <= 1:
            click_list.pop(0)

    character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()
