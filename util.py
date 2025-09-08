import pygame

def load_image(path, size, center):
    img = pygame.image.load(path)
    w, h = int(size[0]), int(size[1])
    img = pygame.transform.scale(img, (w, h))
    rect = img.get_rect()
    rect.center = (int(center[0]), int(center[1]))
    return img, rect