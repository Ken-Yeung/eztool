let urls = {
    "android": "https://play.google.com/store/apps/details?id=com.utaxi.user",
    "ios": "https://apps.apple.com/hk/app/u-taxi-hk/id1607638417",
    "home": "https://utaxihk.org"
};

let main = ()=>{
    const typpo = new URLSearchParams(window.location.search).get('store');

    if (typpo == "android" || typpo == "ios"){
        
        setTimeout(()=>{
            window.location.replace(urls[typpo]);
        }, 333);

    } else {
        setTimeout(()=>{
            window.location.replace(urls['home']);
        }, 333);
    }
};

(function(){
    // console.log("Hello Ken's debug template.");
    main();
})();