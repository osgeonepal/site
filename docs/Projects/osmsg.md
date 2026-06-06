# OSMSG

**OSMSG** (OpenStreetMap Stats Generator) is an open-source CLI tool and Python library designed to analyze OpenStreetMap (OSM) editing history and generate structured contributor statistics. It processes OSM changeset and history data to produce per-user metrics such as counts of nodes, ways, and relations created, modified, or deleted over a specified time range.

The tool is built for flexible geospatial analytics workflows, supporting filtering by country, custom boundaries, tags, and hashtags (e.g., `building`, `highway`, `#hotosm`). It is suitable for both one-time analysis and continuous or incremental updates, making it practical for large-scale OSM data processing pipelines.

osmsg is widely used for understanding mapping activity patterns, contributor behavior, and thematic mapping contributions across regions. It is useful in research, humanitarian mapping analysis, and monitoring OpenStreetMap community engagement.

The tool supports multiple output formats, enabling easy integration into data pipelines and analytics systems. Results can be exported as Parquet, CSV, JSON, Markdown, DuckDB, or PostgreSQL, depending on downstream requirements.

In addition to the CLI, osmsg can also be used as a Python library, allowing developers to embed OSM analytics directly into geospatial workflows, dashboards, and applications.

### Key capabilities

- Per-user OSM edit statistics (nodes, ways, relations)
- Filtering by country, boundary, tags, and hashtags
- Incremental updates for continuous processing
- Support for large-scale OSM history analysis
- Multiple export formats (Parquet, CSV, JSON, Markdown, DuckDB, PostgreSQL)
- CLI + Python library support

### Installation

```bash
pip install osmsg
```

Other installation methods (uvx, Docker, etc.) are available in the documentation.

### Documentation

Full documentation and usage guide:  
[OSMSG Manual](https://github.com/osgeonepal/osmsg/blob/main/docs/Manual.md)

### Repository

[OSMSG Repository](https://github.com/osgeonepal/osmsg)