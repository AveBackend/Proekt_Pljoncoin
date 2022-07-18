window.addEventListener('load', function (){
    let e = document.getElementById('popup');
    document.querySelector("body > section.section-main > header > ul > li.account > a.auth").addEventListener(
        'click',
        function (){
            e.classList.toggle('hide-popup');
        }
    );
    e.addEventListener(
        'click',
        function (event){
            if (!event.target.classList.contains('popup-bg') && !event.target.classList.contains('popup-parent')) return;
            e.classList.toggle('hide-popup', true);

        }
    );
});
