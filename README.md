# 渗透测试和CTF的工具合集
## Tools_G1ngerCat 目录结构和说明

### Tools_Dict - 字典  
+ [fuzzDicts](https://github.com/TheKingOfDuck/fuzzDicts): Web Pentesting Fuzz

### Tools_EXP - 漏洞exp  
+ [shiro_attack-2.2.jar](https://github.com/j1anFen/shiro_attack): shiro反序列化漏洞综合利用 v2.2
+ tomcat-cve_2020_1938
    + [CNVD-2020-10487-Tomcat-ajp-POC](https://github.com/nibiwodong/CNVD-2020-10487-Tomcat-ajp-POC): 
        >Usage: python3 poc.py -p 8009 -f "/WEB-INF/web.xml" 127.0.0.1
### Tools_Information_Gathering - 信息收集  
+ [dirsearch](https://github.com/maurosoria/dirsearch): 目录扫描工具
+ [GitHacker-1.0.0](https://github.com/WangYihang/GitHacker)
    >需要将 .git.bak 修改为 .git，否则会报错；  
    非最新版本，该版本是为了改代码方便;     
    dependency: pip install requests;  
    Usage: python2 GitHacker.py http://192.168.1.181/.git/
    
### Tools_WebShell - WebShell工具  
+ [Godzilla](https://github.com/BeichenDream/Godzilla): 哥斯拉
