window.addEventListener("resize", handleChange);

function handleChange() {
    let headerSpacerHeight = document.getElementsByTagName("header")[0].offsetHeight;
    document.getElementById("header-spacer").style.height = (headerSpacerHeight + "px");
}


$(document).ready(handleChange)


let store_cookie = window.localStorage;
if ('cookie_banner' in store_cookie) {
    document.getElementById('cookie-banner').classList.add('hide')
} else {
    let div = document.createElement('div');
    div.setAttribute('class', 'cookie-banner_inner');
    div.innerHTML = `
        <div class="row">
           <div class="col">
               <p>We use cookies to personalize content and analyze web traffic.</p>
               <p> Please click accept to continue using our website.</p>
           </div>
        </div>
        <div class="row col"><span class="btn btn-success" onclick="accept_cookie();">Accept</span></div>
    `;
    document.getElementById('cookie-banner').appendChild(div);
}

function accept_cookie() {
    localStorage.setItem('cookie_banner', '1');
    document.getElementById('cookie-banner').classList.add('hide')

}
