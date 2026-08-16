# API de Blog (Django + DRF)

Projeto Django com Django REST Framework para gerenciar um blog (categorias, posts, comentários) e autenticação via JWT.

## Requisitos

- Python 3.10+ (ou conforme seu ambiente)
- Virtualenv/venv recomendado
- Dependências listadas em `requirements.txt` (instale com pip)

## Instalação (local)

1. Criar e ativar ambiente virtual:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Aplicar migrações e criar superusuário:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Rodar servidor de desenvolvimento:

```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

## Verificações úteis

- Validar configurações do Django:

```bash
python manage.py check
```

- Rodar testes:

```bash
python manage.py test
```

## Documentação da API

Este projeto inclui `drf-spectacular` para gerar esquema OpenAPI/Swagger.

- Configurações encontradas em `core/settings.py` (SPECTACULAR_SETTINGS).
- Para expor o schema e a UI Swagger/Redoc, adicione as rotas do `drf_spectacular.views` em `core/urls.py`. Exemplo mínimo:

```python
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # ... suas rotas
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
```

Depois disso, acesse `http://127.0.0.1:8000/api/docs/` para a UI do Swagger.

## Autenticação JWT

O projeto inclui `rest_framework_simplejwt`. Endpoints típicos:

- `POST /api/token/` — obter par de tokens (access/refresh)
- `POST /api/token/refresh/` — renovar token

(Verifique suas rotas em `blog/urls.py` ou onde tiver configurado os endpoints de auth.)

Exemplo de requisição para obter token:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"seu_usuario","password":"sua_senha"}' http://127.0.0.1:8000/api/token/
```

## Uploads e mídia

- `MEDIA_ROOT` e `MEDIA_URL` estão configurados em `core/settings.py`. Em dev, adicione `static()` em `core/urls.py` para servir mídia.

## Exemplos de Endpoints

As rotas principais estão em [blog/urls.py](blog/urls.py). Exemplo de endpoints expostos pelo `DefaultRouter` em `blog`:

- Autenticação / Tokens:
    - `POST /auth/register/` — registrar novo usuário
    - `POST /auth/login/` — obter `access`/`refresh` (alias para `/token/`)
    - `POST /token/` — obter tokens (access/refresh)
    - `POST /token/refresh/` — renovar token

- Recursos (ViewSets - CRUD):
    - `GET /categories/` — listar categorias
    - `POST /categories/` — criar categoria (autenticado/admin)
    - `GET /categories/{id}/` — recuperar categoria
    - `PUT/PATCH /categories/{id}/` — atualizar categoria
    - `DELETE /categories/{id}/` — remover categoria

    - `GET /posts/` — listar posts (suporta filtros: `?category=1`, `?search=termo`, `?ordering=-created_at`)
    - `POST /posts/` — criar post (autenticado)
    - `GET /posts/{id}/` — recuperar post
    - `PUT/PATCH /posts/{id}/` — atualizar post (autor/admin)
    - `DELETE /posts/{id}/` — excluir post (autor/admin)

    - `GET /comments/` — listar comentários
    - `POST /comments/` — criar comentário (autenticado)
    - `GET /comments/{id}/` — recuperar comentário
    - `PUT/PATCH /comments/{id}/` — atualizar comentário (autor)
    - `DELETE /comments/{id}/` — remover comentário (autor)

Exemplos `curl`:

Obter token:

```bash
curl -X POST -H "Content-Type: application/json" \
    -d '{"username":"seu_usuario","password":"sua_senha"}' \
    http://127.0.0.1:8000/token/
```

Usar token para criar um post (substitua `YOUR_ACCESS_TOKEN`):

```bash
curl -X POST http://127.0.0.1:8000/posts/ \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{"title":"Meu Post","content":"Conteúdo...","category":1,"published":true}'
```

Listar posts com filtro e ordenação:

```bash
curl "http://127.0.0.1:8000/posts/?category=1&search=Django&ordering=-created_at"
```

## Notas e boas práticas

- Mantenha `DEBUG=False` em produção e configure `ALLOWED_HOSTS` e variáveis secretas via variáveis de ambiente.
- Considere usar `django-environ` ou `python-decouple` para gerenciar variáveis sensíveis.

---
