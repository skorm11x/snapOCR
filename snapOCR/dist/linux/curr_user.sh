#!/bin/bash

# Get the current user
CURRENT_USER=$(whoami)

# Start the snapOCR service as the current user
exec sudo -u $CURRENT_USER /usr/bin/python3 snapocr_service.py