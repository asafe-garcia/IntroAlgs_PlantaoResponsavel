# Plantão Responsável

Projeto final da disciplina de Introdução a Algoritmos/Programação (PUC Minas), desenvolvido com Python e Pygame a partir do [template da disciplina](https://github.com/ICEI-PUC-Minas-PPL-CDIA/IntroAlgs_pygame_template).

**Tema:** Inteligência Artificial no Cotidiano: Aplicações e Uso Responsável. O foco é a **revisão humana das sugestões da IA**, porque uma confiança alta não garante que a sugestão está certa.

## Integrantes do grupo

- Asafe Rodrigues Garcia
- Caio Silveira Figueiredo
- Erick Gabriel Chiaradia Kalil e Silva
- Matheus Wike Carvalho

## Descrição do jogo

Plantão Responsável é um jogo em que o jogador controla um revisor que supervisiona as sugestões de uma IA usada em uma escola ou em uma clínica. No início, o jogador escolhe o ambiente, e cada um tem seu próprio fundo e seus próprios cartões. Cartões com sugestões da IA caem do alto da tela, cada um com um texto curto e um nível de confiança. Alguns cartões estão corretos e outros contêm erros, vieses ou exageram na confiança. O jogador ganha pontos ao tomar a decisão certa e perde vidas ao aprovar sugestões erradas. A partida termina quando as vidas acabam ou quando as 3 rodadas do ambiente escolhido são concluídas.

## Objetivo do jogador

O objetivo é aprovar as sugestões corretas da IA (coletando os cartões) e rejeitar as incorretas (deixando-as passar), usando a revisão humana de forma estratégica. Para vencer, o jogador precisa concluir as 3 rodadas do ambiente escolhido com pelo menos 1 vida e uma taxa mínima de decisões corretas.

## Regras do jogo

- O jogador escolhe o ambiente (escola ou clínica) no menu inicial.
- O jogador começa com 3 vidas, 0 pontos e 3 cargas de revisão.
- Coletar um cartão correto soma pontos; deixar passar um cartão incorreto também soma pontos.
- Coletar um cartão incorreto tira uma vida e zera o combo de acertos.
- Deixar passar um cartão correto não tira vida, mas faz perder o combo e a pontuação daquele cartão.
- A revisão gasta uma carga e revela se o cartão mais próximo é confiável; as cargas se recarregam a cada 5 acertos seguidos.
- A velocidade dos cartões aumenta a cada rodada.
- A partida termina quando as vidas chegam a zero ou quando as 3 rodadas acabam.

## Controles

- Tecla 1: escolher o ambiente escola (no menu)
- Tecla 2: escolher o ambiente clínica (no menu)
- Seta para esquerda (ou A): mover para a esquerda
- Seta para direita (ou D): mover para a direita
- Espaço: revisar o cartão mais próximo
- Enter: iniciar ou reiniciar a partida
- P: pausar o jogo
- ESC: sair do jogo

## Status das entregas

### Entrega 2: versão parcial executável (22/11)

Escopo desta entrega:

- ambiente **Escola** (o jogo já começa nele);
- janela do Pygame e loop principal (eventos, atualização, desenho, 60 FPS);
- revisor se movendo com setas ou A/D, sem sair da tela;
- cartões caindo, lidos do arquivo JSON, com texto e % de confiança;
- coletar o cartão = aprovar, deixar passar = rejeitar;
- pontuação, combo e vidas na tela, com a explicação da última decisão no título da janela;
- fim de jogo com 0 vidas. **Enter** (ou R) reinicia e **ESC** sai.

### Entrega 3: versão final (29/11)

Ainda falta: ambiente Clínica e menu de escolha (teclas 1 e 2), revisão com cargas (Espaço), 3 rodadas com velocidade crescente, pausa (P), condição de vitória e recorde salvo em arquivo.

## Como executar o projeto

Precisa de Python 3 instalado (marque "Add python.exe to PATH" na instalação).

```bash
git clone LINK_DO_REPOSITORIO
cd IntroAlgs_PlantaoResponsavel
pip install -r requirements.txt
python main.py
```

No Windows, se `python` não funcionar, use `py` (por exemplo: `py -m pip install -r requirements.txt` e `py main.py`).

O projeto usa o **pygame-ce**, que é instalado pelo `requirements.txt`. O pygame original não tem versão pronta para o Python 3.14 em diante, e o pygame-ce funciona igual (o código continua usando `import pygame`).

## Como executar os testes

```bash
python -m pytest
```

## Estrutura do projeto

- `main.py`: ponto de entrada; janela, loop principal e integração dos módulos.
- `src/`: código-fonte do jogo.
  - `logica.py`: carregar e filtrar cartões, pontos, combo e vidas.
  - `entidades.py`: revisor e cartões (movimento, queda e colisão).
  - `interface.py`: fundo, HUD, cartões com % de confiança e tela de fim de jogo.
- `data/` ou `dados/`: `cartoes.json` com os cartões do jogo; recorde e ranking.
- `assets/`: imagens, fontes e sons.
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo a proposta inicial.

### Divisão do trabalho

| Integrante | Parte |
|---|---|
| Erick Gabriel Chiaradia Kalil e Silva | Núcleo e integração (`main.py`, repositório, README) |
| Caio Silveira Figueiredo | Jogador e cartões (`entidades.py`) |
| Asafe Rodrigues Garcia | Dados e lógica (`logica.py`, `cartoes.json`, `tests/`) |
| Matheus Wike Carvalho | Interface e recursos (`interface.py`, `docs/proposta.MD`) |

### Funções que o `main.py` usa de cada módulo

**logica.py**
- `carregar_cartoes(caminho) -> lista`
- `filtrar_por_ambiente(cartoes, ambiente) -> lista`
- `calcular_pontos(pontos, combo, acertou) -> (pontos, combo)`
- `perder_vida(vidas) -> int`

**entidades.py**
- `criar_revisor() -> pygame.Rect`
- `mover_revisor(revisor, teclas)`
- `desenhar_revisor(tela, revisor)`
- `criar_cartao(cartao_dados) -> {"rect": pygame.Rect, "dados": cartao_dados}`
- `atualizar_cartao(cartao)`
- `saiu_da_tela(cartao) -> bool`
- `colidiu(revisor, cartao) -> bool`

**interface.py**
- `desenhar_fundo(tela)`
- `desenhar_hud(tela, pontos, vidas, combo)`
- `desenhar_cartao(tela, cartao_rect, cartao_dados)`
- `desenhar_fim_de_jogo(tela, pontos)`

Cada cartão do JSON é um dicionário com as chaves `texto`, `ambiente`, `confianca`, `confiavel` e `explicacao`.

## Recursos externos

- Base do projeto: [template da disciplina](https://github.com/ICEI-PUC-Minas-PPL-CDIA/IntroAlgs_pygame_template).
- Biblioteca: [pygame-ce](https://pyga.me/) (LGPL).
- Imagens, sons e fontes: nenhum até o momento.