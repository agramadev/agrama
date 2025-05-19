#!/bin/bash

# Create the output directory if it doesn't exist
mkdir -p agrama/proto/generated

# Run buf to generate the protobuf files
buf generate

# Make the generated files importable
touch agrama/proto/generated/__init__.py

echo "Protobuf files generated successfully!"
