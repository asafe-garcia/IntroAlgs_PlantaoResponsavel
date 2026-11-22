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

HUD_FUNDO = (35, 45, 60)
HUD_TEXTO = (235, 240, 245)
CORACAO = (220, 60, 70)
CORACAO_VAZIO = (90, 100, 115)
COMBO_DESTAQUE = (255, 200, 60)

# ----------------------------------------------------------------------------
# Medidas da interface
# ----------------------------------------------------------------------------
ALTURA_HUD = 50
VIDAS_MAXIMAS = 3  # mesmo valor de VIDAS_INICIAIS no main.py

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
# HUD
# ----------------------------------------------------------------------------
def desenhar_coracao(tela, centro_x, centro_y, tamanho, cor):
    """Desenha um coração: dois círculos em cima e um triângulo embaixo."""
    raio = tamanho // 4
    pygame.draw.circle(tela, cor, (centro_x - raio, centro_y - raio // 2), raio)
    pygame.draw.circle(tela, cor, (centro_x + raio, centro_y - raio // 2), raio)
    pontas = [
        (centro_x - 2 * raio, centro_y - raio // 4),
        (centro_x + 2 * raio, centro_y - raio // 4),
        (centro_x, centro_y + tamanho // 2),
    ]
    pygame.draw.polygon(tela, cor, pontas)


def desenhar_hud(tela, pontos, vidas, combo):
    """Desenha a faixa do topo: pontos à esquerda, combo no meio e vidas à direita."""
    largura = tela.get_width()
    centro_y = ALTURA_HUD // 2
    fonte = pegar_fonte(24, negrito=True)

    pygame.draw.rect(tela, HUD_FUNDO, (0, 0, largura, ALTURA_HUD))

    # Pontos.
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, HUD_TEXTO)
    tela.blit(texto_pontos, texto_pontos.get_rect(midleft=(20, centro_y)))

    # Combo: só aparece em destaque quando há uma sequência de acertos.
    if combo > 1:
        texto_combo = fonte.render(f"Combo x{combo}", True, COMBO_DESTAQUE)
    else:
        texto_combo = fonte.render(f"Combo x{combo}", True, CORACAO_VAZIO)
    tela.blit(texto_combo, texto_combo.get_rect(center=(largura // 2, centro_y)))

    # Vidas: corações cheios para as vidas restantes e apagados para as perdidas.
    tamanho = 22
    espaco = 32
    for i in range(VIDAS_MAXIMAS):
        x = largura - 30 - (VIDAS_MAXIMAS - 1 - i) * espaco
        if i < vidas:
            cor = CORACAO
        else:
            cor = CORACAO_VAZIO
        desenhar_coracao(tela, x, centro_y, tamanho, cor)


# ----------------------------------------------------------------------------
# Funções ainda em construção (próximos commits).
# Já existem com a assinatura usada no main.py para o jogo abrir sem erro.
# ----------------------------------------------------------------------------


def desenhar_cartao(tela, rect, dados):
    """Desenha um cartão com o texto e a % de confiança. (em construção)"""
    pass


def desenhar_fim_de_jogo(tela, pontos):
    """Desenha a tela de fim de jogo com a pontuação final. (em construção)"""
    pass
