# Proposta Inicial do Jogo

## 1. Nome provisório do jogo

**Nome:** Plantão Responsável

## 2. Integrantes do grupo

- **Nome 1:** Asafe Rodrigues Garcia
- **Nome 2:** Caio Silveira Figueiredo
- **Nome 3:** Erick Gabriel Chiaradia Kalil e Silva
- **Nome 4:** Matheus Wike Carvalho

## 3. Tema escolhido

**Tema:** IA na educação e na saúde: apoio a atividades humanas e importância da revisão por pessoas.

**Como esse tema se relaciona com o jogo?**
O jogador é um(a) profissional que supervisiona um assistente de IA em dois ambientes: uma escola e uma clínica. A IA envia sugestões (correção de redações, recomendação de estudo no mapa da escola; triagem de sintomas, lembrete de medicação no mapa da clínica), e algumas estão corretas e outras contêm erros, vieses ou exageram na confiança. Cada sugestão mostra um "nível de confiança" que nem sempre corresponde à realidade. O jogador precisa decidir o que aprovar e o que rejeitar, e pode gastar um recurso limitado para "revisar" (conferir) a sugestão. Assim, a regra central do jogo é a revisão humana: confiar cegamente na IA gera penalidades.

## 4. Tipo de jogo

**Tipo escolhido:** Coleta de itens e desvio de obstáculos, com tomada de decisão (estilo "pegar ou deixar passar").

## 5. Descrição geral do jogo

**Descrição:**
Ao iniciar, o jogador escolhe o ambiente: escola ou clínica. Cada ambiente tem seu próprio fundo e seus próprios cartões. Na tela, o jogador controla um revisor que se move horizontalmente na parte inferior da janela. Do alto caem cartões de sugestões da IA, cada um com um texto curto (por exemplo, "Aluno com nota baixa: recomendar reforço" na escola ou "Paciente com dor de cabeça: diagnóstico certo, sem consulta" na clínica) e uma porcentagem de confiança. Cartões corretos devem ser coletados (aprovados) e cartões errados ou arriscados devem ser deixados passar (rejeitados). Para decidir melhor, o jogador pode usar o botão de Revisar, que mostra se o cartão mais próximo é confiável, mas há um número limitado de revisões que se recarregam aos poucos. A velocidade de queda aumenta a cada rodada, e ao final aparece uma breve explicação do porquê de certos cartões serem problemáticos (viés, falta de fonte, dado pessoal exposto, etc.).

## 6. Objetivo do jogador

**Objetivo:** Fazer a maior pontuação possível aprovando sugestões corretas e rejeitando as incorretas, usando a revisão humana de forma estratégica e sobrevivendo até o fim das rodadas sem perder todas as vidas.

## 7. Regras principais

- **Regra 1:** O jogador começa com 3 vidas, 0 pontos e 3 cargas de revisão.
- **Regra 2:** Coletar um cartão correto soma pontos; deixar um cartão incorreto passar também soma pontos (rejeição acertada).
- **Regra 3:** Coletar um cartão incorreto (aprovar um erro da IA) tira uma vida e zera o combo de acertos.
- **Regra 4:** Deixar passar um cartão correto não tira vida, mas faz o jogador perder o combo e deixa de pontuar.
- **Regra 5:** A tecla de revisão gasta uma carga e revela se o cartão mais próximo é confiável; as cargas se recarregam a cada 5 acertos seguidos.

## 8. Condição de vitória

**Condição de vitória:** Concluir as 3 rodadas do ambiente escolhido com pelo menos 1 vida, alcançando a taxa mínima de decisões corretas (por exemplo, 70%). A tela final mostra a taxa de acertos e se o recorde foi batido.

## 9. Condição de derrota ou encerramento

**Condição de derrota ou encerramento:** A partida termina quando as vidas chegam a zero (derrota) ou quando as 3 rodadas acabam sem atingir a taxa mínima de acertos. Em ambos os casos aparece uma tela com o resumo das decisões e as explicações dos erros.

