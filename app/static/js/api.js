
var url_api = '';
var source_path = {
    'create_enterprise':      '/api/create/enterprise',
    'create_product':         '/api/create/product',
    'create_item':            '/api/create/item',
    'create_order':           '/api/create/order',
    'create_order_product':   '/api/create/order_product',

    'edit_enterprise':      '/api/edit/enterprise',
    'edit_product':         '/api/edit/product',
    'edit_product_item':    '/api/edit/product_item',
    'edit_order_product':   '/api/edit/order_product',
    'edit_item':            '/api/edit/item',
    'edit_order':            '/api/edit/order',

    'get_enterprise':        '/api/get/enterprise',
    'get_product':           '/api/get/product',
    'get_product_item':      '/api/get/product_item',
    'get_item':              '/api/get/item',
    'get_order':              '/api/get/order',

    'del_enterprise':        '/api/del/enterprise',
    'del_product':           '/api/del/product',
    'del_product_item':      '/api/del/product_item',
    'del_item':              '/api/del/item',
    'del_order':             '/api/del/order',

    'get_enterprises':       '/api/get/enterprises',
    'get_products':          '/api/get/products',
    'get_items':             '/api/get/items',
    'get_orders':            '/api/get/orders',
};

function Get(url){
    let Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("GET",url,false);
    Httpreq.send(null);
    return Httpreq.responseText;
}

function Post(url){
    let Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open("POST",url,false);
    Httpreq.send(null);
    return Httpreq.responseText;
}

function ParamsToString(params={})
{
    let string_params = '';

    for (let key in params) {
        string_params += key;
        if (params.hasOwnProperty(key)) {
            string_params += '=' + encodeURIComponent(params[key]);
        }
        string_params += '&'
    }
    return string_params;
}

function GetWithParams(url, params = {})
{
    return JSON.parse(Get(
        url + '?' + ParamsToString(params)
    ));
}

function PostWithParams(url, params = {})
{
    let result = Get(
        url + '?' + ParamsToString(params)
    );
    return JSON.parse(result);
}

function getUrl(operation_name)
{
    let url = url_api + source_path[operation_name];
    return url;
}
