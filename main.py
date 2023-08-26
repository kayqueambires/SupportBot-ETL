from datetime import datetime
import pandas as pd
import openai

# Caminho para o arquivo CSV de entrada
input_csv = 'data/tickets_clientes.csv'

# Configuração da API da OpenAI
openai.api_key = 'sua-key-openai'

# Criando um arquivo de log
log_file = open('output/log.txt', 'a')

# Carregar os dados do arquivo CSV em um DataFrame
df = pd.read_csv(input_csv)

# Definindo o limite de alterações por execução
max_changes = 3

# Contador de alterações realizadas
changes_made = 0

# Loop para processar os tickets de 1 em 1
for index, row in df.iterrows():
    ticket_status = row['Ticket Status']

    # Verificação do status do ticket
    if ticket_status != 'Closed':
        ticket_description = row['Ticket Description']

        # Criando o prompt
        prompt = f" Faça uma solução fictícia para este problema: {ticket_description}\nSolução: (máximo 150 caracteres)"

        # Chamada para a API GPT-3.5-Turbo para gerar resposta
        generated_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100  # Ajuste conforme necessário
        ).choices[0].text.strip()

        # Atualização das colunas
        df.at[index, 'Resolution'] = generated_response
        df.at[index, 'Ticket Status'] = 'Closed'

        # Registro das alterações no log com horário
        log_entry = "{} - Ticket ID {}: Resposta gerada e status alterado para Closed\n".format(datetime.now().strftime('%d-%m-%y %H:%M:%S'),int(row['Ticket ID']))
        log_file.write(log_entry)

        # Atualizando o contador de alterações
        changes_made += 1

        # Verificando o limite de alterações
        if changes_made >= max_changes:
            break

# Salvando o DataFrame atualizado de volta no arquivo CSV
df.to_csv('data/tickets_clientes.csv', index=False)
print('Salvando arquivo e finalizando o programa.')

# Fechando o arquivo de log
log_file.close()
