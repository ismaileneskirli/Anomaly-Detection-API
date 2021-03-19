# Anomaly-Detection-API
This is a super simle anomaly detection api, developped with  median absolute deviation. For the moment this repository is not finished and probably will not work properly when you try it, please dont waste time on it :)

## Installation

If you don't have flask installed in your machine firstly follow this link :
https://flask.palletsprojects.com/en/1.1.x/installation/

Then you need to install flask restful :
pip install flask-restfull

If it is the first time you run an api and never opened internet explorer, you may get an error like this :
Invoke-WebRequest : The response content cannot be parsed because the Internet Explorer engine is not available, or Internet Explorer's first-launch configuration is not complete. Specify the UseBasicParsing parameter and try again.At line:1 char:1

All you need to do is open internet explorer and select recommend and enter.

Once you have installed venv, when you want to activate it later on navigate to the project folder and type ./venv/Scripts/activate in terminal.

## Anomaly Detection (MAD)

https://towardsdatascience.com/crazy-simple-anomaly-detection-for-customer-success-458e94d4d516

The median absolute deviation or MAD. The MAD is defined as being the median of the absolute value of the residuals between each observation and the median:


```
MAD = median(|Xi - avg(X)|)
```
### Advantage of MAD

In comparison to the standard deviation it's advantage is robustness. Both the mean and the standard deviation are highly influenced by
outliers therefore they are bad for detecting anomalies and may give false alerts.



## Current usage of the api

docker build -t your_docker_image_name -f Dockerfile .
docker run -d -p 5000:8008 your_docker_image_name

now api works in port 5000.
run python client.py to test it.