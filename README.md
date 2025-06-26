# MIMO_SIM
basic MIMO in python 
**# MIMO 4x4 通訊系統模擬 (Python)

這是一個使用 Python 編寫的最基本 MIMO（多輸入多輸出）無線通訊系統模擬程式，支援：

- 4x4 MIMO 系統
- BPSK 調變
- Rayleigh 通道
- 線性接收器（Zero Forcing / MMSE）
- BER（位元錯誤率）對 SNR（訊號雜訊比）分析與繪圖

本專案設計簡潔，適合作為研究或課堂練習的起點。

## 功能簡介

- 支援 BPSK 調變方式
- 實作 Zero Forcing (ZF) 與 MMSE 線性接收器
- 可自訂天線數、SNR 測試範圍與模擬次數
- 使用 Matplotlib 繪製 BER 對 SNR 曲線
- 模組化程式架構，方便日後擴充（例如加入 QPSK 或 OFDM）

## 安裝與執行方式

1. 安裝依賴：
   ```bash
   pip install numpy matplotlib
2. run: python main.py

## structure of the project:
mimo_sim/
│
├── main.py           # 主程式，執行整體流程
├── config.py         # 設定模擬參數（天線數、調變方式、SNR 範圍等）
│
├── modulation.py     # 調變與解調邏輯（目前支援 BPSK）
├── channel.py        # 建立 Rayleigh 通道與加入雜訊
├── receiver.py       # 線性接收器：ZF 與 MMSE
├── simulation.py     # 執行模擬主迴圈，計算 BER
├── plot.py           # 使用 matplotlib 繪圖

**
