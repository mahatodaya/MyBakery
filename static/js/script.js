function loginClicked() {

    // Jquery is used for gettinng login and signup model form
    $('#myModal').modal('show')     

}


// searching for users
const searchBox = document.querySelector('.search-box');
const searchBtn = document.querySelector('#search-btn');

searchBtn.addEventListener('click', (event) => {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/search');
    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    xhr.onload = () => {
        const data = JSON.parse(xhr.responseText);
        const table = document.querySelector('.user-table');
        let html = `<thead class="thead-dark">
        <tr>
            <th scope="col">I.D.</th>
            <th scope="col">Username</th>
            <th scope="col">Email Address</th>
            <th scope="col">First Name</th>
            <th scope="col">Last Name</th>
            <th scope="col">Action</th>
        </tr>
    </thead>`;
        for (d in data) {

            html += '<tbody>';
            html += '<tr>';
            html += `<td>${data[d].id}</td>`;
            html += `<td>${data[d].username}</td>`;
            html += `<td>${data[d].email}</td>`;
            html += `<td>${data[d].first_name}</td>`;
            html += `<td>${data[d].last_name}</td>`;
            html += `<td>
            <a href="/edit/${data[d].id}"><span class="btn btn-success">Edit</span></a>
            <a href="/delete/${data[d].id}"><span class="btn btn-danger">Delete</span></a>
            </td>`;
            html += '</tr>';
            html += '</tbody>';
        }

        table.innerHTML = html;

    }
    const data = new FormData();
    data.append('searchTerm', searchBox.value);
    xhr.send(data);
    return false;
});

// searching for products
const searchBox2 = document.querySelector('.search-box2');
const searchBtn2 = document.querySelector('#search-btn2');
searchBtn2.addEventListener('click', (event) => {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/searchproducts');
    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    xhr.onload = () => {
        const data = JSON.parse(xhr.responseText);
        const table = document.querySelector('.product-table');
        let html = `<thead class="thead-dark">
        <tr>
            <th scope="col">I.D.</th>
            <th scope="col">Image</th>
            <th scope="col">Name</th>
            <th scope="col">Price</th>
            <th scope="col">Action</th>
        </tr>
    </thead>`;

        for (d in data) {

            html += '<tbody>';
            html += '<tr>';
            html += `<td>${data[d].id}</td>`;
            html += `<td><img src="/media/${data[d].img}/" alt="" width="50px"></td>`;
            html += `<td>${data[d].name}</td>`;
            html += `<td>${data[d].price}</td>`;
            html += `<td>
                <a href="/products/update/${data[d].id}"><span class="btn btn-success">Edit</span></a>
                <a href="/products/delete/${data[d].id}"><span class="btn btn-danger">Delete</span></a>
            </td>`;
            html += '</tr>';
            html += '</tbody>';
        }

        table.innerHTML = html;

    }
    const data = new FormData();
    data.append('searchTerm', searchBox2.value);
    xhr.send(data);
    return false;
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
