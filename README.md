# Hệ thống Tự động Tạo Câu hỏi Trắc nghiệm bằng AI
Một dự án xây dựng trang web thông minh sử dụng AI để tự động tạo bộ câu hỏi trắc nghiệm từ tài liệu học tập, giúp giảm tải công việc cho giáo viên và hỗ trợ học sinh ôn tập hiệu quả.
## Giới thiệu Dự án

Dự án này giải quyết hai vấn đề cốt lõi trong nhà trường:
1.  **Giáo viên:** Giảm thiểu thời gian và công sức thủ công cho việc biên soạn đề kiểm tra, ma trận đề và câu hỏi ôn tập.
2.  **Học sinh:** Cung cấp một công cụ học tập linh hoạt, có khả năng tạo ra các bộ câu hỏi đa dạng từ chính tài liệu đang học.

Ứng dụng cho phép người dùng tải lên tài liệu (như `.pdf`, `.docx`), sau đó hệ thống AI sẽ phân tích nội dung và tự động tạo ra một bộ câu hỏi trắc nghiệm.

Điểm khác biệt chính của dự án là khả năng tạo câu hỏi theo **4 cấp độ nhận thức** (Nhận biết, Thông hiểu, Vận dụng, Vận dụng cao), cho phép tạo ra các đề kiểm tra chuẩn hóa và bám sát mục tiêu giảng dạy.

## Tính năng Nổi bật

* **Giao diện Web Trực quan:** Xây dựng bằng Streamlit, cho phép người dùng dễ dàng tải tệp, chọn nội dung và tùy chỉnh số lượng câu hỏi.
* **Xử lý Đa định dạng:** Trích xuất văn bản thông minh và chính xác từ các tệp `.docx` (phân tích XML) và `.pdf`.
* **Tạo Câu hỏi theo 4 Cấp độ:** Tận dụng các prompt kỹ thuật (system prompt) chuyên biệt để yêu cầu AI tạo câu hỏi theo 4 mức độ tư duy, bám sát ma trận đề của Bộ Giáo dục.
* **Đảm bảo Cấu trúc Dữ liệu (Pydantic):** Sử dụng Pydantic để định nghĩa cấu trúc dữ liệu `Exam` và `QuizSample`, đồng thời tích hợp với API của OpenAI (`response_format`) để ép buộc AI trả về kết quả JSON đúng định dạng, loại bỏ lỗi parsing.
* **Kiểm soát Ngữ cảnh (Chunking):** Tự động chia nhỏ văn bản đầu vào theo token để tối ưu hóa cửa sổ ngữ cảnh, cho phép xử lý các tài liệu dài mà không mất thông tin.
* **Xuất tệp Nhanh chóng:** Tự động tạo và cho phép người dùng tải về tệp `.docx` chứa bộ đề hoàn chỉnh, sẵn sàng để in ấn hoặc sử dụng.

## Cài đặt và Chạy dự án

Bạn có thể chạy dự án này cục bộ theo các bước sau:

1.  **Clone repository:**
    ```bash
    git clone https://github.com/MinhPhanAnh/NCKH-Project.git
    cd NCKH-Project.git
    ```

2.  **Tạo và kích hoạt môi trường ảo:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    # Trên Windows: venv\Scripts\activate
    ```

3.  **Cài đặt các thư viện cần thiết:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Thiết lập API Key:**
    Tạo tệp `.streamlit/secrets.toml` và thêm API key của bạn:
    ```toml

5.  **Chạy ứng dụng:**
    ```bash
    streamlit run app.py
    ```
