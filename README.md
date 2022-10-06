# DevPro Django Queryset

## Instalação

### Criação do ambiente virtual

```
python -m venv .venv
```

### Ativar ambiente virtual

```
source .venv/bin/activate
```

### Instalação de dependências

```
pip install -r requirements.txt
```

### Criar container com banco populado

```
docker compose up -d
```

### Aplicar migrações

```
python manage.py migrate
```

### Iniciar aplicação Django

```
python manage.py runserver
```