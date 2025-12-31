# Mini Genomics Pipeline (Python)

## Overview
This project demonstrates a simplified genomics pipeline using Python.
It simulates the core steps of an NGS workflow:
FASTQ generation → Alignment (SAM) → Variant Calling (VCF).

The goal is to understand pipeline structure and data flow, not to run
full-scale bioinformatics tools.

## Pipeline Steps
1. FASTQ generation (mock sequencing reads)
2. Alignment output (SAM format)
3. Variant calling output (VCF format)

## Files
- pipeline.py : Main pipeline script
- sample.fastq : Mock FASTQ reads
- aligned.sam : Mock alignment output
- variants.vcf : Mock variant calls

## Technologies Used
- Python
- Basic genomics file formats (FASTQ, SAM, VCF)

## How to Run
python pipeline.py

## Learning Outcome
- Understanding NGS pipeline structure
- Familiarity with genomics file formats
- Pipeline-style thinking for bioinformatics roles
