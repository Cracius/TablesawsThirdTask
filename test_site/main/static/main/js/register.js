document.getElementById('reg-form').addEventListener('submit', async function (e)
{
    e.preventDefault();
    const { username, pass, gender } = e.target;
    const response = await fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },

        body: JSON.stringify({
            username: username.value,
            password: pass.value,
            gender: gender.value === 'Male'
        })
    });

    const { status, inf } = await response.json();
    switch (status)
    {
        case 'ok':
            window.location.href = inf;
            break;

        case 'err':
            document.getElementById('error_reg').innerText = inf;
    }
});

function getCookie(name)
{
    return document.cookie.split('; ').reduce((acc, cookie) => {
        const [key, value] = cookie.split('=');
        return key === name ? decodeURIComponent(value) : acc;
    }, null);
}