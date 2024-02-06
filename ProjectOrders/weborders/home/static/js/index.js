var enumerable =[]
function Open(git) {
    const request = new XMLHttpRequest();
    request.open("GET", `/home/order/${git}`);
    request.setRequestHeader("Content-type", "application/json; charset=utf-8");
    request.onload = function () {
        if (request.status == 200) {
            enumerable = JSON.parse(request.response).orders;
            Render(git)
        }
    };
    request.send();
}

render = new Map();
function Render(git) {
    res = !render.has(git)
    if(!render.has(git)) {
        render.set(git, document.getElementById(`${git}`).innerHTML)
    value = document.getElementById(`${git}`).innerHTML
        for (let i = 0; i < enumerable.length; i++) {
            console.log(enumerable[i])
            document.getElementById(`${git}`).innerHTML += `<div"
            ${enumerable[i].delete == 1 ? 'class="order delete"' : ''}
            ${enumerable[i].correct == 1 ? 'class="order correct"' : 'class="order"'}
            >
            <div>${enumerable[i].git}</div>
            <div>${enumerable[i].dept}</div>
            <div>${enumerable[i].count}</div>
            <div>${enumerable[i].price}</div>
            <div>${enumerable[i].dateb}</div>
            <div>${enumerable[i].datef}</div>
            </div>`
        }
    }
    else {
        document.getElementById(`${git}`).innerHTML = render.get(git)
        render.delete(git)
    }
}