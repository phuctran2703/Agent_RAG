# Agent_RAG

## Giới thiệu

Agent_RAG là một demo xây dựng hệ thống Retrieval-Augmented Generation (RAG) agent đơn giản, kết hợp sức mạnh của LangGraph, LangChain, và một công cụ tìm kiếm bên ngoài (DuckDuckGoSearch) để cải thiện khả năng trả lời câu hỏi từ người dùng.

Code được thực hiện bằng Jupyter Notebook, cho mục đích học tập, thử nghiệm nhanh. 
[Link Colab](https://colab.research.google.com/drive/1GLlEQ04ULiJP03Pbo7jCFcIvR9kDuz-4?usp=sharing)

## Cấu trúc notebook
**Notebook bao gồm 4 phần chính:**
### Tạo vector embedding từ dữ liệu
- Sử dụng model embedding sentence-transformers/all-mpnet-base-v2 để mã hóa nội dung pdf thành vector embedding.
- Các vector này được lưu trữ trong vector store Chroma để thực hiện tìm kiếm ngữ nghĩa.

### Xây dựng RAG với LangGraph
- Sử dụng langgraph để thiết kế một đồ thị xử lý đơn giản cho tác vụ RAG.
- Ánh xạ luồng dữ liệu giữa các bước như: truy xuất tài liệu → tạo prompt → sinh câu trả lời.
- Giúp hình dung luồng xử lý rõ ràng hơn, dễ dàng kiểm soát các thành phần.

### Tạo Agent tích hợp tìm kiếm (DuckDuckGo) bằng LangChain
- Xây dựng một RAG Agent với langchain.agents có thể tìm kiếm dữ liệu bên ngoài (real-time).
- Tích hợp DuckDuckGoSearch để tìm kiếm dữ liệu trên web.
- Agent tự động quyết định khi nào cần sử dụng công cụ tìm kiếm và tổng hợp câu trả lời.

### Đánh giá chất lượng trả lời
- Dùng bộ dữ liệu từ {Kaggle - Question-Answer Dataset}[https://www.kaggle.com/datasets/rtatman/questionanswer-dataset].
- Thực hiện thủ công các tiêu chí đánh giá agent model.
