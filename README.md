# MythGuardHD
硬件端代码, 通过web服务的方式控制继电器开关


#### 开发环境

- python version:2.7
- pip
- virtualenv
- flask
- gpio


#### api文档

**接口**```http://ip:port[default 5000]/guard/control/door?level={value}```

成功返回
```
{
  "json": {
    "code": 1, 
    "msg": "success", 
    "type": "open"
  }
}
```

```
{
  "json": {
    "code": 1, 
    "msg": "success", 
    "type": "close"
  }
}
```

失败返回
```
{
  "json": {
    "code": 0, 
    "msg": "failed", 
    "type": null
  }
}
```
