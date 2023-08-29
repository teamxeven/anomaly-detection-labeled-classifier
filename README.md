# Anomaly-Detection-Labeled-Classifier
### Description
- Let us assume that, we have a company called "Xeven Spam Detector", and you are a newly joined Machine Learning Engineer at our company. So, the below thing describes our company and the task in hand.
- Currently we at "Xeven Spam Detector", help retailers with pricing intelligence and business monitoring.
- One of our main challenges comprise of monitoring and analyzing our client's business metrics in real time for instant detection of the incidents that may impact their revenue.
- One subpart of this challenge is Anomaly Detection which generates alerts on our client's business metrics.
- The Problem Statement presented below highlights the problem which we are tackling right now
### Column Description
The description of the column are as follows:

timestamp [ float ] : is provided as a Unix epoch in seconds.

value [ int ] : is a real value measurement of some metric at the timestamp.

is_anomaly [ boolean ] : is a boolean value which is True if the corresponding value is identified as an anomaly.

predicted [ float ] : is a real value prediction coming from a black box forecasting model for that timestamp. This black box forecasting model is assumed to be aware of only the true data distribution.
