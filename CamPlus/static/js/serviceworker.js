var staticCacheName = 'CamPlus';
var filesToCache = [
  '/',
  '/index',
  'signup',
  '/static/js/popper.js',
  'mess/menu',
  'lecture/timetable',
  'trans/bus'
]

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll(filesToCache);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '')) {
        event.respondWith(caches.match(filesToCache));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});
