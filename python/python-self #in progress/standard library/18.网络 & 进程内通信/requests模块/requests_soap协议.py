import requests
# 请求头中必须要有特殊Content-type


headers = {
            'Content-type': "text/xml; charset=UTF-8",  # 其他可以没有，必须有这一项
            'SOAPAction': "http://service.hzfc.comwscdSelectAqjdByCID",
        }
url = "https://wxapp.hzfc.cn/fgfw/axz/WS_ToZzcx/services/WS_ToZzcx"
params = f"""
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://service.hzfc.com">
                <soapenv:Header />
                <soapenv:Body>
                    <ser:wscdSelectAqjdByCID>
                        <arg0 />
                        <arg1>
                            <![CDATA[{self.name}]]>
                        </arg1>
                        <arg2>
                            <![CDATA[{self.idcard}]]>
                        </arg2>
                        <arg3>
                            <![CDATA[{self.phone}]]>
                        </arg3>
                        <arg4>
                            <![CDATA[10]]>
                        </arg4>
                        <arg5>
                            <![CDATA[<?xml version="1.0" encoding="GBK"?><CDUserList><Users><Name>{name}</Name><CID1>{idcard}</CID1></Users></CDUserList>]]>
                        </arg5>
                        <arg6>
                            <![CDATA[2]]>
                        </arg6>
                    </ser:wscdSelectAqjdByCID>
                </soapenv:Body>
            </soapenv:Envelope>
        """
resp = requests.post(url, data=params.encode(), headers=headers, verify=False)
ret = resp.content.decode()