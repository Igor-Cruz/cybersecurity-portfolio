import json

# Função para carregar os dados do arquivo JSON
def carregar_usuarios(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        usuarios = json.load(arquivo)
    return usuarios

# Função que define as permissões ideais para cada papel
def permissoes_recomendadas(papel):
    if papel == "Administrator":
        return ["read", "write", "delete", "manage_users"]
    elif papel == "User":
        return ["read", "write"]
    elif papel == "Guest":
        return ["read"]
    else:
        return []

# Função para verificar se o usuário está com permissões a mais
def verificar_acessos(usuarios):
    for usuario in usuarios:
        recomendadas = permissoes_recomendadas(usuario["role"])
        excessos = [p for p in usuario["permissions"] if p not in recomendadas]

        print(f"\n🔍 Usuário: {usuario['username']}")
        print(f"🔑 Papel: {usuario['role']}")
        print(f"📄 Permissões atuais: {usuario['permissions']}")
        print(f"✅ Permissões ideais: {recomendadas}")

        if excessos:
            print(f"⚠️ Acesso excessivo detectado: {excessos}")
        else:
            print("✔️ Acesso dentro do padrão recomendado.")

# Execução do programa
usuarios = carregar_usuarios("sample_users.json")
verificar_acessos(usuarios)
