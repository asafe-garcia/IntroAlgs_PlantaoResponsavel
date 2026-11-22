"""Interface do jogo Plantão Responsável: fundo, HUD, cartões e fim de jogo.

Responsável: Matheus (interface e recursos).

Tudo é desenhado com primitivas do pygame (retângulos, linhas e texto),
então o jogo não depende de imagens externas.
As medidas são tiradas da própria tela (tela.get_width / get_height),
assim a interface acompanha o tamanho definido no main.py.
"""
import pygame

# ----------------------------------------------------------------------------
# Cores (R, G, B)
# ----------------------------------------------------------------------------
BRANCO = (255, 255, 255)
PRETO = (20, 20, 20)

PAREDE = (232, 222, 196)
RODAPE = (150, 110, 70)
PISO = (176, 132, 88)
PISO_LINHA = (156, 114, 74)

QUADRO = (38, 84, 62)
QUADRO_MOLDURA = (120, 82, 46)
GIZ = (225, 235, 225)

# ----------------------------------------------------------------------------
# Fontes
# ----------------------------------------------------------------------------
# As fontes só podem ser criadas depois do pygame.init(), por isso não são
# criadas aqui no topo: ficam neste dicionário e são criadas na 1ª vez que
# alguém pede (e reaproveitadas nas próximas, sem recriar a cada quadro).
_fontes = {}


def pegar_fonte(tamanho, negrito=False):
    """Retorna uma fonte do sistema no tamanho pedido, guardada em cache."""
    chave = (tamanho, negrito)
    if chave not in _fontes:
        _fontes[chave] = pygame.font.SysFont("arial", tamanho, bold=negrito)
    return _fontes[chave]


# ----------------------------------------------------------------------------
# Fundo
# ----------------------------------------------------------------------------
def desenhar_fundo(tela):
    """Desenha uma sala de aula: parede, quadro-negro e piso de madeira."""
    largura = tela.get_width()
    altura = tela.get_height()
    altura_piso = 80
    topo_piso = altura - altura_piso

    # Parede.
    tela.fill(PAREDE)

    # Quadro-negro com moldura, centralizado abaixo da faixa do HUD.
    quadro = pygame.Rect(0, 0, int(largura * 0.6), int(altura * 0.32))
    quadro.centerx = largura // 2
    quadro.top = 70
    moldura = quadro.inflate(16, 16)
    pygame.draw.rect(tela, QUADRO_MOLDURA, moldura, border_radius=6)
    pygame.draw.rect(tela, QUADRO, quadro)

    # "Escrita" de giz no quadro.
    titulo = pegar_fonte(22, negrito=True).render("Revise antes de aprovar!", True, GIZ)
    tela.blit(titulo, titulo.get_rect(center=(quadro.centerx, quadro.top + 32)))
    for i, fracao in enumerate((0.7, 0.55, 0.62)):
        y = quadro.top + 70 + i * 22
        pygame.draw.line(tela, GIZ, (quadro.left + 30, y),
                         (quadro.left + 30 + int(quadro.width * fracao), y), 2)

    # Bandeja de giz embaixo do quadro.
    bandeja = pygame.Rect(quadro.left, moldura.bottom, quadro.width, 6)
    pygame.draw.rect(tela, QUADRO_MOLDURA, bandeja)

    # Piso de madeira com rodapé e tábuas.
    pygame.draw.rect(tela, PISO, (0, topo_piso, largura, altura_piso))
    pygame.draw.rect(tela, RODAPE, (0, topo_piso - 8, largura, 8))
    for x in range(0, largura, 100):
        pygame.draw.line(tela, PISO_LINHA, (x, topo_piso), (x, altura), 2)


# ----------------------------------------------------------------------------
# Funções ainda em construção (próximos commits).
# Já existem com a assinatura usada no main.py para o jogo abrir sem erro.
# ----------------------------------------------------------------------------
def desenhar_hud(tela, pontos, vidas, combo):
    """Desenha pontos, vidas e combo no topo da tela. (em construção)"""
    pass


def desenhar_cartao(tela, rect, dados):
    """Desenha um cartão com o texto e a % de confiança. (em construção)"""
    pass


def desenhar_fim_de_jogo(tela, pontos):
    """Desenha a tela de fim de jogo com a pontuação final. (em construção)"""
    pass
