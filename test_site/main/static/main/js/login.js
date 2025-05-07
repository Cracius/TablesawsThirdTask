document.getElementById('log-form').addEventListener('submit', async function (e)
{
    e.preventDefault();
    const { username, pass } = e.target;
    const response = await fetch('', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },

        body: JSON.stringify({
            username: username.value,
            password: pass.value
        })
    });

    const ans = await response.json();
    document.getElementById('error_log').innerText = ans.inf;
});

function getCookie(name)
{
    return document.cookie.split('; ').reduce((acc, cookie) => {
        const [key, value] = cookie.split('=');
        return key === name ? decodeURIComponent(value) : acc;
    }, null);
}