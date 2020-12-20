/*
  Update the bookmarklet. Check if it has already is loaded. Stupidly copied
   from a book and seems very dirty to me. `Date().GetTime()` is used to
   prevent the browser cache from being used.
*/

(function(){
    const BOOKMARKLET_URL = [
        'https://18ecb7a0c0e6.ngrok.io/static/images/js/bookmarklet.js?r=',
        `${new Date().getTime()}`
    ].join('');
    document.body.appendChild(document.createElement('script')
    ).src=BOOKMARKLET_URL;
})();
