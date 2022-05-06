window.onload = main;

function close_window_wrapper()
{
    close_window('wrapper');
}
function close_window_wrapper_notificator()
{
    close_window('wrapper-notificator');
}

function notify(message)
{
    alert(message);
}

function ft_atoi(string)
{
    let num = '0';

    for (let i = 0; i < string.length; ++i)
    {
        if (string[i] == '0' && num.length == 1 && num == '0')
            continue;
        if (string[i] >= '0' && string[i] <= '9')
        {
            if (num.length == 1 && num == '0')
                num = string[i]
            else
                num += string[i];
        }
        else
            break;
    }
    return num;
}

function isURL(str) {
  let pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
  '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.?)+[a-z]{2,}|'+ // domain name
  '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
  '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
  '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
  '(\\#[-a-z\\d_]*)?$','i'); // fragment locator

  return pattern.test(str);
}

function init_current()
{
    //alert("base");
}

function main()
{
    set_standart_window_header(
        {
            'self': {
                'className': 'window-top',
                'id': 'window-top'
            },
            'title-container': {
                'className': 'window-title',
                'id': 'window-title'
            },
            'title-image': {
                'className': 'window-title-image',
                'id': 'window-title-image',
            },
            'title-text': {
                'className': 'window-title-text',
                'id': 'window-title-text'
            },
            'action-bar': {
                'className': 'window-action-bar',
                'id': 'window-action-bar',
                'buttons': [
                {
                    'button-name': 'close-wrapper',
                    'children_construct': [
                        {
                            'tag': 'img',
                            'attributes': {
                                'class': 'window-action-element-img',
                                'src':'/static/img/x.svg'
                            }
                        }
                    ],
                    'attributes': {
                        'onclick': 'close_window_wrapper()',
                        'class': 'window-action-element wae-',
                        'id': 'window-action-close'
                    }
                }
            ]
            }
        }
    );
    set_standart_window_btn_container(
        {
            'self': {
                'className': 'window-data',
                'id': 'window-data',
            },
            'button-container': {
                'className': 'window-data-action-container',
                'id': 'window-data-action-container'
            }
        }
    );
    init_current();
}