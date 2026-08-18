import pytest
from src.models import Produto
from src.exceptions import ValorInvalidoError

def test_criar_produto_com_valor_positivo():
    produto = Produto(nome="Mouse", valor=50.0)
    assert produto.valor == 50.0

def test_criar_produto_com_valor_negativo_deve_falhar():
    with pytest.raises(ValorInvalidoError):
        Produto(nome="Erro", valor=-10)
