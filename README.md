# Paperless-ngx for ARM64 with ZXING Support

This repository houses Dockerfiles necessary for building amd64/arm64 Paperless-ngx images. Notably, these images also support zxing-cpp—a feature that the standard image for the arm64 platform [lacks](https://github.com/paperless-ngx/paperless-ngx/blob/e3257b8fa303a2e6ff9e31ff746212f171d98b5b/Pipfile#L59).

This image stands out further by incorporating the [Paperless-ngx-postprocessor](https://github.com/jgillula/paperless-ngx-postprocessor) right into the image, thereby providing a powerful and customizable post-processing script for Paperless-ngx.

## How to Use the Image

To pull the latest version, use `ghcr.io/cryptoluks/paperless-ngx` as your image tag.

## Enabling Barcode Features

To utilize the ASN-barcode feature with the zxing library in the Paperless-ngx container, add the following environment variables:

```
PAPERLESS_CONSUMER_BARCODE_SCANNER=ZXING
PAPERLESS_CONSUMER_ENABLE_ASN_BARCODE=true
PAPERLESS_CONSUMER_ENABLE_BARCODES=true
```

## Using Paperless-ngx-postprocessor

To use the Paperless-ngx-postprocessor, first mount the rules into your container:

```
./rules.yml:/usr/src/paperless-ngx-postprocessor/rulesets.d/rules.yml
```

Next, add the following environment variable to your Paperless-ngx container:

```
PAPERLESS_POST_CONSUME_SCRIPT=/usr/src/paperless-ngx-postprocessor/post_consume_script.sh
```

Since the Python virtual environment is pre-installed, you should be able to run the script directly without executing the `setup_venv.sh` script beforehand.

## Additional Resources

For more information, consider the following resources:
- [Paperless-ngx with QR Codes as ASN: My Workflow](https://margau.net/posts/2023-04-16-paperless-ngx-asn/)
- [Paperless-ngx-postprocessor](https://github.com/jgillula/paperless-ngx-postprocessor)
- [Post Consume Script Examples](https://github.com/paperless-ngx/paperless-ngx/wiki/Post-Consume-Script-Examples)
- [Feature: Support Barcode Upscaling for Better Detection of Small Barcodes](https://github.com/paperless-ngx/paperless-ngx/pull/3655)
- [AveryLabels.py: A Class to Manage Printing on Avery Labels with ReportLab](https://gist.github.com/timrprobocom/3946aca8ab75df8267bbf892a427a1b7)
