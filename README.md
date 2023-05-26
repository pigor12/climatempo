# API Meteorológica

Esta é uma API simples que fornece informações meteorológicas atuais e previsões do tempo para diferentes cidades usando a API OpenWeatherMap.

## Requisitos

- Python 3.6+
- Flask
- Requests

## Instalação

1. Clone este repositório.
2. Instale as dependências necessárias com o seguinte comando: `pip install flask requests`.
3. Substitua a variável `OPEN_WEATHER_MAP_API_KEY` no arquivo `ow.py` pela sua chave de API do OpenWeatherMap.

## Uso

1. Execute o servidor com o comando: `python ow.py`.
2. Faça uma solicitação GET para `http://localhost:5000/weather`, passando o nome da cidade e do país como parâmetros de consulta.
3. A API retornará as informações meteorológicas atuais e a previsão do tempo para essa cidade.

Por exemplo, para obter as informações meteorológicas para São Paulo, Brasil, faça uma solicitação para `http://localhost:5000/weather?city=Sao%20Paulo&country=br`.

Por padrão, se você não passar nenhum parâmetro de cidade ou país, a API retornará as informações meteorológicas para Belo Horizonte, Brasil.

## Contribuindo

Contribuições são sempre bem-vindas! Por favor, consulte a página de "Issues" para ver os recursos e correções de bugs que precisam ser implementados.

## Licença

Este projeto está sob a licença [GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). Veja o arquivo `LICENSE` para mais detalhes.
