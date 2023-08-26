---

# SupportBot-ETL 🤖

O SupportBot-ETL é um projeto em Python que utiliza a engine OpenAI GPT-3.5-Turbo para automatizar a resolução de tickets de suporte. Ele processa tickets de suporte e gera soluções fictícias.

## Começando 💬

1. Clone o repositório para a sua máquina local.
   
3. Instale as dependências necessárias:
```bash
pip install pandas openai
```
5. Obtenha uma chave de API da OpenAI seguindo os passos abaixo:

> 1. Acesse o site da OpenAI em [https://platform.openai.com/signup/](https://platform.openai.com/signup/) e faça o seu cadastro.
> 2. Depois de criar uma conta, vá até seu perfil no canto superior direito.
> 3. Clique nele e selecione a opção "View API keys."
> 4. Crie sua API key a partir do botão "Create new secret key."
> 5. Copie a sua chave de API fornecida pela OpenAI.
> 6. No arquivo `main.py`, substitua `'sua-key-openai'` pela chave de API que você copiou.

## Uso ✔

1. Coloque o seu arquivo CSV de tickets de suporte com o nome `tickets_clientes.csv` no diretório `data/`.
2. Execute o script `main.py` para processar os tickets e gerar soluções.

## Configuração ⚙

- O script está configurado para processar um máximo de 3 tickets por execução. Você pode ajustar isso modificando a variável `max_changes`.
- A OpenAi limita a 3 usos por minuto.
- As respostas geradas estão limitadas a 150 caracteres.
- Os registros de alterações são armazenados no arquivo `output/log.txt`.

## Licença 📖

**Este projeto está licenciado sob a [Licença MIT](LICENSE).**

## Contato 📩

#### **_Para qualquer dúvida ou feedback, entre em contato:_**
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-000?style=for-the-badge&logo=linkedin&logoColor=30A3DC)](https://www.linkedin.com/in/kayqueambires/)
[![E-mail](https://img.shields.io/badge/-Email-000?style=for-the-badge&logo=microsoft-outlook&logoColor=E94D5F)](mailto:kayqueasilveira@gmail.com)

---
