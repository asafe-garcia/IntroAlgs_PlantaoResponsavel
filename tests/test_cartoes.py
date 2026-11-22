from src.logica import calcular_pontos, perder_vida, filtrar_por_ambiente


def test_acerto_soma_pontos_e_combo():
    """Acertar deve somar pontos e aumentar o combo."""
    assert calcular_pontos(0, 0, True) == (10, 1)


def test_erro_zera_combo():
    """Errar deve manter os pontos e zerar o combo."""
    assert calcular_pontos(30, 3, False) == (30, 0)


def test_perder_vida():
    """Perder vida deve reduzir o total em 1."""
    assert perder_vida(3) == 2


def test_filtrar_por_ambiente():
    """O filtro deve devolver só os cartões do ambiente pedido."""
    cartoes = [
        {"ambiente": "escola"},
        {"ambiente": "clinica"},
        {"ambiente": "escola"},
    ]
    resultado = filtrar_por_ambiente(cartoes, "escola")
    assert len(resultado) == 2