let $body = $(document.body);
let scrollPosition = 0;

function disable_scroll() {
    var oldWidth = $body.innerWidth();
    scrollPosition = window.pageYOffset;
    $body.css('overflow', 'hidden');
    $body.css('position', 'fixed');
    $body.css('top', `-${scrollPosition}px`);
    $body.width(oldWidth);
    return;
}

(function(){
    // disable_scroll();
    console.log("Hello Ken's debug template.");
})();