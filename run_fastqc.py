#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 19:21:15 2025

@author: mariarf
"""

import os
import subprocess
from pathlib import Path

# ============================
# SET PATHS
# ============================

# Ruta del ejecutable FastQC
FASTQC_BIN = "/Applications/FastQC.app/Contents/MacOS/fastqc"

# Directorio con FASTQ originales
RAW_DIR = Path("/Users/mariarf/Desktop/IR/Original_fastq")

# Directorio de salida de reportes
OUT_DIR = RAW_DIR / "fastqc_reports"

# ============================
# MAIN FUNCTIONS
# ============================

def run_fastqc(input_file, output_dir):
    """Ejecuta FastQC sobre un archivo FASTQ."""
    try:
        subprocess.run(
            [FASTQC_BIN, str(input_file), "-o", str(output_dir)],
            check=True
        )
        print(f"[OK] FastQC completado: {input_file.name}")
    except subprocess.CalledProcessError:
        print(f"[ERROR] Falló FastQC en: {input_file}")
        raise


def main():
    print("\n=== INICIANDO FASTQC ===")

    # Crear directorio de salida si no existe
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Buscar archivos FASTQ
    fastq_files = sorted(list(RAW_DIR.glob("*.fastq")))

    if not fastq_files:
        print("No se encontraron archivos FASTQ.")
        return

    print(f"Archivos detectados ({len(fastq_files)}):")
    for f in fastq_files:
        print(" -", f.name)

    print("\nEjecutando FastQC...\n")

    # Procesar archivos uno por uno
    for fastq in fastq_files:
        run_fastqc(fastq, OUT_DIR)

    print("\n=== FASTQC COMPLETADO ===")
    print(f"Reportes disponibles en: {OUT_DIR}")


if __name__ == "__main__":
    main()