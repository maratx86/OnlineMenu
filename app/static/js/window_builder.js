var standart_window = {
    'header': {
        //
    },
    'button-container': {
        //
    }
};
var saved_params = {

};

function get_header(data)
{

}

function set_standart_window_header(data)
{
    standart_window['header'] = data;
}
function set_standart_window_btn_container(data)
{
    standart_window['button-container'] = data;
}

function log(message)
{
    console.log(message);
}

function create_with_string_attributes(element_type, element_attributes)
{
    let elem = document.createElement('div');

    elem.innerHTML =
        "<" + element_type + " " + element_attributes + ">" +
        "</" + element_type + ">";
    return elem.children[0];
}

function create_with_attributes(element_type, element_attributes, string_attributes="")
{
    for (const key of Object.keys(element_attributes)) {
        if (typeof element_attributes[key] === 'string'
            || element_attributes[key] instanceof String)
            string_attributes += ' ' + key + '="' + element_attributes[key].replaceAll('\"', '\'') + '"';
        else
            string_attributes += ' ' + key + '="' + element_attributes[key] + '"';
    }
    return create_with_string_attributes(element_type, string_attributes);
}

function create_element(element_data){
    if (!('attributes' in element_data))
        element_data['attributes'] = {};
    if (!('string_attributes' in element_data))
        element_data['string_attributes'] = '';
    if (!('tag' in element_data))
        element_data['tag'] = 'div';

    let elem = create_with_attributes(
        element_data['tag'],
        element_data['attributes'],
        element_data['string_attributes']
    );
    if ('parent' in element_data)
        element_data['parent'].appendChild(elem);
    if ('id' in element_data)
        elem.id = element_data['id'];
    if ('type' in element_data)
        elem.type = element_data['type'];
    if ('className' in element_data)
        elem.className = element_data['className'];
    if ('disabled' in element_data)
        elem.disabled = element_data['disabled'];
    if ('value' in element_data)
        elem.value = element_data['value'];
    if ('innerText' in element_data)
        elem.innerText = element_data['innerText'];
    if ('innerHTML' in element_data)
        elem.innerHTML = element_data['innerHTML'];
    if ('children_construct' in element_data)
    {
        let ch_construct = element_data['children_construct'];
        for (let child_id = 0; child_id < ch_construct.length; ++child_id) {
            if ('parent' in element_data)
                ch_construct[child_id]['parent'] = elem;
            elem.appendChild(
                create_element(
                    ch_construct[child_id]
                )
            );
        }
    }
    if ('children' in element_data)
    {
        let ch = element_data['children'];
        for (let child_id = 0; child_id < ch.length; ++child_id) {
            elem.appendChild(
                ch[child_id]
            );
        }
    }

    return elem;
}

function create_window()
{
    let window;

    window = document.createElement('div');
    window.classList.add('window');

    return (window);
}

function put_window_into(container, window)
{
    container.children.clear();
    container.appendChild(window);
}

function close_window(wrapper_name = 'wrapper')
{
    let wrapper = document.getElementById(wrapper_name);

    if (wrapper)
    {
        wrapper.innerHTML = '';
    }
    wrapper.style.visibility = "hidden";
}

function  create_window_panel(window_header)
{
    let panel = document.createElement('div');
    let elements = [];
    let except_buttons = [];

    panel.classList.add(standart_window['header']['self']['className']);
    elements.push(document.createElement('div'));
    elements[0].classList.add(standart_window['header']['title-container']['className']);
    elements[0].id = standart_window['header']['title-container']['id'];
    elements.push(document.createElement('div'));
    elements[1].classList.add(standart_window['header']['title-image']['className']);
    elements[1].id = standart_window['header']['title-image']['id'];
    if ('image' in window_header)
        elements[1].innerHTML = '<img style="max-height: 100%; max-width: 100%" src="' + window_header['image'] + '"/>';
    elements.push(document.createElement('div'));
    elements[2].classList.add(standart_window['header']['title-text']['className']);
    elements[2].id = standart_window['header']['title-text']['id'];
    if ('text' in window_header)
        elements[2].innerText = window_header['text'];
    elements[0].appendChild(elements[1]);
    elements[0].appendChild(elements[2]);
    panel.appendChild(elements[0])
    elements.pop();elements.pop();elements.pop();

    elements.push(document.createElement('div'));
    elements[0].classList.add(standart_window['header']['action-bar']['className']);
    elements[0].id = standart_window['header']['action-bar']['id'];
    if ('except_buttons' in window_header)
        except_buttons = window_header['except_buttons'];
    if ('buttons' in window_header)
    {
        window_header['buttons'].forEach(function(btn_info, i, arr) {
            if (!('tag' in btn_info))
                btn_info['tag'] = 'div';
            elements[0].appendChild(
                create_element(btn_info)
            );
        });
    }
    if ('buttons' in standart_window['header']['action-bar'])
    {
        standart_window['header']['action-bar']['buttons'].forEach(function(btn_info, i, arr) {
            if ('button-name' in btn_info
                && except_buttons.indexOf(btn_info['button-name']) > -1)
                return ;
            if (!('tag' in btn_info))
                btn_info['tag'] = 'div';
            elements[0].appendChild(
                create_element(btn_info)
            );
        });
    }
    panel.appendChild(elements[0]);
    return panel;
}

