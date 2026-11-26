// Guarda o app no celular para funcionar sem internet.
// Ao publicar uma versão nova, troque o número abaixo (v4 -> v5).
const CACHE = 'caderneta-v6';
const ARQUIVOS = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png'];

// Guarda cada arquivo separadamente: se um faltar, os outros continuam funcionando.
self.addEventListener('install', e => e.waitUntil(
  caches.open(CACHE).then(c => Promise.all(ARQUIVOS.map(a => c.add(a).catch(() => null)))).then(() => self.skipWaiting())
));
self.addEventListener('activate', e => e.waitUntil(
  caches.keys().then(k => Promise.all(k.filter(x => x !== CACHE).map(x => caches.delete(x)))).then(() => self.clients.claim())
));
// Tenta a internet primeiro; sem conexão, usa o que está guardado.
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    fetch(e.request)
      .then(r => { const cp = r.clone(); caches.open(CACHE).then(c => c.put(e.request, cp)); return r; })
      .catch(() => caches.match(e.request).then(r => r || caches.match('./index.html')))
  );
});
