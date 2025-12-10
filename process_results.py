#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 19:51:26 2025

@author: mariarf
"""

import pandas as pd
import numpy as np
from pathlib import Path

# ==============================
# CONFIGURACIÓN GLOBAL
# ==============================

BASE_DIR = Path("/Users/mariarf/Desktop/agu_mama_IR/231")  # Carpeta donde están los resultados MAGeCK

# ==============================
# FUNCIÓN PRINCIPAL
# ==============================

def merge_gene_summary_with_counts(
    gene_summary_file: str,
    count_file: str,
    output_file: str,
    muestras: list
):
    """
    Combina el archivo gene_summary con los conteos de sgRNAs
    para cada muestra.

    Parameters
    ----------
    gene_summary_file : str
        Archivo gene_summary.txt de MAGeCK
    count_file : str
        Archivo .count.txt de MAGeCK
    output_file : str
        Nombre del archivo CSV de salida
    muestras : list
        Columnas (muestras) a pivotar del count
    """

    print(f"\n→ Procesando: {gene_summary_file}")

    gene_summary_path = BASE_DIR / gene_summary_file
    count_path = BASE_DIR / count_file
    output_path = BASE_DIR / output_file

    # ==============================
    # LECTURA DE ARCHIVOS
    # ==============================

    tabla_summary = pd.read_csv(gene_summary_path, sep="\t")
    tabla_count = pd.read_csv(count_path, sep="\t")

    # ==============================
    # NORMALIZACIÓN DE COLUMNAS
    # ==============================

    # Asegurar que el identificador del gen siempre se llame "id"
    if "Gene" in tabla_summary.columns:
        tabla_summary.rename(columns={"Gene": "id"}, inplace=True)

    if "id" not in tabla_summary.columns:
        raise ValueError("No se encuentra columna 'Gene' ni 'id' en gene_summary")

    tabla_summary["id"] = tabla_summary["id"].astype(str)
    tabla_count["id"] = tabla_count["id"].astype(str)

    # ==============================
    # INDEXADO DE SGRNAS
    # ==============================

    tabla_count["variable"] = tabla_count.groupby("id").cumcount() + 1

    # ==============================
    # MERGE Y PIVOT
    # ==============================

    tabla_final = tabla_summary.copy()

    for col in muestras:
        if col not in tabla_count.columns:
            raise ValueError(f"La columna '{col}' no existe en el archivo count")

        tabla_pivot = tabla_count.pivot(
            index="id",
            columns="variable",
            values=col
        )

        tabla_pivot.columns = [f"{col}_sgRNA{i}" for i in tabla_pivot.columns]
        tabla_pivot.reset_index(inplace=True)

        tabla_final = tabla_final.merge(tabla_pivot, on="id", how="left")

    # ==============================
    # LIMPIEZA Y GUARDADO
    # ==============================

    tabla_final.replace("", np.nan, inplace=True)
    tabla_final.to_csv(output_path, index=False)

    print(f"[OK] Archivo generado: {output_path.name}")


# ==============================
# EJECUCIONES CONCRETAS
# ==============================

def main():

    print("\n=== POSTPROCESAMIENTO DE RESULTADOS MAGeCK ===")

    # ==============================
    # 231 Control vs IR
    # ==============================

    merge_gene_summary_with_counts(
        gene_summary_file="231_CvsIR.gene_summary.txt",
        count_file="231_controlvsIR.count.txt",
        output_file="231_CvsIR.gene_summary_final.csv",
        muestras=["R1", "R8", "R2", "R5"]
    )

    print("\n=== POSTPROCESAMIENTO FINALIZADO ===")


# ==============================
# ENTRY POINT
# ==============================

if __name__ == "__main__":
    main()
