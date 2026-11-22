"""Ponto de entrada do jogo: janela, loop principal e integração dos módulos.

Responsável: Erick (núcleo e integração).

Este arquivo só junta as partes do grupo:
- logica.py    (Asafe)    -> cartões do JSON, pontos, combo e vidas
- entidades.py (Caio) -> revisor e cartões que caem
- interface.py (Matheus) -> fundo, HUD, cartões e tela de fim de jogo

Regras da Entrega 2 (ambiente ESCOLA):
- o revisor COLETOU o cartão   -> APROVOU a sugestão da IA
- deixou o cartão PASSAR       -> REJEITOU a sugestão da IA
- acerto (aprovar o correto ou rejeitar o incorreto) soma pontos e combo
- coletar um cartão incorreto tira 1 vida e zera o combo
- deixar passar um cartão correto não tira vida, mas zera o combo
A % de confiança aparece no cartão, mas NÃO decide se a resposta está certa.
"""
import os
import random

import pygame

# Os módulos do grupo podem ficar em src/ (padrão do template) ou na raiz.
try:
    from src import logica, entidades, interface
except ImportError:
    import logica
    import entidades
    import interface


# ----------------------------------------------------------------------------
# Configurações do núcleo
# ----------------------------------------------------------------------------
LARGURA_TELA = 800
ALTURA_TELA = 600
FPS = 60
TITULO_JOGO = "Plantão Responsável"

AMBIENTE = "escola"
VIDAS_INICIAIS = 3
INTERVALO_CARTOES = 150  # quadros entre um cartão e outro (2,5 s a 60 FPS)
MAX_CARTOES_NA_TELA = 2

PASTA_RAIZ = os.path.dirname(os.path.abspath(__file__))


def caminho_dos_cartoes():
    """Procura o JSON em dados/ (combinado do grupo) ou data/ (template)."""
    for pasta in ("dados", "data"):
        caminho = os.path.join(PASTA_RAIZ, pasta, "cartoes.json")
        if os.path.exists(caminho):
            return caminho
    return os.path.join(PASTA_RAIZ, "dados", "cartoes.json")


# ----------------------------------------------------------------------------
# Estado da partida
# ----------------------------------------------------------------------------
def criar_estado(cartoes_do_ambiente):
    """Monta o estado de uma partida nova num dicionário."""
    return {
        "pontos": 0,
        "vidas": VIDAS_INICIAIS,
        "combo": 0,
        "revisor": entidades.criar_revisor(),
        "cartoes_na_tela": [],
        "baralho": [],
        "todos_cartoes": cartoes_do_ambiente,
        "tempo_proximo": 0,
        "ultima_mensagem": "Pegue = APROVAR | Deixe cair = REJEITAR",
        "fim": False,
    }


def sortear_proximo(estado):
    """Tira um cartão do baralho; quando acaba, embaralha tudo de novo."""
    if len(estado["baralho"]) == 0:
        estado["baralho"] = list(estado["todos_cartoes"])
        random.shuffle(estado["baralho"])
    return estado["baralho"].pop()


def registrar_decisao(estado, cartao_dados, aprovou):
    """Aplica a decisão do jogador: pontos, combo, vidas e mensagem."""
    acertou = aprovou == cartao_dados["confiavel"]

    estado["pontos"], estado["combo"] = logica.calcular_pontos(
        estado["pontos"], estado["combo"], acertou
    )
    # Só perde vida quem APROVA (coleta) um cartão incorreto.
    # Deixar passar um cartão correto só zera o combo (feito em calcular_pontos).
    if aprovou and not acertou:
        estado["vidas"] = logica.perder_vida(estado["vidas"])

    acao = "Aprovou" if aprovou else "Rejeitou"
    resultado = "certo" if acertou else "errado"
    estado["ultima_mensagem"] = f"{acao} ({resultado}): {cartao_dados['explicacao']}"

    if estado["vidas"] <= 0:
        estado["fim"] = True


# ----------------------------------------------------------------------------
# As três etapas do loop: eventos, atualização e desenho
# ----------------------------------------------------------------------------
def processar_eventos(estado, cartoes_do_ambiente):
    """Trata fechar a janela, ESC (sair) e Enter/R (reiniciar no fim de jogo).

    Devolve (rodando, estado).
    """
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            return False, estado
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                return False, estado
            reiniciar = evento.key in (pygame.K_RETURN, pygame.K_r)
            if reiniciar and estado["fim"]:
                estado = criar_estado(cartoes_do_ambiente)
    return True, estado


def atualizar(estado):
    """Atualiza um quadro: move o revisor, solta e derruba cartões, colisões."""
    if estado["fim"]:
        return

    teclas = pygame.key.get_pressed()
    entidades.mover_revisor(estado["revisor"], teclas)

    # Solta um cartão novo de tempos em tempos
    estado["tempo_proximo"] -= 1
    if estado["tempo_proximo"] <= 0 and len(estado["cartoes_na_tela"]) < MAX_CARTOES_NA_TELA:
        dados = sortear_proximo(estado)
        estado["cartoes_na_tela"].append(entidades.criar_cartao(dados))
        estado["tempo_proximo"] = INTERVALO_CARTOES

    # Percorre uma cópia da lista para poder remover durante o laço
    for cartao in list(estado["cartoes_na_tela"]):
        entidades.atualizar_cartao(cartao)

        if entidades.colidiu(estado["revisor"], cartao):
            registrar_decisao(estado, cartao["dados"], aprovou=True)
            estado["cartoes_na_tela"].remove(cartao)
        elif entidades.saiu_da_tela(cartao):
            registrar_decisao(estado, cartao["dados"], aprovou=False)
            estado["cartoes_na_tela"].remove(cartao)

        if estado["fim"]:
            break


def desenhar(tela, estado):
    """Desenha a cena na ordem: fundo, cartões, revisor, HUD e fim de jogo."""
    interface.desenhar_fundo(tela)

    for cartao in estado["cartoes_na_tela"]:
        interface.desenhar_cartao(tela, cartao["rect"], cartao["dados"])

    entidades.desenhar_revisor(tela, estado["revisor"])
    interface.desenhar_hud(tela, estado["pontos"], estado["vidas"], estado["combo"])

    if estado["fim"]:
        interface.desenhar_fim_de_jogo(tela, estado["pontos"])

    pygame.display.flip()


def atualizar_titulo(estado):
    """Mostra pontos, vidas e o resultado da última decisão no título."""
    pygame.display.set_caption(
        f"{TITULO_JOGO} | Pontos: {estado['pontos']} | Vidas: {estado['vidas']}"
        f" | {estado['ultima_mensagem']}"
    )


# ----------------------------------------------------------------------------
# Programa principal
# ----------------------------------------------------------------------------
def executar_jogo():
    """Abre a janela e roda o loop principal até o jogador sair."""
    cartoes = logica.carregar_cartoes(caminho_dos_cartoes())
    cartoes_do_ambiente = logica.filtrar_por_ambiente(cartoes, AMBIENTE)
    if len(cartoes_do_ambiente) == 0:
        print("Nenhum cartão do ambiente", AMBIENTE, "foi encontrado no JSON.")
        return

    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    estado = criar_estado(cartoes_do_ambiente)
    rodando = True
    while rodando:
        relogio.tick(FPS)
        rodando, estado = processar_eventos(estado, cartoes_do_ambiente)
        atualizar(estado)
        desenhar(tela, estado)
        atualizar_titulo(estado)

    pygame.quit()


if __name__ == "__main__":
    executar_jogo()