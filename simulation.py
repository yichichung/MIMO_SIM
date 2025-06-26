# simulation.py
import numpy as np
from modulation import modulate, demodulate
from channel import generate_channel, add_noise
from receiver import zf_detector, mmse_detector
import config

def run_simulation():
    ber_list = []

    for snr_dB in config.snr_dBs:
        bit_errors = 0
        total_bits = 0
        snr_linear = 10 ** (snr_dB / 10)

        for _ in range(config.num_symbols // config.Nt):
            bits = np.random.randint(0, 2, config.Nt)
            x = modulate(bits, config.modulation)
            H = generate_channel(config.Nr, config.Nt)
            y = H @ x
            y = add_noise(y, snr_dB)

            if config.receiver_type == 'ZF':
                x_hat = zf_detector(H, y)
            elif config.receiver_type == 'MMSE':
                x_hat = mmse_detector(H, y, snr_linear)
            else:
                raise ValueError("Unsupported receiver type")

            bits_hat = demodulate(x_hat, config.modulation)
            bit_errors += np.sum(bits != bits_hat)
            total_bits += config.Nt

        ber = bit_errors / total_bits
        ber_list.append(ber)
        print(f"SNR {snr_dB} dB -> BER: {ber:.5f}")

    return config.snr_dBs, ber_list
