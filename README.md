
## CRISPR Screening Analysis Pipeline (FastQC · Cutadapt · MAGeCK · Python)
'''
Pipeline reproducible para el análisis completo de datos de **CRISPR-Cas9 screening**, desde control de calidad de archivos FASTQ hasta análisis de enriquecimiento génico con **MAGeCK** y postprocesamiento en **Python**.

Este workflow fue diseñado para comparar **condiciones control vs irradiadas** en diferentes líneas celulares humanas.
'''

## Características principales

✅ Control de calidad automático con **FastQC**  
✅ Trimming de adaptadores con **Cutadapt**  
✅ Análisis estadístico con **MAGeCK (count, test, mle)**  
✅ Postprocesamiento de resultados con **Python + Pandas**  

## Workflow del análisis

FASTQ (raw)
↓
FastQC (QC inicial)
↓
Cutadapt (trimming)
↓
FastQC (QC post-trimming)
↓
MAGeCK count
↓
MAGeCK test / MLE
↓
Postprocesamiento en Python
↓
Resultados finales (.csv)

## Estructura del repositorio

pipeline_crispr/
 ── scripts/
  ── run_fastqc.sh # QC pre y post trimming
  ── run_cutadapt.sh # Trimming de reads
  ── run_mageck.sh # Análisis MAGeCK completo
  ── process_results.py# Integración gene_summary + conteos
 ── README.md

## Requisitos

- Linux / macOS  
- Python ≥ 3.8  
- Conda / Mamba  
- FastQC  
- Cutadapt  
- MAGeCK  
- pandas, numpy  

## Instalación del entorno

conda create -n mageck_env python=3.9
conda activate mageck_env

conda install -c bioconda fastqc cutadapt mageck
pip install pandas numpy
