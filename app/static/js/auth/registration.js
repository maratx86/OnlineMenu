
window.onload = function ()
{
    let elems;

    elems = document.getElementsByClassName("auth-password-eye");
    for (let i = 0; i < elems.length; i++)
    {
        elems[i].onclick = function () {
            if (this.parentElement.children[0].type == 'text')
            {
                this.parentElement.children[0].type = 'password';
                this.children[0].src = '/static/img/eye-closed.svg';
            }
            else
            {
                this.parentElement.children[0].type = 'text';
                this.children[0].src = '/static/img/eye-opened.svg';
            }
        }
    }
    elems = document.getElementsByClassName('auth-container-data-input');
    for (let i = 0; i < elems.length; i++)
    {
        if (elems[i].type == 'email')
            elems[i].addEventListener('input', input_email_process);
        else if (elems[i].type == 'password')
            elems[i].addEventListener('input', input_password_process);
        else if (elems[i].name == 'username')
            elems[i].addEventListener('input', input_username_process);
        login.trySubmitButtonActivate();
    }
}
