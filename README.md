# Python-SecureShield-Firewall
Xây dựng fire wall đơn giản bằng python

Mục tiêu: Xây dựng firewall để kiểm soát lưu lượng mạng, phát hiện và chặn các kết nối không mong muốn.
1. Các bước thực hiện:
Bước 1. Chuẩn bị môi trường:
- Cài đặt Python và các thư viện liên quan: Scapy, NetfilterQueue.
- Cài đặt và thiết lập iptables.

- Xây dựng chức năng cơ bản:- Sử dụng Scapy để phân tích lưu lượng mạng.
- Viết logic chặn IP dựa trên blacklist.

- Phát hiện tấn công DDoS:- Xây dựng thuật toán kiểm tra lưu lượng bất thường (số lượng gói tin trên giây).
- Chặn lưu lượng từ các nguồn có hành vi đáng ngờ.

- Chặn quét cổng (Port Scanning):- Xác định các gói SYN liên tiếp từ một nguồn.
- Lập quy tắc chặn lưu lượng từ IP thực hiện quét.

- Kiểm thử và báo cáo:- Kiểm tra firewall trên một mạng thử nghiệm.
- Tạo báo cáo chi tiết về lưu lượng bị chặn và các hành vi đáng ngờ.




