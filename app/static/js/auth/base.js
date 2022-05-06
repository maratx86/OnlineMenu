const error_labels = document.getElementsByClassName('auth-container-data-error');
const input_fields = document.getElementsByTagName('input');

function isEmailCorrect(string)
{
    const email_regex = /(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/;
    if (email_regex.exec(string))
        return true;
    return false;
}

function isPasswordNorm(string)
{
    const uld_string_regex = /((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{6,20})/;

    let res = uld_string_regex.exec(string);
    if (res)
        return true;
    return false;
}

function isUsernameNorm(string) {
    const regex = /^[a-zA-Z0-9_]{5,30}$/;
    if (regex.exec(string))
        return true;
    return false;
}

const login = {
    submitButtonActivate: function () {
        let submit_button;

        submit_button = document.getElementsByClassName('auth-button');
        for (let i = 0; i < submit_button.length; i++)
        {
            if (submit_button[i].type == "submit")
            {
                submit_button = submit_button[i];
                break;
            }
        }
        submit_button.removeAttribute('disabled');
    },
    submitButtonDisactivate: function () {
        let submit_button;

        submit_button = document.getElementsByClassName('auth-button');
        for (let i = 0; i < submit_button.length; i++)
        {
            if (submit_button[i].type == "submit")
            {
                submit_button = submit_button[i];
                break;
            }
        }
        submit_button.setAttribute('disabled', 'disabled');
    },
    trySubmitButtonActivate: function () {
        let errors = 0;
        for (let i = 0; i < error_labels.length; i++)
            if (error_labels[i].innerText.length)
                errors++;
        for (let i = 0; i < input_fields.length; i++)
            if (input_fields[i].value.length == 0)
                errors++;
        if (errors == 0)
            this.submitButtonActivate();
        else
            this.submitButtonDisactivate();
    }
};

function input_email_process() {
    let error = this.parentElement.children[1];
    let string;

    string = this.value.trim();
    this.value = string;
    if (string == "")
    {
        error.innerText = 'This field is required';
        return ;
    }
    if (this.type == 'email')
    {
        if (isEmailCorrect(string))
            error.innerText = "";
        else
            error.innerText = "Invalid email address";
        login.trySubmitButtonActivate();
        return ;
    }
    else if (this.type == 'password')
    {
        if (string.length < 8)
            error.innerText = "Notice - password has at least 8 length short";
        else if (!isPasswordNorm(string))
            error.innerText = "Notice - password should contains lowercase, uppercase, digit and special symbols";
        else
            error.innerText = "";
        login.trySubmitButtonActivate();
        return;
    }
    error.innetText = "";
}


function input_password_process() {
    let error = this.parentElement.children[1];
    let string;

    string = this.value.trim();
    this.value = string;
    if (string == "")
    {
        error.innerText = 'This field is required';
        return ;
    }
    if (string.length < 8)
        error.innerText = "Notice - password has at least 8 length short";
    else if (!isPasswordNorm(string))
        error.innerText = "Notice - password should contains lowercase, uppercase, digit and special symbols";
    else
        error.innerText = "";
    login.trySubmitButtonActivate();
}

function input_username_process()
{
    let error = this.parentElement.children[1];
    let string;

    string = this.value.trim();
    if (string.length == 0)
    {
        this.value = '';
        error.innerText = '';
        return;
    }
    if (string.length < 3)
        error.innerText = "Notice - username should has at least 3 symbols";
    else if (!isUsernameNorm(string))
        error.innerText = "Notice - username should contains ";
    else
        error.innerText = "";
    this.value = string;
    login.trySubmitButtonActivate();
}
