function removeParam(parameter)
{
    let url = document.location.href;
    let url_parts = url.split('?');

     if (url_parts.length>=2)
     {
          let urlBase = url_parts.shift();
          let queryString = url_parts.join("?");

          let prefix = encodeURIComponent(parameter) + '=';
          let pars = queryString.split(/[&;]/g);
          for (let i= pars.length; i-->0;)
              if (pars[i].lastIndexOf(prefix, 0)!==-1)
                  pars.splice(i, 1);
          if (pars.length==0) url = urlBase
          else url = urlBase + '?' + pars.join('&');
          window.history.pushState('',document.title,url);
    }
    return url;
}

function getParam(urlString, key)
{
    let paramString = urlString.split('?')[1];
    let queryString = new URLSearchParams(paramString);

    for (let pair of queryString.entries()) {
        if (pair[0] == key)
            return pair[1];
    }
    return null;
}
