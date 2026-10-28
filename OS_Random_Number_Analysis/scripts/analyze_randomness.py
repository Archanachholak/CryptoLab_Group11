
from pathlib import Path
from collections import Counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chisquare, binomtest, norm


# ============================================================
# Operating System Random Number Analysis
# Person 1: Data Analysis and Statistical Testing
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"
PLOTS_DIR = RESULTS_DIR / "plots"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)
PLOTS_DIR.mkdir(parents=True, exist_ok=True)


def analyze_file(file_path):
    """Analyze the randomness properties of a binary file."""

    data = np.fromfile(file_path, dtype=np.uint8)

    if data.size == 0:
        print(f"\nSkipping empty file: {file_path.name}")
        return None

    print("\n" + "=" * 65)
    print(f"FILE: {file_path.name}")
    print("=" * 65)

    print(f"File size: {data.size:,} bytes")

    if data.size < 1_048_576:
        print("WARNING: File contains less than 1 MiB of data.")

    results = {
        "file": file_path.name,
        "bytes": int(data.size),
    }

    # --------------------------------------------------------
    # 1. BYTE FREQUENCY DISTRIBUTION
    # --------------------------------------------------------

    frequencies = np.bincount(data, minlength=256)
    expected = np.full(256, data.size / 256)

    chi_stat, chi_p = chisquare(
        frequencies,
        f_exp=expected
    )

    probabilities = frequencies / data.size
    nonzero = probabilities > 0

    entropy = -np.sum(
        probabilities[nonzero] *
        np.log2(probabilities[nonzero])
    )

    results["byte_chi_square"] = float(chi_stat)
    results["byte_chi_square_p"] = float(chi_p)
    results["shannon_entropy_bits_per_byte"] = float(entropy)

    plt.figure(figsize=(12, 5))

    plt.bar(range(256), frequencies)

    plt.axhline(
        data.size / 256,
        linestyle="--",
        label="Expected frequency"
    )

    plt.xlabel("Byte value (0-255)")
    plt.ylabel("Frequency")
    plt.title(f"Byte Frequency Distribution: {file_path.name}")
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        PLOTS_DIR / f"{file_path.stem}_byte_frequency.png"
    )
    plt.close()

    # --------------------------------------------------------
    # 2. BIT DISTRIBUTION AND MONOBIT TEST
    # --------------------------------------------------------

    bits = np.unpackbits(data)

    total_bits = int(bits.size)
    ones = int(bits.sum())
    zeros = total_bits - ones

    monobit_p = binomtest(
        ones,
        n=total_bits,
        p=0.5
    ).pvalue

    results["zero_bits"] = zeros
    results["one_bits"] = ones
    results["one_bit_proportion"] = float(ones / total_bits)
    results["monobit_p"] = float(monobit_p)

    plt.figure(figsize=(7, 5))

    plt.bar(
        ["Zero bits", "One bits"],
        [zeros, ones]
    )

    plt.ylabel("Number of bits")
    plt.title(f"Bit Distribution: {file_path.name}")
    plt.tight_layout()

    plt.savefig(
        PLOTS_DIR / f"{file_path.stem}_bit_distribution.png"
    )
    plt.close()

    # --------------------------------------------------------
    # 3. RUNS TEST
    # --------------------------------------------------------

    # A run is a consecutive sequence of identical bits.
    transitions = int(
        np.count_nonzero(bits[1:] != bits[:-1])
    )

    runs = transitions + 1

    expected_runs = 1 + (2 * zeros * ones / total_bits)

    if total_bits > 1 and zeros > 0 and ones > 0:

        variance = (
            2 * zeros * ones *
            (2 * zeros * ones - total_bits)
            / (total_bits**2 * (total_bits - 1))
        )

        if variance > 0:

            z_score = (
                (runs - expected_runs) /
                np.sqrt(variance)
            )

            # Approximate two-sided normal p-value.
            runs_p = 2 * norm.sf(abs(z_score))

        else:
            z_score = np.nan
            runs_p = np.nan

    else:
        z_score = np.nan
        runs_p = np.nan

    results["runs_observed"] = int(runs)
    results["runs_expected"] = float(expected_runs)
    results["runs_z_score"] = float(z_score)
    results["runs_p_approx"] = float(runs_p)

    # --------------------------------------------------------
    # 4. SERIAL CORRELATION
    # --------------------------------------------------------

    values = data.astype(np.float64)

    if data.size > 1 and np.std(values[:-1]) > 0:

        correlation = np.corrcoef(
            values[:-1],
            values[1:]
        )[0, 1]

    else:
        correlation = np.nan

    results["lag1_serial_correlation"] = float(correlation)

    # --------------------------------------------------------
    # 5. REPEATED FOUR-BYTE BLOCKS
    # --------------------------------------------------------

    raw_data = data.tobytes()

    usable_length = (len(raw_data) // 4) * 4

    blocks = [
        raw_data[i:i + 4]
        for i in range(0, usable_length, 4)
    ]

    block_counts = Counter(blocks)

    repeated_types = sum(
        count > 1
        for count in block_counts.values()
    )

    excess_occurrences = sum(
        count - 1
        for count in block_counts.values()
        if count > 1
    )

    results["repeated_4byte_block_types"] = int(repeated_types)

    results["excess_4byte_block_occurrences"] = int(
        excess_occurrences
    )

    # --------------------------------------------------------
    # 6. DISPLAY RESULTS
    # --------------------------------------------------------

    print("\nBYTE DISTRIBUTION")
    print(f"Chi-square statistic: {chi_stat:.4f}")
    print(f"Chi-square p-value: {chi_p:.6g}")
    print(f"Shannon entropy: {entropy:.6f} bits per byte")

    print("\nBIT DISTRIBUTION")
    print(f"Zero bits: {zeros:,}")
    print(f"One bits: {ones:,}")
    print(f"One-bit proportion: {ones / total_bits:.6f}")
    print(f"Monobit p-value: {monobit_p:.6g}")

    print("\nRUNS TEST")
    print(f"Observed runs: {runs:,}")
    print(f"Expected runs: {expected_runs:.2f}")
    print(f"Z-score: {z_score:.6f}")
    print(f"Approximate p-value: {runs_p:.6g}")

    print("\nSERIAL CORRELATION")
    print(f"Lag-1 correlation: {correlation:.8f}")

    print("\nREPEATED PATTERNS")
    print(f"Repeated 4-byte block types: {repeated_types}")
    print(f"Excess repeated block occurrences: {excess_occurrences}")

    return results


def main():

    filenames = [
        "linux_urandom.bin",
        "openssl_rand.bin",
        "windows_cng.bin",
    ]

    all_results = []

    for filename in filenames:

        file_path = DATA_DIR / filename

        if not file_path.exists():

            print(f"\nFile not found: {filename}")
            continue

        result = analyze_file(file_path)

        if result is not None:
            all_results.append(result)

    if all_results:

        output_file = RESULTS_DIR / "statistical_results.csv"

        dataframe = pd.DataFrame(all_results)

        dataframe.to_csv(
            output_file,
            index=False
        )

        print("\n" + "=" * 65)
        print("ANALYSIS COMPLETED")
        print("=" * 65)

        print(f"Results saved to: {output_file}")
        print(f"Graphs saved to: {PLOTS_DIR}")

        print("\nSummary table:")
        print(
            dataframe[
                [
                    "file",
                    "bytes",
                    "shannon_entropy_bits_per_byte",
                    "byte_chi_square_p",
                    "monobit_p",
                    "lag1_serial_correlation",
                ]
            ].to_string(index=False)
        )

    else:

        print("\nNo non-empty random-data files were found.")


if __name__ == "__main__":
    main()
