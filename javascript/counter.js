if(!localStorage.getItem('counter')){
    localStorage.setItem('counter', 0)
}

let count = function () {
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').textContent = counter;
    localStorage.setItem('counter', counter)
    // if (counter % 10 === 0) {
    //     alert(`Count is now: ${counter}`);
    // }
}
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('button').onclick = count;
    document.querySelector('h1').textContent = localStorage.getItem('counter');
    // document.querySelector('button').addEventListener('click', count);
    setInterval(count, 1000)
});

