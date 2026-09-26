import os
import subprocess
import sys

print("Definindo o layout do teclado como br-abnt2... \n loadkeys br-abnt2 \n")

subprocess.run(["loadkeys", "br-abnt2"])

print(
    "\nPegando a arquitetura do seu sistema... \nMentira, vou pegar lá nada. Se vira. Eu vou instalar assumindo que cê tá em UEFI 64 Bits :)\n"
)

print("Sincronizando teu relógio\n timedatectl set-timezone America/Sao_Paulo")

subprocess.run(["timedatectl", "set-timezone", "America/Sao_Paulo"])

print(
    "Iniciando sistema de particionamento...\nEscolha um dos drives a seguir pra particionar "
)

subprocess.run(["lsblk", "-d"])

disk_drive = input("Digite o nome do drive, ex: sda ")
disk_drive_path = "/dev/" + disk_drive

if not os.path.exists(disk_drive_path):
    print("Não encontrei nada disso em /dev/.\nEncerrando instalador.")
    quit()

print(
    "Agora você vai precisar de particionar sozinho. Eu não posso fazer isso por você, por que eu não sou adivinhador.\nSe você sair do fdisk eu vou assumir que você já terminou de particionar.\n fdisk /dev/"
    + disk_drive
)

subprocess.run(["fdisk", disk_drive_path])

print("\nEssas são as partições de " + disk_drive_path)

subprocess.run(["lsblk", disk_drive_path])

efi_name = input(
    "Agora digite o nome da partição que você vai escolher como EFI (/boot)"
)
root_name = input("Agora digite o nome da partição que você vai escolher como root (/)")

efi_path = "/dev/" + efi_name
root_path = "/dev/" + root_name

if not os.path.exists(efi_name) or not os.path.exists(root_name):
    print(
        "Uma ou mais partições não foram encontradas em /dev/.\nEncerrando instalador."
    )
    quit()

quer_formatar_efi = input(
    "Quer formatar a partição EFI? ("
    + efi_name
    + ") Isso é opcional, e SE CERTIFIQUE DE QUE É ESSA PARTIÇÃO MESMO E FORMATAR PODE GERAR PERCA DE DADOS. (S ou N): "
)
quer_formatar_root = input(
    "Quer formatar a partição ROOT? ("
    + root_name
    + ") Isso é definitivamente nescessário, e SE CERTIFIQUE DE QUE É ESSA PARTIÇÃO MESMO E FORMATAR PODE GERAR PERCA DE DADOS. (S ou N): "
)

if quer_formatar_efi.lower() == "s":
    subprocess.run(["mkfs.fat", "-F", "32", efi_path])

if quer_formatar_root.lower() == "s":
    subprocess.run(["mkfs.ext4", root_path])
else:
    print("Não posso prosseguir sem formatar a partição ROOT.")
    quit()

print("Agora vou montar a partição EFI e ROOT...")

subprocess.run(["mount", "--mkdir", efi_path, "/mnt/boot"])
subprocess.run(["mount", root_path, "/mnt"])
