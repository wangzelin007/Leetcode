# 给你一个初始地址startUrl和一个 HTML 解析器接口HtmlParser，请你实现一个多线程的网页爬虫，用于获取与startUrl有相同主机名的所有链接。
# 以任意顺序返回爬虫获取的路径。
# 爬虫应该遵循：
# 从startUrl开始
# 调用HtmlParser.getUrls(url) 从指定网页路径获得的所有路径。
# 不要抓取相同的链接两次。
# 仅浏览与startUrl相同主机名的链接。
# 如上图所示，主机名是example.org。
# 简单起见，你可以假设所有链接都采用http 协议，并且没有指定端口号。
# 举个例子，链接http://leetcode.com/problems 和链接http://leetcode.com/contest 属于同一个主机名，
# 而http://example.org/test与http://example.com/abc 并不属于同一个主机名。
# HtmlParser 的接口定义如下：
# interface HtmlParser {
#     // Return a list of all urls from a webpage of given url.
#     // This is a blocking call, that means it will do HTTP request and return when this request is finished.
#     public List<String> getUrls(String url);
# }
# 注意一点，getUrls(String url)模拟执行一个HTTP的请求。
# 你可以将它当做一个阻塞式的方法，直到请求结束。
# getUrls(String url)保证会在15ms内返回所有的路径。
# 单线程的方案会超过时间限制，你能用多线程方案做的更好吗？
# 对于问题所需的功能，下面提供了两个例子。
# 为了方便自定义测试，你可以声明三个变量urls，edges和startUrl。
# 但要注意你只能在代码中访问startUrl，并不能直接访问urls和edges。
# 拓展问题：
# 假设我们要要抓取 10000 个节点和 10 亿个路径。
# 并且在每个节点部署相同的的软件。
# 软件可以发现所有的节点。
# 我们必须尽可能减少机器之间的通讯，并确保每个节点负载均衡。
# 你将如何设计这个网页爬虫？
# 如果有一个节点发生故障不工作该怎么办？
# 如何确认爬虫任务已经完成？
# 示例 1：
# 输入：
# urls = [
#     "http://news.yahoo.com",
#     "http://news.yahoo.com/news",
#     "http://news.yahoo.com/news/topics/",
#     "http://news.google.com",
#     "http://news.yahoo.com/us"
# ]
# edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
# startUrl = "http://news.yahoo.com/news/topics/"
# 输出：[
#     "http://news.yahoo.com",
#     "http://news.yahoo.com/news",
#     "http://news.yahoo.com/news/topics/",
#     "http://news.yahoo.com/us"
# ]
# 示例 2：
# 输入：
# urls = [
#     "http://news.yahoo.com",
#     "http://news.yahoo.com/news",
#     "http://news.yahoo.com/news/topics/",
#     "http://news.google.com"
# ]
# edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
# startUrl = "http://news.google.com"
# 输出：["http://news.google.com"]
# 解释：startUrl 链接与其他页面不共享一个主机名。
# 提示：
# 1 <= urls.length <= 1000
# 1 <= urls[i].length <= 300
# startUrl是urls中的一个。
# 主机名的长度必须为 1 到 63 个字符（包括点 . 在内），只能包含从 “a” 到 “z” 的 ASCII 字母和 “0” 到 “9” 的数字，以及中划线 “-”。
# 主机名开头和结尾不能是中划线 “-”。
# 参考资料：
# https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames
# 你可以假设路径都是不重复的。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/web-crawler-multithreaded
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from typing import List

# 通过 htmlParser.getUrls 获取所有的urls
# 只访问hostname 和 startUrl 匹配的urls
from threading import Lock, Thread
from collections import deque
class Solution1:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url: str) -> str:
            return url.split('//', 1)[1].split('/', 1)[0]

        def fetch(url: str) -> None:
            for url in htmlParser.getUrls(url):
                if get_hostname(url) == hostname:
                    with lock:
                        if url in visited:
                            continue
                        visited.add(url)
                    thread = Thread(target=fetch, args=(url,)) # todo ?
                    thread.start()
                    queue.append(thread)

        hostname = get_hostname(startUrl)
        lock = Lock()
        visited = {startUrl} # todo ?
        main_thread = Thread(target=fetch, args=(startUrl,))
        main_thread.start()
        queue = deque([main_thread])
        while queue:
            queue.popleft().join()
        return list(visited)

import threading
import queue
from urllib.parse import urlsplit
# https://yifei.me/note/818/
# 过程中并没有显式使用锁（queue 本身是线程安全的，带锁的）。
# 原因就在于，我们把对于需要并发访问的结构 set 限制在了一个线程中。
class Solution2:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain = urlsplit(startUrl).netloc
        requestQueue = queue.Queue()
        resultQueue = queue.Queue()
        requestQueue.put(startUrl)
        for _ in range(5):
            t = threading.Thread(target=self._crawl,
                                 args=(domain, htmlParser, requestQueue, resultQueue))
            t.daemon = True
            t.start()
        running = 1
        visited = set([startUrl])
        while running > 0:
            # 主线程:
            # 从 resultQueue 中读取一个访问的结果
            # 判断每个 URL 是否已经被访问过
            # 并分发到 requestQueue 中。
            urls = resultQueue.get()
            for url in urls:
                if url in visited:
                    continue
                visited.add(url)
                requestQueue.put(url)
                running += 1
            running -= 1
        return list(visited)

    def _crawl(self, domain, htmlParser, requestQueue, resultQueue):
        # 5个并发worker:
        # 从 requestQueue 中读取一个待访问的 url；
        # 执行一个很耗时的网络请求：htmlParser.getUrls；
        # 然后把获取到的新的 url 处理后放到 resultQueue 中。
        while True:
            url = requestQueue.get()
            urls = htmlParser.getUrls(url)
            newUrls = []
            for url in urls:
                u = urlsplit(url)
                if u.netloc == domain:
                    newUrls.append(url)
            resultQueue.put(newUrls)