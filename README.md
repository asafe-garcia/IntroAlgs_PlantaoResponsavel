# Plantão Responsável

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Asafe Rodrigues Garcia
- Caio Silveira Figueiredo
- Erick Gabriel Chiaradia Kalil e Silva
- Matheus Wike Carvalho

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

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

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
