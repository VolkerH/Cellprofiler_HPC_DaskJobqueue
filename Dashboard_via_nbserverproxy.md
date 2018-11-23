## Dask Dashboard via nbserverproxy

Dask Dashboard is a GUI that allows you to monitor the progress of your workers in the browser.
Dask starts a web server on a specific port number and you need to paste the URL into a web browser.
As the the compute note is not visible from your local network, you would normally have to set up a ssh tunnel to connect to the dashboard, similar to the tunnel we set up for accessing Jupyter. 

However, if you register the jupyter notebook extension nbserverproxy (as outlined below) you don't need to 
set up another tunnel. You can use the Jupyter notebook server as a proxy. What you will have to do is to look
at the URL that you are running Jupyter notbeook in. It will look something like

`https://localhost:9497/notebooks/...`

Dask might tell you the dashboard is at:
`https://some.ip.address:8787/status`
note that the port number might be different from `8787`.


Now if you point your local browser to the URL:
`https:localhost:9497/proxy/8787/status` 
you should be able to see the Dask Dashboard on your local browser.

The general recipe is
`Base URL of your tunnel to jupyter` + `/proxy/` + Port number of dashboard + `/` + URL file location

port number is different from the Jupyter notebook server this would normally have to set up


# Installing nbserverproxy

To install and register nbserverproxy activate your python enviroment on a cluster node and  execute:
```
pip install nbserverproxy
jupyter serverextension enable --py nbserverproxy
```
