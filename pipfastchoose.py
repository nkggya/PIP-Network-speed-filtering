import time
import typing
import requests



def select_fastest_url(urls:typing.List[str]):
    print("将测试一下网站：{}".format(','.join(urls)))
    fastest_time = 999
    fastest_url = urls[0]
    requests.packages.urllib3.disable_warnings()
    for url in urls:
        print("-------------开始测试：{}-----------------".format(url))
        total_time = 0
        domain = url[:url.replace("http://", '').replace("https://", "").rfind('/') + url.find('://') + 3]
        for i in range(4):
            pt = time.time()
            try:
                r = requests.get(domain, verify=False, proxies=None, timeout=90)
                if r.status_code == 200:
                    try_download_url = f"{domain}/packages/00/00/0188b746eefaea75d665b450c9165451a66aae541e5f73db4456eebc0289/loginhelper-0.0.5-py3-none-any.whl"
                    r2 = requests.get(try_download_url, verify=False, proxies=None, timeout=300)
                    if r2.status_code == 200:
                        use_time = time.time()-pt
                        print(f'get {domain} code: {r.status_code} time: {use_time}')
                    else:
                        total_time = 9999999999999.999999999
                        print(f'get {domain} error: 被风控/无法下载 code_1:{r.status_code} code_1:{r2.status_code} time: {total_time}')
                        break
                else:
                    use_time = time.time() - pt
                    print(f'get {domain} code: {r.status_code} time: {use_time}')
                if r.status_code > 210:
                    total_time += 4
                else:
                    total_time += use_time
            except Exception as e:
                print(f'get {domain} error: {e}')
                total_time += 4
        if total_time <= fastest_time:
            fastest_time = total_time
            fastest_url = url
    print(f'Fastest url: {fastest_url}; average cost {fastest_time/4}')
    return fastest_url

select_fastest_url(["https://pypi.org/simple", "http://pypi.tuna.tsinghua.edu.cn/simple", "http://mirrors.aliyun.com/pypi/simple","https://mirrors.bfsu.edu.cn/pypi/web/simple"])
input("Press Enter to exit...")