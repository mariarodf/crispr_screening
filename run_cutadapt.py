#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 19:35:46 2025

@author: mariarf
"""

import os
import subprocess
from pathlib import Path

# ==============================
# SET PATHS
# ==============================

RAW_DIR = Path("/Users/mariarf/Desktop/agu_mama_IR/Original_fastq")
TRIM_DIR = RAW_DIR / "trimmed"

CUTADAPT_BIN = "cutadapt"
ADAPTER = "CGAAACACCG"
MINLEN = 20
MAXLEN = 20
OVERLAP = 10
SHORTEN = 20

# ==============================
# FUNCIONES
# ==============================

def run_cutadapt(input_file, output_file):
    """Ejecuta cutadapt desde Python."""
    cmd = [
        CUTADAPT_BIN,
        "-g", ADAPTER,
        "-e", "0",
        "-m", str(MINLEN),
        "-M", str(MAXLEN),
        "-O", str(OVERLAP),
        "-l", str(SHORTEN),
        "-o", str(output_file),
        str(input_file)
    ]

    print(f"→ Ejecutando Cutadapt para: {input_file.name}")
    try:
        subprocess.run(cmd, check=True)
        print(f"[OK] Trimming finalizado → {output_file.name}\n")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Cutadapt falló en {input_file.name}")
        raise


def main():
    print("\n=== EJECUTANDO CUTADAPT ===")

    TRIM_DIR.mkdir(parents=True, exist_ok=True)

    fastq_files = sorted(RAW_DIR.glob("IR-R*_L001_R1_001.fastq"))

    if not fastq_files:
        print("No se encontraron archivos con patrón IR-R*_L001_R1_001.fastq")
        return

    print(f"Archivos detectados ({len(fastq_files)}):")
    for f in fastq_files:
        print(" -", f.name)

    print("\nProcesando...\n")

    for f in fastq_files:
        output_file = TRIM_DIR / f"Trimmed_{f.name}"
        run_cutadapt(f, output_file)

    print("=== CUTADAPT COMPLETADO ===")


if __name__ == "__main__":
    main()
