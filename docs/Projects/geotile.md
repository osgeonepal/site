# GeoTile

**GeoTile** is an open-source Python library designed for efficient creation and manipulation of raster tiles. It is built to simplify geospatial raster data handling, especially for workflows involving large datasets, remote sensing imagery, and deep learning model training.

The library provides a straightforward API to split raster datasets into uniform tiles, generate tiled datasets with configurable size and stride, and optionally select specific spectral bands. It also supports advanced geospatial operations such as mosaicking tiled outputs back into a single raster, generating raster masks from vector data, and rasterizing shapefiles based on attribute values.

GeoTile is particularly useful in geospatial machine learning pipelines where consistent tile-based datasets are required for training computer vision models on satellite or aerial imagery.

### Key capabilities

* Raster tile generation with configurable tile size and stride
* Band-specific tile extraction for multispectral datasets
* Mosaicking tiles back into georeferenced rasters
* Raster mask creation from shapefiles
* Rasterization of vector data using attribute fields
* Simple lifecycle management for raster datasets

### Installation

GeoTile can be installed via conda or pip:

```bash
conda install -c conda-forge geotile
```

More installation options are available in the official documentation.

### Documentation

Full usage guides, examples, and API reference are available at: [GeoTile Documentation](https://geotile.readthedocs.io/)

**Repository:** [GeoTile Repository](https://github.com/osgeonepal/geotile)