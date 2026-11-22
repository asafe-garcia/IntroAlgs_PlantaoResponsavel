"""Regras do jogo Plantão Responsável: cartões, pontos, combo e vidas."""

import json

def perder_vida(vidas):
    """Tira uma vida do jogador e retorna as vidas"""
    return vidas - 1

def calcular_pontos(pontos, combo, acertou):
    """Atualiza pontos e combo depois de uma decisão do jogador.

    Se acertou, soma 10 pontos e aumenta o combo em 1.
    Se errou, mantém os pontos e zera o combo.
    Retorna pontos e combo.
    """
    if acertou:
        pontos += 10
        combo += 1
    else:
        combo = 0

    return pontos,combo

def carregar_cartoes(caminho):
    """Lê o arquivo JSON e devolve a lista de cartões (lista de dicionários).

    Se o arquivo não existir, devolve uma lista vazia.
    """
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def filtrar_por_ambiente(cartoes, ambiente):
    """Devolve só os cartões do ambiente pedido ('escola' ou 'clinica')."""
    cartoes_filtrados = []
    for cartao in cartoes:
        if cartao["ambiente"] == ambiente:
            cartoes_filtrados.append(cartao)

    return cartoes_filtrados



    