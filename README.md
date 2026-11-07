
# KnowFlow

KnowFlow 是一个基于 RAG（Retrieval-Augmented Generation，检索增强生成）的个人知识库问答系统。

## 项目目标

用户可以上传个人文档，通过自然语言提问，从文档中检索相关内容，并利用大语言模型生成带有原文来源引用的回答。

## 核心功能

- [ ] PDF 文档上传
- [ ] PDF 文本提取
- [ ] 文本切分（Chunking）
- [ ] 文本向量化（Embedding）
- [ ] 向量数据库存储
- [ ] 相似度检索
- [ ] 基于检索结果生成回答
- [ ] 回答附带原文引用
- [ ] 多轮对话与历史记录
- [ ] 检索效果评估

## 技术栈

- Python 3.13
- FastAPI
- LangChain
- FAISS / Chroma
- MySQL
- Streamlit
- pytest

## 项目进度

当前阶段：开发环境搭建

## 项目结构

```text
KnowFlow/
├── .venv/          # Python 虚拟环境，不提交到 Git
├── README.md       # 项目说明
└── .gitignore      # Git 忽略规则
```

## 开发计划

- V1.0：实现基础 RAG 问答流程
- V1.5：加入 API、前端界面、历史记录和测试
- V2.0：开展检索效果评估与优化
