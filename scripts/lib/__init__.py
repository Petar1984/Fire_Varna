"""Shared core for hydrant field-report ingest.

H1 (docs/plans/h1_shared_core_spatial_dedup.md) extracts the reusable,
non-network logic of scripts/apply_approved_reports.py into hydrant_core so the
H2 KMZ adapter can reuse the same match/merge/provenance pipeline.
"""
