"""Demonstração da parte do Caio, sem depender de logica.py e interface.py.

Execute na raiz do repositório: python demo_entidades.py
O jogo oficial continua sendo iniciado por main.py.
"""

import pygame
from src import entidades


def executar():
    pygame.init()
    tela = pygame.display.set_mode((entidades.LARGURA_TELA, entidades.ALTURA_TELA))
    pygame.display.set_caption("Plantão Responsável - teste de entidades")
    relogio = pygame.time.Clock()
    fonte = pygame.font.Font(None, 24)
    fonte_menor = pygame.font.Font(None, 21)

    revisor = entidades.criar_revisor()
    cartoes = []
    tempo_para_novo = 0
    coletados = 0
    rejeitados = 0
    dados_exemplo = {
        "texto": "IA: revisar antes de aprovar",
        "ambiente": "escola",
        "confianca": 96,
        "confiavel": True,
        "explicacao": "A revisão humana é necessária.",
    }

    rodando = True
    while rodando:
        relogio.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                rodando = False

        if not rodando:
            break

        entidades.mover_revisor(revisor, pygame.key.get_pressed())
        tempo_para_novo -= 1
        if tempo_para_novo <= 0 and len(cartoes) < 2:
            cartoes.append(entidades.criar_cartao(dados_exemplo))
            tempo_para_novo = 100

        for cartao in list(cartoes):
            entidades.atualizar_cartao(cartao)
            if entidades.colidiu(revisor, cartao):
                coletados += 1
                cartoes.remove(cartao)
            elif entidades.saiu_da_tela(cartao):
                rejeitados += 1
                cartoes.remove(cartao)

        tela.fill((22, 33, 52))
        titulo = fonte.render("TESTE: revisor, cartoes e colisao", True, (247, 247, 247))
        tela.blit(titulo, (20, 20))
        instrucoes = fonte_menor.render("Setas ou A/D: mover  |  ESC: sair", True, (214, 228, 244))
        tela.blit(instrucoes, (20, 50))
        placar = fonte.render(f"Coletados: {coletados}   Passaram: {rejeitados}",
                             True, (255, 216, 136))
        tela.blit(placar, (20, 78))

        for cartao in cartoes:
            rect = cartao["rect"]
            pygame.draw.rect(tela, (242, 247, 252), rect, border_radius=8)
            pygame.draw.rect(tela, (100, 120, 143), rect, 2, border_radius=8)
            linha1 = fonte.render("Sugestao da IA", True, (27, 51, 79))
            linha2 = fonte_menor.render("Confianca: 96%", True, (27, 51, 79))
            tela.blit(linha1, (rect.x + 12, rect.y + 15))
            tela.blit(linha2, (rect.x + 12, rect.y + 43))

        entidades.desenhar_revisor(tela, revisor)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    executar()
