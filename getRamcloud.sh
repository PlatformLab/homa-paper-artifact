#!/bin/bash

git clone --branch homa-artifact-eval https://github.com/PlatformLab/RAMCloud.git
cd RAMCloud
git submodule update --init --recursive
ln -s ../../hooks/pre-commit .git/hooks/pre-commit

# Generate localconfig.py for RAMCloud
let num_rcxx=$(geni-get manifest | grep -o "<node " | wc -l)-2
/local/repository/localconfigGen.py $num_rcxx > scripts/localconfig.py

# Generate private makefile configuration
mkdir private
cat >>private/MakefragPrivateTop <<EOL
DEBUG := no

CCACHE := yes
DEBUG_OPT := yes

HOMA_BENCHMARK := yes

DPDK := yes
DPDK_DIR := dpdk
DPDK_SHARED := no
EOL

# Build DPDK libraries
MLNX_DPDK=y scripts/dpdkBuild.sh

# Build RAMCloud
make clean; make -j
