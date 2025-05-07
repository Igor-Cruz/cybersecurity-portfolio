# 🔐 IAM Policy Checker

🚀 Projeto introdutório em Python voltado para Cibersegurança, com foco em práticas de **Identity and Access Management (IAM)**.

---

## 🧠 Objetivo

Este script analisa as permissões dos usuários definidas em um arquivo JSON e identifica casos de **acesso excessivo** (overprivileged access), baseado em papéis como `Administrator`, `User` e `Guest`.

---

## 📂 Estrutura

policy-checker
- policy_checker.py
- sample_users.json
- README.md

  
---

## ▶️ Como executar

### ✅ Pré-requisitos
- Python instalado (recomendado: versão 3.8+)

### 🚀 Passos

1. Clone o repositório ou copie os arquivos para seu computador.
2. No terminal, execute:

```bash
python policy_checker.py

```

🧪 Exemplo de Saída

- 🔍 Usuário: user2
- 🔑 Papel: User
- 📄 Permissões atuais: ['read', 'write', 'delete']
- ✅ Permissões ideais: ['read', 'write']
- ⚠️ Acesso excessivo detectado: ['delete']


