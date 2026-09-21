AIOps Service Monitoring
About

This project is a simple AIOps simulation for a payment service.

It checks service data, finds abnormal values, creates an event, and passes it through a producer, topic and consumer.

Flow:

Data → Anomaly Detection → Event → Producer → Topic → Consumer → Output
Data

The data is stored in:

data/service_data.json

It contains:

Response time
CPU usage
Memory usage
Log level
Log message
Timestamp

Most records are normal.

The main abnormal records are at:

10:05 - Response time 610 ms and ERROR log
10:06 - Response time 640 ms, CPU 94%, memory 91% and ERROR log
Anomalies

The detector found 2 anomalies.

At 10:05:

High response time
Error log

At 10:06:

High response time
High CPU
High memory
Error log
Problems Fixed
The detector was checking WARNING instead of ERROR.
The producer and consumer were using different topics.

Both issues were fixed using the existing code structure.

Final Result

I ran:

python src/aiops_pipeline.py

Result:

Records processed: 10
Anomalies detected: 2
Events consumed: 2

The events successfully went from the producer to the topic and then to the consumer.

Testing

I ran:

python -m pytest

Result:

8 passed
Limitation

The detector uses fixed thresholds. Dynamic thresholds based on historical data could improve the detection.

Run
pip install -r requirements.txt
python src/aiops_pipeline.py
python -m pytest