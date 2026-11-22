import pygame

from src.interface import pegar_fonte, quebrar_texto

pygame.font.init()


def test_quebrar_texto_curto_fica_em_uma_linha():
    """Um texto que cabe na largura deve continuar em uma linha só."""
    fonte = pegar_fonte(15)
    assert quebrar_texto("Revisar a nota", fonte, 500) == ["Revisar a nota"]


def test_quebrar_texto_longo_respeita_a_largura():
    """Cada linha deve caber na largura e nenhuma palavra pode se perder."""
    fonte = pegar_fonte(15)
    texto = "Aluno com dificuldade em frações: recomendar exercícios de reforço"
    linhas = quebrar_texto(texto, fonte, 150)
    assert len(linhas) > 1
    for linha in linhas:
        assert fonte.size(linha)[0] <= 150
    assert " ".join(linhas) == texto


def test_quebrar_texto_vazio():
    """Texto vazio não deve gerar nenhuma linha."""
    assert quebrar_texto("", pegar_fonte(15), 200) == []
