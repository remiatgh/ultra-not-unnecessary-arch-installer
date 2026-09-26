import os
import subprocess

print("Definindo o layout do teclado como br-abnt2... \n loadkeys br-abnt2 \n")

subprocess.run(["loadkeys", "br-abnt2"])

print(
    "\nPegando a arquitetura do seu sistema usando \n cat /sys/firmware/efi/fw_platform_size \nMentira, vou pegar lá nada. Se vira. Eu vou instalar assumindo que cê tá em UEFI 64 Bits :)\n"
)

print("Sincronizando teu relógio\n timedatectl set-timezone America/Sao_Paulo")

subprocess.run(["timedatectl", "set-timezone", "America/Sao_Paulo"])

print(
    "Iniciando sistema de particionamento...\nEscolha um dos drives a seguir pra particionar "
)

subprocess.run(["lsblk", "-d"])

disk_drive = input("Digite o nome do drive, ex: sda")
disk_drive_path = "/dev/" + disk_drive

if not os.path.exists(disk_drive_path):
    print("Não encontrei nada disso aqui não viu...")

print(
    "Agora você vai precisar de particionar sozinho. Eu não posso fazer isso por você, por que eu não sou adivinhador.\nSe você sair do fdisk eu vou assumir que você já terminou de particionar.\n fdisk /dev/"
    + disk_drive
)

subprocess.run(["fdisk", disk_drive_path])

print("Agora digite o nome da partição que você vai escolher como EFI")

subprocess.run(["lsblk", disk_drive_path])
