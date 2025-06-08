from speedtest import Speedtest
from typing import Tuple

def test_internet_speed() -> Tuple[float, float, float]:
    """
    测试网络速度，返回下载速度、上传速度和延迟。

    Returns:
        download_mbps (float): 下载速度，单位 Mbps
        upload_mbps (float): 上传速度，单位 Mbps
        ping_ms (float): 延迟，单位 ms
    """
    st: Speedtest = Speedtest()
    # 选择最佳测试服务器（基于 ping）
    st.get_best_server()

    # 测试下载和上传（返回值单位是 bit/s）
    download_bps: float = st.download()
    upload_bps: float = st.upload()

    # 将 bit/s 转为 Mbps
    download_mbps: float = download_bps / 1_000_000
    upload_mbps: float = upload_bps / 1_000_000

    # 延迟
    ping_ms: float = st.results.ping

    return download_mbps, upload_mbps, ping_ms

def main() -> None:
    download: float
    upload: float
    ping: float

    download, upload, ping = test_internet_speed()

    print(f"下载速度: {download:.2f} Mbps")
    print(f"上传速度: {upload:.2f} Mbps")
    print(f"延迟 (ping): {ping:.2f} ms")


if __name__ == "__main__":
    main()
