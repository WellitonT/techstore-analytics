class TechStoreError(Exception):
    """Exceção base para todos os erros de negócio do projeto."""
    pass
class ValorInvalidoError(TechStoreError):
    pass
class PercentualInvalidoError(TechStoreError):
    pass