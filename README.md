# Python-SecureShield-Firewall
Xây dựng fire wall đơn giản bằng python

Mục tiêu: Xây dựng firewall để kiểm soát lưu lượng mạng, phát hiện và chặn các kết nối không mong muốn.
1. Các bước thực hiện:</br>

Bước 1. Chuẩn bị môi trường:
- Cài đặt Python và các thư viện liên quan: Scapy, NetfilterQueue.
- Cài đặt và thiết lập iptables.
      
Bước 2. Xây dựng chức năng cơ bản: </br>
- Sử dụng Scapy để phân tích lưu lượng mạng.</br>
- Viết logic chặn IP dựa trên blacklist.
      
Bước 3. Phát hiện tấn công DDoS:</br>
- Xây dựng thuật toán kiểm tra lưu lượng bất thường (số lượng gói tin trên giây).</br>
- Chặn lưu lượng từ các nguồn có hành vi đáng ngờ.
        
Bước 4.Chặn quét cổng (Port Scanning):</br>
- Xác định các gói SYN liên tiếp từ một nguồn.</br>
- Lập quy tắc chặn lưu lượng từ IP thực hiện quét.
        
Bước 5.Kiểm thử và báo cáo:</br>
- Kiểm tra firewall trên một mạng thử nghiệm. </br>
- Tạo báo cáo chi tiết về lưu lượng bị chặn và các hành vi đáng ngờ.
  



