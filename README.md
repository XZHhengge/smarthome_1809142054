# smarthome_1809142054
django project dir structure

[csdn博客解析](https://blog.csdn.net/qq_40965177/article/details/97296666)
```
├── C(C语言的client端)
├── db.sqlite3
├── hreatbeat_server.py
├── manage.py
├── remote_operation
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── udp_service(历史版本的智能家居项目)
│   │   ├── common
│   │   │   ├── __init__.py
│   │   │   └── __init__.pyc
│   │   ├── equipments（设备控制脚本）
│   │   │   ├── air_conditioner.py
│   │   │   ├── ceiling_fan.py
│   │   │   ├── controller.py
│   │   │   ├── device.py
│   │   │   ├── device.pyc
│   │   │   ├── equipment_manager.py
│   │   │   ├── equipment.py
│   │   │   ├── __init__.py
│   │   │   ├── light.py
│   │   │   └── __pycache__
│   │   ├── __init__.py
│   │   ├── setting.py
│   │   ├── udp_server.py（旧版本的智能家居main控制）
│   └── views.py
├── server.py（单独的测试脚本）
├── smarthome_1809142054
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── udp_cilent.py（单独的测试脚本）
```


