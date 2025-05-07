from collections import defaultdict
import time
import pydivert

ip_request = defaultdict(list)
with pydivert.WinDivert("ip") as w:
    for packet in w:
        src_ip = packet.src_addr
        current_time = time.time()
        ip_request[src_ip].append(current_time)
        ip_request[src_ip] = [t for t in ip_request[src_ip] if current_time - t < 5]

        # Giới hạn số lượng gói tin từ một địa chỉ IP trong khoảng thời gian nhất định
        # Nếu số lượng gói tin vượt quá giới hạn, chặn gói tin
        if len(ip_request[src_ip]) > 100: # nếu ip gửi quá nhiều yêu cầu 
            print(f"Phát hiển DDoS từ {src_ip}, chặn!!!")
            continue 
        else:
            print(f"Địa chỉ IP {src_ip} gửi yêu cầu hợp lệ")    
        w.send(packet)
        