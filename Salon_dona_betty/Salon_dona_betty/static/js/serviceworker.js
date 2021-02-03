var staticCacheName = 'salon-pwa';
var filesToCache = ['/', 'home/', 'cortes/', 'quienessomos/'];

/*Método encargado de registrar el service worker,
además de crear cache bazar-pwa en donde se copia
el sitio raiz / */
self.addEventListener('install', function(event) {
    console.log('registrando en serviceworker');
    event.waitUntil(
        caches.open(staticCacheName).then(function(cache) {
            return cache.addAll(filesToCache);
        })
    );
});

/*Método encargado de verificar si se posee conexión
en caso de existir se va al servidor, en caso contrario se
utiliza la cache*/
/*self.addEventListener('fetch', function(event) {
    var requestUrl = new URL(event.request.url);
    event.respondWith(caches.match(event.request).then(function(response) {
        //Si la respuesta no esta definida se carga información
        //desde la cache
        if (response !== undefined) {
            console.log('respuesta no definida, cargado desde la cache ->  -> ' + event.request.url);
            return response;
        } else {
            //sección que es utilizada para clonar
            //en cache el modulo ingresado 
            //(se copian todos los recursos imagenes, css, js, html, etc.)            
            return fetch(event.request).then(function(response) {
                console.log('recurso clonado en cache ->' + event.request.url);
                let responseClone = response.clone();

                caches.open(staticCacheName).then(function(cache) {
                    cache.put(event.request, responseClone);
                });
                return response;
            }).catch(function() {
                //sección que es utilizada cuando hay error al clonar en la cache
                //se procede a buscar el recurso en la cache de existir               
                console.log('recurso cargado desde la cache -> ' + event.request.url);
                var requestUrl = new URL(event.request.url);
                return caches.match(requestUrl.pathname);
            });
        }
    }));
});*/