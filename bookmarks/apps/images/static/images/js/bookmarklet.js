(function(){
  const JQUERY_VERSION = '3.5.1';
  const SITE_URL = 'https://18ecb7a0c0e6.ngrok.io/';
  const STATIC_URL = `${SITE_URL}static/images/`;
  // Minimal image size for add to bookmarklet.
  const MIN_WIDTH = 100;
  const MIN_HEIGHT = 100;
  const JQUERY_TIMEOUT_ATTEMPTS = 250;

  function bookmarklet(msg) {
    // Loading CSS styles (`bookmarklet.css`). `new Date().getTime()` returns
    // an integer to prevent caching bookmarklet by the browser for loading it
    // on change.
    let css = jQuery('<link>');
    css.attr({
      rel: 'stylesheet',
      type: 'text/css',
      href: `${STATIC_URL}css/bookmarklet.css?r=${new Date().getTime()}`
    });
    jQuery('head').append(css);

    // Load HTML
    const BOX_HTML = [
        '<div id="bookmarklet"><a href="#" id="close">&times;</a>',
        '<h1>Select an image to bookmark:</h1><div class="images"></div></div>'
    ].join('');

    // Add all finded images from a third-party site to its `<body>`.
    jQuery('body').append(BOX_HTML);

    // An event that removes the injected code. Use the selector
    // `#bookmarklet # close` to find an element with id` close` and parent
    // with id `bookmarklet`.
    // Details: https: //api.jquery.com/category/selectors
    jQuery('#bookmarklet #close').click(function(){
      jQuery('#bookmarklet').remove();
    });

    // Find images and display them. Use `jQuery.each` to iterate over them.
    jQuery.each(jQuery('img'), (index, image) => {
      if (jQuery(image).width() >= MIN_WIDTH
          && jQuery(image).height() >= MIN_HEIGHT)
      {
        const IMAGE_URL = jQuery(image).attr('src');
        let regex = new RegExp("(.*)\.(jpg|jpeg|png|gif)$");
        if (regex.test(IMAGE_URL)) {
          jQuery('#bookmarklet .images').append(
            `<a class="item" href="#"><img src="${IMAGE_URL}"></a>`
          );
        }
      }
    });

    // When an image is selected open URL with it.
    jQuery('#bookmarklet .images a').click(function(e){
      const SELECTED_IMAGE = jQuery(this).children('img').attr('src');

      // Hide bookmarklet.
      jQuery('#bookmarklet').hide();

      // Open new window to submit the image.
      const URL = [
        SITE_URL,
        'images/create/?url=',
        encodeURIComponent(SELECTED_IMAGE),
        '&title=',
        encodeURIComponent(jQuery('title').text()),
        '_blank'
      ].join('');

      window.open(URL);
    });
  }

  // If `JQuery` has not loaded yet - loads it. If the library is already
  // connected - run `bookmarklet()`.

  // Check if jQuery is loaded.
  if(typeof window.jQuery != 'undefined') {
    bookmarklet();
  } else {
    // Create the script and point to Google API.
    let script = document.createElement('script');
    const JQUERY_URL = [
      `http://ajax.googleapis.com/ajax/libs/jquery/${JQUERY_VERSION}`,
      '/jquery.min.js'
    ].join('');
    script.setAttribute('src', JQUERY_URL);
    // Add the script to the `<head>` for processing.
    document.getElementsByTagName('head')[0].appendChild(script);
    // Add the ability to use multiple JQuery load attempts.
    let attempts = 15;
    (function(){
      // Check again if jQuery is undefined.
      if(typeof window.jQuery == 'undefined') {
        if(--attempts > 0) {
          // Calls himself in a few milliseconds.
          // if not loaded - try again.
          window.setTimeout(arguments.callee, JQUERY_TIMEOUT_ATTEMPTS);
        } else {
          // Too many attempts to load, send error.
          console.log('An error ocurred while loading jQuery');
        }
      } else {
          bookmarklet();
      }
    })();
  }
})();
