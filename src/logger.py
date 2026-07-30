# src/logger.py
from datetime import datetime

def registrar_log(mensagem: str, caminho: str = "data/log_operacoes.txt"):
    """Adiciona uma entrada de log com timestamp, sem apagar o histórico anterior."""
    with open(caminho, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {mensagem}\n")