function create_data_container(data_container_info)
{
    let container = create_element(data_container_info);
    return container;
}

function create_input_container(data)
{
    let container, elem_title, elem_input, elem_input_field, elem_error;

    if ('self' in data)
        container = create_element(data['self']);
    else
        container = document.createElement('div');

    elem_title = create_element(
        data['title']
    );

    elem_input = create_element(data['elem_input'])

    if (!('tag' in data['elem_input_field']))
        data['elem_input_field']['tag'] = 'input';
    elem_input_field = create_element(data['elem_input_field'])

    if ('elem_input_error' in data)
    {
        elem_error = create_element(data['elem_input_error'])
        elem_input.appendChild(elem_error);
    }
    elem_input.appendChild(elem_input_field);
    container.appendChild(elem_title);
    container.appendChild(elem_input);
    return container;
}


function create_button(button_data)
{
    let btn;
    let attributes = {};
    let string_attributes = "";

    if (!('onclick' in button_data))
        button_data['onclick'] = '';

    if (!('type' in button_data))
        button_data['type'] = 'button';
    if (!('tag' in button_data))
        button_data['tag'] = 'button';
    if ('disabled' in button_data)
        string_attributes += 'disable="' + button_data['disabled'] + '" ';
    if ('enable' in button_data)
        string_attributes += 'enable="' + button_data['enable'] + '" ';

    return create_element(
        {
            'tag': 'div',
            'children_construct': [
                {
                    'tag': button_data['tag'],
                    'innerHTML': button_data['value'],
                    'attributes': {
                        'id': button_data['id'],
                        'type': button_data['type'],
                        'class': button_data['className'],
                        'onclick': button_data['onclick']
                    },
                    'string_attributes': string_attributes
                }
            ]
        }
    );
    //
    btn = document.createElement('div');
    btn.innerHTML = '<button onclick="' + button_data['onclick']  +'">' + button_data['value'] + '</button>';
    btn = btn.children[0];

    btn.type = button_data['type'];
    btn.id = button_data['id'];
    btn.className = button_data['className'];
    btn.disabled = button_data['disabled'];
    return btn;
}

function create_button_container(buttons_data = [])
{
    let button_container, window_data;

    window_data = document.createElement('div');
    window_data.className = standart_window['button-container']['self']['className'];
    window_data.id = standart_window['button-container']['self']['id'];
    button_container = document.createElement('div');
    button_container.className = standart_window['button-container']['button-container']['className'];
    button_container.id = standart_window['button-container']['button-container']['id'];
    window_data.appendChild(button_container);

    buttons_data.forEach(function (item, i, arr)
    {
        button_container.appendChild(
            create_button(item)
        );
    });
    return window_data;
}

function create_window(window_panel, data_containers = [], buttons_data = [])
{
    let window = document.createElement('div');
    let current_element;

    window.classList.add('window');

    current_element = create_window_panel(window_panel);
    window.appendChild(current_element);
    // window-content creating
    current_element = document.createElement('div');
    current_element.className = 'window-content';
    window.appendChild(current_element);
    data_containers.forEach(function (item, index, arr){
        current_element.appendChild(
            create_data_container(item)
        );
    });
    // window-data
    current_element.appendChild(
        create_button_container(buttons_data)
    );
    return window;
}

function open_on_wrapper(wrapper_id, window_header, data_containers, buttons_data)
{
    let wrapper = document.getElementById(wrapper_id);

    if (!wrapper)
    {
        log('Wrapper { id: ' + wrapper_id + ' } not found');
        return;
    }
    wrapper.innerHTML = '';
    wrapper.style.visibility = "visible";

    let window = create_window(window_header, data_containers, buttons_data);
    wrapper.appendChild(window);
    return wrapper;
}
