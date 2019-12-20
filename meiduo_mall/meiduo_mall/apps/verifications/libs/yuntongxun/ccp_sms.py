# -*- coding:utf-8 -*-

# import ssl
# ssl._create_default_https_context =ssl._create_stdlib_context # 解决Mac开发环境下，网络错误的问题

from verifications.libs.yuntongxun.CCPRestSDK import REST

# 说明：主账号，登陆云通讯网站后，可在"控制台-应用"中看到开发者主账号ACCOUNT SID
_accountSid = '8a216da86f17653b016f22a469ef0a2e'

# 说明：主账号Token，登陆云通讯网站后，可在控制台-应用中看到开发者主账号AUTH TOKEN
_accountToken = '2c62ee0981b049f3b742c56d53720265'

# 请使用管理控制台首页的APPID或自己创建应用的APPID
_appId = '8a216da86f17653b016f22b673ce0a47'

# 说明：请求地址，生产环境配置成app.cloopen.com
_serverIP = 'sandboxapp.cloopen.com'

# 说明：请求端口 ，生产环境为8883
_serverPort = "8883"

# 说明：REST API版本号保持不变
_softVersion = '2013-12-26'

# 云通讯官方提供的发送短信代码实例
# 发送模板短信
# @param to 手机号码
# @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
# @param $tempId 模板Id
# def sendTemplateSMS(to, datas, tempId):
#     # 初始化REST SDK
#     rest = REST(_serverIP, _serverPort, _softVersion)
#     rest.setAccount(_accountSid, _accountToken)
#     rest.setAppId(_appId)
#
#     result = rest.sendTemplateSMS(to, datas, tempId)
#     print(result)

class CCP(object):
    """发送短信的单例类"""
    def __new__(cls, *args, **kwargs):
        """判断是否存在类属性_instance"""
        if not hasattr(CCP, "_instance"):
            cls._instance = super(CCP, cls).__new__(cls, *args, **kwargs)

            rest = REST(_serverIP, _serverPort, _softVersion)
            cls._instance.rest = rest  # rest可以连写(cls._instance_rest = REST(_serverIP, _serverPort, _softVersion))，将REST与_instance绑定在一起

            cls._instance.rest.setAccount(_accountSid, _accountToken)
            cls._instance.rest.setAppId(_appId)
        return cls._instance

    def send_template_sms(self, to, datas, temp_id):
        """
        发送模板短信单列方法
        :param to: 注册手机号
        :param datas: 模板短信内容数据，格式是列表格式
        :param temp_id: 模板编号
        :return: 发送短信结果
        """
        result = self.rest.sendTemplateSMS(to, datas, temp_id)
        print(result)
        if result.get("statusCode") == "000000":
            return 0  # 0表示发送成功
        else:
            return -1  # -1表示发送失败


if __name__ == '__main__':
    # 注意： 测试的短信模板编号为1
    res = CCP()  # 类创建对象可以连写（CCP().send_template_sms('13667982328', ['123456', 5], 1)）
    res.send_template_sms('13667982328', ['123456', 5], 1)
