# 🔥 Secure IIoT SCADA Motor Temperature Monitoring & Alert System

## 📌 Project Overview

This project demonstrates a **Secure Industrial Internet of Things (IIoT)** system for monitoring motor temperature using a **SCADA-based simulation**. The system continuously monitors temperature data using the Modbus protocol and generates an **email alert when the temperature exceeds 70°C**.

---

## 🎯 Objectives

* Monitor motor temperature using Modbus protocol
* Visualize real-time data using Node-RED dashboard
* Generate automatic email alerts when temperature exceeds threshold (70°C)
* Implement cybersecurity concepts in IIoT systems

---

## 🛠️ Technologies Used

* Node-RED
* Modbus TCP Server (Python)
* SCADA Demo Machine
* Gmail SMTP (Email Alert System)
* Kali Linux

---

## ⚙️ System Architecture

```
SCADA Motor → Modbus Server → Node-RED → Dashboard + Alert System → Email Notification
```

---

## 🔁 Working Principle

1. A Python-based Modbus server simulates motor temperature (20°C – 80°C)
2. Node-RED reads temperature using Modbus protocol
3. Data is processed and converted into numeric format
4. If temperature ≥ 70°C:

   * Email alert is triggered automatically
5. Dashboard displays real-time temperature values

---

## 🚨 Alert Logic

To avoid repeated alerts, a **state-based logic** is implemented:

* Email is sent **only once** when temperature crosses 70°C
* Prevents alert flooding/spamming

---

## 📊 Features

* ✅ Real-time temperature monitoring
* ✅ Automated email alert system
* ✅ Dashboard visualization (Gauge UI)
* ✅ Modbus protocol integration
* ✅ Smart alert logic (no repeated emails)
* ✅ Cybersecurity-aware implementation


---

## 🔐 Cybersecurity Implementation

* Secure SMTP authentication using Gmail App Password
* Threshold-based anomaly detection
* Controlled access to Node-RED environment
* Prevention of alert flooding using state logic

---

## 🚀 Future Scope

* Integration with real hardware (ESP8266 / ESP32)
* SMS / Telegram alerts
* Cloud integration (AWS / Azure IoT)
* AI-based predictive maintenance

---

iiot-scada-temperature-alert-system/
│
├── README.md
├── report/
│   └── iiot_scada_temperature_report.pdf
│
├── flows/
│   └── flows.json
│
├── modbus/
│   └── modbus_server.py
│
├── images/
│   ├── scada.png
│   ├── flow.png
│   ├── dashboard.png
│   ├── email.png
│   └── modbus.png

---

## 👨‍💻 Author

**Kiran Karenavar**

---

## 📌 Conclusion

This project successfully demonstrates a **secure IIoT-based SCADA monitoring system** capable of detecting abnormal temperature conditions and generating real-time alerts. It ensures improved safety, automation, and reliability in industrial environments.

---
