# 🎵 Metrônomo PRO - Live Edition

Um metrônomo profissional moderno, responsivo e com suporte offline para músicos. Construído como uma Progressive Web App (PWA) com tecnologias web puras.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

## ✨ Características

### Funcionalidades Principais
- ⏱️ **Metrônomo Configurável** - Ajuste BPM de forma intuitiva
- 🎼 **Assinaturas de Tempo** - Suporte a diferentes time signatures (4/4, 3/4, 6/8, etc)
- 🔄 **Subdivisões** - Configure subdivisões de batida para maior precisão
- 📚 **Setlist Profissional** - Crie e gerencie listas de músicas com configurações personalizadas
- 🟢 **Indicador Visual** - Visualize as batidas em tempo real
- 🌙 **Tema Claro/Escuro** - Alternar entre temas para melhor conforto visual

### Características Técnicas
- 📱 **Responsivo** - Funciona perfeitamente em desktop, tablet e mobile
- 🔌 **Offline First** - Funciona completamente sem internet (PWA)
- 💾 **Persistência Local** - Todas as configurações são salvas no LocalStorage
- 🔊 **Web Audio API** - Som de alta qualidade gerado em tempo real
- 🚀 **Instalável** - Pode ser instalado como aplicativo nativo

## 🚀 Como Usar

### Acesso Online
Acesse diretamente em seu navegador (quando implementado em um servidor)

### Instalação como App
1. Abra a aplicação no navegador
2. Clique no ícone de instalação (endereço ou menu)
3. Selecione "Instalar"
4. O app será adicionado à sua tela inicial

### Modo Offline
Após a primeira visita, o app fica disponível offline graças ao Service Worker. Todos os dados são salvos localmente no seu dispositivo.

## 📖 Guia de Funcionalidades

### Metrônomo Básico
1. **BPM (Batidas por Minuto)** - Ajuste com os botões + e - ou digite diretamente
2. **Start/Stop** - Clique no botão central para iniciar/parar o metrônomo
3. **Signature** - Selecione o compasso (4/4, 3/4, 6/8, etc)
4. **Subdivision** - Configure quantas subdivisões por batida

### Gerenciador de Setlist
1. **Adicionar Música**
   - Preencha Nome, BPM, Assinatura e Subdivisão
   - Clique em "Adicionar à Lista"
   - A música é salva no seu dispositivo

2. **Carregar Música**
   - Clique em "PLAY" ao lado da música desejada
   - As configurações serão carregadas automaticamente
   - O metrônomo iniciará em seguida

3. **Excluir Música**
   - Clique no botão "X" para remover da lista
   - Confirme a exclusão

### Tema
- Clique no ícone de tema para alternar entre modo escuro e claro
- A preferência é salva automaticamente

## 🛠️ Estrutura do Projeto

```
metronomojs/
├── index.html          # Página principal (HTML, CSS e JS embutidos)
├── manifest.json       # Arquivo de configuração PWA
├── service-worker.js   # Arquivo para suporte offline
└── README.md          # Este arquivo
```

### Arquivos

#### `index.html`
- **HTML**: Estrutura da interface
- **CSS**: Estilos modernos com variáveis CSS e tema claro/escuro
- **JavaScript**: Toda a lógica da aplicação

#### `manifest.json`
Configuração da Progressive Web App:
- Nome e descrição
- Ícone da aplicação
- Cores do tema
- Modo de exibição standalone

#### `service-worker.js`
Implementa funcionalidade offline:
- Cache de arquivos na instalação
- Estratégia "cache first" com fallback para rede
- Funciona sem internete após primeira visita

## 💾 Armazenamento de Dados

Todos os dados são salvos no **LocalStorage** do navegador:
- Configurações do metrônomo
- Lista de músicas (setlist)
- Preferência de tema

**Dados salvos:**
```json
{
  "musics_v2": [
    {
      "name": "Música 1",
      "bpm": 120,
      "signature": "4/4",
      "subdivision": 1
    }
  ]
}
```

**Nota:** Limpar dados do navegador resultará na perda de todas as configurações salvas.

## 🎨 Customização

### Cores
As cores estão definidas como variáveis CSS. Para modificar:

```css
:root {
    --bg: #0a0a0a;           /* Fundo */
    --card: #161616;         /* Cards */
    --text: #ffffff;         /* Texto */
    --primary: #00ff95;      /* Cor primária (verde) */
    --secondary: #252525;    /* Cor secundária */
    --accent: #ff3e3e;       /* Cor de ênfase (vermelho) */
}
```

## 📱 Compatibilidade

| Navegador | Desktop | Mobile |
|-----------|---------|--------|
| Chrome    | ✅ Excelente | ✅ Excelente |
| Firefox   | ✅ Excelente | ✅ Excelente |
| Safari    | ✅ Bom | ✅ Bom |
| Edge      | ✅ Excelente | ✅ Excelente |

**Requisitos:**
- Web Audio API support
- Service Worker support (para offline)
- LocalStorage support

## 🔧 Desenvolvimento

### Instalação Local
1. Clone ou baixe o repositório
2. Abra `index.html` em um navegador local
3. Execute em um servidor web local (recomendado) para funcionalidade offline:

```bash
# Com Python 3
python -m http.server 8000

# Com Node.js
npx http-server
```

Então acesse `http://localhost:8000`

### Estrutura de Código

**Variáveis Principais:**
- `bpm` - Batidas por minuto atual
- `isPlaying` - Estado do metrônomo
- `audioContext` - Contexto da Web Audio API
- `activeMusicIndex` - Índice da música selecionada

**Funções Principais:**
- `toggleMetronome()` - Inicia/para o metrônomo
- `addMusic()` - Adiciona música à setlist
- `loadMusic(index)` - Carrega configurações de uma música
- `deleteMusic(index)` - Remove música da setlist
- `updateBeatIndicator()` - Atualiza indicador visual

## 🐛 Troubleshooting

### "Nenhum som saindo"
- Verifique se o volume do dispositivo está ativo
- Tente clicar na página para "descongelar" o áudio (requerimento de navegadores modernos)
- Verifique o console do desenvolvedor para erros

### "Dados não estão sendo salvos"
- Verifique se o LocalStorage está habilitado
- Tente limpar cache do navegador
- Alguns navegadores em modo incógnito podem não permitir LocalStorage

### "Service Worker não funciona"
- A aplicação deve estar em HTTPS para service workers persistentes
- Em desenvolvimento local (localhost), HTTP é permitido
- Verifique o Console > Application > Service Workers

## 📄 Licença

Projeto open source. Sinta-se livre para usar, modificar e distribuir.

## 👨‍💻 Autor

Desenvolvido por **Bruno Correia**

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação

---

**Versão:** 1.0  
**Última atualização:** Julho 2026  
**Status:** Em desenvolvimento ativo
