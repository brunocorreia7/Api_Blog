const CACHE_NAME = 'metronomo-cache-v1';
const ASSETS = [
  './',
  './index.html',
  './manifest.json'
];

// Instalação: Salva os arquivos no cache do navegador
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS);
    })
  );
});

// Ativação: Limpa caches antigos se você atualizar o app
self.addEventListener('activate', (event) => {
  console.log('Service Worker ativo!');
});

// Busca: Tenta pegar do cache primeiro; se não tiver (e tiver rede), busca na web
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});