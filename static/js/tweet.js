const togle = document.querySelectorAll('#menu');
let x = 0;
for (let i = 0; i < togle.length; i++){
    togle[i].addEventListener('click', function () {
    if (x == 0) {
        togle[i].nextElementSibling.style.display = 'block';
        x += 1;
    }
    else if (x == 1) {
        togle[i].nextElementSibling.style.display = 'none';
        x = 0;
    }
})
}

