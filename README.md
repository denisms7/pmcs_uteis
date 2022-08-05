# Uteis
## 🚀 Pagina Web de atalhos e Informação 

Pagina web para auxilio dos servidores públicos do município de Centenário do Sul, tem por objetivo reunir todos caminhos de informação em apenas um local

## 📦 Configuração

### 📋 Pré-requisitos

Crie um ambiente virtual conforme o arquivo de [requerimentos](https://github.com/denisms7/pmcs_uteis/blob/main/requirements.txt)

### 🔧 Instalação

Após a configuração do ambiente virtual basta executar o arquivo app.py e a aplicação estará on-line no link: http://127.0.0.1 não sendo necessário informar a porta pois o mesmo está sendo disponibilizado na porta 80 do servidor, esta porta pode ser alterada na variável port= localizada ao final do arquivo app.py

Ambiente de produção:
````
if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=80, debug=False)
````

Ambiente de teste:
````
if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=80, debug=True)
````


## 📦 Desenvolvimento

Este e um projeto desenvolvido em Flask então para implementação da aplicação em produção recomendamos utilizar a documentação do próprio Flask: [Deploying to Production](https://flask.palletsprojects.com/en/2.1.x/deploying/)


## 🛠️ Construído com

* [Python](https://www.python.org) - Linguagem matriz utilizada
* [Pandas](https://pandas.pydata.org) - Usado para análise de dados
* [Flask](https://flask.palletsprojects.com/en/2.1.x/deploying/) - Framework Web
* [HTML5](https://www.w3c.br) - Linguagem de marcação 
* [Bootstrap](https://getbootstrap.com) - Framework CSS usado


## ✒️ Autores

* **Desenvolvedor** - *Denis Muniz Silva* - [Portfólio](https://denisms7.github.io/portifolio_dms) - [LinkedIn](https://www.linkedin.com/in/denisms/)


## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](https://github.com/denisms7/pmcs_uteis/blob/main/LICENSE) para detalhes.
