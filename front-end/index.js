const btn = document.getElementById('req_btn')
const inputVal = document.getElementById('message_val')
btn.addEventListener('click', (e) => {
    e.preventDefault();
    console.log(inputVal.value);

    fetch('http://localhost:8000/detect_spam', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"text": inputVal.value})
    }).then(res => res.json())
    .then(data => console.log(data))
    .catch(error => {
        console.error('Error:', error);
    });

    inputVal.value = "";
})