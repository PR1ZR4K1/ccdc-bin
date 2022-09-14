a = {
    "host-69": {
      "ip": "192.168.1.69",
      "OS": "Linux",
      "services": [
        { "port": 80, "service": "http" },
        { "port": 8008, "service": "http" },
        { "port": 8009, "service": "ajp13" },
        { "port": 8443, "service": "https-alt" }
      ],
      "isOn": True
    },
    "host-86": {
      "ip": "192.168.1.86",
      "OS": "Linux",
      "services": [{ "port": 49154, "service": "unknown" }],
      "isOn": True
    }
}

print(dict(a.items()))
