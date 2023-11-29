# Paperless-ngx for ARM64 with ZXING Support

This repository houses Dockerfiles necessary for building amd64/arm64 Paperless-ngx images. Notably, these images also support zxing-cpp—a feature that the standard image for the arm64 platform [lacks](https://github.com/paperless-ngx/paperless-ngx/blob/e3257b8fa303a2e6ff9e31ff746212f171d98b5b/Pipfile#L59).

## How to Use the Image

To pull the latest version, use `ghcr.io/cryptoluks/paperless-ngx` as your image tag.

## Enabling Barcode Features

To utilize the ASN-barcode feature with the zxing library in the Paperless-ngx container, add the following environment variables:

```
PAPERLESS_CONSUMER_BARCODE_SCANNER=ZXING
PAPERLESS_CONSUMER_ENABLE_ASN_BARCODE=true
PAPERLESS_CONSUMER_ENABLE_BARCODES=true
```
## Additional Resources

For more information, consider the following resources:
- [Paperless-ngx with QR Codes as ASN: My Workflow](https://margau.net/posts/2023-04-16-paperless-ngx-asn/)
- [Feature: Support Barcode Upscaling for Better Detection of Small Barcodes](https://github.com/paperless-ngx/paperless-ngx/pull/3655)
- [AveryLabels.py: A Class to Manage Printing on Avery Labels with ReportLab](https://gist.github.com/timrprobocom/3946aca8ab75df8267bbf892a427a1b7)
