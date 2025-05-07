#  chặn ip ko mong muốn

import pydivert

blocked_ips = ["192.168.1.5", " 10.0.0.1"]
with pydivert.WinDivert("ip") as w:
    for packet in w:
        if packet.src_addr in blocked_ips:
            print(f"Blocked packet to {packet.ip.dst}")
            continue  # Skip this packet
        else:
            print(f"Allowed packet to {packet.ip.dst}")
        w.send(packet)  # Send the packet if not blocked
        w.send(packet)

        # Pydirvver giúp kiểm soát gói tin trên windows
        # Chặn IP bằng cách kiểm tra packet.src_addr