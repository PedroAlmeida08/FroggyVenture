import Globals as gl


def draw_text(text, font, color, x, y):
    img = font.render(text, True, (255, 255, 255))
    gl.screen.blit(img, (x, y))
