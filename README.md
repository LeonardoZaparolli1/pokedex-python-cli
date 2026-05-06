# 🧾 Pokédex em Python (CLI)

Projeto desenvolvido em Python com o objetivo de simular um sistema de gestão de Pokédex via terminal, permitindo o cadastro, consulta, atualização e remoção de Pokémons.

---

## 🚀 Funcionalidades

* 📌 Adicionar novos Pokémons
* 📋 Listar todos os Pokémons cadastrados
* ✏️ Atualizar informações de um Pokémon
* ❌ Deletar Pokémons da Pokédex
* 💾 Persistência de dados em arquivo `.json`
* 🕒 Registro de histórico de alterações (com data e mudanças)

---

## 🧠 Conceitos aplicados

* Funções em Python
* Estruturas de decisão (`if/else`)
* Estruturas de repetição (`while`, `for`)
* Manipulação de arquivos (`json`)
* Tratamento de exceções (`try/except`)
* Estruturas de dados (listas e dicionários)

---

## 🗂️ Estrutura dos dados

Cada Pokémon é armazenado no seguinte formato:

```json
{
    "nome": "Pikachu",
    "tipo": "Elétrico",
    "shiny": true,
    "historico": []
}
```

---

## ▶️ Como executar

1. Certifique-se de ter o Python instalado
2. Baixe ou clone o repositório
3. Execute o arquivo principal:

```bash
python main.py
```

---

## 💻 Comandos disponíveis

* `ABOUT` → Informações sobre o sistema
* `ADD` → Adicionar novos Pokémons
* `LIST` → Listar Pokémons cadastrados
* `UPDATE` → Atualizar dados de um Pokémon
* `DELETE` → Remover um Pokémon
* `QUIT` → Salvar e sair do sistema


---

## 📌 Observações

* Os dados são armazenados localmente em um arquivo `pokemons.json`
* Caso o arquivo não exista, ele será criado automaticamente
* O sistema trata erros básicos de entrada do usuário

---

## 👨‍💻 Autor

Projeto desenvolvido por Leonardo Zaparolli como parte dos estudos em programação e desenvolvimento com Python proposto pela faculdade PUCPR.
