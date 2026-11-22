"""Revisor, cartões e colisões do jogo Plantão Responsável."""

import random
import pygame

LARGURA_TELA = 800
ALTURA_TELA = 600

# Medidas dos objetos em pixels.
LARGURA_REVISOR = 120
ALTURA_REVISOR = 44
LARGURA_CARTAO = 250
ALTURA_CARTAO = 90

# Velocidades em pixels por quadro, considerando 60 FPS no main.py.
VELOCIDADE_REVISOR = 6
VELOCIDADE_CARTAO = 3


def criar_revisor():
    """Retorna um pygame.Rect centralizado próximo à borda inferior."""
    x = (LARGURA_TELA - LARGURA_REVISOR) // 2
    y = ALTURA_TELA - ALTURA_REVISOR - 20
    return pygame.Rect(x, y, LARGURA_REVISOR, ALTURA_REVISOR)


def mover_revisor(revisor, teclas):
    """Move o revisor horizontalmente com setas ou A/D, sem sair da tela."""
    esquerda = teclas[pygame.K_LEFT] or teclas[pygame.K_a]
    direita = teclas[pygame.K_RIGHT] or teclas[pygame.K_d]

    if esquerda and not direita:
        revisor.x -= VELOCIDADE_REVISOR
    elif direita and not esquerda:
        revisor.x += VELOCIDADE_REVISOR

    # Mantém o revisor inteiramente dentro da janela.
    revisor.x = max(0, min(revisor.x, LARGURA_TELA - revisor.width))


def desenhar_revisor(tela, revisor):
    """Desenha o revisor e uma identificação visual simples."""
    azul = (36, 126, 211)
    borda = (171, 224, 255)
    branco = (245, 250, 255)

    pygame.draw.rect(tela, azul, revisor, border_radius=10)
    pygame.draw.rect(tela, borda, revisor, width=2, border_radius=10)

    # Ícone simples de uma pessoa (cabeça e corpo) à esquerda.
    cabeca = (revisor.x + 22, revisor.y + 15)
    pygame.draw.circle(tela, branco, cabeca, 7)
    corpo = pygame.Rect(revisor.x + 12, revisor.y + 24, 20, 12)
    pygame.draw.rect(tela, branco, corpo, border_radius=4)

    # Linhas de identificação à direita, como um crachá.
    pygame.draw.line(tela, branco, (revisor.x + 46, revisor.y + 16),
                     (revisor.right - 12, revisor.y + 16), 3)
    pygame.draw.line(tela, branco, (revisor.x + 46, revisor.y + 27),
                     (revisor.right - 28, revisor.y + 27), 3)


def criar_cartao(cartao_dados):
    """Cria um cartão acima da tela, usando o dicionário vindo do JSON.

    Retorna {'rect': pygame.Rect, 'dados': cartao_dados, 'velocidade': int},
    conforme esperado pelo main.py e pela interface.py.
    A verdade ('confiavel') permanece nos dados, sem desenho neste módulo.
    """
    x = random.randint(0, LARGURA_TELA - LARGURA_CARTAO)
    rect = pygame.Rect(x, -ALTURA_CARTAO, LARGURA_CARTAO, ALTURA_CARTAO)
    return {
        "rect": rect,
        "dados": cartao_dados,
        "velocidade": VELOCIDADE_CARTAO,
    }


def atualizar_cartao(cartao):
    """Move o cartão para baixo uma vez por quadro.

    A velocidade fica em cada cartão para permitir aumentá-la em novas rodadas.
    """
    cartao["rect"].y += cartao["velocidade"]


def saiu_da_tela(cartao):
    """Retorna True somente após o cartão sair completamente pelo rodapé."""
    return cartao["rect"].top >= ALTURA_TELA


def colidiu(revisor, cartao):
    """Retorna True se o retângulo do revisor intercepta o cartão."""
    return revisor.colliderect(cartao["rect"])