## 10. Elementos previstos no jogo

- **Personagem ou elemento principal:** o revisor (profissional de escola/clínica), que se move para a esquerda e para a direita.
- **Obstáculos ou desafios:** cartões de sugestões incorretas da IA (com viés, dado inventado, falta de fonte, exposição de dados pessoais ou confiança exagerada), separados por ambiente (escola e clínica).
- **Itens ou objetos de interação (se houver):** cartões de sugestões corretas e confiáveis; cargas de revisão (ícone de lupa).
- **Pontuação, vidas, tempo ou progresso:** pontuação com combo, 3 vidas, cargas de revisão restantes, número da rodada e recorde salvo em arquivo.

## 11. Controles previstos

**Controles:**
- Tecla 1: escolher o ambiente escola (no menu)
- Tecla 2: escolher o ambiente clínica (no menu)
- Setas esquerda/direita (ou A/D) para mover o revisor.
- Barra de espaço para usar a revisão (conferir o cartão mais próximo).
- Enter para iniciar/reiniciar e P para pausar.

## 12. Principais dificuldades esperadas

- **Dificuldade 1:** Detectar colisões entre o revisor e os cartões e controlar a velocidade de queda por rodada.
- **Dificuldade 2:** Organizar o código em funções e módulos (lógica separada da parte gráfica) para poder testar.
- **Dificuldade 3:** Trabalhar em grupo com o GitHub (commits, conflitos) e escrever testes e docstrings.

## 13. Escopo mínimo para a entrega final

**Escopo mínimo:**
Menu simples para escolher entre dois ambientes (escola e clínica), cada um com fundo próprio. Uma tela de jogo com o revisor móvel e cartões caindo, lidos de um arquivo (JSON) com as sugestões daquele ambiente (texto, ambiente, confiável ou não, explicação). Pontuação, 3 vidas, combo, revisão limitada, 3 rodadas com velocidade crescente, tela de fim de jogo com resumo e explicações, e recorde salvo em arquivo. Testes simples para as funções de lógica (filtro de cartões por ambiente, cálculo de pontos, perda de vida, regras de combo e carga de revisão) e README.md com a descrição e os recursos externos usados.

## 14. Possíveis melhorias, caso haja tempo

- **Melhoria 1:** Sons e animações simples.
- **Melhoria 2:** Ranking com os melhores jogadores.
- **Melhoria 3:** Rodada especial de privacidade, em que os cartões pedem dados pessoais e o jogador decide o que pode ser compartilhado.

## 15. Declaração de originalidade

Declaramos que a ideia, as regras e o código deste projeto são de autoria do grupo. Qualquer recurso externo (imagens, sons, fontes, código ou tutoriais) será identificado no README.md, com origem e licença quando possível.

## 16. Atualizações desde a proposta (Entrega 2)

- **Interface desenhada por código:** o fundo da escola (parede, quadro-negro e piso), o HUD, os cartões e a tela de fim de jogo são feitos com primitivas do pygame (`pygame.draw` e texto), em `src/interface.py`. Assim o jogo não depende de imagens externas.
- **HUD:** faixa no topo com pontos, combo (em destaque quando há sequência de acertos) e vidas em forma de corações.
- **Cartões:** mostram o rótulo "Sugestão da IA", o texto quebrado em linhas e a % de confiança em um selo e em uma barra. A confiança tem sempre a mesma cor, para não entregar se o cartão está certo, reforçando que confiança alta não garante acerto.
- **Fim de jogo:** por enquanto mostra a pontuação final e os controles para jogar de novo ou sair. O resumo das decisões e as explicações dos erros ficam para a entrega final.
- **Recursos externos:** a lista atualizada, com origem e licença, está na seção "Recursos externos" do README.md. Até agora não usamos imagens, sons ou fontes baixados da internet.