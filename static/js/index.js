"use strict"

function changeCheck(cb) {
    if(cb.checked == true) {
        console.log(cb.parentNode);
        console.log(cb.parentNode.parentNode);
        cb.parentNode.parentNode.className = "ball selected";
    }else {
        cb.parentNode.parentNode.className = "ball";
    }
}
