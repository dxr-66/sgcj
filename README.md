# 拾光萃集 (ShiGuangJi)

> 收集值得回看的文字

一个静态的个人文章收藏与发布网站，支持收录外部文章和发布原创内容（含视频嵌入），并提供 RSS 订阅功能。

## 功能特性

- **分类导航** — 全部 / 人文 / 旅游 / AI / 科技 / 读书 / 设计 / 生活
- **标签筛选与搜索** — 按标签过滤、关键词搜索
- **文章管理** — 管理模式下支持文章增删改（密码保护）
- **Markdown 支持** — 原创文章支持完整 Markdown 语法渲染
- **代码高亮** — 代码块自动语法着色（highlight.js）
- **视频嵌入** — 支持 B站、YouTube 自动解析，抖音外链跳转
- **文章导出** — 生成 JS 代码供 GitHub 提交
- **RSS 订阅** — 标准 RSS 2.0 格式订阅源
- **暗色主题** — Ayu Dark 风格，响应式布局适配移动端
- **离线存储** — 用户数据持久化至浏览器 localStorage

## 项目结构

```
├── index.html          # 主页面（单文件 SPA，含 HTML + CSS + JS）
├── articles.js         # 文章数据源
├── generate-rss.py     # RSS 生成脚本（Python 3）
├── rss.xml             # RSS 订阅源文件
├── sync.bat           # Windows 同步脚本
├── sync.sh            # Linux/Mac 同步脚本
└── README.md          # 项目说明
```

## 快速开始

### 本地预览

直接在浏览器中打开 `index.html` 即可运行，无需安装任何依赖或构建工具。

### 添加文章

1. 打开网站，点击右下角 **+** 按钮
2. 输入密码进入管理模式（默认密码：`admin`）
3. 填写文章标题、分类、标签、摘要、链接等信息
4. 点击保存，文章将存储在浏览器 localStorage 中

### 同步到 GitHub

1. 在管理模式下点击导出按钮
2. 将生成的 JS 代码复制到 `articles.js` 文件中
3. 运行同步脚本：
   - **Windows**: 双击 `sync.bat`
   - **Linux/Mac**: `./sync.sh`
4. 等待 GitHub Pages 自动部署（约 1-5 分钟）

### 生成 RSS

```bash
python generate-rss.py
```

该脚本会读取 `articles.js` 中的文章数据并生成 `rss.xml`，仅依赖 Python 标准库，无需安装第三方包。

## Markdown 支持

原创文章支持完整的 Markdown 语法：

```markdown
## 二级标题
### 三级标题

**加粗文字** *斜体文字* ~~删除线~~

> 引用块
> 多行引用

- 无序列表项
- 另一个列表项

1. 有序列表
2. 第二项

`行内代码`

```python
# 代码块
def hello():
    print("Hello World")
```

[链接文字](https://example.com)
![图片描述](https://example.com/image.jpg)

| 表头1 | 表头2 |
|-------|-------|
| 内容1 | 内容2 |
```

## 技术栈

| 维度 | 技术 |
|------|------|
| 前端 | 原生 HTML / CSS / JavaScript |
| Markdown | marked.js + highlight.js |
| 样式 | 原生 CSS + CSS 变量（暗色主题） |
| 数据存储 | localStorage + JS 文件 |
| RSS 生成 | Python 3（标准库） |
| 视频嵌入 | iframe（B站 / YouTube / 抖音） |
| 部署平台 | GitHub Pages |

## 密码管理

- **默认密码：** `admin`
- **修改密码：** 管理模式下进入密码管理，输入旧密码和新密码
- **找回密码：** 通过预设的找回密语重置密码

## 浏览器兼容

支持所有现代浏览器，响应式布局在 768px 断点适配移动端。