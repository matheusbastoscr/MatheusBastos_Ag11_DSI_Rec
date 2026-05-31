# Controle de Níveis de Água

## Descrição

Este projeto simula um sistema de monitoramento de um reservatório de água utilizando Python e a biblioteca Colorama.

O sistema exibe mensagens coloridas no terminal de acordo com o nível de água do reservatório.

## Tecnologias Utilizadas

- Python
- Colorama

## Funcionalidades

- Utilização de listas para armazenar os níveis do reservatório.
- Utilização de funções para definir as cores das mensagens.
- Exibição de alertas coloridos no terminal.
- Restauração automática do estilo padrão do terminal.

## Níveis Monitorados

| Nível | Situação | Cor |
|---------|---------|---------|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Como Executar

Instale a biblioteca:

```bash
pip install colorama
```

Execute o programa:

```bash
py controle_agua.py
```
