import pygame
from util import load_image

width=1200
height=600

# Importa imagem de carregamento
Loadingimage, Loadingimage_rect = load_image(
    'images/imagens/LogoTelaCarregamento.png',
    (width/2, height*(2/3)),
    (width/2, height/2)
)

# Cria barra de carregamento
verticesloadbar1=[(width/4,510*(height/600)),(width/4,525*(height/600)),(3*(width/4),525*(height/600)),(3*(width/4),510*(height/600))]
colorload1=(255,255,255)
colorload2=(15,255,3)


# Fonte "concluído"
concfont = pygame.font.SysFont(None, 24)
conctext = concfont.render('Concluído!', True, (255,255,255))
conctextrect=conctext.get_rect()


# Gera imagem background
BGSSimage, BGSSimage_rect = load_image(
    'images/imagens/BGtelainicial.png',
    (width, height),
    (width/2, height/2)
)

# Importa imagem de título
Titleimage, Titleimage_rect = load_image(
    'images/imagens/BattlefightersArco.png',
    (width/2, height/3),
    (width/2, (height/2)-(height/4))
)

# Importa imagem de grade de personagens
Gradeimage, Gradeimage_rect = load_image(
    'images/imagens/Gradepersonagens.png',
    (width*(2/3), height*(5/6)),
    (width/2, height/2)
)

# Imagem Versus
Versus, Versusrect = load_image(
    'images/imagens/Versus.png',
    (width/4, height/3),
    (width/2, height/2)
)

# Plano de fundo da vitória
plano_de_fundo_vitoria_image, plano_de_fundo_vitoria_rect = load_image(
    "images/imagens/plano_de_fundo_vitoria.jpeg",
    size=(width, height),
    center=(width/2, height/2)
)
