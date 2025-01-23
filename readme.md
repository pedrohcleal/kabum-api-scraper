# Kabum API Scraper

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![Requests](https://img.shields.io/badge/requests-FF4F00?style=flat&logo=requests&logoColor=white)
![Openpyxl](https://img.shields.io/badge/openpyxl-1C1C1C?style=flat&logo=openpyxl&logoColor=F8C200)

Este projeto realiza o scraping (coleta de dados) de produtos da categoria **Hardware** do site Kabum utilizando a API pública da empresa. As informações são extraídas em formato JSON e exportadas para um arquivo Excel.

## Funcionalidades

- **Coleta de dados de produtos de hardware**: Através de requisições para a API da Kabum, são coletadas informações como:

  - Nome do produto
  - Preço
  - Preço com desconto
  - Quantidade disponível
  - Avaliação de usuários
  - Garantia
  - Fotos

- **Exportação para Excel**: Os dados coletados são salvos em um arquivo Excel, com a possibilidade de adicionar mais categorias de produtos no futuro.

## Tecnologias Utilizadas

- Python
- Requests
- Openpyxl
- ThreadPoolExecutor

## Instalação

Clone este repositório e instale as dependências:

```bash
git clone https://github.com/pedrohcleal/kabum-api-scraper.git
cd kabum-api-scraper
pip install -r requirements.txt
```

## Como Usar

1. Execute o arquivo `main.py` para iniciar a coleta de dados e gerar o arquivo Excel:

```bash
python main.py
```

2. O arquivo `hardware_products.xlsx` será gerado com os produtos extraídos da API.

## Estrutura do Projeto

```
kabum-api-scraper/
├── main.py                # Script principal de coleta e exportação
├── requirements.txt       # Dependências do projeto
└── readme.md              # Documentação do projeto
```

## Contribuição

Sinta-se à vontade para contribuir com o projeto, criando novos recursos ou corrigindo problemas.

1. Faça um fork deste repositório.
1. Crie uma branch para a sua modificação (`git checkout -b feature/nova-modificacao`).
1. Faça commit das suas alterações (`git commit -am 'Adicionando nova funcionalidade'`).
1. Envie para o repositório remoto (`git push origin feature/nova-modificacao`).
1. Abra um pull request.
