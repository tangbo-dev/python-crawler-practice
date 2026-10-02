# Python Crawler Practice & Data Processing

本仓库用于记录我在学习 Python 爬虫、数据处理及 AI 辅助编程（Vibe Coding）过程中的实战练习代码。包含从基础数据抓取到高级并发、多进程架构设计的完整学习路径。

## 📁 包含的练习项目：

### 一、 基础爬虫与数据处理 (Basic Crawler & Data Processing)
1. **电影票房数据抓取 (Movies Box Office)**
   - 文件：`01 电影票房提取练习.py` / `02_抓取电影票房.py`
   - 说明：使用 Requests + BeautifulSoup / lxml 抓取实时票房数据，并清洗导出为 CSV 格式。
   - 涉及技能：HTTP 请求、HTML 解析、Pandas 数据清洗。

2. **新华书店/当当网图书数据抓取 (Book Store Data)**
   - 文件：`03_新华书店.py` / `03_当当网.py`
   - 说明：针对电商网站进行列表页抓取，提取书名、价格、评论数等字段。
   - 涉及技能：多页面循环抓取、异常处理。

3. **雪球/冶金金融数据爬取 (Financial Data)**
   - 文件：`05_雪球.py` / `04_冶金数据.py`
   - 说明：抓取特定金融接口（API）的数据并结构化输出。
   - 涉及技能：JSON 数据解析、接口参数构造。

### 二、 进阶并发与多进程架构 (Advanced Concurrency & Multiprocessing)
1. **线程池实战案例 (ThreadPoolExecutor Case)**
   - 文件：`01_线程池的实战案例.py`
   - 说明：使用 `ThreadPoolExecutor` 并发抓取 1994-2025 年电影票房数据，大幅提升抓取效率。
   - 涉及技能：线程池管理、并发任务调度、lxml 高效解析。

2. **多进程实战 (Multiprocessing)**
   - 文件：`02_多进程.py`
   - 说明：演示了多进程的创建与启动，对比多线程与多进程在 CPU 密集型任务中的差异。
   - 涉及技能：`multiprocessing.Process`、进程间通信基础。

3. **生产者-消费者模型 (Producer-Consumer Model)**
   - 文件：`03_生产者和消费者模型.py`
   - 说明：基于 `multiprocessing.Queue` 实现多进程间的生产者-消费者架构，用于高效下载图片，实现任务解耦。
   - 涉及技能：进程间通信（IPC）、队列（Queue）、多进程协同、生产者-消费者设计模式。

## 🛠️ 使用工具与 AI 辅助：
- **主要语言**：Python
- **核心库**：Requests, BeautifulSoup, lxml, Pandas, concurrent.futures, multiprocessing
- **AI 辅助开发**：在编写和调试过程中，大量使用了 AI 编程助手（如 Claude/Cursor）协助排查 Bug 和优化代码结构，具备 Vibe Coding 实践经验。

## 📌 个人背景说明：
本人拥有扎实的编程逻辑基础，曾参与 WorldQuant 全球量化挑战赛并获 **Gold Level** 成就，具备在真实场景下处理数据和解决复杂逻辑问题的能力。擅长将复杂的业务需求拆解为可执行的代码逻辑，并利用 AI 工具高效完成开发。
